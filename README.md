# Hormuz Daily Brief — Operations

This folder is a complete daily intelligence brief system. It produces one HTML page (`index.html`) that can be hosted anywhere as a standalone file.

## Files in this folder

| File | Purpose |
|------|---------|
| `index.html` | **One-pager.** FORDEC overview · force majeure tracker · commodity wave timeline. The page most people read. |
| `brief.html` | **Deep dive.** Six categories · watchlist · scenarios · methodology · sources · calibration log. For analysts. Linked from the one-pager. |
| `methodology.md` | Operating manual — signal tiers, trend rules, threat levels, anti-bias defaults, learning loop. |
| `sources.md` | Tiered source list (Tier 1 primary → Tier 6 excluded). |
| `daily-update-prompt.md` | Procedure the daily agent runs. Also the manual-run prompt. |
| `knowledge-base.md` | **Slot for Marco's project-specific context.** Paste content from your Claude.ai "Iran Escalation" project here — especially force majeure positions and commodity-chain exposure profiles. |
| `backtest-log.md` | Predictions, T+1/T+3/T+7 scoring, weekly calibration, source reliability. |
| `daily-briefs\YYYY-MM-DD.md` | Daily archive of each published brief. |
| `daily-briefs\_template.md` | Template structure for new daily archives. |

## Two-page architecture

The public site has two pages, both regenerated each morning by the same scheduled run:

- **`index.html`** is the front door. FORDEC layout (Facts / Options / Risks / Decision / Execution / Check) plus a force majeure tracker and commodity wave timeline. Designed to fit on one screen.
- **`brief.html`** is the deep dive. Linked from the one-pager nav, contains the full six-category read, watchlist with directional implications, three-scenario probability outlook, and the methodology / sources / calibration sections collapsed.

The same headline indicators (trend, threat, day-of-war, date, last-updated) appear on both pages and are kept in sync by the daily run. The same design system applies to both — clean light theme, serif masthead, one accent color.

## How the daily run works

A scheduled task `hormuz-daily-brief` is registered with Claude Code and runs **every morning at 08:00 local time** (CET in winter, CEST in summer — cron `0 8 * * *` is evaluated in your local timezone).

Each run:
1. Reads methodology, sources, knowledge base, backtest log, yesterday's brief.
2. Scores yesterday's predictions (T+1), three-day-old (T+3), seven-day-old (T+7) — appends results to `backtest-log.md`.
3. WebSearches Tier 1–3 sources (UKMTO, MARAD, ISW, ICG, Kpler proxies, wire services).
4. Classifies inputs by signal tier; discards noise.
5. Scores all six categories, sets trend and threat level, writes 4–6 CEO talking points, builds 5-item watchlist, sets 3 scenarios with probabilities.
6. Edits the BRIEF:* blocks inside `index.html` — does not touch CSS or structure.
7. Archives yesterday's brief to `daily-briefs\YYYY-MM-DD.md`.
8. Appends today's predictions to `backtest-log.md`.
9. **Friday only** — runs Week-in-Review, computes Brier scores, logs one methodology delta and one source-weight adjustment.

You will get a notification when each run completes (notifyOnCompletion: true).

## Manual run

If the schedule misses or you want to force a regenerate:

1. Open Claude Code in this folder, or any session.
2. Paste the contents of `daily-update-prompt.md` into a new message.
3. The agent will follow the same procedure.

The scheduled task itself can also be triggered ad-hoc from the **Scheduled** section in the Claude Code sidebar — click the `hormuz-daily-brief` task and "Run now."

## Hosting options for the public page

The output is `index.html` — a self-contained file with no external dependencies. Pick whichever hosting matches your existing infrastructure:

### Option A — GitHub Pages (recommended for durability)
1. Create a new public GitHub repo (or use an existing one).
2. Add a workflow or commit `index.html` from this folder. The scheduled task can be extended to also `git push` (let me know and I'll wire it).
3. Enable GitHub Pages → URL becomes `https://<username>.github.io/<repo>/`.
4. Optional: point a subdomain (e.g., `hormuz.resilience-engineers.com`) at it via a CNAME record.

**Pros:** free, durable, version history, custom domain.
**Cons:** requires GitHub setup; the scheduled task needs to be told to push.

### Option B — Direct upload to your existing website
If `resilience-engineers.com` is on a host where you can SFTP/upload static files, drop `index.html` there at a known path (e.g., `/hormuz`). The scheduled task can be extended to push via SCP/FTP — tell me the host and I'll wire it.

**Pros:** lives at your own domain; no third-party dependency.
**Cons:** sync mechanism needs setup.

### Option C — OneDrive public link (simplest, ugly URL)
The file already lives in `C:\Users\Marco\OneDrive\Agentic Workflows\Scenario Planner\hormuz-tracker\index.html`. Right-click → Share → "Anyone with the link" → "Copy link." OneDrive will render it as a downloadable file by default; for in-browser preview, append `&embed=true` or use the "Open in browser" rendering.

**Pros:** zero setup; the file is already there and OneDrive auto-syncs each daily update.
**Cons:** ugly URL, OneDrive may not render HTML inline reliably for external users.

### Option D — Netlify Drop (drag-and-drop)
Go to `https://app.netlify.com/drop`, drag the folder onto the page. You get a URL in 30 seconds. Updates require re-dragging unless you wire the CLI.

**Pros:** fastest path to a public URL with a clean domain.
**Cons:** updates aren't automated unless you set up the CLI.

### Option E — Cloudflare Pages
Similar to GitHub Pages but Cloudflare's edge network. Can connect to a GitHub repo for automatic deploys.

**My recommendation:** Option A (GitHub Pages) for production durability + Option C (OneDrive) as a personal preview/backup. If you want, I can wire the scheduled task to commit + push to a GitHub repo each morning so the public page updates without you doing anything.

## Plugging in your "Iran Escalation" Claude.ai project

I can't read claude.ai project content from this environment. To bring your existing knowledge in:

1. Open `knowledge-base.md` in this folder.
2. From your Claude.ai "Iran Escalation" project, copy:
   - Any standing analytical frames, hypotheses, or assessments
   - Custom source lists or non-public input pointers
   - Stakeholder/CEO context you want the brief to address
   - Sector-specific exposure profiles (refined products / LNG / containers / chemicals)
   - Things to NOT do or NOT say
3. Paste into the corresponding sections in `knowledge-base.md`.

The agent will read this file every morning and apply the frames before drafting. Until you fill it, the agent operates from `methodology.md` + `sources.md` + your standing skills (resilience-doctrine, krisonomics, vester-systems, supply-chain-process-engineering, anti-ai-writing).

## Today's first brief

`index.html` already contains today's brief content (9 May 2026, day 70 of war). It was written from open-source Tier 1–3 inputs and follows the methodology. The first archive is `daily-briefs\2026-05-09.md`. The first backtest entry is in `backtest-log.md`.

Tomorrow's run will:
- Score today's predictions (W1, W2, W3, W4, W5; trend; threat level; scenarios).
- Update `index.html`.
- Archive today's brief to `daily-briefs\2026-05-10.md` (the date moves automatically — actually `daily-briefs\2026-05-09.md` is already created; tomorrow archives nothing new since it's already there. The first dynamic archive happens 11 May, archiving 10 May).

## Methodology evolution

Each Friday the brief logs one concrete methodology delta — a heuristic added, removed, or sharpened — based on the week's calibration. Changes are appended to:
- `methodology.md` Changelog (bottom)
- `sources.md` Source weighting log

Audit the trail any time. The system never silently learns.

## Editing the framework

If you want to change category names, add a 7th category, change the threat-level definition, or alter the scoring — edit `methodology.md` first, then update `index.html` to match the new structure. The daily prompt re-reads `methodology.md` each morning, so changes propagate automatically to subsequent runs.

To stop the scheduled task: open Claude Code → Scheduled section → toggle `hormuz-daily-brief` off.
To delete it: same panel, delete.
