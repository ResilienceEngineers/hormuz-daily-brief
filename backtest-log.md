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

---

## 2026-05-09 (evening update — second cycle)

### T+1 re-scoring of 2026-05-08 predictions (final, after full 9 May data)

- **Trend (Same, Conf Medium) — MISS confirmed.** As scored in this morning's entry, the trailing 72h delivered Hard escalation that meets §2's "Worse" threshold (US strikes on three Iranian ports; three US destroyers attacked; Sea Star III + Sevda disabled; Hezbollah first cross-border claim). Surprise also confirmed: US sovereign-territory strike on three Iranian ports affected 5 categories.
- **Threat level (4) — HIT (held all day).** No formal Iranian closure announcement and no Gulf-state energy infrastructure strike inside trailing 72h, despite the kinetic exchange.
- **W1 (Iran formal response by EOD Sun 10 May) — STILL PENDING at 20:10 UTC 9 May.** Trump (TF1, 9 May) said "expects to hear very soon"; CNN live blog confirms US "still awaiting" response. Score finalises in tomorrow's 10 May entry.
- **W2 (new vessel incident in/near Hormuz) — HIT confirmed both directions:** US strikes on Sea Star III + Sevda (8 May); Al Kharaitiyat transit attempt (9 May, in progress) also relevant as inverse — first attempted commercial transit, not incident.
- **W3 (Houthi statement on Red Sea posture) — MISS / Lindy validated again.** UKMTO JMIC 041 confirms "Houthi messaging continues without associated operational indicators."
- **W4 (Israeli strikes ≥3/day on Lebanon sustained) — HIT.** 19+ killed today; 23 per Al Jazeera count; Hezbollah claimed 9 attacks Saturday after 26 Friday including 2 cross-border into Israel. Cascade vector confirmed.
- **W5 (Iran airspace/maritime closure announcement) — MISS.** No formal closure declared.

### Surprise log (9 May)

- Qatari LNG **Al Kharaitiyat** transit attempt — first since war start, coordinated via Pakistan with Iranian acquiescence. Affects Maritime, Diplomatic, Infrastructure, Outlook (4 categories). Logged as positive-direction surprise.
- Bahrain arrest of 41 alleged IRGC-linked individuals — Tier 1 Bahrain MoI release. Affects Diplomatic, Military.
- UK pre-positions HMS Dragon for future European-led Hormuz escort mission — Tier 1 UK MoD. Forward-looking, no immediate operational change.

### Source notes (9 May, evening)

- **Reuters/LSEG** broke Al Kharaitiyat AIS data — Tier 2 Hard signal at first detection. Bloomberg corroborated within 1h. Strong positive calibration.
- **CNN live blog** maintained continuous Tier 5 corroboration of CENTCOM, Hezbollah, and Iranian Foreign Ministry signals through the day.
- **UKMTO recent-incidents page** still lagging on 7–9 May events (no public update as of writing). Standing flag: when the structural threat level is 4+ and a kinetic exchange is unfolding, UKMTO is *trailing* indicator, not leading.
- **Al Jazeera live blog (9 May)** consolidated Lebanon casualty count (19→23) faster than wire services. Consistent with prior calibration.

### Methodology delta candidate (Friday review queue)

- **Recency-bias trap, confirmed in second cycle:** the morning brief flagged "Worse" with High confidence on the 7–8 May exchange. By evening, the Al Kharaitiyat transit emerged as the first Hard de-escalation maritime signal in three weeks — but did not flip the trend, because the 7–8 May events remain inside the 72h window. The methodology held: a single Hard de-escalation event does not override prior Hard escalation. Confidence drops to Medium.
- **Add to Friday review:** when a high-novelty Hard de-escalation signal (e.g., first-of-kind transit) emerges inside an active kinetic-exchange window, the brief should explicitly call out the asymmetric weighting and flag the directional ambiguity rather than treating the trend as binary.

---

### 2026-05-09 evening — Predictions logged for scoring at T+1 (10 May), T+3 (12 May), T+7 (16 May)

**Trend:** Worse (Confidence: Medium — downgraded from morning High on Al Kharaitiyat counter-signal)
**Threat level:** 4/5 (held)

**Watchlist (24–72h):**
- W1 — Iranian formal written response to US 14-point framework via Pakistan — deadline EOD Sun 10 May (24h)
- W2 — Al Kharaitiyat transit completion to Port Qasim, OR halt/seizure by IRGCN — rolling 48h
- W3 — Strike on Gulf-state energy infrastructure (Ras Laffan, Ras Tanura, Fujairah refinery, Jebel Ali, Bandar Abbas terminals, Kharg) — rolling 72h
- W4 — Hezbollah third+ cross-border attack on Israel and major Israeli response — rolling 72h
- W5 — Iranian airspace or maritime closure announcement (SNSC / IRGC Navy via state outlet) — rolling 72h

**Scenarios (30d):**
- A — Negotiated framework — 27% (Δ +2pp vs morning)
- B — Frozen attrition — 43% (Δ −2pp)
- C — Re-escalation — 30% (Δ 0pp)

**Predictions to score at T+1 (10 May), T+3 (12 May), T+7 (16 May).**

## 2026-05-10

### T+1 scoring of 2026-05-09 (evening) predictions

- **Trend (Worse, Conf Medium) — HIT.** Trailing 72h continues to deliver Hard escalation events meeting §2 "Worse" rule. New 10 May signals reinforce: bulk carrier struck by unknown projectile 23nm NE of Doha (UKMTO Hard signal); IRGC public threat of "heavy assault" on US assets; Saturday's 39-dead Lebanon escalation; Sevda still smouldering on Sentinel-2 imagery 9 May. Confidence revised UP to High this morning.
- **Threat level (4) — HIT (held).** No formal Iranian closure announcement. The 10 May Doha-area strike was at-sea and not against a named Gulf-state energy asset (Ras Laffan, Ras Tanura, Fujairah refinery, Jebel Ali, Bandar Abbas terminals, Kharg). 4→5 trigger not flipped, but boundary actively probed.
- **W1 (Iranian formal written response by EOD Sun 10 May) — MISS.** Reply not delivered. Trump (Saturday): "expects to hear very soon"; Iranian FM spokesperson Baghaei: "We do our own work, we don't pay attention to deadlines or timing." Deadline reset to EOD Mon 11 May per methodology §11.
- **W2 (Al Kharaitiyat completion to Port Qasim, OR halt/seizure) — PENDING.** Vessel finder shows arrival expected Monday. No halt or seizure observed. Scores at 11 May entry.
- **W3 (Strike on named Gulf-state energy infrastructure) — MISS (technical) but watchlist conditions actively probed.** Doha-area at-sea strike (10 May UKMTO) is in the risk-margin but not against a named asset. Continues to hold W3 active.
- **W4 (Hezbollah third+ cross-border attack with major Israeli ground response) — PARTIAL HIT (cascade vector).** Hezbollah confirmed Saturday drone attacks; severely wounded IDF reservist; 39 killed in Lebanon Saturday. Scope is in the cascade pattern but no third cross-border strike + major ground response yet.
- **W5 (Iranian airspace/maritime closure announcement) — MISS (no announcement).** IRGC "heavy assault" threat is rhetorical, not formal closure declaration.

### Surprise log (10 May)

- **Bulk carrier struck by unknown projectile 23nm NE of Doha** (UKMTO 10 May). First at-sea projectile strike in Qatari proximity since 1 April Aqua 1 attack. Affects Maritime, Military, Diplomatic, Infrastructure, Outlook (5 categories). Logged as Hard escalation surprise.
- **IRGC explicit "heavy assault" threat** if Iranian tankers struck again. Affects Military, Diplomatic, Outlook. Tier 1 Iranian state-media communication.
- **Sentinel-2 satellite imagery** confirms Sevda still burning Saturday after Friday F/A-18 strike. Hard verification of CENTCOM claim. Tier 2 commercial satellite.

### Source notes (10 May)

- **UKMTO Twitter/X** broke the Doha bulk carrier strike at near-real-time speed — strong calibration. UKMTO recent-incidents page still lagging on web publication; X-feed remains the leading edge.
- **ABC News, CNN live blog, Times of Israel** all corroborated within 1–2h with consistent details (23nm NE Doha; small fire extinguished; no casualties).
- **Reuters/LSEG** Al Kharaitiyat tracking remains gold-standard Hard signal on AIS movement.
- **Bloomberg** confirmed Iran-approval framing on Al Kharaitiyat, narrowing the Tier 5 corroboration set.
- **Wikipedia 2026 SoH crisis** updated within 4h on multiple events — useful Tier 5 consolidation.

### Methodology delta candidate (Friday review queue)

- **Confirmed in third cycle:** When the structural threat level is 4+ and a diplomatic deadline window is active, treat both:
  - (a) any Hard de-escalation signal (e.g. selective-passage transit) as conditional and reversible inside 24h, AND
  - (b) any Hard escalation signal (e.g. at-sea strike near a Gulf-state ZEE) as resetting the trend assessment.
  The Al Kharaitiyat (positive) and Doha-area projectile strike (negative) both occurring within the same 24h window confirms the asymmetric weighting heuristic.

---

### 2026-05-10 — Predictions logged for scoring at T+1 (11 May), T+3 (13 May), T+7 (17 May)

**Trend:** Worse (Confidence: High — upgraded on Doha-area strike + Lebanon 39-dead day + IRGC threat)
**Threat level:** 4/5 (held — no closure announcement, no named-asset strike inside 72h, but boundary actively probed)

**Watchlist (24–72h):**
- W1 — Iranian formal written response to US 14-point framework — deadline EOD Mon 11 May (reset)
- W2 — Al Kharaitiyat arrival at Port Qasim, OR halt/seizure by IRGCN — deadline EOD Mon 11 May
- W3 — Strike on Gulf-state energy infrastructure (Ras Laffan, Ras Tanura, Fujairah refinery, Jebel Ali, Bandar Abbas terminals, Kharg) — rolling 72h
- W4 — Hezbollah third+ cross-border strike with major Israeli ground response — rolling 72h
- W5 — Iranian airspace or maritime closure announcement — rolling 72h

**Scenarios (30d):**
- A — Negotiated framework — 22% (Δ −5pp)
- B — Frozen attrition — 40% (Δ −3pp)
- C — Re-escalation — 38% (Δ +8pp)

**Predictions to score at T+1 (11 May), T+3 (13 May), T+7 (17 May).**

## 2026-05-11 (Day 73)

### T+1 scoring of 2026-05-10 predictions (scored before drafting today's brief)

- **Trend (Worse, Conf High) — HIT.** Trump rejected Iran's counterproposal as "TOTALLY UNACCEPTABLE" (Truth Social, 10 May); Iran demanded Hormuz sovereignty recognition; UAE intercepted 2 drones; Kuwait air defenses activated; Qatar cargo vessel struck. All five signals hard-confirm Worse direction.
- **Threat level (4) — HIT (held).** No formal Iranian closure announcement; no named Gulf-state energy asset struck inside 72h. Boundary probed (UAE drones, Kuwait airspace, Qatar vessel) but 4→5 trigger not crossed.
- **W1 (Iranian formal response by EOD 11 May) — PARTIAL HIT.** Iran delivered counterproposal via Pakistan on 10 May. However, Trump rejected it immediately as "TOTALLY UNACCEPTABLE." Response arrived on schedule; content rejected. Scores as Partial Hit: delivery criterion met, diplomatic advance criterion failed.
- **W2 (Al Kharaitiyat arrival Port Qasim) — HIT.** Al Kharaitiyat transited Hormuz successfully (Kpler/LSEG confirmed) and was en route to Port Qasim with arrival expected 11 May. No halt or seizure. Full confirmation pending docking.
- **W3 (Strike on named Gulf-state energy infrastructure) — MISS.** UAE/Kuwait drone events and Qatar vessel strike are at-sea/airspace, not against named energy assets (Ras Laffan, Ras Tanura, Fujairah refinery, Jebel Ali, Kharg). Condition not met. W3 remains active.
- **W4 (Hezbollah third+ cross-border attack + major Israeli ground response) — MISS.** No confirmed third Hezbollah cross-border attack with major Israeli ground response in trailing 24h. W4 active rolling.
- **W5 (Iranian closure announcement) — MISS.** Iran warned UK/France of "decisive response" if warships deployed but no formal SNSC/IRGC-Navy maritime closure declaration. W5 active rolling.

### Surprise log (11 May)

- **Iran demands Hormuz sovereignty recognition** in counterproposal (Iranian state TV, CNBC, Reuters). Structural shift: Iran is now publicly claiming control rights over an international waterway. Affects Diplomatic, Military, Maritime (3 categories). Hard signal.
- **UK/France 40+ nation defence ministers meeting announced for 13 May** (UK MoD statement, AFP). First ministerial-level coordination for post-ceasefire Hormuz escort mission. Affects Alternative Routes, Diplomatic, Outlook (3 categories). Hard signal.
- **Kuwait air defenses activated against hostile drones** (Reuters/CNBC 10 May). First confirmed Kuwait airspace incursion since war began. Expands geographic footprint of Iranian drone operations beyond UAE.

### 2026-05-11 — Predictions logged for scoring at T+1 (12 May), T+3 (14 May), T+7 (18 May)

**Trend:** Worse (Confidence: High — dual rejection of proposals + 40-nation coalition formation + Iran Hormuz sovereignty claim)
**Threat level:** 4/5 (held — no formal closure, no named energy asset struck, but boundary conditions at maximum pressure)

**Watchlist (24–72h):**
- W1 — US diplomatic response to Iran rejection; any new mediation channel via Oman or Pakistan — deadline EOD 13 May (UK/France ministers meeting)
- W2 — UK/France 40-nation defence ministers meeting outcome (13 May) — will it produce a commitment or a communiqué only?
- W3 — Strike on Gulf-state energy infrastructure (Ras Laffan, Ras Tanura, Fujairah refinery, Jebel Ali, Bandar Abbas terminals, Kharg) — rolling 72h
- W4 — Trump orders resumption of Project Freedom or new military operation following Iran rejection — rolling 72h
- W5 — Iranian formal airspace/maritime closure upgrade OR declaration of Hormuz as Iranian sovereign waters — rolling 72h

**Scenarios (30d):**
- A — Negotiated framework — 18% (Δ −4pp)
- B — Frozen attrition — 42% (Δ +2pp)
- C — Re-escalation — 40% (Δ +2pp)

**Predictions to score at T+1 (12 May), T+3 (14 May), T+7 (18 May).**
