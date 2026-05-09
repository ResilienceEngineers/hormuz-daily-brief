#!/usr/bin/env python3
"""
Daily Hormuz Brief updater.

Run by GitHub Actions at ~06:00 UTC every day. Reads the operating files
(methodology.md, sources.md, knowledge-base.md, backtest-log.md,
daily-update-prompt.md) plus the current index.html and brief.html, calls
Claude with web_search enabled, and applies the returned JSON to:
  - index.html  (one-pager, FORDEC + status board)
  - brief.html  (deep dive, six categories + sources + calibration)
  - daily-briefs/YYYY-MM-DD.md  (yesterday's archive)
  - backtest-log.md  (predictions + scoring of T+1, T+3, T+7)

The script is intentionally strict: if Claude does not return a valid JSON
object with the expected keys, it exits non-zero so the GitHub Actions run
fails visibly and no broken HTML is committed.
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from anthropic import Anthropic

ROOT = Path(__file__).resolve().parents[2]  # repo root from .github/scripts/

MODEL = os.environ.get("CLAUDE_MODEL", "claude-opus-4-7")
MAX_OUTPUT_TOKENS = int(os.environ.get("CLAUDE_MAX_TOKENS", "16000"))
MAX_WEB_SEARCHES = int(os.environ.get("CLAUDE_MAX_SEARCHES", "25"))

# War start anchor (28 Feb 2026 = day 1).
WAR_START = datetime(2026, 2, 28, tzinfo=timezone.utc)

EXPECTED_KEYS = {
    # Headline / metadata
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
    # Cross-platform "1 May 2026" without leading zero on day.
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return f"{dt.day} {months[dt.month - 1]} {dt.year}"


def build_prompts(context: dict) -> tuple[str, str]:
    today_str = context["today_str"]
    yesterday_str = context["yesterday_str"]
    human_date = context["human_date"]
    last_updated = context["last_updated"]
    day_of_war = context["day_of_war"]

    system_prompt = f"""You are producing today's Hormuz Daily Brief for Marco Felsberger
(resilience-engineers.com), published at https://resilienceengineers.github.io/hormuz-daily-brief/.

Today: {human_date}, day {day_of_war} of the US/Israel-Iran war.
Last-updated stamp: {last_updated}.
Yesterday (for archiving): {yesterday_str}.

You operate strictly under the procedure in `daily-update-prompt.md` (provided in the user message).
Apply it without shortcuts.

Use web search aggressively but disciplined: pull from Tier 1-3 sources first
(UKMTO, MARAD, ISW, ICG, Reuters/AP, AJ live blogs). Cap at ~25 searches.
A claim that moves the trend assessment or threat level requires >=1 Hard source
AND >=1 independent Tier 1-3 corroboration. Without both, put the item on the
watchlist as "unconfirmed" rather than into the brief content.

OUTPUT FORMAT — your final response MUST be ONLY a single JSON object. No prose,
no commentary, no markdown code fences. The object must have exactly this shape:

{{
  "date": "{today_str}",
  "day_of_war": {day_of_war},
  "last_updated": "{last_updated}",
  "interim": false,
  "blocks": {{
    "DATE": "human-readable date string, e.g. \\"{human_date}\\"",
    "DAY": "{day_of_war}",
    "LAST_UPDATED": "{last_updated}",
    "MAP_TS": "e.g. \\"{human_date}, {context['utc_hm']} UTC\\"",
    "TREND": "HTML for the trend cell. Match the existing markup: <div class=\\"value\\"><span class=\\"arrow arrow-{{up|side|down}}\\">{{symbol}}</span>{{Worse|Same|Better}}</div><div class=\\"sub\\">{{one-line context}}. Confidence: {{Low|Medium|High}}.</div>",
    "THREAT": "HTML for the threat cell. Match the existing markup including <div class=\\"value\\">N / 5 · {{Routine|Elevated|Concerning|Severe|Crisis}}</div> followed by the threat-dots row with the right number of lit-N classes.",
    "ONELINER": "<p class=\\"one-line\\">single-sentence summary used on the one-pager hero, ~25-40 words.</p>",
    "SUMMARY": "executive summary paragraph for brief.html — 2 to 4 sentences, plain text optionally with <em> tags, no <p> wrapper needed (it's inside summary-box).",
    "TILE_1": "Full <article class=\\"tile\\">...</article> for Maritime shipping. Match the existing structure exactly: row1 with num/h3/badge/arrow-inline, then <p class=\\"syn\\">.",
    "TILE_2": "Full tile for Military escalation.",
    "TILE_3": "Full tile for Diplomatic escalation.",
    "TILE_4": "Full tile for Infrastructure damage.",
    "TILE_5": "Full tile for Alternative routes.",
    "TILE_6": "Full tile for Outlook (30d).",
    "ACTIONS": "<ul class=\\"actions\\">...</ul> with exactly 3 <li> items, each starting with a bold operational verb in <strong>...</strong>.",
    "WATCHLIST": "<ul class=\\"watchlist\\">...</ul> with exactly 5 <li> items. Each item: <span class=\\"num\\">W{{n}}</span><div>Description. <span class=\\"deadline\\">deadline</span><span class=\\"imp\\">directional implication</span></div>.",
    "FM": "Force Majeure tracker — the inner content of <div class=\\"fm-table\\">. Include the head row plus 4-8 rows. Use <span class=\\"pip red|amber|ink\\"></span> + Declared|Likely|Watch.",
    "WAVE": "Commodity wave timeline — the inner content of the wave section. Include the intro <p>, the <div class=\\"wave-grid\\">...</div>, and the closing <p class=\\"wave-note\\">.",
    "MAP_PINS": "JavaScript object literals for the pinsConfig array, separated by commas. Do NOT include surrounding [ ] brackets. Format: {{ lat: 27.18, lng: 56.27, color: 'red', name: 'Bandar Abbas', sub: '...', status: '...' }}, ... etc. 8-12 pins. Status tag is one of 'Active incident', 'Iranian military', 'At risk', 'Operating'.",
    "CATEGORY_1": "Full <article class=\\"cat\\">...</article> for category 1 (Maritime). Match deep-brief structure: head with num/h3/badge/arrow-inline/conf, ul.signals with ~3 li, p.why with strong intro, p.impl with strong intro, div.sources-line.",
    "CATEGORY_2": "Full cat article for Military escalation.",
    "CATEGORY_3": "Full cat article for Diplomatic escalation.",
    "CATEGORY_4": "Full cat article for Infrastructure damage.",
    "CATEGORY_5": "Full cat article for Alternative routes.",
    "CATEGORY_6": "Full cat article for Outlook scenarios.",
    "SCENARIOS": "<div class=\\"scenarios\\">...</div> with exactly 3 <article class=\\"scenario\\"> entries summing to 100%. Include name, prob, delta vs yesterday, observable, impl-line, and the bar div.",
    "BACKTEST": "yesterday's predictions scored — short HTML, mostly <ul> with hit/miss/false-alarm/pending markers. End with link to brief.html#backtest. On Fridays only, also include Brier score line."
  }},
  "archive_filename": "{yesterday_str}.md",
  "archive_markdown": "the full markdown of yesterday's brief in the daily-briefs/_template.md structure, ready to write to daily-briefs/{yesterday_str}.md",
  "backtest_append": "markdown to append under today's date in backtest-log.md. Includes (a) scoring of T+1/T+3/T+7 predictions from prior days, (b) today's new trend/threat/watchlist/scenarios as predictions for the next cycle."
}}

Stop conditions — set "interim": true and prefix the TREND value with "[INTERIM] " when:
- You cannot find >=1 Hard source for a claim that affects trend or threat.
- All sources you found are Tier 5 or below.
- You did not score yesterday's predictions before drafting.
In INTERIM mode, the TREND text should explicitly say "Insufficient Tier 1-3 input today; no trend update issued."

Hard rule: do NOT include markdown code fences, do NOT prefix or suffix the JSON with prose.
The first character of your final response must be `{{` and the last must be `}}`.
"""

    user_prompt = f"""## Procedure (canonical — follow this strictly)

{context['update_prompt']}

## Methodology

{context['methodology']}

## Sources

{context['sources']}

## Knowledge base (Marco's project context)

{context['knowledge_base']}

## Backtest log (recent — score predictions before drafting today's)

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
before writing today's. Output the JSON object only — no prose, no fences.
"""

    return system_prompt, user_prompt


def parse_response(text: str) -> dict:
    """Parse Claude's JSON response, tolerating optional code fences."""
    s = text.strip()
    # Strip optional ```json ... ``` fence.
    if s.startswith("```"):
        s = re.sub(r"^```(?:json)?\s*\n", "", s)
        s = re.sub(r"\n```\s*$", "", s)
        s = s.strip()
    # Find the first { and last } as a safety net for prefix/suffix prose.
    first = s.find("{")
    last = s.rfind("}")
    if first == -1 or last == -1 or last <= first:
        raise ValueError("No JSON object found in response.")
    return json.loads(s[first : last + 1])


def validate_blocks(blocks: dict) -> None:
    missing = EXPECTED_KEYS - set(blocks.keys())
    if missing:
        raise ValueError(f"Missing required block keys: {sorted(missing)}")


def apply_to_file(rel_path: str, blocks: dict) -> dict:
    """Apply BRIEF:* replacements to the given file. Returns counts per key."""
    html = read(rel_path)
    counts: dict[str, int] = {}
    for key, content in blocks.items():
        html, n = replace_block(html, key, content)
        counts[key] = n
    write(rel_path, html)
    return counts


def update_titles(date_human: str) -> None:
    """Refresh the <title> tags so browser tabs show today's date."""
    for path, prefix in [
        ("index.html", "Hormuz Daily Brief — "),
        ("brief.html", "Hormuz Brief — deep dive · "),
    ]:
        s = read(path)
        s = re.sub(
            rf"(<title>{re.escape(prefix)}).*?(</title>)",
            rf"\1{date_human}\2",
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

    # Trim large files defensively to leave room in context window.
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
        print("Claude returned no text content. stop_reason=" + str(response.stop_reason), file=sys.stderr)
        return 2

    try:
        data = parse_response(text)
    except (ValueError, json.JSONDecodeError) as e:
        print(f"Failed to parse JSON: {e}", file=sys.stderr)
        print("--- response head ---", file=sys.stderr)
        print(text[:4000], file=sys.stderr)
        return 3

    blocks = data.get("blocks") or {}
    try:
        validate_blocks(blocks)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 4

    if data.get("interim"):
        print("[update_brief] Claude returned an INTERIM brief. Writing as flagged.", flush=True)

    # Apply blocks to both pages. Replace counts of 0 just mean the key isn't in
    # that file (e.g., FM only exists in index.html); that's fine.
    print("[update_brief] Applying blocks to index.html...", flush=True)
    apply_to_file("index.html", blocks)
    print("[update_brief] Applying blocks to brief.html...", flush=True)
    apply_to_file("brief.html", blocks)

    # Refresh <title> tags.
    update_titles(blocks["DATE"])

    # Archive yesterday's brief.
    arch_name = data.get("archive_filename") or f"{yesterday_str}.md"
    arch_md = data.get("archive_markdown")
    if arch_md:
        write(f"daily-briefs/{arch_name}", arch_md)
        print(f"[update_brief] Archived yesterday's brief to daily-briefs/{arch_name}", flush=True)
    else:
        print("[update_brief] No archive_markdown returned; skipping archive write.", flush=True)

    # Append to backtest log.
    bt_append = data.get("backtest_append", "").strip()
    if bt_append:
        bt_path = ROOT / "backtest-log.md"
        existing = bt_path.read_text(encoding="utf-8")
        if bt_append not in existing:
            bt_path.write_text(existing.rstrip() + "\n\n" + bt_append + "\n", encoding="utf-8")
            print("[update_brief] Appended to backtest-log.md", flush=True)
        else:
            print("[update_brief] backtest_append already present; skipped.", flush=True)
    else:
        print("[update_brief] No backtest_append returned; skipping.", flush=True)

    # Sanity check: BRIEF marker pairs still balance in both files.
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
