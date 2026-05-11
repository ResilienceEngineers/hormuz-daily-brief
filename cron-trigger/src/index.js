/**
 * daily-brief-trigger — Cloudflare Worker with Cron Triggers.
 *
 * Fires the GitHub Actions `daily-brief.yml` workflow every morning via the
 * GitHub REST API workflow_dispatch endpoint. More reliable than GitHub's own
 * scheduled workflows (which are best-effort and frequently delayed/dropped).
 *
 * Cloudflare cron fires at 06:00 UTC daily. The GitHub Actions workflow has
 * its own skip-guard: if today's brief is already published, the run exits in
 * <10 seconds. Adding this Worker on top of the existing 6 GitHub cron slots
 * is purely additive — first trigger of the day publishes, rest no-op.
 *
 * Secrets (set via `wrangler secret put`):
 *   GITHUB_TOKEN  — fine-grained PAT with actions:write on the target repo
 */

const REPO = 'ResilienceEngineers/hormuz-daily-brief';
const WORKFLOW = 'daily-brief.yml';
const REF = 'main';

async function triggerGitHub(env) {
  const url = `https://api.github.com/repos/${REPO}/actions/workflows/${WORKFLOW}/dispatches`;
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.GITHUB_TOKEN}`,
      'Accept': 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
      'User-Agent': 'daily-brief-trigger/1.0',
    },
    body: JSON.stringify({ ref: REF, inputs: {} }),
  });

  if (!response.ok) {
    const body = await response.text();
    throw new Error(`GitHub API ${response.status}: ${body.slice(0, 400)}`);
  }
  return response.status; // 204 on success
}

export default {
  // Cloudflare cron handler — fires on the schedule in wrangler.toml
  async scheduled(event, env, ctx) {
    const now = new Date().toISOString();
    try {
      const status = await triggerGitHub(env);
      console.log(`[${now}] Triggered ${WORKFLOW} on ${REPO} (HTTP ${status})`);
    } catch (e) {
      console.error(`[${now}] Trigger failed: ${e.message}`);
      throw e; // Cloudflare marks the cron run as failed and surfaces in dashboard
    }
  },

  // Status / diagnostic page (no auth — read-only info, no secrets exposed)
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Optional manual-trigger endpoint, gated by a secret query key
    if (url.pathname === '/trigger' && env.MANUAL_TRIGGER_KEY) {
      if (url.searchParams.get('key') !== env.MANUAL_TRIGGER_KEY) {
        return new Response('Unauthorized', { status: 401 });
      }
      try {
        const status = await triggerGitHub(env);
        return new Response(`Triggered ${WORKFLOW} (HTTP ${status})`, { status: 200 });
      } catch (e) {
        return new Response(`Failed: ${e.message}`, { status: 500 });
      }
    }

    return new Response(
      'daily-brief-trigger · cloudflare cron worker\n\n' +
      'Schedule:  06:00 UTC daily (08:00 CEST)\n' +
      'Repo:      ' + REPO + '\n' +
      'Workflow:  ' + WORKFLOW + '\n\n' +
      'Scheduled trigger fires automatically. For manual trigger use:\n' +
      '  gh workflow run ' + WORKFLOW + ' --repo ' + REPO + '\n\n' +
      'Or if MANUAL_TRIGGER_KEY is set:\n' +
      '  GET /trigger?key=<secret>\n',
      { status: 200, headers: { 'Content-Type': 'text/plain; charset=utf-8' } }
    );
  },
};
