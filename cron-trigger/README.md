# daily-brief-trigger · Cloudflare cron Worker

Cloudflare Workers Cron Triggers fire reliably — unlike GitHub Actions scheduled workflows, which are best-effort and frequently delayed or dropped (we hit two missed mornings in a row). This Worker fires every day at 06:00 UTC and calls GitHub's REST API to dispatch the `daily-brief.yml` workflow on `ResilienceEngineers/hormuz-daily-brief`.

The GitHub side's 6 cron slots stay in place as belt-and-suspenders. If Cloudflare ever has its own outage, GitHub still fires. If GitHub's scheduler drops every slot (today's failure mode), Cloudflare publishes the brief. Two independent schedulers — the system stays up if either survives.

## Deploy steps (one-time)

### 1 · Generate a GitHub fine-grained PAT

1. Open https://github.com/settings/personal-access-tokens/new
2. Token name: `cloudflare-cron-trigger-hormuz`
3. Expiration: **1 year** (or longer; rotate manually before expiry)
4. Resource owner: **ResilienceEngineers**
5. Repository access: **Only select repositories** → tick `hormuz-daily-brief`
6. Repository permissions → expand → set:
   - **Actions: Read and write**
   - Leave everything else as "No access"
7. Click **Generate token** at the bottom
8. **Copy the token** — starts with `github_pat_...`. You'll only see it once.

### 2 · Deploy the Worker

From this directory (`cron-trigger/`):

```
wrangler deploy
```

If wrangler asks you to log in, run `wrangler login` first (one-time browser auth).

### 3 · Set the GitHub token as a secret

```
wrangler secret put GITHUB_TOKEN
```

Paste the token from Step 1 when prompted.

### 4 · Test it immediately

Don't wait for tomorrow's cron to verify. Trigger the Worker's scheduled handler manually:

```
wrangler triggers deploy
```

Or just visit the Worker URL in a browser — the GET handler shows status info. Then verify in GitHub:

```
gh run list --workflow=daily-brief.yml --limit 3
```

You should see a new `workflow_dispatch`-event run started seconds after you triggered the Worker.

### 5 · Verify tomorrow's run

Tomorrow morning at 06:00 UTC (08:00 CEST), the cron should fire automatically. Check:

```
wrangler tail   # streams live Worker logs
```

Or check the Cloudflare dashboard → Workers & Pages → `daily-brief-trigger` → Logs.

## What this Worker does NOT do

- It does NOT run the brief itself. It just calls GitHub's API to trigger the existing workflow.
- It does NOT bypass the skip-guard. If today's brief is already published (by anyone), the GitHub workflow exits in <10 sec and no API cost is incurred.
- It does NOT replace the 6 GitHub cron slots. Those stay in place as backup; if Cloudflare ever fails, GitHub fires. The skip-guard ensures only the first successful trigger of the day pays for the brief.

## Rotation reminder

The GitHub PAT expires in 12 months (whatever you set). Add a calendar reminder for 11 months from now to rotate it. To rotate:

1. Generate a new PAT (Step 1 above).
2. `wrangler secret put GITHUB_TOKEN` — paste the new value.
3. Delete the old PAT from GitHub.

## Cost

Cloudflare Workers free tier: 100,000 requests/day. This Worker fires once daily plus diagnostic GETs — well within free.
