# Hormuz Daily Brief — Methodology

**Purpose:** Produce a daily, signal-disciplined intelligence brief on the Strait of Hormuz that supply chain and resilience leaders can hand to a CEO without caveat.

This document is the operating manual. The daily-update prompt enforces it. The backtest log measures whether it works.

---

## 1. Operating principles (Taleb-grounded)

These are not slogans. Each rule has a defeat condition: ignore it and the brief drifts toward noise.

### 1.1 Signal vs noise — the four-tier weighting

Every input is classified before it can shape the brief.

| Tier | What | Examples | Weight |
|------|------|----------|--------|
| **Hard** | Physical actions, verified incidents, deployments visible in AIS/SAR, ratified sanctions, ratified treaties | UKMTO incident reports, Kpler vessel counts, MARAD advisories, confirmed strikes with imagery | ×5 |
| **Medium** | Official orders from authorized voices, formal closures, mobilization announcements | IRGC commander order, MFA closure of airspace, US ExecOrder, OFAC designation | ×3 |
| **Soft** | Statements from authorized voices not yet translated into action | President/FM remarks, parliament resolutions, central bank guidance | ×1 |
| **Noise** | Anonymous attribution, op-eds, social media, repeat-statements that don't change behavior | "Officials say", X/Telegram OSINT, columnists' speculation, leaked drafts | ×0 |

**Rule:** A claim that downgrades or upgrades the threat level must be supported by at least one **Hard** source and at least one independent **Tier 1–3** corroboration (see `sources.md`).

### 1.2 Base rates before exceptions

Before flagging anything as "escalation" or "de-escalation," the analyst checks the **rolling 30-day baseline** and the **pre-crisis baseline**. A single incident is not a trend. Three incidents in 48h with rising severity is.

The brief reports **deviation from baseline**, not raw counts. Example: "37 incidents since 1 March" alone is meaningless — what matters is whether the trailing 7-day rate is rising, flat, or falling.

### 1.3 Convexity beats consensus

Tail risks dominate. A 5% probability of strait closure × catastrophic impact > 80% probability of "broadly stable." The scenario outlook always reports the **fat tail** (best 25th and worst 25th percentile), not just the modal expectation.

### 1.4 Lindy on tensions, anti-Lindy on novelty

- Long-running tensions (Iran rhetoric, sanction-by-sanction patterns) have inertia; assume they continue absent **observable physical change**.
- Novelty (a new actor entering, a never-before-targeted asset hit, a new weapon used) is a regime-change signal. Weight it.

### 1.5 Distinguish "no news" from "no event"

Absence of incidents in last 48h is a signal *only if Tier 1–3 sources are actively reporting* and reporting "nil." Quiet because nobody is looking ≠ quiet because nothing is happening.

### 1.6 Asymmetric updating (Popper)

Every brief makes falsifiable predictions. The backtest log records them at T+1, T+3, T+7. The methodology updates **when predictions fail**, not when they succeed. (Success only confirms the existing model; failure forces revision.)

### 1.7 No hindsight reframing

Once a prediction is logged, it cannot be retroactively softened. Calibration is meaningless if "I said the trend was sideways" gets re-described as "I correctly identified mixed signals" after the fact.

---

## 2. Trend assessment — Worse / Same / Better

The headline indicator. One of three values, with explicit confidence and time horizon.

**Time horizon:** Trailing 72h vs prior 72h. (Not "vs pre-war baseline" — that comparison is structural and goes in the threat level instead.)

**Decision rule:**

- **Worse (↑):** Net Hard + Medium signal flow indicates escalation. Either (a) ≥2 new Hard escalation events in trailing 72h with no offsetting Hard de-escalation, or (b) 1 Hard escalation event of regime-change character (e.g., new asset class targeted).
- **Same (→):** Mixed Hard signals, or no Hard signals in trailing 72h. Default state during attrition phases.
- **Better (↓):** ≥1 Hard de-escalation event (ceasefire announcement with verifiable terms, vessel resumption confirmed by AIS, formal channel established) **and** no offsetting Hard escalation in trailing 72h.

**Confidence:** Low / Medium / High. High requires ≥3 independent Tier 1–3 corroborations of the trailing 72h signal mix.

---

## 3. Threat level — 1 to 5

This is **structural**, not directional. It captures the operational state, regardless of whether today is slightly better or slightly worse than yesterday.

| Level | Label | Trigger conditions |
|-------|-------|-------------------|
| **1** | Routine | Baseline tensions only. No vessel incidents in trailing 30 days. Insurance war-risk premium <0.1% hull value. |
| **2** | Elevated | Heightened rhetoric or limited incidents (≤2 in 30 days). No flow impact. War-risk premium 0.1–0.5%. |
| **3** | Concerning | Operational disruptions visible: tanker delays >24h on average, insurance >0.5%, ≥1 port restriction, ≥3 incidents in 30 days. |
| **4** | Severe | Sustained multi-front escalation; >30–80% volume reduction sustained <7 days OR not yet sustained; alternative routes activated under stress; mediation channel still open or rebuildable; insurance >1%. |
| **5** | Crisis | Sustained de-facto closure (>80% volume reduction sustained ≥7 days) **AND** any of: (a) formal closure announcement, (b) confirmed strike on Gulf-state energy infrastructure, (c) alternative-route saturation forcing price rationing on a refined-product class, (d) insurance unobtainable for new transits or >5%, (e) public collapse of mediation channel with no successor. |

A threat level change requires a documented trigger condition shift. The brief logs which trigger flipped. The level-4 vs level-5 boundary is the single most consequential call in the brief — the criteria above are the operative test, not the prose label.

---

## 4. The six categories — scoring and structure

Each category gets:
- **Status:** Red / Amber / Green (operational state)
- **Arrow:** ↑ worsening / → sideways / ↓ improving (trailing 72h)
- **Confidence:** Low / Medium / High
- **3 signal bullets** (Hard or Medium tier only)
- **Why this matters** (1–2 lines, the causal mechanism)
- **Implication** (1–2 lines, what a supply chain/resilience leader does about it)
- **Sources** (Tier 1–3, named)

The six categories are fixed:

1. **Maritime shipping through the Strait** — vessel counts, AIS coverage, anchorage queues, insurance, escort operations, vessel incidents
2. **Military escalation** — kinetic events, deployments, force posture changes, casualties on either side, weapons/asset loss
3. **Diplomatic escalation** — official statements (weight by speaker authority), backchannel activity, mediator status, withdrawal/restoration of recognition, formal proposals on the table
4. **Infrastructure damage** — strikes on energy infra (refineries, ports, pipelines, terminals), critical civilian infra, both directions (Iran ↔ US/Israel/Gulf states)
5. **Alternative routes status** — Bab el-Mandeb (Houthi posture, transit volume), East-West and Habshan-Fujairah pipelines, Cape route, Suez throughput, regional port utilization
6. **Outlook scenarios** — 7–30 day forward look with **explicit probabilities summing to 100%**, named scenarios, and one observable that would shift the distribution

---

## 5. CEO talking points — what gets surfaced to the top

A CEO does not read the full brief. The talking points (4–6 bullets at the top of the page) must answer:

1. Is the situation getting worse, the same, or better — and how confident?
2. What is the **single most important fact** today that wasn't true yesterday?
3. What is the dominant **near-term swing factor** (the thing whose resolution moves the trajectory)?
4. What action does this brief change for our supply chain posture (or confirm)?
5. What is the **fat-tail risk** (low probability, severe impact) we are watching?
6. Optional: what would falsify today's read?

Each talking point ends with a Tier 1–3 source citation.

---

## 6. Watchlist — next 24–72h

Five or fewer specific, observable events. Each watchlist item is a **falsifiable trigger** — either it happens or it doesn't.

Bad watchlist item: "Continued tensions in the region."  
Good watchlist item: "Iranian formal response to the 14-point proposal (expected by Fri 8 May per State Dept)."

Each item has a **directional implication**: if event X occurs, threat level moves Y; if event X does not occur by deadline, threat level moves Z.

---

## 7. Scenario outlook — 30 days

Three scenarios, exhaustive, mutually exclusive. Probabilities sum to 100%.

Each scenario has:
- **Probability** (and how it changed from last brief)
- **Defining observable** (the one signal that would confirm we're in this scenario)
- **Supply chain implication** (what cargo flows / sourcing / inventory posture this scenario implies)
- **Time-to-resolve** (how soon we'd know we're in it)

Scenarios are reviewed weekly (Friday). If any scenario has been flagged for >14 days at <10% probability without de-flagging, it gets dropped or reclassified.

---

## 8. The learning loop — calibration and methodology updates

### 8.1 Daily backtest hooks

Every brief logs in `backtest-log.md`:
- Trend assessment (Worse/Same/Better)
- Threat level
- Scenario probabilities
- Watchlist items with explicit deadlines

### 8.2 T+1, T+3, T+7 checks

Each morning before writing the new brief, the agent checks predictions made 1, 3, and 7 days ago against what actually happened. Each prediction is scored:

- **Hit** (predicted, occurred)
- **Miss** (predicted, did not occur)
- **False alarm** (flagged escalation, none occurred)
- **Surprise** (unforecast event of materiality ≥3 categories affected)

### 8.3 Weekly calibration (Friday)

Friday's brief includes a Week-in-Review section:
- Brier score on probabilistic scenario forecasts
- Hit/miss/false-alarm counts
- Source-by-source reliability tally (which sources predicted reality, which generated noise)
- One concrete methodology delta — a heuristic added, removed, or sharpened

### 8.4 Source weight adjustment

Sources that consistently signal noise (false alarms, excited reporting that doesn't translate to operational reality) get downweighted. Sources that surface Hard signal early get upweighted. Adjustments are logged in `sources.md` with date and reason.

### 8.5 No silent learning

Every methodology change is logged in this file's **Changelog** (bottom). Marco can audit drift.

---

## 9. Anti-bias defaults

- **Recency bias:** The 72h window is the trend window, but the threat level is a 30-day structural read. Don't let yesterday's headline move the structural assessment.
- **Confirmation bias:** Each brief must include at least one signal **against** the current trend assessment, if any exists. If none, say so explicitly.
- **Authority bias:** A senior official saying X without observable change is **Soft tier**, not Hard. The brief never quotes a head of state as if a quote is an event.
- **Availability bias:** Just because something dominated coverage today doesn't mean it dominates the strategic picture. Coverage volume is excluded from the signal hierarchy.
- **Narrative bias:** Avoid "the situation is X because story Y." Each claim is supported by a discrete observation, not a story arc.

---

## 10. What the brief does NOT do

- It does not predict markets.
- It does not recommend specific trades, hedges, or financial positions.
- It does not name individual companies as targets unless the company is the subject of a Hard-tier event.
- It does not forecast beyond 30 days.
- It does not assign moral judgment to actors. Behavior is described, not evaluated.

---

## 11. Daily production cadence

- **08:00 local (CET/CEST):** Scheduled task fires. Agent reads this file, `sources.md`, `knowledge-base.md`, latest 7 entries of `backtest-log.md`, and yesterday's brief.
- **08:00–08:20:** Agent runs WebSearch/WebFetch on Tier 1–3 sources (URL list in `sources.md`).
- **08:20–08:35:** Agent classifies inputs, scores categories, drafts brief.
- **08:35–08:40:** Agent writes new `index.html`, archives yesterday into `daily-briefs/`, appends today's predictions to `backtest-log.md`.
- **Friday only — 08:40–08:55:** Agent runs Week-in-Review calibration and writes one methodology delta.

If a Hard-tier breaking event occurs **between** scheduled runs, an interim "Flash" version of the brief can be triggered manually. Flash versions are logged separately and do not replace the morning archive.

---

## 12. Changelog

| Date | Change | Reason |
|------|--------|--------|
| 2026-05-09 | Initial methodology established | Tracker launch |

(Each future change appended here with date and reason.)
