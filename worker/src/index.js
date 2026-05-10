/**
 * brief-hormuz.resilience-engineers.com — auth gateway + GitHub Pages proxy.
 *
 * Flow:
 *   1. User hits brief-hormuz.resilience-engineers.com (no cookie yet)
 *   2. Worker redirects to https://intel.resilience-engineers.com/auth/bridge?return=<url>
 *   3. intel validates studio_session, mints 60-sec HMAC-signed token, redirects to
 *      brief-hormuz.resilience-engineers.com/auth/consume?token=<jwt>&return=<path>
 *   4. This Worker verifies the HMAC, creates its own brief_session in KV,
 *      sets brief_session cookie, redirects to <path>
 *   5. Subsequent requests carry brief_session cookie -> Worker proxies origin
 *
 * Origin: https://resilienceengineers.github.io/hormuz-daily-brief
 *
 * Sessions are scoped to brief-hormuz only. No cookie scope expansion.
 * Status (stripe_status / access_expires_at) re-checked on every request via D1.
 */

const ORIGIN = 'https://resilienceengineers.github.io/hormuz-daily-brief';
const INTEL_HOST = 'intel.resilience-engineers.com';
const COOKIE_NAME = 'brief_session';
const SESSION_TTL_SEC = 86400;       // 24 h
const TOKEN_MAX_AGE_SEC = 60;        // bridge token validity window
const SESSION_KEY_PREFIX = 'brief_session:';
const NONCE_KEY_PREFIX = 'brief_nonce:';

// ============================================================
// HMAC token verification
// ============================================================
async function verifyToken(env, token) {
  if (!token || typeof token !== 'string' || !token.includes('.')) return null;
  const [payloadB64, sigB64] = token.split('.');
  if (!payloadB64 || !sigB64) return null;

  const enc = new TextEncoder();
  let key;
  try {
    key = await crypto.subtle.importKey(
      'raw', enc.encode(env.HMAC_SECRET),
      { name: 'HMAC', hash: 'SHA-256' }, false, ['verify']
    );
  } catch { return null; }

  let sig;
  try { sig = base64UrlDecode(sigB64); } catch { return null; }

  const valid = await crypto.subtle.verify('HMAC', key, sig, enc.encode(payloadB64));
  if (!valid) return null;

  let payload;
  try {
    payload = JSON.parse(new TextDecoder().decode(base64UrlDecode(payloadB64)));
  } catch { return null; }

  const now = Math.floor(Date.now() / 1000);
  if (typeof payload.exp !== 'number' || payload.exp < now) return null;
  if (typeof payload.iat !== 'number' || payload.iat > now + 5) return null;
  if (now - payload.iat > TOKEN_MAX_AGE_SEC) return null;
  if (typeof payload.nonce !== 'string' || payload.nonce.length < 8) return null;

  // Replay protection: each token is single-use
  const nonceKey = NONCE_KEY_PREFIX + payload.nonce;
  const used = await env.KV.get(nonceKey);
  if (used) return null;
  await env.KV.put(nonceKey, '1', { expirationTtl: TOKEN_MAX_AGE_SEC * 2 });

  return payload;
}

function base64UrlDecode(s) {
  s = s.replaceAll('-', '+').replaceAll('_', '/');
  while (s.length % 4) s += '=';
  const bin = atob(s);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

// ============================================================
// Cookie helpers
// ============================================================
function getCookie(request, name) {
  const cookieHeader = request.headers.get('Cookie') || '';
  const match = cookieHeader.match(new RegExp('(?:^|;\\s*)' + name + '=([^;]+)'));
  return match ? match[1] : null;
}

function buildSessionCookie(token, maxAge) {
  return COOKIE_NAME + '=' + token +
    '; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=' + maxAge;
}

function clearedCookie() {
  return COOKIE_NAME + '=deleted; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=0';
}

// ============================================================
// Session management (KV-backed, brief-scoped)
// ============================================================
async function validateSession(env, request) {
  const token = getCookie(request, COOKIE_NAME);
  if (!token) return null;
  const session = await env.KV.get(SESSION_KEY_PREFIX + token, 'json');
  if (!session) return null;
  return { token, ...session };
}

async function createSession(env, payload) {
  const token = crypto.randomUUID();
  const sessionData = {
    userId: payload.userId,
    email: payload.email,
    role: payload.role || 'member',
    stripe_status: payload.stripe_status,
    issued_at: Math.floor(Date.now() / 1000),
  };
  await env.KV.put(
    SESSION_KEY_PREFIX + token,
    JSON.stringify(sessionData),
    { expirationTtl: SESSION_TTL_SEC }
  );
  return token;
}

// ============================================================
// Per-request status freshness check (mirrors intel pattern)
// ============================================================
async function statusOk(env, userId) {
  if (!env.DB) return true; // if DB not bound, skip (defensive; shouldn't happen in prod)
  try {
    const row = await env.DB.prepare(
      'SELECT stripe_status, access_expires_at FROM users WHERE id = ?'
    ).bind(userId).first();
    if (!row) return false;
    if (!['active', 'comp', 'free'].includes(row.stripe_status)) return false;
    if (row.access_expires_at) {
      const exp = new Date(row.access_expires_at);
      if (!Number.isNaN(exp.getTime()) && exp < new Date()) return false;
    }
    return true;
  } catch (e) {
    console.error('statusOk DB error', e);
    return false; // fail closed
  }
}

// ============================================================
// Redirect helpers
// ============================================================
function bridgeRedirect(originalUrl) {
  const ret = encodeURIComponent(originalUrl);
  return Response.redirect(
    'https://' + INTEL_HOST + '/auth/bridge?return=' + ret,
    302
  );
}

function upgradeRedirect() {
  return Response.redirect('https://' + INTEL_HOST + '/?upgrade=1', 302);
}

// ============================================================
// Origin proxy
// ============================================================
async function proxyOrigin(request, url) {
  // Map / -> /index.html etc., let GitHub Pages handle directory indexes natively.
  const originUrl = ORIGIN + url.pathname + url.search;
  const upstream = await fetch(originUrl, {
    method: request.method,
    headers: { 'User-Agent': 'brief-hormuz-worker/1.0' },
    cf: { cacheEverything: true, cacheTtl: 60 },
  });

  // Strip any origin-set cookies (defensive — GitHub Pages doesn't set any)
  const headers = new Headers(upstream.headers);
  headers.delete('Set-Cookie');
  // Mark as private so intermediaries don't cache authenticated content
  headers.set('Cache-Control', 'private, max-age=60');

  return new Response(upstream.body, { status: upstream.status, headers });
}

// ============================================================
// Main fetch handler
// ============================================================
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // --- Logout ---
    if (url.pathname === '/auth/logout') {
      const token = getCookie(request, COOKIE_NAME);
      if (token) await env.KV.delete(SESSION_KEY_PREFIX + token);
      return new Response(
        '<html><body style="font-family:sans-serif;padding:2rem;">' +
        '<p>Logged out of Hormuz Daily Brief.</p>' +
        '<p><a href="https://' + INTEL_HOST + '/">Return to intel.resilience-engineers.com</a></p>' +
        '</body></html>',
        {
          status: 200,
          headers: {
            'Content-Type': 'text/html',
            'Set-Cookie': clearedCookie(),
          },
        }
      );
    }

    // --- Bridge consumer (entry from intel) ---
    if (url.pathname === '/auth/consume') {
      const token = url.searchParams.get('token');
      const ret = url.searchParams.get('return') || '/';

      const payload = await verifyToken(env, token);
      if (!payload) {
        return new Response(
          '<html><body style="font-family:sans-serif;padding:2rem;">' +
          '<h2>Authentication failed</h2>' +
          '<p>The login link is invalid or has expired (60-second window). Please try again.</p>' +
          '<p><a href="https://' + INTEL_HOST + '/">Sign in at intel.resilience-engineers.com</a></p>' +
          '</body></html>',
          { status: 401, headers: { 'Content-Type': 'text/html' } }
        );
      }

      // Status check — refuse session creation if user is not entitled
      const ok = await statusOk(env, payload.userId);
      if (!ok) return upgradeRedirect();

      const sessionToken = await createSession(env, payload);
      // Only allow same-host paths (prevents open redirect)
      const cleanReturn = ret.startsWith('/') && !ret.startsWith('//') ? ret : '/';
      return new Response(null, {
        status: 302,
        headers: {
          'Location': cleanReturn,
          'Set-Cookie': buildSessionCookie(sessionToken, SESSION_TTL_SEC),
        },
      });
    }

    // --- Authenticated path: validate session, re-check status, proxy origin ---
    const session = await validateSession(env, request);
    if (!session) {
      return bridgeRedirect(request.url);
    }

    const ok = await statusOk(env, session.userId);
    if (!ok) {
      // Kill stale session
      await env.KV.delete(SESSION_KEY_PREFIX + session.token);
      return upgradeRedirect();
    }

    return proxyOrigin(request, url);
  },
};
