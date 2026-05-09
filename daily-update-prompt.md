# Hormuz Daily Brief — Update Procedure

This is the prompt the scheduled task runs each morning at 08:00 local (CET/CEST). It is also the manual-run prompt: paste it into a fresh Claude session at any time to produce a brief.

---

## 0. Before you write a single word

Open and read these files. Do not skip. The brief inherits its discipline from them:

1. `methodology.md` — operating rules. Especially Sections 1 (signal tiers), 2 (trend assessment), 4 (category scoring), 8 (learning loop), 9 (anti-bias defaults).
2. `sources.md` — tiered source list. Use Tier 1–3 by default; Tier 4–5 for context; Tier 6 only as leads.
3. `knowledge-base.md` — Marco's project context. Apply analytical frames it specifies.
4. `backtest-log.md` — last 7 days of predictions. Read what was claimed and what happened.
5. `daily-briefs/` — yesterday's archived brief (latest file). Use as continuity reference, not a template to copy.

---

## 1. Run the predictions check (T+1, T+3, T+7)

Before drafting today's brief, score yesterday's, three-days-ago, and seven-days-ago predictions:

For each:
- Did the trend assessment hold?
- Did watchlist items materialize? (hit / miss / false alarm)
- Was there a surprise event the brief missed?

Append findings to `backtest-log.md` under today's date. This step takes ≤5 minutes and forces honesty before today's claims are made.

If today is **Friday**, also run the Week-in-Review (see Section 8 below).

---

## 2. Gather inputs (Tier 1–3 first, parallel)

Run these queries (WebSearch / WebFetch). Run them in parallel where possible. Cap inputs — do not exceed ~25 source lookups; the brief is signal-disciplined, not exhaustive.

### Mandatory pulls
- UKMTO recent-incidents page: `https://www.ukmto.org/recent-incidents`
- UKMTO latest JMIC advisory note (linked from the products page)
- MARAD MSCI latest Hormuz/Persian Gulf advisory
- ISW Iran Update for yesterday and today
- ICG Iran/US/Israel flashpoint page (check for updates)
- A Tier 5 wire (Reuters or AP) live blog or topic page for the trailing 24h

### Conditional pulls (run if relevant)
- Bab el-Mandeb / Houthi-related: MARAD Red Sea advisory + EUNAVFOR Aspides + ACLED if a Houthi-related signal is suspected
- Pipeline status: a Tier 4 energy analyst comment if a redirection signal is suspected
- Sanctions: OFAC press releases if a designation is suspected today
- Diplomatic: State Dept daily briefing transcript

### Search query patterns
- "Strait of Hormuz incident [DATE]"
- "UKMTO advisory [WEEK]"
- "Iran [DATE] official statement"
- "Hormuz tanker [DATE]"
- "Houthi [DATE]"
- "Beirut strike [DATE]" (only if Lebanon front is active)

---

## 3. Classify every input by signal tier

For each piece of evidence:

- **Hard**: physical event, verified incident, AIS-confirmed movement, ratified order/sanction
- **Medium**: official order from authorized voice, formal closure
- **Soft**: statement from authorized voice not yet acted on
- **Noise**: anonymous, op-ed, social media chatter, repeat-of-prior-statement

Discard everything below Soft tier from the brief content. Keep Soft tier as **context**, not as a basis for trend movement.

For any claim that affects the trend assessment or threat level: **require ≥1 Hard source + ≥1 independent Tier 1–3 corroboration**. If you cannot find both, do not include the claim — flag it as "watching, unconfirmed" in the Watchlist.

---

## 4. Score the categories

For each of the six categories, produce:

- **Status:** Red / Amber / Green
- **Arrow:** ↑ ↓ → (trailing 72h)
- **Confidence:** Low / Medium / High
- **3 signal bullets** (Hard or Medium tier only, each with source citation)
- **Why this matters** (1–2 lines, the causal mechanism — no narrative arc)
- **Implication for SC/resilience leaders** (1–2 lines, what changes about posture)

Categories are fixed (do not invent new ones):
1. Maritime shipping through the Strait
2. Military escalation
3. Diplomatic escalation
4. Infrastructure damage
5. Alternative routes status
6. Outlook scenarios (next 7–30 days)

---

## 5. Set the headline indicators

### Trend assessment (Worse / Same / Better)
Apply the rule from `methodology.md` §2. The trend is not "vs pre-war" — it is **trailing 72h vs prior 72h**.

### Threat level (1–5)
Apply the rule from `methodology.md` §3. The threat level is **structural** — it does not move with each daily fluctuation. Document which trigger condition shifted if you change it.

### Confidence
Low / Medium / High on the trend assessment specifically. High requires ≥3 independent Tier 1–3 corroborations of the trailing 72h signal mix.

---

## 6. CEO talking points

Produce 4–6 bullets that answer (per `methodology.md` §5):
1. Worse / same / better — and how confident
2. Single most important new fact since yesterday
3. Dominant near-term swing factor
4. Action implication for supply chain posture
5. Fat-tail risk being watched
6. Optional: what would falsify today's read

Each bullet ends with a source citation in parentheses.

---

## 7. Watchlist (24–72h) and scenario outlook (30 days)

### Watchlist
≤5 items. Each is a falsifiable, observable trigger with a deadline. Each has a directional implication (if X happens → Y; if X does not happen by deadline → Z).

### Scenario outlook
Three scenarios, mutually exclusive, summing to 100%. Each has:
- Probability (and delta from yesterday's brief)
- Defining observable
- Supply chain implication
- Time-to-resolve

---

## 8. Friday only — Week-in-Review calibration

If today is Friday, additionally produce:

- **Brier score** on probabilistic scenario forecasts from the past 7 days
- **Hit / miss / false-alarm tally** on watchlist items
- **Source reliability tally** — which sources surfaced Hard signal early, which generated noise
- **One concrete methodology delta** — a heuristic added, removed, or sharpened. Logged in `methodology.md` Changelog.
- **One source-weight adjustment** if warranted, logged in `sources.md`.

The Week-in-Review goes into Friday's `index.html` as an additional collapsible section, and is archived with the brief.

---

## 9. Write the two HTML pages — index.html (one-pager) and brief.html (deep dive)

The site has two pages. Both are public. Both are regenerated daily. The structure is fixed; only the content inside the marked blocks changes.

### 9A. index.html — the FORDEC one-pager

This is the page most people read. Everything important at a glance. The marked blocks:

```
<!-- BRIEF:DATE_START --> ... <!-- BRIEF:DATE_END -->
<!-- BRIEF:DAY_START --> ... <!-- BRIEF:DAY_END -->
<!-- BRIEF:LAST_UPDATED_START --> ... <!-- BRIEF:LAST_UPDATED_END -->
<!-- BRIEF:TREND_START --> ... <!-- BRIEF:TREND_END -->
<!-- BRIEF:THREAT_START --> ... <!-- BRIEF:THREAT_END -->
<!-- BRIEF:ONELINER_START --> ... <!-- BRIEF:ONELINER_END -->
<!-- BRIEF:FORDEC_F_START --> ... <!-- BRIEF:FORDEC_F_END -->
<!-- BRIEF:FORDEC_O_START --> ... <!-- BRIEF:FORDEC_O_END -->
<!-- BRIEF:FORDEC_R_START --> ... <!-- BRIEF:FORDEC_R_END -->
<!-- BRIEF:FORDEC_D_START --> ... <!-- BRIEF:FORDEC_D_END -->
<!-- BRIEF:FORDEC_E_START --> ... <!-- BRIEF:FORDEC_E_END -->
<!-- BRIEF:FORDEC_C_START --> ... <!-- BRIEF:FORDEC_C_END -->
<!-- BRIEF:FM_START --> ... <!-- BRIEF:FM_END -->
<!-- BRIEF:WAVE_START --> ... <!-- BRIEF:WAVE_END -->
```

**FORDEC content rules** (the cells must be tight — this is a one-pager):

- **F · Facts** — 3–5 short bullets. Today's most material observations only. Each ends with a `<small>` source citation.
- **O · Options** — 4–6 posture choices a SC/resilience leader could take, labeled A–F. One line each. No commentary.
- **R · Risks &amp; benefits** — 4–5 items. Each is a near-term swing condition with a directional consequence. Use `pip-red` for severe / `pip-amber` for elevated / `pip-green` for upside.
- **D · Decision** — single recommended posture in the `.recommend` block (combine option labels: e.g. "Hold A · add C"). Plus 1–2 review/reset triggers underneath.
- **E · Execution** — 4–6 concrete actions changing this week. Operational verbs ("Confirm", "Hold", "Re-confirm", "Brief", "Diary"). Diary line at end with named decision dates.
- **C · Check** — 4 items: trend hit (yesterday), watchlist hits, 7-day Brier (or "first run Friday"), source flag (or "none yet"). Always ends with link to deep brief calibration section.

**Force Majeure tracker** — replace each row with current state. Status column uses `stat-declared` / `stat-likely` / `stat-watch`. Pull from Tier 2 (Lloyd's List, Argus, Platts) and Tier 4 (trader desks, sector analysts) wherever public commentary supports it. If `knowledge-base.md` provides project-specific FM positions, use those instead of the defaults.

**Commodity wave timeline** — replace each cell. Use `class="stage-cell hit"` (pink) for active hits, `class="stage-cell hit amber"` (cream) for approaching, blank `class="stage-cell"` for not-yet. Each populated cell starts with a `<strong>` label (Direct / Sustained / Building / Active / Risk) followed by the specific signal. If `knowledge-base.md` provides sector-specific exposure profile, weight commodities accordingly.

### 9B. brief.html — the deep dive

This is for analysts and anyone who wants the full picture. The marked blocks:

```
<!-- BRIEF:DATE_START --> ... <!-- BRIEF:DATE_END -->
<!-- BRIEF:DAY_START --> ... <!-- BRIEF:DAY_END -->
<!-- BRIEF:LAST_UPDATED_START --> ... <!-- BRIEF:LAST_UPDATED_END -->
<!-- BRIEF:TREND_START --> ... <!-- BRIEF:TREND_END -->
<!-- BRIEF:THREAT_START --> ... <!-- BRIEF:THREAT_END -->
<!-- BRIEF:SUMMARY_START --> ... <!-- BRIEF:SUMMARY_END -->
<!-- BRIEF:CATEGORY_1_START --> ... <!-- BRIEF:CATEGORY_1_END -->
... (same for categories 2–6)
<!-- BRIEF:WATCHLIST_START --> ... <!-- BRIEF:WATCHLIST_END -->
<!-- BRIEF:SCENARIOS_START --> ... <!-- BRIEF:SCENARIOS_END -->
<!-- BRIEF:BACKTEST_START --> ... <!-- BRIEF:BACKTEST_END -->
```

**Category content rules** — preserve the existing structure (`.head`, `.signals`, `.why`, `.impl`, `.sources-line`). The badge class (`badge-red`/`badge-amber`/`badge-green`) and arrow class (`arrow-up`/`arrow-side`/`arrow-down`) must match the trend assessment.

### 9C. Procedure

1. Read the current `index.html` and `brief.html`.
2. For each file, use the **Edit** tool to replace the content of every BRIEF:* block. Do NOT rewrite the whole file — preserve all CSS, structure, and tags outside the markers.
3. Update both files' `<title>` and the date / day-of-war / last-updated blocks.
4. Keep the indicator triplet (trend / threat / one-liner on index; trend / threat / summary on brief) consistent across both files. The `value` and arrow classes must match.
5. The summary on `brief.html` is one paragraph (2–4 sentences). The one-liner on `index.html` is one sentence — derived from the summary's most material clause.

---

## 10. Archive yesterday's brief

Before overwriting `index.html`:
- Extract yesterday's content (everything between BRIEF:* markers as a Markdown summary).
- Write to `daily-briefs/YYYY-MM-DD.md` (the date of yesterday's brief, not today's).
- Use a consistent template: see `daily-briefs/_template.md` if present.

This preserves the audit trail for backtesting.

---

## 11. Append today's predictions to backtest-log.md

Under today's date in `backtest-log.md`, append:

```markdown
## YYYY-MM-DD

**Trend:** [Worse / Same / Better] (Confidence: [Low/Med/High])
**Threat level:** [1–5]

**Watchlist (24–72h):**
- [Item 1] — deadline: [date]
- ...

**Scenarios (30d):**
- A: [name] — [P%]
- B: [name] — [P%]
- C: [name] — [P%]

**Predictions to score at T+1, T+3, T+7.**
```

The next day's run reads this and scores it.

---

## 12. Tone and writing rules

Apply these to every line of the brief:

- **Be a practitioner, not a narrator.** Talk to peers — supply chain executives, resilience officers, intelligence analysts. Not to a general audience.
- **Lead with the fact, then the why, then the so-what.** Never lead with narrative.
- **No hedge-everything language.** "Iran appears to potentially be considering" → "Iran has signaled" or "Iran has not signaled" — pick one based on evidence.
- **No filler ("it is important to note"), no AI tells (synonym cycling, em-dash chains, "moreover/furthermore"), no generic frames ("in today's complex environment").**
- **Every claim is sourced.** Inline citations end with `(Source: NAME — Tier N)` or `(Source: ORG, [date])`.
- **Numbers when available, ranges when not.** "Roughly 90% reduction" beats "significant decrease." "Insurance war-risk premium >1%" beats "elevated insurance costs."
- **Distinguish "we observe X" from "we believe X." Brief reports observations; the outlook section is for beliefs.**

---

## 13. Stop conditions — do NOT publish if:

- You cannot find ≥1 Hard source for a claim that affects the trend assessment.
- All sources are Tier 5 or below.
- The brief contains a claim that originated in Tier 6 without independent Tier 1–3 confirmation.
- Predictions from yesterday have not been scored.
- The watchlist contains items without deadlines or directional implications.

In any of these cases, write a "thin brief" that explicitly says: "Insufficient Tier 1–3 input today. The following signals are tracking but unconfirmed. No trend update issued." Mark the brief `[INTERIM]` in the title bar.

---

## 14. Output checklist before publish

- [ ] Yesterday's predictions scored, written to `backtest-log.md`
- [ ] Today's predictions appended to `backtest-log.md`
- [ ] Yesterday's brief archived to `daily-briefs/YYYY-MM-DD.md`
- [ ] `index.html` updated, all BRIEF:* blocks replaced (FORDEC F/O/R/D/E/C, FM tracker, Wave timeline, headline indicators)
- [ ] `brief.html` updated, all BRIEF:* blocks replaced (categories, watchlist, scenarios, backtest)
- [ ] Indicators (trend / threat / day count / date / last-updated) consistent across both files
- [ ] `<title>` and header dates updated on both files
- [ ] Friday only: Week-in-Review section produced; methodology/sources changelog updated
- [ ] No Tier 6 sources cited unconfirmed
- [ ] Every Hard claim has ≥1 Hard source and ≥1 corroborating Tier 1–3 source

If any box is unchecked, fix it before publishing. The brief's value is in its discipline, not its existence.
