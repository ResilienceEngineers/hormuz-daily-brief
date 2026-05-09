#!/usr/bin/env python3
"""
Daily Hormuz Brief updater.

Run by GitHub Actions at ~06:00 UTC every day. Reads the operating files
(methodology.md, sources.md, knowledge-base.md, backtest-log.md,
daily-update-prompt.md) plus the current index.html and brief.html, calls
Claude with web_search enabled, and applies the returned content to:
  - index.html  (one-pager, FORDEC + status board)
  - brief.html  (deep dive, six categories + sources + calibration)
  - daily-briefs/YYYY-MM-DD.md  (yesterday's archive)
  - backtest-log.md  (predictions + scoring of T+1, T+3, T+7)

Output format from Claude: delimiter-based blocks of the form

    ###BEGIN:KEY###
    raw content (HTML, JS, markdown — no escaping needed)
    ###END:KEY###

This avoids the JSON-escape fragility that fails on ~30KB of HTML strings.
"""

import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from anthropic import Anthropic

ROOT = Path(__file__).resolve().parents[2]  # repo root from .github/scripts/

MODEL = os.environ.get("CLAUDE_MODEL", "claude-opus-4-7")
MAX_OUTPUT_TOKENS = int(os.environ.get("CLAUDE_MAX_TOKENS", "32000"))
MAX_WEB_SEARCHES = int(os.environ.get("CLAUDE_MAX_SEARCHES", "15"))

# War start anchor (28 Feb 2026 = day 1).
WAR_START = datetime(2026, 2, 28, tzinfo=timezone.utc)

# BRIEF:* markers that the daily run must replace inside the HTML files.
EXPECTED_BLOCK_KEYS = {
    # Headline / metadata (shared)
    "DATE", "DAY", "LAST_UPDATED", "MAP_TS",
    "TREND", "THREAT",
    # One-pager only
    "ONELINER", "TILE_1", "TILE_2", "TILE_3", "TILE_4", "TILE_5", "TILE_6",
    "ACTIONS", "FM", "WAVE", "MAP_PINS",
    # Shared
    "WATCHLIST",
    # Deep brief only
    "SUMMARY",
    "CATEGORY_1", "CATEGORY_2", "CATEGORY_3", "CATEGORY_4", "CATEGORY_5", "CATEGORY_6",
    "SCENARIOS", "BACKTEST",
}

# Top-level meta keys (not BRIEF:* HTML markers — used to write archive / backtest).
META_KEYS = {"INTERIM", "ARCHIVE_FILENAME", "ARCHIVE_MARKDOWN", "BACKTEST_APPEND"}


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, content: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def replace_block(html: str, key: str, content: str) -> tuple[str, int]:
    """Replace content between <!-- BRIEF:KEY_START --> and <!-- BRIEF:KEY_END -->.

    Returns (new_html, count_of_replacements).
    """
    pattern = re.compile(
        rf"(<!-- BRIEF:{re.escape(key)}_START -->)(.*?)(<!-- BRIEF:{re.escape(key)}_END -->)",
        re.DOTALL,
    )
    inner = "\n" + content.strip() + "\n"
    new_html, n = pattern.subn(lambda m: m.group(1) + inner + m.group(3), html)
    return new_html, n


def vienna_now(now_utc: datetime) -> tuple[datetime, str]:
    """Approximate Vienna local time. CEST (UTC+2) Apr–Oct, CET (UTC+1) Nov–Mar."""
    is_summer = 4 <= now_utc.month <= 10
    offset = timedelta(hours=2 if is_summer else 1)
    return now_utc + offset, ("CEST" if is_summer else "CET")


def humanize_date(dt: datetime) -> str:
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return f"{dt.day} {months[dt.month - 1]} {dt.year}"


def build_prompts(context: dict) -> tuple[str, str]:
    today_str = context["today_str"]
    yesterday_str = context["yesterday_str"]
    human_date = context["human_date"]
    last_updated = context["last_updated"]
    day_of_war = context["day_of_war"]
    utc_hm = context["utc_hm"]

    block_keys_list = sorted(EXPECTED_BLOCK_KEYS)
    block_lines = "\n".join(f"  - {k}" for k in block_keys_list)

    system_prompt = f"""You are producing today's Hormuz Daily Brief for Marco Felsberger
(resilience-engineers.com), published at https://resilienceengineers.github.io/hormuz-daily-brief/.

Today: {human_date}, day {day_of_war} of the US/Israel-Iran war.
Last-updated stamp: {last_updated}.
Yesterday (for archiving): {yesterday_str}.

You operate strictly under the procedure in `daily-update-prompt.md` (provided in the user message).
Apply it without shortcuts.

Use web search aggressively but disciplined. Pull from Tier 1-3 sources first
(UKMTO, MARAD, ISW, ICG, Reuters/AP, AJ live blogs). Cap at ~{MAX_WEB_SEARCHES} searches.
A claim that moves the trend assessment or threat level requires >=1 Hard source
AND >=1 independent Tier 1-3 corroboration. Without both, put the item on the
watchlist as "unconfirmed" rather than into the brief content.

OUTPUT FORMAT — delimiter blocks, no JSON, no code fences

Your final response is a sequence of delimiter blocks. Each block has this exact shape:

    ###BEGIN:KEY###
    raw content here, any characters allowed (HTML, JS, markdown, quotes,
    backslashes, newlines — everything is literal)
    ###END:KEY###

The KEY is uppercase letters, digits, and underscores only.
Do NOT use JSON. Do NOT use markdown code fences.
Do NOT escape characters inside the content — write HTML and JS verbatim.

You MUST emit exactly these blocks (one per key):

{block_lines}

Plus these meta blocks:

  - INTERIM           (the literal text "true" or "false")
  - ARCHIVE_FILENAME  (e.g. "{yesterday_str}.md")
  - ARCHIVE_MARKDOWN  (the full markdown of YESTERDAY'S brief, structured per daily-briefs/_template.md)
  - BACKTEST_APPEND   (markdown to append under today's date in backtest-log.md;
                       includes scoring of T+1/T+3/T+7 from prior days, plus today's
                       new trend/threat/watchlist/scenarios as predictions)

Block specifications:

DATE              — human-readable date, e.g. "{human_date}"
DAY               — "{day_of_war}"
LAST_UPDATED      — "{last_updated}"
MAP_TS            — e.g. "{human_date}, {utc_hm} UTC"
TREND             — HTML for the trend cell. Match existing markup exactly:
                    <div class="value"><span class="arrow arrow-up|side|down">↑|→|↓</span>Worse|Same|Better</div>
                    <div class="sub">{{one-line context}}. Confidence: {{Low|Medium|High}}.</div>
THREAT            — HTML for the threat cell. Match existing markup:
                    <div class="value">N / 5 · {{Routine|Elevated|Concerning|Severe|Crisis}}</div>
                    <div class="threat-dots" aria-hidden="true">
                      <span class="lit-1"></span>... up to N lit, rest empty
                    </div>
ONELINER          — <p class="one-line">single-sentence summary, ~25-40 words</p>
SUMMARY           — executive summary paragraph for brief.html, 2-4 sentences,
                    plain text optionally with <em> tags. No <p> wrapper (it lives
                    inside summary-box).
TILE_1..TILE_6    — Full <article class="tile">...</article> for each of the six
                    status categories (Maritime, Military, Diplomatic, Infrastructure,
                    Alt routes, Outlook). Match existing structure: row1 with num/h3/
                    badge/arrow-inline, then <p class="syn">.
ACTIONS           — <ul class="actions">...</ul> with exactly 3 <li> items, each
                    starting with a bold operational verb in <strong>...</strong>.
WATCHLIST         — <ul class="watchlist">...</ul> with exactly 5 items. Each:
                    <span class="num">W{{n}}</span><div>Description.
                    <span class="deadline">deadline</span><span class="imp">directional implication</span></div>
FM                — Inner content of <div class="fm-table"> — head row plus 4-8 rows.
                    Use <span class="pip red|amber|ink"></span> + Declared|Likely|Watch.
WAVE              — Inner content of the wave section: intro <p>, the
                    <div class="wave-grid">...</div>, and the closing <p class="wave-note">.
MAP_PINS          — JavaScript object literals for the pinsConfig array, separated
                    by commas. Do NOT include the surrounding [ ] brackets. Format:
                    {{ lat: 27.18, lng: 56.27, color: 'red', name: 'Bandar Abbas',
                    sub: '...', status: '...' }}, ... 8-12 pins.
CATEGORY_1..6     — Full <article class="cat">...</article> for each category.
                    Match deep-brief structure: head with num/h3/badge/arrow-inline/conf,
                    ul.signals with ~3 li, p.why with strong intro, p.impl with strong
                    intro, div.sources-line.
SCENARIOS         — <div class="scenarios">...</div> with exactly 3 <article class="scenario">
                    entries summing to 100%. Include name, prob, delta vs yesterday,
                    observable, impl-line, and the bar div.
BACKTEST          — yesterday's predictions scored. Mostly <ul> with hit/miss/false-alarm/
                    pending markers. End with link to brief.html#backtest. On Fridays
                    only, also include Brier score line.

Stop conditions — set INTERIM block to "true" and prefix the TREND value text
with "[INTERIM]" when:
- You cannot find >=1 Hard source for a claim that affects trend or threat.
- All sources you found are Tier 5 or below.
- You did not score yesterday's predictions before drafting.

In INTERIM mode, the TREND text should explicitly say "Insufficient Tier 1-3 input today;
no trend update issued."

Do NOT include any prose outside the blocks. Do NOT include code fences.
The first three characters of your final response must be "###" and the last three "###".
"""

    user_prompt = f"""## Procedure (canonical — follow strictly)

{context['update_prompt']}

## Methodology

{context['methodology']}

## Sources

{context['sources']}

## Knowledge base (Marco's project context)

{context['knowledge_base']}

## Backtest log (recent — score predictions BEFORE drafting today's)

{context['backtest_log']}

## Latest archived brief (continuity reference, not a template)

{context['last_archive']}

## Current index.html (one-pager — preserve all structure outside BRIEF:* markers)

```html
{context['current_index']}
```

## Current brief.html (deep dive — preserve all structure outside BRIEF:* markers)

```html
{context['current_brief']}
```

Now: produce today's brief per the procedure. Score yesterday's predictions
before writing today's. Output only the delimiter blocks — no prose, no fences.
"""

    return system_prompt, user_prompt


_BLOCK_RE = re.compile(
    r"###BEGIN:([A-Z0-9_]+)###\s*\n(.*?)\n\s*###END:\1###",
    re.DOTALL,
)


def parse_delimited(text: str) -> dict[str, str]:
    """Parse all ###BEGIN:KEY### ... ###END:KEY### blocks into a dict."""
    items: dict[str, str] = {}
    for m in _BLOCK_RE.finditer(text):
        key = m.group(1)
        content = m.group(2)
        items[key] = content
    return items


def validate_blocks(items: dict[str, str]) -> None:
    missing = EXPECTED_BLOCK_KEYS - set(items.keys())
    if missing:
        raise ValueError(f"Missing required block keys: {sorted(missing)}")
    # Meta keys are advisory but archive/backtest at least should be present.
    for k in ("ARCHIVE_FILENAME", "ARCHIVE_MARKDOWN", "BACKTEST_APPEND"):
        if k not in items:
            print(f"[update_brief] WARNING: meta block {k} missing.", file=sys.stderr)


def apply_to_file(rel_path: str, blocks: dict[str, str]) -> dict[str, int]:
    html = read(rel_path)
    counts: dict[str, int] = {}
    for key, content in blocks.items():
        html, n = replace_block(html, key, content)
        counts[key] = n
    write(rel_path, html)
    return counts


def update_titles(date_human: str) -> None:
    """Refresh the <title> tag on each page. Uses a lambda for replacement so
    digits in date_human (e.g. '9 May 2026') are not misread as backreferences."""
    for path, prefix in [
        ("index.html", "Hormuz Daily Brief — "),
        ("brief.html", "Hormuz Brief — deep dive · "),
    ]:
        s = read(path)
        s = re.sub(
            rf"(<title>{re.escape(prefix)}).*?(</title>)",
            lambda m: m.group(1) + date_human + m.group(2),
            s,
            count=1,
        )
        write(path, s)


def main() -> int:
    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ANTHROPIC_API_KEY missing.", file=sys.stderr)
        return 1

    now_utc = datetime.now(timezone.utc)
    now_local, tz_label = vienna_now(now_utc)
    today_str = now_local.strftime("%Y-%m-%d")
    yesterday_str = (now_local - timedelta(days=1)).strftime("%Y-%m-%d")
    human_date = humanize_date(now_local)
    utc_hm = now_utc.strftime("%H:%M")
    local_hm = now_local.strftime("%H:%M")
    last_updated = f"{utc_hm} UTC / {local_hm} {tz_label}"
    day_of_war = (now_utc.date() - WAR_START.date()).days + 1

    backtest_log = read("backtest-log.md")
    backtest_log = backtest_log[-12000:] if len(backtest_log) > 12000 else backtest_log

    archive_dir = ROOT / "daily-briefs"
    archives = sorted(p for p in archive_dir.glob("2*.md") if p.is_file())
    last_archive_text = archives[-1].read_text(encoding="utf-8") if archives else "(no prior archive on file yet)"
    if len(last_archive_text) > 10000:
        last_archive_text = last_archive_text[-10000:]

    context = {
        "today_str": today_str,
        "yesterday_str": yesterday_str,
        "human_date": human_date,
        "last_updated": last_updated,
        "utc_hm": utc_hm,
        "day_of_war": day_of_war,
        "update_prompt": read("daily-update-prompt.md"),
        "methodology": read("methodology.md"),
        "sources": read("sources.md"),
        "knowledge_base": read("knowledge-base.md"),
        "backtest_log": backtest_log,
        "last_archive": last_archive_text,
        "current_index": read("index.html"),
        "current_brief": read("brief.html"),
    }

    system_prompt, user_prompt = build_prompts(context)

    print(f"[update_brief] Calling {MODEL} for {today_str} (day {day_of_war}). UTC now {utc_hm}.", flush=True)

    client = Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_OUTPUT_TOKENS,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
        tools=[
            {
                "type": "web_search_20250305",
                "name": "web_search",
                "max_uses": MAX_WEB_SEARCHES,
            }
        ],
    )

    text_parts = [b.text for b in response.content if getattr(b, "type", None) == "text"]
    text = "\n".join(text_parts).strip()
    if not text:
        print(f"Claude returned no text content. stop_reason={response.stop_reason}", file=sys.stderr)
        return 2

    print(f"[update_brief] Response length: {len(text)} chars. stop_reason={response.stop_reason}", flush=True)

    items = parse_delimited(text)
    print(f"[update_brief] Parsed {len(items)} blocks: {sorted(items.keys())[:10]}...", flush=True)

    try:
        validate_blocks(items)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        print("--- response head ---", file=sys.stderr)
        print(text[:4000], file=sys.stderr)
        print("--- response tail ---", file=sys.stderr)
        print(text[-2000:], file=sys.stderr)
        return 4

    interim = items.get("INTERIM", "false").strip().lower() == "true"
    if interim:
        print("[update_brief] Claude returned an INTERIM brief. Writing as flagged.", flush=True)

    # Split items into HTML blocks vs meta.
    html_blocks = {k: v for k, v in items.items() if k in EXPECTED_BLOCK_KEYS}

    print("[update_brief] Applying blocks to index.html...", flush=True)
    apply_to_file("index.html", html_blocks)
    print("[update_brief] Applying blocks to brief.html...", flush=True)
    apply_to_file("brief.html", html_blocks)

    update_titles(html_blocks.get("DATE", human_date).strip())

    arch_name = items.get("ARCHIVE_FILENAME", f"{yesterday_str}.md").strip()
    arch_md = items.get("ARCHIVE_MARKDOWN")
    if arch_md:
        write(f"daily-briefs/{arch_name}", arch_md)
        print(f"[update_brief] Archived yesterday's brief to daily-briefs/{arch_name}", flush=True)
    else:
        print("[update_brief] No ARCHIVE_MARKDOWN block returned; skipping archive write.", flush=True)

    bt_append = items.get("BACKTEST_APPEND", "").strip()
    if bt_append:
        bt_path = ROOT / "backtest-log.md"
        existing = bt_path.read_text(encoding="utf-8")
        if bt_append not in existing:
            bt_path.write_text(existing.rstrip() + "\n\n" + bt_append + "\n", encoding="utf-8")
            print("[update_brief] Appended to backtest-log.md", flush=True)
        else:
            print("[update_brief] BACKTEST_APPEND already present; skipped.", flush=True)
    else:
        print("[update_brief] No BACKTEST_APPEND block; skipping.", flush=True)

    # Sanity check — BRIEF:* markers still balance.
    for path in ("index.html", "brief.html"):
        s = read(path)
        starts = len(re.findall(r"<!-- BRIEF:[A-Z0-9_]+_START -->", s))
        ends = len(re.findall(r"<!-- BRIEF:[A-Z0-9_]+_END -->", s))
        if starts != ends:
            print(f"[update_brief] WARNING: marker imbalance in {path}: {starts} starts vs {ends} ends.", file=sys.stderr)
            return 5

    print(f"[update_brief] Done for {today_str} (day {day_of_war}).", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
