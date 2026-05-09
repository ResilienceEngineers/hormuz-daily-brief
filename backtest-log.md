# Backtest Log — Hormuz Daily Brief

The discipline lives here. Every brief makes falsifiable claims; this file scores them.

---

## How this works

Each daily entry has three parts:

1. **Predictions made** — trend, threat level, watchlist items with deadlines, scenario probabilities.
2. **T+1 / T+3 / T+7 scoring** — appended on the days the predictions come due. Each prediction is marked Hit / Miss / False alarm / Surprise (unforecast event of materiality ≥3 categories affected).
3. **Source notes** — which sources delivered Hard signal early, which generated noise.

Scoring happens **before** the new brief is written each morning. No brief publishes without scoring yesterday's.

---

## Calibration metrics

- **Brier score** on scenario probabilities (computed weekly, lower is better). Target: <0.20.
- **Trend hit rate** — % of trend assessments that held over their 72h window. Target: >65%.
- **Watchlist hit rate** — % of falsifiable watchlist items resolved as predicted. Target: >50% (high baseline because items must be observable).
- **False alarm rate** — % of escalation flags that did not produce a downstream Hard event. Target: <30%.
- **Surprise rate** — number of T+0 events the brief did not have on watchlist. Target: <1 per week of meaningful surprises.

These are tracked in the **Week-in-Review** entries (Fridays).

---

## Source reliability tally (running)

When a source materially helped or hurt brief calibration, log it here.

| Source | Hard signal early | False alarm | Net |
|--------|-------------------|-------------|-----|
| (initial — no entries yet) | | | |

---

## Daily entries

---

### 2026-05-09 (initial brief — day 70 of war)

**Trend:** Same (sideways with marginal diplomatic upside skew) — Confidence: Medium  
**Threat level:** 4/5 (Severe — sustained shipping disruption, kinetic incidents continuing, alternative routes activated under stress)

**Predictions to score at T+1 (10 May), T+3 (12 May), T+7 (16 May):**

**Watchlist (24–72h):**
- W1 — Iranian formal response to US 14-point proposal (mediated by Pakistan), expected by ~Fri 8 May per State Dept. **Implication:** acceptance → diplomatic AMBER → AMBER↑; rejection or no-response by EOD Sun 10 May → AMBER↓.
- W2 — New vessel incident in or adjacent to Hormuz (UKMTO advisory). **Implication:** any incident → maritime RED-status sustained; nil for 72h+ → first marginal evidence of de-escalation in transit risk.
- W3 — Houthi public statement on Red Sea posture (Tier 1: official Saba/Al-Masirah broadcast). **Implication:** explicit threat to resume → alt-routes status downgrade Amber → Red; continued silence/pause → Amber holds.
- W4 — Israeli strike pattern on Lebanon (frequency vs trailing 7d baseline per ISW). **Implication:** ≥3 strikes/day sustained → cascade vector activates, weight Lebanon-front re-escalation scenario higher; <1/day → cascade vector dormant.
- W5 — Iranian airspace or maritime closure announcement (Tier 1: Iran SNSC or IRGC Navy). **Implication:** announcement → threat level 4→5 trigger; no announcement → status quo holds.

**Scenarios (30d):**
- A — Negotiated framework: Hormuz partially reopens under monitored escort; insurance war-risk premium begins easing — **35%**
- B — Frozen attrition: Sideways, sporadic incidents, no diplomatic breakthrough; supply chains stay rerouted — **45%**
- C — Re-escalation: Mediation collapses, Lebanon spillover triggers wider front, Houthi resumption likely, Hormuz hardens to full closure — **20%**

**Sources cited in today's brief:** UKMTO JMIC update 041 (5 May); Kpler April Hormuz vessel data via NBC News and CNN visual deep-dive; Reuters/Al Jazeera live blogs (8–9 May); CMA CGM corporate statement on San Antonio incident; Hapag-Lloyd public commentary on weekly cost of closure; The National on Houthi pause; ISW Iran Update; ICG Hormuz flashpoint page.

**Notes for tomorrow's scoring:**
- W1's deadline is EOD Sun 10 May. Score at T+1 (10 May entry). If response not arrived, score as MISS for "by Friday" but reset deadline.
- Houthi pause is a high-conviction Lindy bet — surprise to date. Track whether next 72h validates or breaks it.
- Threat level 4 is structural; do not move it on a single day's fluctuation. Trigger to move to 5 = formal Iranian closure announcement OR sustained kinetic strikes on Gulf-state energy infra (none in trailing 72h).

---

## Methodology deltas (running)

When a Friday Week-in-Review identifies a methodology change, append it here with date and reason.

| Date | Delta | Reason |
|------|-------|--------|
| 2026-05-09 | Initial methodology established | Tracker launch |

---

## Failure-mode catalog (running)

Patterns of brief failure to learn from. Updated as they emerge.

- (no entries yet)

Examples of what would go here once observed:
- "Repeatedly underestimated speed of Houthi position changes — Tier 5 regional press surfaced shifts 24–48h before Tier 1 advisories."
- "Treated 'IRGC commander statement' as Soft when subsequent kinetic action validated it as Medium-tier order. Methodology updated to weight specific commander-X statements higher."

## 2026-05-09

### T+1 scoring of 2026-05-08 predictions

- **Trend (Same, Conf Medium) — MISS.** The trailing 72h delivered Hard escalation events that meet methodology §2's "Worse" rule: US strikes on three named Iranian ports (Bandar Abbas, Qeshm, Bandar Kargan); three US Navy destroyers attacked in Hormuz; US disabled two Iranian-flagged tankers (Sea Star III, Sevda); Hezbollah first publicly claimed cross-border attack into Israel since 17 Apr truce. No offsetting Hard de-escalation.
- **Threat level (4) — HIT (held).** No formal Iranian closure announcement. No strike on Gulf-state energy infrastructure inside the trailing 72h window. Threat-5 trigger not flipped.
- **W1 (Iran formal response by EOD Sun 10 May) — PENDING.** Reply not delivered as of 9 May 18:17 UTC. Rubio (8 May Rome) and Trump (9 May TF1) both publicly noted non-arrival. Score finalizes 10 May entry.
- **W2 (New vessel incident in/near Hormuz) — HIT (escalation direction).** Multiple events: US strikes on Sea Star III and Sevda; Iranian fire on three US destroyers; reported US strike on Iranian fishing/cargo vessels near Khasab (6 missing, per Iranian official, not US-confirmed).
- **W3 (Houthi public statement on Red Sea posture) — MISS (no statement) / Lindy validated.** No Saba/Al-Masirah resumption threat in trailing 72h.
- **W4 (Israeli strike pattern on Lebanon ≥3/day sustained) — HIT (cascade vector activated).** 19+ killed in Lebanon 9 May; Hezbollah claimed 26 attacks Friday including two cross-border into Israel — first since 17 Apr ceasefire.
- **W5 (Iranian airspace/maritime closure announcement) — MISS (no announcement).** Status quo holds.
- **Surprise (unforecast event affecting ≥3 categories):** US sovereign-territory strikes on three named Iranian ports. Affects Maritime, Military, Diplomatic, Infrastructure, Outlook (5 categories). Logged.

### Source notes (2026-05-09)

- CENTCOM press releases (via Fox / CBS / CNN) led on the 7–8 May kinetic exchange. UKMTO recent-incidents page lagged with no public 9 May update. ISW posted Iran Update Special Report at 19:31 UTC 8 May capturing the exchange — useful Tier 3 corroboration.
- Wikipedia 2026 SoH crisis entry was used for cross-checking event sequence (Tier 5 consolidation, not primary).

### Methodology delta candidate (for Friday review)

- **Recency-bias trap:** the 8 May brief weighted "nil incidents in trailing 48h" as a positive signal. Within 24h that read inverted on a Hard regime-change event. Heuristic to consider Friday: when the structural threat level is 4+ and a diplomatic deadline is within 72h, treat short-window quiet as null information, not as positive signal.

---

### 2026-05-09 — Predictions logged for scoring at T+1 (10 May), T+3 (12 May), T+7 (16 May)

**Trend:** Worse (Confidence: High)
**Threat level:** 4/5 (held — no closure announcement, no Gulf-state energy infra strike inside 72h window)

**Watchlist (24–72h):**
- W1 — Iranian formal written response to US 14-point framework via Pakistan — deadline EOD Sun 10 May
- W2 — Further US strike on Iranian port or naval asset (CENTCOM release) — rolling 72h
- W3 — Strike on Gulf-state energy infrastructure (Ras Laffan, Ras Tanura, Fujairah refinery, Jebel Ali, Bandar Abbas terminals, Kharg) — rolling 72h
- W4 — Hezbollah second cross-border attack on Israel and Israeli response — rolling 72h
- W5 — Iranian airspace or maritime closure announcement (SNSC / IRGC Navy via state outlet) — rolling 72h

**Scenarios (30d):**
- A — Negotiated framework — 25% (Δ −10pp)
- B — Frozen attrition — 45% (Δ 0pp)
- C — Re-escalation — 30% (Δ +10pp)

**Predictions to score at T+1 (10 May), T+3 (12 May), T+7 (16 May).**
