# Intel Worker patch — `/auth/bridge` endpoint

This patch adds an SSO bridge endpoint to your existing `intel.resilience-engineers.com` Worker. It reads a logged-in user's `studio_session` cookie, mints a 60-second HMAC-signed token, and redirects them back to `brief-hormuz.resilience-engineers.com/auth/consume?token=...`.

The new subdomain Worker validates the HMAC and issues its own session — no cookie scope change required.

## Step 1 — Add the bridge handler

Open your intel Worker code (likely `worker/auth.js` or `worker/index.js` based on your setup). Add this function:

```javascript
// =====================================================================
// SSO bridge to other RE subdomains
// GET /auth/bridge?return=<full_url_on_trusted_subdomain>
//
// If the caller has a valid studio_session, mints a 60-second HMAC-signed
// token and redirects to <return-host>/auth/consume?token=...&return=<path>
// =====================================================================
async function handleAuthBridge(request, env) {
  const url = new URL(request.url);
  const returnTo = url.searchParams.get('return');
  if (!returnTo) {
    return new Response('Missing return parameter', { status: 400 });
  }

  let returnUrl;
  try { returnUrl = new URL(returnTo); }
  catch { return new Response('Invalid return URL', { status: 400 }); }

  // Allowlist — extend this when more RE subdomains adopt the bridge
  const trustedHosts = new Set([
    'brief-hormuz.resilience-engineers.com',
  ]);
  if (!trustedHosts.has(returnUrl.hostname)) {
    return new Response('Untrusted return host', { status: 400 });
  }

  // Reuse your existing session validator
  const session = await validateSession(request, env);
  if (!session) {
    // Not logged in — bounce to login with the original return preserved
    const loginUrl = new URL('/?login=1', request.url);
    loginUrl.searchParams.set('return', returnTo);
    return Response.redirect(loginUrl.toString(), 302);
  }

  // Fresh status check from D1 (your existing pattern)
  const user = await env.DB.prepare(
    'SELECT id, email, role, stripe_status FROM users WHERE id = ?'
  ).bind(session.userId).first();

  if (!user || !['active', 'comp', 'free'].includes(user.stripe_status)) {
    return Response.redirect('/?upgrade=1', 302);
  }

  // Mint signed token (60-second TTL, single-use via nonce)
  const now = Math.floor(Date.now() / 1000);
  const payload = {
    userId: user.id,
    email: user.email,
    role: user.role,
    stripe_status: user.stripe_status,
    iat: now,
    exp: now + 60,
    nonce: crypto.randomUUID(),
  };
  const payloadB64 = base64UrlEncode(JSON.stringify(payload));

  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey(
    'raw', enc.encode(env.HMAC_SECRET),
    { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']
  );
  const sig = await crypto.subtle.sign('HMAC', key, enc.encode(payloadB64));
  const sigB64 = base64UrlEncode(new Uint8Array(sig));
  const token = payloadB64 + '.' + sigB64;

  // Redirect to consumer endpoint
  const consumeUrl = new URL('/auth/consume', returnUrl.origin);
  consumeUrl.searchParams.set('token', token);
  consumeUrl.searchParams.set('return', returnUrl.pathname + returnUrl.search);
  return Response.redirect(consumeUrl.toString(), 302);
}

function base64UrlEncode(input) {
  let bytes;
  if (typeof input === 'string') bytes = new TextEncoder().encode(input);
  else bytes = input;
  let bin = '';
  for (const b of bytes) bin += String.fromCharCode(b);
  return btoa(bin)
    .replaceAll('+', '-')
    .replaceAll('/', '_')
    .replaceAll('=', '');
}
```

## Step 2 — Wire the route

In your fetch handler (or wherever you dispatch routes), add:

```javascript
if (url.pathname === '/auth/bridge') return handleAuthBridge(request, env);
```

Place it before the catch-all / static-asset handler.

## Step 3 — Set the HMAC secret on intel

In your intel Worker project directory:

```bash
wrangler secret put HMAC_SECRET
```

Paste the secret value when prompted. It must match exactly the value set on `brief-hormuz-gateway` Worker. The secret is **hex-encoded 32 bytes**, generated for you and shared via the chat — do not commit it anywhere.

## Step 4 — Deploy intel

```bash
wrangler deploy
```

## Step 5 — Verify

After deploy, visit (in a browser already logged into intel):

```
https://intel.resilience-engineers.com/auth/bridge?return=https://brief-hormuz.resilience-engineers.com/
```

Expected behavior:
- Browser does the bridge → consume → cookie set → land on the brief one-pager
- No second login

If you see a 400/401 error, the most likely causes are:
- HMAC_SECRET not yet set or mismatched between intel and brief-hormuz
- `validateSession` helper has a different name in your worker — adjust the call
- D1 binding name differs from `DB` — adjust to whatever your binding is

If the bridge endpoint returns the right token but `/auth/consume` shows "Authentication failed", the secrets don't match. Re-set both.

## Adding more subdomains later

When you build another tracker (`research-X.resilience-engineers.com`, etc.):
1. Add its hostname to the `trustedHosts` set in `handleAuthBridge`
2. Deploy a Worker on the new subdomain mirroring `brief-hormuz-gateway/src/index.js`
3. Set the same `HMAC_SECRET` on the new Worker
4. Same DNS pattern — proxied subdomain on Cloudflare with a Worker route

The bridge is generic; one intel-side endpoint handles every future subdomain.
