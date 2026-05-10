# brief-hormuz-gateway · auth Worker

Cloudflare Worker that gates `https://brief-hormuz.resilience-engineers.com/` behind the same login as `intel.resilience-engineers.com`. Validates an HMAC bridge token from intel, sets its own session cookie scoped to the brief subdomain, proxies content from GitHub Pages.

No cookie scope change to intel required. Sessions are independent per subdomain.

## What this contains

| File | Purpose |
|------|---------|
| `src/index.js` | Worker code: bridge consumer, session manager, origin proxy |
| `wrangler.toml` | Cloudflare deployment config — fill in three IDs before first deploy |
| `INTEL_PATCH.md` | Patch + setup steps for the existing intel Worker |
| `package.json` | Standard wrangler scripts |

## Deploy steps

### 0 · Prerequisites

```bash
npm install -g wrangler@latest
wrangler login           # one-time, opens browser
```

### 1 · Fill in `wrangler.toml`

Run:

```bash
wrangler kv:namespace list
wrangler d1 list
```

Copy the existing intel KV namespace ID into `wrangler.toml` `kv_namespaces[].id`, and the D1 database name + ID into `[[d1_databases]]`.

### 2 · Set the HMAC secret

```bash
cd worker
wrangler secret put HMAC_SECRET
# paste the secret when prompted (must match the one you set on intel)
```

### 3 · Deploy intel patch first

See `INTEL_PATCH.md`. Apply the patch, set the same `HMAC_SECRET` on intel, and `wrangler deploy` from your intel project. **Do this before deploying brief-hormuz** so the bridge endpoint exists when customers first hit it.

### 4 · Deploy brief-hormuz Worker

```bash
cd worker
wrangler deploy
```

### 5 · Cloudflare DNS

The DNS record `brief-hormuz` already exists pointing at GitHub Pages with proxy enabled. The Worker route in `wrangler.toml` intercepts traffic before it reaches the origin, so no DNS change is needed. Verify the orange cloud (proxied) is on for that record.

### 6 · Test end-to-end

In a browser already logged into `intel.resilience-engineers.com`:
- Visit `https://brief-hormuz.resilience-engineers.com/`
- Should redirect: brief-hormuz → intel/auth/bridge → brief-hormuz/auth/consume → land on the one-pager
- No second login

In a fresh incognito browser (no intel session):
- Visit `https://brief-hormuz.resilience-engineers.com/`
- Should redirect to intel login page

## What the auth flow looks like

```
Browser  ─→ GET https://brief-hormuz.resilience-engineers.com/

Worker  · no brief_session cookie
        · 302 → https://intel.resilience-engineers.com/auth/bridge?return=https://brief-hormuz...

Browser ─→ GET https://intel.resilience-engineers.com/auth/bridge?return=...

intel  · validates studio_session cookie (existing auth)
       · re-checks stripe_status from D1
       · mints HMAC-signed token (60s TTL, nonce, HS256)
       · 302 → https://brief-hormuz.resilience-engineers.com/auth/consume?token=...

Browser ─→ GET .../auth/consume?token=...

Worker  · verifies HMAC, expiry, nonce uniqueness
       · re-checks stripe_status from D1
       · creates KV session, sets brief_session cookie (HttpOnly, Secure, SameSite=Lax, scoped)
       · 302 → /

Browser ─→ GET / with brief_session cookie

Worker  · validates session in KV
       · re-checks stripe_status (per-request, mirrors intel pattern)
       · fetches https://resilienceengineers.github.io/hormuz-daily-brief/...
       · returns content with Cache-Control: private, max-age=60
```

## What this Worker enforces on every authenticated request

- Valid `brief_session` cookie matching a KV record (24h TTL)
- `stripe_status` is one of `active`, `comp`, `free` (re-fetched from D1 every request — same pattern intel uses)
- `access_expires_at` is in the future (if set)

If any check fails, session is killed and user is redirected to intel for re-auth or upgrade.

## Tail logs (for debugging)

```bash
wrangler tail
```

Streams live logs from the Worker.

## Update flow when content changes

The daily GitHub Actions run continues to push the new HTML to GitHub Pages. The Worker fetches the live origin on every request (with 60s edge cache). No Worker redeploy needed for content updates.

The Worker only needs redeploy when:
- Auth logic changes
- HMAC secret rotates
- Origin URL or trusted-host list changes
