# Daily Intelligence Tracker — Blueprint

A self-contained build manual for spinning up a daily auto-updating intelligence brief website, modelled on the Hormuz Daily Brief at https://resilienceengineers.github.io/hormuz-daily-brief/. Paste this whole document into a fresh Claude Code session in an empty folder, fill in the **Use case profile** block at the top, and Claude will build the full system end-to-end.

## What you get

- A public website hosted on GitHub Pages with a clean URL
- A one-pager dashboard (status board + map + domain widgets) at the URL
- A deep-brief secondary page (full categories, watchlist, scenarios)
- A geographic threat map (Leaflet + OpenStreetMap, no paid APIs)
- Domain-specific widgets adapted to the topic (e.g., commodity tracker, force-majeure tracker, transit stats — pick what fits)
- Daily auto-update via GitHub Actions calling the Claude API
- An "Export PDF for management" button producing a 10-slide branded PDF
- A private internal calibration loop (predictions tested against outcomes; methodology updates weekly)

## How to use

1. Open Claude Code in an empty folder you control (e.g., `C:\Users\you\Documents\new-tracker\`).
2. Fill in the **Use case profile** block below — that's your only writing task.
3. Paste this entire document into a fresh chat.
4. Claude executes the build. You'll be asked to: install GitHub CLI if absent, run `gh auth login` once, generate an Anthropic API key, and paste it into the new repo's Actions secrets. ~10–15 min total including your inputs.

---

# Use case profile — fill in before pasting

```
TRACKER NAME:           [e.g., "European Energy Crisis Brief", "AI Regulation Tracker"]
TOPIC ONE-LINER:        [10–20 word description]
PRIMARY AUDIENCE:       [e.g., "supply chain executives", "compliance officers at energy utilities"]
GEOGRAPHIC SCOPE:       [e.g., "EU + UK + Norway", "South China Sea", "global"]
TIME WINDOW:            [trend window — default "trailing 72h vs prior 72h"; can be weekly]
DAY-COUNT ANCHOR:       [optional — e.g., "war started 28 Feb 2026" enables Day-N counter; or leave blank]

SIX CATEGORIES:         [adapt to topic — defaults work for most crisis trackers]
  1. [Operational disruption / supply / flow]
  2. [Enforcement / kinetic / regulatory action]
  3. [Diplomatic / stakeholder / policy posture]
  4. [Asset / infrastructure damage or change]
  5. [Alternative routes / workarounds / substitutes]
  6. [Outlook scenarios — 3 scenarios summing to 100%]

DOMAIN WIDGETS:         [3–5 unique to this topic — for Hormuz: vessel transit stats / force majeure tracker / commodity cascade timeline / threat map. Pick equivalents for yours.]

THREAT-LEVEL DOMAIN:    [optional rename — default "Threat" 1–5; could be "Risk", "Disruption", "Compliance", etc. Define what each level means for the topic.]

KEY SOURCES (PRIVATE):  [the kinds of outlets that matter — central bank releases / industry trade press / specific government agencies / etc. Stays in sources.md, not exposed publicly.]

BRAND:                  [your company name — appears on PDF every-page footer]
CONTACT EMAIL:          [shown on PDF cover and site footer]
GITHUB OWNER:           [your GitHub account or org]
GITHUB REPO NAME:       [kebab-case, e.g., "ai-regulation-tracker"]
SCHEDULE LOCAL TIME:    [default 08:00 CEST — translates to 06:00 UTC primary cron slot]
ACCENT COLOR:           [optional — default deep red #a4242a; can be navy #1e3a5f, dark green #1f5132, etc.]
```

---

# Build instructions for Claude

You are setting up a daily intelligence tracker following the architecture below. **Read the Use case profile** the user filled in. If essential fields are blank, ask **one consolidated round** of questions, then proceed without further check-ins. Build in this order, committing along the way.

## Stage 1 — Repo setup

1. `git init` in the current folder, set local user identity to the user's name + email.
2. Create `.gitignore` (OS files, editor caches, `.env`).
3. Create `LICENSE` (MIT, owner = `BRAND` from profile).
4. Verify `gh` CLI is installed. On Windows: `& "C:\Program Files\GitHub CLI\gh.exe" --version`. If absent, instruct: `winget install --id GitHub.cli -e --accept-source-agreements --accept-package-agreements`, then `gh auth login` in a fresh PowerShell. Pause until user confirms `gh auth status` shows logged in.
5. First commit: `git add .` + commit "Initial scaffold".
6. Create public GitHub repo: `gh repo create [GITHUB REPO NAME] --public --description "[TOPIC ONE-LINER]" --source . --remote origin --push`.
7. Enable Pages: `gh api -X POST /repos/[OWNER]/[REPO]/pages -f "source[branch]=main" -f "source[path]=/"`.
8. Capture and tell the user the live URL: `https://[owner-lowercased].github.io/[repo]/`.

## Stage 2 — Operating files (markdown, repo root)

### `methodology.md`
Full private methodology. Includes:
- Signal tier weights: **Hard ×5** (verified physical events / official orders / data), **Medium ×3** (orders from authorized voices not yet acted on with verifiable consequence), **Soft ×1** (statements not yet acted on), **Noise ×0** (anonymous, op-eds, social, AI summaries)
- Trend rule: trailing 72h vs prior 72h — Worse if ≥2 Hard escalation events with no offsetting de-escalation OR 1 regime-change event; Same if mixed/no Hard signals; Better if ≥1 Hard de-escalation event AND no offsetting escalation
- Threat level 1–5 scale with **explicit and consistent triggers** at each level. Levels 4 and 5 must use the same operative test in both criteria and trigger language. Adapt thresholds to the topic.
- Anti-bias defaults: base rates first, convexity beats consensus, Lindy on tensions and anti-Lindy on novelty, "no news ≠ no event," asymmetric updating (Popper), no hindsight reframing, authority-bias check
- Learning loop: T+1 / T+3 / T+7 prediction scoring, Friday Brier-score calibration, methodology delta logged with date and reason
- Stop conditions: insufficient Tier 1–3 input → write thin INTERIM brief, never publish unsourced claims as Hard

### `sources.md`
Six-tier source list adapted to the topic. Specifics stay private — the public site shows only meta categories.
- **Tier 1** — primary, official, verifiable (the most important first-party sources for this topic)
- **Tier 2** — specialized commercial intelligence with operational track record (data providers, AIS-style trackers, specialized intelligence services)
- **Tier 3** — analytical institutions with rigorous publication standards
- **Tier 4** — commercial analysts and columnists with multi-year track records
- **Tier 5** — wire services and reputable regional/sector press
- **Tier 6** — excluded by default (anonymous OSINT, op-eds, social, AI-summaries) — admitted only after Tier 1–3 corroboration

### `knowledge-base.md`
Template the user fills in over time. Sections: analytical frames, stakeholder context, prior assessments, sector exposure profile, internal sources, glossary, things-not-to-do.

### `backtest-log.md`
Internal calibration log. Header explains the loop. Tracks daily predictions, T+1 / T+3 / T+7 scoring (Hit / Miss / False alarm / Surprise), weekly Brier on scenario probabilities, source reliability tally, methodology deltas. **Never displayed publicly.**

### `daily-update-prompt.md`
Canonical procedure for the daily run. Steps: read context files, score yesterday's predictions before drafting today's, web-search Tier 1–3, classify signals, score categories, set trend + threat, draft 3 actions / 5 watchlist items / 3 scenarios, write block content. Tone rules: practitioner not narrator; lead with fact, then why, then so-what; no AI tells; numbers when available, ranges when not. Stop conditions and output checklist at the end.

### `daily-briefs/_template.md`
Template for daily archives. Mirrors the deep brief structure.

### `README.md`
Operations doc: file table, two-page architecture, hosting options, how the daily run works.

## Stage 3 — HTML pages

### `index.html` — one-pager dashboard

This is the URL the user shares. Layout (top to bottom):

1. **Masthead** — title (with one accent-color word), day-count if anchor set, date, last-updated, nav linking to deep brief / methodology / sources, **"Export PDF for management" button**
2. **Hero strip** (3 cells, full-width row) — Trend (arrow + label + confidence), Threat level (1–5 with dot row indicator), Today in one line (serif italic)
3. **Dashboard grid** (~60% / ~40% split) — Map left, 6-tile status board right
4. **Domain widgets row** (full-width, 2–3 columns) — e.g., transit stats / metric tiles
5. **Today's posture · 3 actions** — numbered list, big text, operational verbs
6. **Watchlist · 24–72h** — 5 items, each with deadline + directional implication
7. **Domain tracker section** (optional, e.g., FM tracker) — clean status table
8. **Cascade timeline** (optional, e.g., commodity wave) — T+0 / T+7 / T+30 / T+90 grid
9. **More-link** to deep brief
10. **Footer** with brand contact

Design system:
- Light, newspaper feel — white background, near-black text (`#14171c`), one accent color (default deep red `#a4242a`, override per profile)
- Serif masthead (Iowan Old Style → Palatino → Times fallback)
- Sans-serif body (system stack)
- Mono for labels, dates, status pips
- Status colors used sparingly: red `#c1272d`, amber `#b67a08`, green `#2c7a4a`
- Generous whitespace; no shadows, no gradients, no decoration that doesn't earn its place

### `brief.html` — deep brief

Linked from one-pager nav. Same masthead style, links back. Contains:
- Headline section (trend, threat, summary paragraph 2–4 sentences)
- 6 category articles, each with: head row (number, title, badge, arrow, confidence), 3 signal bullets, "Why this matters" paragraph, "Implication" paragraph (border-left accent), sources line
- Watchlist (full)
- Scenario outlook (3 scenarios with bars summing to 100%)
- **Methodology section: ONE paragraph meta-level only.** Example wording: *"This brief uses a tiered signal-weighting framework. Only verified physical events from primary sources can move the threat assessment. Trend movement requires confirmed change versus the prior 72 hours. The system continuously calibrates against outcomes — when predictions miss, the underlying heuristics are sharpened. The full operating ruleset is kept private to preserve analytical edge."*
- **Sources section: tier categories only**, no specific outlet names. Six tiers with one-line descriptions of the kinds of outlets each contains.
- **NO public calibration section.** Calibration data flows internally to `backtest-log.md` only.

### Map (Leaflet + OpenStreetMap)

Use Leaflet 1.9.4 from unpkg with CartoDB Positron tile layer (clean editorial style):

```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
      integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
        integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
```

```javascript
const map = L.map('map', { scrollWheelZoom: false, attributionControl: true, zoomControl: true });
map.fitBounds([[lat_south, lon_west], [lat_north, lon_east]]);
L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; OpenStreetMap &copy; CARTO',
  subdomains: 'abcd', maxZoom: 19
}).addTo(map);
```

Pins are color-coded by status (red/amber/green) using `L.circleMarker` with `radius: 6, color: '#fff', weight: 1.8, fillColor: <status color>, fillOpacity: 1`. Polylines for routes/pipelines (thicker, status-colored). Choke/risk zones via `L.circle` with `weight: 0, fillOpacity: 0.10`.

The pins live in a JS array bracketed by `// BRIEF:MAP_PINS_START` and `// BRIEF:MAP_PINS_END` comments — the daily updater edits this array.

### PDF export — 10 branded slides via print CSS

Use **print CSS only** (no html2canvas / external PDF libs — they have CORS issues with map tiles and bloat the bundle). The PDF is generated by the browser's built-in "Save as PDF" function via `window.print()`.

Architecture:
- A `<div class="pdf-export">` after `</main>` contains 10 `<section class="pdf-slide">` elements
- On screen: `.pdf-export { display: none; }`
- On print: `body > *:not(.pdf-export) { display: none !important; } .pdf-export { display: block !important; }`
- `@page { size: A4 landscape; margin: 0; }`
- Each slide: `width: 297mm; height: 210mm; page-break-after: always; page-break-inside: avoid; overflow: hidden; box-sizing: border-box; display: flex; flex-direction: column;`
- **Last slide MUST have** `:last-child { page-break-after: auto; }` to avoid a trailing blank page

Each slide structure:
- **Top header (~14mm)**: BRAND wordmark left in red small-caps, "Tracker Name · [date]" right, thin red rule below
- **Center content** (`.ps-content`, `flex: 1`)
- **Bottom footer (~10mm)**: brand contact left, page number "N / 10" right

10 slides:
1. **Cover** — eyebrow "[TOPIC] · DAILY BRIEF", big serif title, **prominent assessment date and time** (large red serif "9 May 2026", below "06:00 UTC / 08:00 CEST · Day N"), 3-column key row (threat / trend / executive line), brand footer
2. **Executive summary** — slide title, full summary paragraph in large serif, key metric stats below
3. **Status board** — 6-category 3×2 grid
4. **Key sites / focal points** — 3-column geographic exposure list (auto-built from map pins via JS at beforeprint)
5. **Recommended posture** — 3 actions in big consultancy format (huge serif numbers, bold leads)
6. **Watchlist** — 5 items in clean grid (number / body / deadline)
7. **Scenarios** — 3 scenarios horizontal, each with name, big probability number, bar, observable, implication
8. **Domain tracker** (e.g., FM table)
9. **Cascade timeline**
10. **Methodology + sources + about** — meta-level summary, six-tier descriptions, brand contact

Slide content syncs from the visible page via `window.addEventListener('beforeprint', syncPdfSlides)`. The function clones DOM elements (scoreboard tiles, watchlist, FM table, wave grid) and rebuilds slide containers from those cloned elements plus a few hand-extracted values (cover threat/trend/oneliner). The map slide does NOT render the live Leaflet map (won't print cleanly) — instead it renders a 3-column "Key sites" list built from the `pinsConfig` array.

### BRIEF:* markers

Both HTML files use HTML-comment markers to delimit blocks the daily updater replaces:

```html
<!-- BRIEF:CATEGORY_1_START -->
<article class="cat">...</article>
<!-- BRIEF:CATEGORY_1_END -->
```

Markers are GLOBAL — if the same key appears in both `index.html` and `brief.html` (e.g., `DATE`), the updater replaces both occurrences with the same content. Two pages stay in sync without duplicate work for the agent.

Required keys (adapt names to topic):
- Headline metadata: `DATE`, `DAY` (if anchor set), `LAST_UPDATED`, `MAP_TS`
- Indicators: `TREND`, `THREAT`, `ONELINER`, `SUMMARY`
- Status board (one-pager): `TILE_1` through `TILE_6`
- Map pins: `MAP_PINS` (JS array contents — daily updater edits this)
- Posture: `ACTIONS`
- Watchlist: `WATCHLIST`
- Scenarios: `SCENARIOS`
- Categories (deep brief): `CATEGORY_1` through `CATEGORY_6`
- Domain widgets: e.g., for Hormuz `FM`, `WAVE`, `VESSEL_HORMUZ`, `VESSEL_BAB_MANDEB` — adapt to topic

## Stage 4 — Automation

### `.github/workflows/daily-brief.yml` — triple cron + skip-guard

```yaml
name: Daily Brief Update

on:
  schedule:
    - cron: '0 6 * * *'    # 06:00 UTC primary
    - cron: '30 7 * * *'   # 07:30 UTC backup
    - cron: '0 10 * * *'   # 10:00 UTC last-chance
  workflow_dispatch:

permissions:
  contents: write

concurrency:
  group: daily-brief
  cancel-in-progress: false

jobs:
  update:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 5 }

      - name: Skip if today's brief already published
        id: skip
        shell: bash
        run: |
          TODAY=$(date -u +%Y-%m-%d)
          LAST=$(git log --oneline --grep="Daily brief update" -1 --pretty=format:"%s" || echo "")
          if [[ "$LAST" == *"$TODAY"* ]]; then
            echo "skip=true" >> "$GITHUB_OUTPUT"
          else
            echo "skip=false" >> "$GITHUB_OUTPUT"
          fi

      - if: steps.skip.outputs.skip != 'true'
        uses: actions/setup-python@v5
        with: { python-version: '3.12' }

      - if: steps.skip.outputs.skip != 'true'
        run: pip install -r .github/scripts/requirements.txt

      - if: steps.skip.outputs.skip != 'true'
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: python .github/scripts/update_brief.py

      - if: steps.skip.outputs.skip != 'true'
        run: |
          git config user.name "Brief Bot"
          git config user.email "actions@github.com"
          git add -A
          if git diff --quiet --cached; then
            echo "No changes."
          else
            git commit -m "Daily brief update: $(date -u +%Y-%m-%d)"
            git push
          fi
```

### `.github/scripts/requirements.txt`
```
anthropic>=0.45.0,<1.0
```

### `.github/scripts/update_brief.py`

Key constants and patterns (full implementation should follow these):

```python
MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-4-6")
MAX_OUTPUT_TOKENS = int(os.environ.get("CLAUDE_MAX_TOKENS", "24000"))
MAX_WEB_SEARCHES = int(os.environ.get("CLAUDE_MAX_SEARCHES", "12"))

# Trim aggressively for token efficiency
MAX_BACKTEST_CHARS = 6000
MAX_LAST_ARCHIVE_CHARS = 5000
MAX_METHODOLOGY_CHARS = 4000
MAX_SOURCES_CHARS = 1500
MAX_KNOWLEDGE_CHARS = 6000
MAX_HTML_PER_FILE_CHARS = 12000
```

```python
def compress_html_for_context(html: str) -> str:
    """Strip <style>, <script> (except MAP_PINS), long style attrs.
    Saves ~70% of tokens vs raw HTML."""
    s = re.sub(r"<style[^>]*>.*?</style>", "<!-- styles omitted -->", html, flags=re.DOTALL)
    def script_repl(m):
        return m.group(0) if "BRIEF:MAP_PINS" in m.group(0) else "<!-- script omitted -->"
    s = re.sub(r"<script[^>]*>.*?</script>", script_repl, s, flags=re.DOTALL)
    s = re.sub(r'\s+style="[^"]{120,}"', "", s)
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", s)
```

**Output format from Claude must use delimiter blocks**, NOT JSON. Reason: JSON-escape errors fail at scale (a single unescaped `"` in 30KB of HTML strings breaks the parse).

```
###BEGIN:KEY###
raw HTML / JS / markdown — any characters allowed, no escaping
###END:KEY###
```

Parser:
```python
_BLOCK_RE = re.compile(r"###BEGIN:([A-Z0-9_]+)###\s*\n(.*?)\n\s*###END:\1###", re.DOTALL)
def parse_delimited(text: str) -> dict[str, str]:
    return {m.group(1): m.group(2) for m in _BLOCK_RE.finditer(text)}
```

**Use streaming** (required for `max_tokens >= 24000`):
```python
with client.messages.stream(
    model=MODEL,
    max_tokens=MAX_OUTPUT_TOKENS,
    system=system_prompt,
    messages=[{"role": "user", "content": user_prompt}],
    tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": MAX_WEB_SEARCHES}],
) as stream:
    final = stream.get_final_message()
text = "\n".join(b.text for b in final.content if getattr(b, "type", None) == "text").strip()
```

**BRIEF:* block replacement** in HTML:
```python
def replace_block(html: str, key: str, content: str) -> tuple[str, int]:
    pattern = re.compile(
        rf"(<!-- BRIEF:{re.escape(key)}_START -->)(.*?)(<!-- BRIEF:{re.escape(key)}_END -->)",
        re.DOTALL,
    )
    return pattern.subn(lambda m: m.group(1) + "\n" + content.strip() + "\n" + m.group(3), html)
```

**Title update — must use lambda** (NOT raw string), digits in date misread as backreferences:
```python
re.sub(rf"(<title>{re.escape(prefix)}).*?(</title>)",
       lambda m: m.group(1) + date_human + m.group(2),
       s, count=1)
```

**Sanity check after edits**: count `<!-- BRIEF:*_START -->` and `<!-- BRIEF:*_END -->` markers in each file — must balance. Fail loud if they don't.

System prompt structure:
- Encode the full daily-update-prompt procedure inline (don't send the file separately — saves tokens)
- Specify the OUTPUT FORMAT contract (delimiter blocks, full key list, format spec for each block)
- Stop conditions: set `INTERIM=true` if Tier 1–3 input insufficient; do NOT publish unsourced claims
- Tone rules

User message structure (the dynamic context):
- Procedure ref: "(See system prompt — full procedure encoded there.)"
- Methodology (trimmed)
- Sources (trimmed)
- Knowledge base (trimmed)
- Backtest log recent entries (trimmed)
- Latest archived brief (trimmed)
- Current `index.html` (compressed + trimmed)
- Current `brief.html` (compressed + trimmed)
- "Now: produce today's brief. Score yesterday's predictions before drafting today's. Output only the delimiter blocks."

After parsing, the script:
1. Validates all expected block keys present (else fail with response head/tail printed)
2. Applies BRIEF:* replacements to both HTML files
3. Updates `<title>` tags via lambda re.sub
4. Archives yesterday's brief to `daily-briefs/YYYY-MM-DD.md`
5. Appends today's predictions to `backtest-log.md`
6. Sanity-checks BRIEF:* markers balance
7. Returns 0 on success, non-zero on any failure (workflow fails visibly)

## Stage 5 — Final steps

1. Commit and push the workflow + script.
2. Tell the user: generate Anthropic API key at console.anthropic.com/settings/keys, add as repo secret `ANTHROPIC_API_KEY` at `https://github.com/[OWNER]/[REPO]/settings/secrets/actions/new`. Pause for confirmation.
3. Trigger workflow once via `gh workflow run daily-brief.yml`. Watch with `gh run watch <id> --exit-status`.
4. If success: confirm live URL renders today's brief.
5. Document next steps: tomorrow's run fires automatically; user can fill `knowledge-base.md` over time; PDF button works on the live site; Pages rebuilds within 1–2 min of each commit.

---

# Architectural patterns (apply strictly)

**DO use delimiter-based output, NOT JSON.** JSON escape errors fail at scale.

**DO use streaming** when `max_tokens >= 24000`. SDK enforces this.

**DO use lambda for `re.sub`** when replacement strings contain digits.

**DO keep methodology private.** Public page shows ONE paragraph meta-description. Specifics stay in `methodology.md`.

**DO keep calibration internal.** Backtest log is for the agent's learning, not public.

**DO trim HTML aggressively** before sending to Claude. Strip `<style>`, `<script>` (except MAP_PINS), long `style=` attrs, blank lines.

**DO use Sonnet 4.6 for daily ops.** Opus is overkill — same quality, 5× cheaper.

**DO use triple cron with skip-guard.** GitHub Actions schedules are best-effort; one slot is unreliable.

**DO use the same BRIEF:* markers in both HTML files** for shared content (date, day, indicators) — the updater handles all occurrences in one pass.

**DO add a `:last-child { page-break-after: auto }`** on print slides to kill the trailing blank page.

# Pitfalls (real failures from the Hormuz build — save yourself the time)

1. **JSON output fails on large HTML.** A single unescaped `"` in 30KB of strings breaks the parse. → use delimiters.
2. **`re.error: invalid group reference`** when `date_human` starts with a digit. → use lambda for `re.sub`.
3. **`max_tokens` triggers SDK 10-min timeout error** in non-streaming mode. → use `client.messages.stream(...)`.
4. **First scheduled cron drops** with no error message and no run. → triple cron with skip-guard.
5. **Hand-coded SVG coastlines look amateur** even with effort. → use OpenStreetMap via Leaflet.
6. **Blank pages in PDF** from competing `page-break-before` and `page-break-after` rules. → only `page-break-after: always` on each slide; `:last-child { page-break-after: auto }`.
7. **`html2canvas`/`jsPDF` choke on Leaflet tiles** due to CORS. → don't try to embed live maps in PDF; use a "Key sites" table built from the pins array.
8. **Race conditions** between local edits and the daily bot's commits. → always `git pull --rebase` before pushing local changes; treat HTML files / archives / backtest-log as bot-owned, your edits go to workflows / scripts / methodology / design.
9. **Threat-level criteria and trigger language drifting apart** (e.g., criteria say "de-facto closure" → 5, but trigger says "formal closure announcement" → 5). → write the level-N→N+1 boundary as a single operative test that appears in both criteria and trigger.

# What's NOT in this blueprint (ask Claude separately if needed)

- Custom domain (CNAME) setup
- Live API integrations to paid data providers (AIS, ADS-B subscription feeds)
- Multilingual versions
- Email / Slack notifications when threat level changes
- Authentication / paywall
- Mobile app

---

That's everything. Save this file, copy it whole, fill in the **Use case profile** at the top, paste into a fresh Claude Code session in an empty folder. Build time ~10–15 min including your one-time API-key + repo-secret step. The daily run starts the next morning automatically.
