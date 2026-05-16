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

## 2026-05-12 (Day 74)

### T+1 scoring of 2026-05-11 predictions (scored before drafting)

- **Trend (Worse, Conf High) — HIT.** Trump called ceasefire "on massive life support"; met generals on military options; two US officials signalled "leaning toward military action"; Hezbollah launched 3 attacks on Israeli forces; US imposed 12 new Iran-oil-to-China sanctions; Brent rose 2.5–3% on ceasefire-collapse signals. All vectors confirm Worse.
- **Threat level (4/5 held) — HIT.** No formal Iranian closure upgrade; no confirmed strike on named Gulf-state energy asset (Kharg spill origin unattributed). 4→5 trigger not crossed. Boundary conditions at maximum pressure.
- **W1 (US diplomatic response / new mediation by EOD 13 May) — PARTIAL HIT.** Trump departed for China today; China track now primary diplomatic node. No formal new US proposal; no Oman/Pakistan back-channel signal. Partial: new channel (China) activated; no proposal content. Scored as Partial.
- **W2 (40-nation ministers meeting outcome today) — ACTIVE / PENDING.** Meeting convenes today 12 May (UK MoD confirmed). Outcome not yet known at time of brief. Will score at T+1 (13 May).
- **W3 (Strike on named Gulf-state energy infrastructure) — MISS (rolling).** No confirmed strike on Ras Laffan, Ras Tanura, Fujairah refinery, Jebel Ali, Bandar Abbas, or Kharg terminal. Kharg spill is adjacent risk but cause unattributed. W3 rolls forward.
- **W4 (Trump resumes Project Freedom or new military operation) — PARTIAL.** Trump met generals; US officials on record about "leaning toward military action"; Project Freedom resumption under consideration (Axios). Not yet executed — deferred to post-China summit. Scored as Partial.
- **W5 (Iranian closure upgrade / sovereignty declaration) — MISS.** No formal SNSC/IRGC-Navy upgraded closure declaration. Iran re-stated Hormuz sovereignty demand in diplomatic context but no operational declaration. W5 rolls forward.

### Surprise log (12 May)
- **Kharg Island oil spill (~80,000 bbl, Copernicus confirmed)** — Structural signal for Iranian oil export capacity degradation; cause unattributed. Affects Infrastructure, Maritime (2 categories). Hard satellite signal (Tier 2 equivalent via Copernicus/Reuters).
- **US SPR release of 53.3 million barrels** — First coordinated SPR release in this conflict; signals US domestic political pressure threshold crossed. Affects Infrastructure, Outlook (2 categories). Hard (DOE announcement).
- **Trump departs for Beijing TODAY** — Iran war top agenda; no major Iran decision before summit (14–15 May); China track now primary diplomatic node. Affects Diplomatic, Military, Outlook (3 categories). Hard (CNN/AP/The National).
- **Re-escalation scenario (C) becomes modal (44%)** — First time in conflict. Structural milestone for scenario assessment.

### 2026-05-12 — Predictions logged for scoring at T+1 (13 May), T+3 (15 May), T+7 (19 May)

**Trend:** Worse (Confidence: High — ceasefire "on massive life support," re-escalation modal, military options actively under consideration)
**Threat level:** 4/5 (held — no formal closure, no named energy asset confirmed struck; but post-summit window is highest-risk period yet)

**Watchlist predictions:**
- W1 — 40-nation ministers meeting (today 12 May) produces binding commitment vs. communiqué only — deadline EOD 12 May
- W2 — Trump–Xi summit (14–15 May) produces Chinese Iran deliverable vs. symbolic only — deadline EOD 15 May
- W3 — Strike on named Gulf-state energy infrastructure — rolling 72h
- W4 — Trump resumes Project Freedom or orders new military strikes post-China summit — by EOD 17 May
- W5 — Kharg Island oil spill cause attribution (US strike / deliberate release / infrastructure failure) — rolling 72h

**Scenarios (30d):**
- A — Negotiated framework — 16% (Δ −2pp)
- B — Frozen attrition — 40% (Δ −2pp)
- C — Re-escalation — 44% (Δ +4pp) ← MODAL for first time

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(ceasefire holds through 15 May without new US strikes) = 0.62
- P(40-nation meeting produces binding commitment today) = 0.30
- P(Trump–Xi summit produces named Chinese deliverable on Iran) = 0.22
- P(strike on named Gulf-state energy asset within 72h) = 0.12
- P(Kharg spill confirmed as US strike within 72h) = 0.25

## 2026-05-13 (Day 75) — Backtest scoring and new predictions

### T+1 scoring of 2026-05-12 predictions (scored before drafting Day 75 brief)

- **Trend (Worse, Conf High) — HIT.** IRGC Bubiyan infiltration confirmed (Kuwait KUNA/Al Jazeera, 12 May); 40-nation coalition reached operational commitment milestone (Australia MoD, 13 May); Trump downplayed Iran at Beijing departure; Brent held $107–110/bbl range. All vectors confirm Worse.
- **Threat level (4/5 held) — HIT.** No formal closure upgrade; no confirmed strike on named Gulf-state energy asset. IRGC Bubiyan infiltration is threshold-adjacent but not a strike on infrastructure. 4→5 trigger not crossed.
- **W1 (40-nation meeting produces binding commitment) — HIT.** Australian MoD confirmed multinational military mission with named asset contributions (E-7A Wedgetail). UK/France co-chaired. Not just communiqué — specific national contributions pledged. P(binding commitment) was scored at 0.30 — well-calibrated for a correct outcome.
- **W2 (Trump–Xi summit produces Chinese Iran deliverable by EOD 15 May) — PENDING.** Summit underway 14–15 May. Roll to T+3 (15 May) scoring.
- **W3 (Strike on named Gulf-state energy infrastructure) — MISS (rolling).** No confirmed strike on Ras Laffan, Ras Tanura, Fujairah, Jebel Ali, Bandar Abbas, or Kharg terminal. IRGC Bubiyan infiltration is a significant security event but not an energy infrastructure strike per W3 definition. W3 rolls forward.
- **W4 (Trump resumes Project Freedom or new military strikes) — MISS (rolling).** Trump departed for Beijing; no new operation. Post-summit window (16 May+) is the next risk period. W4 rolls forward.
- **W5 (Kharg spill cause attribution within 72h) — PARTIAL.** Iran's VP attributed to foreign tanker ballast; independent experts (Windward AI, Conflict and Environment Observatory) contradict this. A second slick detected. Official attribution still unconfirmed. Scored as Partial. P(US strike confirmed within 72h) = 0.25 — well-calibrated for a non-confirmation.

### Surprise log (13 May)
- **IRGC Bubiyan Island infiltration disclosed** (Kuwait KUNA / Al Jazeera, 12 May): Four IRGC naval officers arrested, two escaped, one Kuwaiti soldier wounded. First confirmed IRGC covert ground operation on Gulf-state soil. Affects Military, Maritime, Diplomatic (3 categories). Hard signal (Kuwait government official statement / state news agency).
- **Second Kharg Island oil slick detected** (Windward AI, 12 May): ~12–20 sq km; assessed as crude not bunker fuel. Affects Infrastructure (1 category). Tier 2 commercial intelligence (Windward AI).
- **Bahrain sentences three for IRGC espionage** (The National, 12 May): Same day as Kuwait disclosure — pattern signal for coordinated IRGC Gulf-state operations. Affects Military (1 category).

### 2026-05-13 — Predictions logged for scoring at T+1 (14 May), T+3 (16 May), T+7 (20 May)

**Trend:** Worse (Confidence: High — IRGC Bubiyan confirmed; 40-nation operational commitment; diplomatic window narrowing)
**Threat level:** 4/5 (held — no formal closure, no named energy asset confirmed struck; IRGC infiltration threshold-adjacent)

**Watchlist predictions:**
- W1 — Trump–Xi summit (14–15 May) produces named Chinese Iran deliverable vs. symbolic outcome — deadline EOD 15 May
- W2 — New IRGC covert operation on Gulf-state soil following Bubiyan exposure — rolling 72h
- W3 — Strike on Gulf-state energy infrastructure (named assets) — rolling 72h
- W4 — Trump resumes Project Freedom or orders new military strikes post-China summit — by EOD 18 May
- W5 — Kharg Island slick reaches Qatar EEZ (~4 days per Windward) AND/OR second slick cause attribution — rolling 96h

**Scenarios (30d):**
- A — Negotiated framework — 16% (Δ 0pp)
- B — Frozen attrition — 38% (Δ −2pp)
- C — Re-escalation — 46% (Δ +2pp) ← MODAL, widening lead

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(ceasefire holds through summit without new US strikes) = 0.70
- P(Trump–Xi summit produces named Chinese Iran deliverable) = 0.18
- P(IRGC executes another confirmed Gulf-state covert operation within 72h) = 0.25
- P(strike on named Gulf-state energy asset within 72h) = 0.10
- P(Kharg slick reaches Qatar EEZ within 4 days) = 0.55
- P(Project Freedom resumed or new US strikes by EOD 18 May) = 0.30

**Methodology note:** IRGC Bubiyan infiltration was a Surprise (forecast as W2-type risk but not specifically as IRGC ground-infiltration of Gulf-state territory). It represents a new operational category: IRGC covert ground/maritime operations inside Gulf-state sovereign territory. Adding to watchlist as standing item separate from air/drone attacks going forward. Source: Kuwait KUNA / Al Jazeera (Hard tier — government official statement).

## 2026-05-14 (Day 76) — Backtest scoring and new predictions

### T+1 scoring of 2026-05-13 predictions (scored before drafting Day 76 brief)

- **Trend (Worse, Conf High) — HIT.** IRGC fast-boat swarm peaked at ~668 craft on 12 May (2.9× prior peak, Windward AI); Kuwait summoned Iran's envoy (KUNA/The National, 13 May); GCC condemned Bubiyan as "systematic attempt"; Brent at $107.77 (CNBC, 12 May). All vectors confirm Worse.
- **Threat level (4/5) — HIT.** No formal closure upgrade; no confirmed strike on named Gulf-state energy asset. Bubiyan follow-on covert op not confirmed within 72h.
- **W1 (Trump–Xi summit — Chinese Iran deliverable) — PENDING.** Summit opened 14 May (CNBC/AJ confirmed live); Xi avoided Iran in opening remarks; no deliverable announced through 06:00 UTC. Roll to T+3 (16 May scoring).
- **W2 (New IRGC covert operation on Gulf-state soil within 72h) — MISS (rolling).** No new confirmed IRGC ground infiltration disclosed. Kuwait on high alert; Iran denied Bubiyan allegations. W2 rolls forward.
- **W3 (Strike on named Gulf-state energy infrastructure) — MISS (rolling).** Marshall Islands bulk carrier struck 10 May in Qatar EEZ — vessel attack, not named energy infrastructure per W3 definition. Rolls forward.
- **W4 (Project Freedom resumed or new US strikes by EOD 18 May) — PENDING.** Trump in Beijing through 15 May; no new operation. Post-summit window (16–18 May) remains primary risk period. Roll to T+3.
- **W5 (Kharg slick Qatar EEZ / attribution) — PARTIAL.** Slick confirmed drifting SW; The National (13 May) analysts lean toward vessel discharge/aging pipeline. Slick now ~5+ days old with no confirmed US strike attribution. P(US strike) = 0.25 — correct non-confirmation. Attribution still open.

### Surprise log (14 May)
- **IRGC fast-boat surge to ~668 craft** (Windward AI, 12 May): 2.9× prior peak; Eastern Polygon (Bandar-e Jask) newly active. No prior collection in this zone. Significant escalation signal.
- **Xi Jinping opens Trump summit without mentioning Iran** (NBC News, 14 May): Trade and Taiwan foregrounded; reduces probability of Chinese Iran deliverable.

### 2026-05-14 — Predictions logged for scoring at T+1 (15 May), T+3 (17 May), T+7 (21 May)

**Trend:** Worse (Confidence: High — IRGC speedboat surge confirmed; summit talks underway without named deliverable; blockade sustained at ~5% transit baseline; Brent $107–110 range)
**Threat level:** 4/5 (held — no strike on named Gulf-state energy asset; no formal Iranian closure declaration; IRGC covert pattern continues but no new threshold event)

**Watchlist predictions:**
- W1 — Trump–Xi summit readout (EOD 15 May) — named Chinese Iran deliverable vs. symbolic/trade-only outcome
- W2 — IRGC follow-on covert operation on Gulf-state soil — rolling 72h
- W3 — Strike on Gulf-state energy infrastructure (Ras Laffan, Ras Tanura, Fujairah refinery, Jebel Ali, Bandar Abbas) — rolling 72h
- W4 — Trump resumes Project Freedom or orders new US military strikes post-summit — by EOD Mon 18 May
- W5 — Kharg slick reaches Qatar EEZ (~16 May) AND/OR confirmed cause attribution — rolling 96h

**Scenarios (30d):**
- A — Negotiated framework — 15% (Δ −1pp)
- B — Frozen attrition — 38% (Δ 0pp)
- C — Re-escalation — 47% (Δ +1pp) ← MODAL, extending lead

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(Trump–Xi summit produces named Chinese Iran deliverable by EOD 15 May) = 0.15
- P(IRGC executes another confirmed Gulf-state covert operation within 72h) = 0.22
- P(strike on named Gulf-state energy asset within 72h) = 0.10
- P(Kharg slick reaches Qatar EEZ or confirmed attribution by EOD 17 May) = 0.60
- P(Project Freedom resumed or new US strikes by EOD 18 May) = 0.32
- P(ceasefire formally declared dead / new US kinetic action before EOD 18 May) = 0.25

**Methodology note (14 May):** Xi Jinping's deliberate omission of Iran in opening summit remarks (NBC News, confirmed CCTV broadcast) is classified as a Soft-tier diplomatic signal — a head-of-state communication, not an operational event. It reduces but does not eliminate probability of Chinese deliverable. Source-behavior log: NBC News live blog (Tier 5) confirmed against CCTV official broadcast (Tier 1 Chinese state, regime communication) and CNBC analysis (Tier 4). Weighted as Soft-tier per methodology.

## 2026-05-15 (Day 77) — Backtest scoring and new predictions

### T+1 scoring of 2026-05-14 predictions (scored before drafting Day 77 brief)

- **Trend (Worse, Conf High) — HIT.** Trump "military decimation to be continued" (Truth Social, 15 May); vessel seized off Fujairah (UKMTO Hard tier, 14 May); Brent $111.37 (summit sentiment dip, not physical improvement); transit held at ~6 vessels/day (~10% baseline). All vectors confirm continued deterioration.
- **Threat level (4/5) — HIT.** No upgrade to 5/5: no strike on named Gulf-state energy infrastructure; no formal Iranian closure declaration; no new confirmed IRGC ground infiltration within 72h. Vessel seizure near Fujairah is escalatory but within existing pattern.
- **W1 (Trump–Xi Chinese Iran deliverable by EOD 15 May) — PARTIAL / MISS on binding deliverable.** Summit concluded with verbal Xi offer to help + no-military-equipment assurance + joint statement on Hormuz. No named deliverable (oil purchase cuts, formal pressure mechanism). Rubio confirmed Trump did NOT ask Xi to help end the war. Scored as MISS on W1 definition (named Chinese Iran deliverable). Rolling to W2 in new predictions (China transmits named deliverable by 22 May).
- **W2 (IRGC covert op on Gulf-state soil within 72h) — MISS (rolling).** No new confirmed IRGC ground infiltration beyond Bubiyan. Rolls forward as W5 in new predictions.
- **W3 (Strike on named Gulf-state energy infrastructure) — MISS (rolling).** UKMTO vessel seizure off Fujairah is a maritime seizure, not a named energy infrastructure strike per W3 definition. Rolls forward as W4.
- **W4 (Project Freedom resumed / new US strikes by EOD 18 May) — PENDING.** Trump "to be continued" posted but no kinetic operation confirmed yet. Post-summit window (16–18 May) open. Rolls to T+3 (scoring at EOD 18 May).
- **W5 (Kharg slick Qatar EEZ / attribution by EOD 17 May) — PENDING.** Slick approaching Qatar EEZ ~16 May per Windward. Attribution still unresolved. Rolls to T+3.

**Brier score inputs (Day 76 predictions):**
- P(Trump–Xi summit produces named Chinese Iran deliverable by EOD 15 May) = 0.15 → MISS. Score: (0.15−0)² = 0.0225 (good calibration — low probability, correctly not materialised on Hard definition)
- P(IRGC executes another confirmed Gulf-state covert operation within 72h) = 0.22 → MISS. Score: (0.22−0)² = 0.0484
- P(strike on named Gulf-state energy asset within 72h) = 0.10 → MISS. Score: (0.10−0)² = 0.01 (good calibration)
- P(Kharg slick reaches Qatar EEZ or confirmed attribution by EOD 17 May) = 0.60 → PENDING
- P(Project Freedom resumed or new US strikes by EOD 18 May) = 0.32 → PENDING
- P(ceasefire formally declared dead / new US kinetic action before EOD 18 May) = 0.25 → PENDING

### Surprise log (15 May)
- **Trump "military decimation to be continued" on Truth Social (NBC News / Times of Israel, 15 May Beijing time):** First direct public pre-announcement of kinetic resumption during an active diplomatic summit. Unusual signal; suggests post-summit military action is being communicated deliberately rather than accidentally.
- **IRGC vessel seizure off Fujairah (UKMTO, 14 May):** First confirmed IRGC maritime operation at Fujairah anchorage — directly adjacent to the Habshan–Fujairah bypass pipeline terminal. Qualitative escalation in IRGC operational geography.
- **Rubio: Trump did NOT ask Xi for help ending the war (NBC News, 15 May):** Counterintuitive given summit framing; suggests US is not relying on Chinese leverage as a primary peace mechanism, reducing the diplomatic constraint on military resumption.

### 2026-05-15 — Predictions logged for scoring at T+1 (16 May), T+3 (18 May), T+7 (22 May)

**Trend:** Worse (Confidence: High — "to be continued" Trump signal; vessel seizure at Fujairah bypass terminal; transit at ~10% baseline; Brent sentiment-driven not physical; IRGC surge unreversed)
**Threat level:** 4/5 (held — no strike on named Gulf-state energy asset; no new confirmed IRGC ground infiltration; no formal closure declaration)

**Watchlist predictions:**
- W1 — Trump resumes Project Freedom or orders new US military strikes — by EOD Mon 18 May
- W2 — China transmits named, verifiable Iran deliverable (measurable Iranian oil import reduction OR formal diplomatic action with observable Iranian response) — by EOD Fri 22 May
- W3 — Kharg slick reaches Qatar EEZ (~16 May per Windward) AND/OR confirmed cause attribution — rolling 96h
- W4 — Strike on named Gulf-state energy infrastructure (Ras Laffan, Ras Tanura, Fujairah refinery, Jebel Ali, Bandar Abbas, Habshan–Fujairah terminal) — rolling 72h
- W5 — IRGC follow-on covert operation on Gulf-state soil — rolling 72h

**Scenarios (30d):**
- A — Negotiated framework — 13% (Δ −2pp)
- B — Frozen attrition — 38% (Δ 0pp)
- C — Re-escalation — 49% (Δ +2pp) ← MODAL, 11pp lead

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(Trump resumes kinetic operation / Project Freedom by EOD 18 May) = 0.38
- P(China transmits named verifiable Iran deliverable by EOD 22 May) = 0.12
- P(Kharg slick confirmed in Qatar EEZ by EOD 17 May) = 0.65
- P(strike on named Gulf-state energy asset within 72h) = 0.11
- P(IRGC ground/maritime infiltration on Gulf-state soil within 72h) = 0.18
- P(ceasefire collapses / formally declared dead before EOD 18 May) = 0.30

**Methodology note (15 May):** IRGC maritime seizure near Fujairah (UKMTO Hard tier) classified as a new operational geography event — IRGC extending interdiction from Hormuz channel to Fujairah anchorage, directly threatening the Habshan–Fujairah bypass pipeline terminal. Adding "Fujairah bypass terminal" to W4 named asset list. Source reliability note: Rubio's State Dept confirmation that Trump did NOT ask Xi for help (NBC News, Tier 5 confirmed via Tier 1 State Dept) is treated as Hard-tier per methodology (government official statement in named capacity). Polymarket Hormuz normalisation resolved 0% — consistent with 0% being the correct calibration from Day 1 of this tracker (no false alarm generated).

## 2026-05-16 — Day 78 Backtest Entry

### T+1 scoring of 2026-05-15 predictions (scored before drafting Day 78 brief)

**Trend (Worse, Confidence High) — HIT.** UKMTO Warnings 057/26 (vessel seized 38nm NE Fujairah) and 058/26 (Indian livestock carrier sunk off Oman) both Hard-tier. Iran five-condition ultimatum (Fars/PBS/AP). Diplomatic deadlock deepening. All trend vectors confirm continued deterioration.

**Threat level (4/5 Severe) — HELD (correct).** No strike on named Gulf-state energy asset; no new confirmed IRGC ground infiltration; no formal kinetic US resumption. Vessel seizure + sinking qualify as maritime incidents within existing 4/5 pattern — no single event crosses 4→5 threshold per methodology (named energy infrastructure strike, formal closure declaration with kinetic enforcement, or new confirmed Gulf-state ground op).

**W1 (Trump resumes Project Freedom / strikes by EOD 18 May) — PENDING.** No kinetic action as of 06:00 UTC 16 May. EOD 18 May not yet reached.

**W2 (China transmits named verifiable Iran deliverable by EOD 22 May) — PARTIAL / LOW.** Xi pledged no military equipment to Iran (Trump/Fox); White House readout that Hormuz must remain open. But Chinese FM readout omitted Iran; Rubio said Trump asked nothing; no measurable reduction in Chinese oil imports from Iran. Scored as PARTIAL — verbal commitment only, no observable metric. Brier input: P=0.12, outcome remains 0 on Hard definition; tracking.

**W3 (Kharg slick Qatar EEZ by EOD 17 May) — LIKELY MISS.** Copernicus Sentinel and The National (13 May) confirm slick was single-event pattern; May 8 images showed no active continuation. Slick likely dissipated before reaching Qatar EEZ. Scored MISS for practical purposes, pending 17 May satellite confirmation.

**W4 (Strike on named Gulf-state energy infrastructure, rolling 72h) — MISS for window.** No confirmed strike. Rolling forward.

**W5 (IRGC follow-on covert operation on Gulf-state soil, rolling 72h) — MISS for window.** No new confirmed ground infiltration. Rolling forward.

**Brier score inputs (Day 77 / 15 May predictions):**
- P(Trump kinetic by EOD 18 May) = 0.38 → PENDING
- P(China named deliverable by EOD 22 May) = 0.12 → PARTIAL (trending toward 0 on Hard definition)
- P(Kharg slick Qatar EEZ by EOD 17 May) = 0.65 → LIKELY MISS → (0.65−0)² = 0.4225 (poor calibration — overconfident)
- P(strike named Gulf-state energy asset 72h) = 0.11 → MISS → (0.11−0)² = 0.0121
- P(IRGC ground op 72h) = 0.18 → MISS → (0.18−0)² = 0.0324

**Surprise log (16 May):**
- **Iran five-condition ultimatum (Fars / PBS / AP, 15 May):** First time Iran has publicly listed sovereignty over Hormuz as a pre-condition for any talks (not just a negotiating demand). Qualitative escalation in Iranian diplomatic posture — moves from bargaining to position-stating.
- **IRGC Chinese-vessel admission (14–15 May):** First operational selective-access event since ceasefire that creates a precedent for flag-state bilateral passage agreements under IRGC protocols. Embeds Iranian sovereignty operationally, not just rhetorically.
- **Indian livestock carrier sunk (UKMTO 058/26, 14 May):** First confirmed sinking of a non-tanker civilian cargo vessel in Gulf of Oman approaches since early conflict period. IRGC attack zone now confirmed to extend to Gulf of Oman sea lanes.

### 2026-05-16 — Predictions logged for scoring at T+1 (17 May), T+3 (19 May), T+7 (23 May)

**Trend:** Worse (Confidence: High — five-condition Iranian ultimatum; two UKMTO Hard-tier incidents; diplomatic track frozen; IRGC sovereignty operationalisation via Chinese access)
**Threat level:** 4/5 (held — no strike on named energy asset; no formal kinetic US resumption; no new Gulf-state ground op)

**Watchlist predictions:**
- W1 — Trump resumes Project Freedom or orders new US military strikes — by EOD Mon 18 May
- W2 — Iran submits verified written response to any new US nuclear proposal via Pakistan channel — rolling 72–96h
- W3 — Strike on named Gulf-state energy infrastructure (Ras Laffan, Ras Tanura, Fujairah terminal, Habshan) — rolling 72h
- W4 — China transmits named, verifiable Iran deliverable by EOD Fri 22 May
- W5 — IRGC follow-on covert operation on Gulf-state soil — rolling 72h

**Scenarios (30d):**
- A — Negotiated framework — 11% (Δ −2pp)
- B — Frozen attrition — 38% (Δ 0pp)
- C — Re-escalation — 51% (Δ +2pp) ← MODAL, 13pp lead

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(Trump resumes kinetic operation by EOD 18 May) = 0.35 (slight reduction from 0.38: inflation constraint confirmed, summit outcome soft)
- P(Iran submits verified written response via Pakistan by EOD 19 May) = 0.25
- P(Strike on named Gulf-state energy asset within 72h) = 0.10
- P(China transmits named verifiable Iran deliverable by EOD 22 May) = 0.10 (reduced from 0.12: Chinese FM silent on Iran)
- P(IRGC ground/maritime infiltration on Gulf-state soil within 72h) = 0.16
- P(Kharg slick confirmed Qatar EEZ by EOD 17 May) = 0.15 (revised sharply down from 0.65: single-event dissipation pattern confirmed)

**Methodology note (16 May):** Kharg slick probability was over-estimated at 0.65 yesterday — Windward 4-day projection was based on May 8 active slick data; the single-event dissipation pattern confirmed by The National/Copernicus on 13 May should have reduced this materially. Future slick trajectory predictions should incorporate single-event vs. continuous-release distinction before assigning high confidence to drift projections. Adjust Windward trajectory estimates: treat as Hard-tier only when active release confirmed in most recent satellite pass (≤48h old), not legacy drift model alone.

Source reliability update: IRIB/Fars reporting on Chinese vessel admissions was confirmed by Reuters shipping data within 12h — Fars semi-official channel on maritime facts (not political claims) has demonstrated two-day track record of advance signal ahead of western wire confirmation. Upweight Fars maritime operational reporting as Tier 4.5 lead (requires same-day Tier 3 corroboration, not 24h window).

## 2026-05-16 — Day 78 Backtest Entry

### T+1 scoring (predictions made Day 77 / 15 May, evaluated at Day 78 / 16 May)

**Trend (Worse, Confidence High) — HELD CORRECT.**
Trump transmitted new nuclear proposal to Iran 16 May with "serious consequences" warning. Shamkhani advisor response confirmed diplomatic incoherence deepening. BRICS ended without joint statement. PGSA toll system operational. All trend vectors confirm continued deterioration at same pace.

**Threat level (4/5 Severe) — HELD CORRECT.**
No strike on named Gulf-state energy infrastructure. No new confirmed IRGC ground infiltration. No US kinetic resumption. EOD 18 May deadline not yet reached. Threshold conditions for 4→5 not met.

**W1 (Trump resumes Project Freedom / strikes by EOD 18 May) — PENDING.** EOD 18 May not yet reached as of 09:50 UTC 16 May. No kinetic action as of brief cutoff.

**W2 (Iran submits verified written response via Pakistan by EOD 19 May) — PARTIAL/AMBIGUOUS.** Shamkhani publicly signalled readiness to sign; Iranian officials denied receiving new proposal. No Hard-tier Pakistan-channel confirmation of formal written response. Scored as ambiguous — tracking.

**W3 (Strike on named Gulf-state energy asset 72h) — MISS.** No confirmed strike. Rolling forward.

**W4 (China transmits named verifiable Iran deliverable by EOD 22 May) — MISS TRENDING.** China sent Ambassador (not FM Wang Yi) to BRICS; no named measurable deliverable. PENDING but trajectory strongly toward miss.

**W5 (IRGC follow-on covert/maritime op on Gulf-state soil 72h) — MISS.** No new confirmed ground infiltration. Rolling forward.

**Brier score inputs (Day 77 / 15 May predictions — evaluated 16 May):**
- P(Trump resumes kinetic by EOD 18 May) = 0.35 → PENDING
- P(Iran submits verified written response via Pakistan by EOD 19 May) = 0.25 → AMBIGUOUS/PARTIAL (Shamkhani signal only; Iranian FM denial)
- P(Strike named Gulf-state energy asset 72h) = 0.10 → MISS → (0.10−0)² = 0.0100
- P(China transmits named verifiable deliverable by EOD 22 May) = 0.10 → MISS TRENDING
- P(IRGC ground/maritime infiltration 72h) = 0.16 → MISS → (0.16−0)² = 0.0256
- P(Kharg slick Qatar EEZ by EOD 17 May) = 0.15 → MISS (consistent with Day 77 revision) → (0.15−0)² = 0.0225

**Surprise log (16 May):**
- **Trump 16 May nuclear proposal transmission:** First new formal proposal since Iran's "TOTALLY UNACCEPTABLE" rejection on 11 May — breaks the 5-day impasse with a new escalation-or-deal ultimatum framing.
- **Shamkhani vs. Iranian FM contradiction:** First public instance of a senior Khamenei-circle advisor publicly contradicting the Iranian FM's denial of receiving a proposal — operationally significant leadership incoherence signal.
- **BRICS FM meeting no joint statement:** Second consecutive BRICS meeting (April + May) to fail to produce a joint statement on Iran — Iran/UAE division confirmed as structural, not procedural.

---

### 2026-05-16 — Predictions logged for scoring at T+1 (17 May), T+3 (19 May), T+7 (23 May)

**Trend:** Worse (Confidence: High — Trump 16 May ultimatum; Iranian leadership incoherence; PGSA operational; dual blockade intact; Brent $108-109)
**Threat level:** 4/5 Severe (held — no named energy-infrastructure strike; no US kinetic resumption; no confirmed Gulf-state ground op)

**Watchlist predictions:**
- W1 — Trump resumes Project Freedom or orders new US military strikes — by EOD Mon 18 May
- W2 — Iran official Hard-tier confirmation of receipt/rejection of 16 May proposal via Pakistan channel — by EOD 19 May
- W3 — Strike on named Gulf-state energy infrastructure (Ras Laffan, Ras Tanura, Fujairah terminal, Habshan) — rolling 72h
- W4 — China transmits named, verifiable Iran deliverable by EOD Fri 22 May
- W5 — IRGC follow-on covert/maritime operation on Gulf-state soil or territorial waters — rolling 72h

**Scenarios (30d):**
- A — Negotiated framework — 10% (Δ −1pp)
- B — Frozen attrition — 37% (Δ −1pp)
- C — Re-escalation — 53% (Δ +2pp) ← MODAL, 16pp lead

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(Trump resumes kinetic operation by EOD 18 May) = 0.38 (increased from 0.35: "annihilation" rhetoric + new proposal + 18 May deadline convergence)
- P(Iran Hard-tier formal response via Pakistan by EOD 19 May) = 0.30 (new W2 formulation; Shamkhani signal is positive but FM denial creates ambiguity)
- P(Strike on named Gulf-state energy asset within 72h) = 0.10 (unchanged)
- P(China transmits named verifiable Iran deliverable by EOD 22 May) = 0.08 (reduced from 0.10: BRICS no joint statement; Wang Yi absence signals Chinese deflection)
- P(IRGC ground/maritime infiltration on Gulf-state soil within 72h) = 0.16 (unchanged)

**Methodology note (16 May):** Iranian leadership incoherence pattern (senior advisor vs FM contradiction) should be treated as a distinct signal category: it indicates internal factional dynamics that make formal diplomatic outcomes less predictable than either a coherent hardline or coherent pragmatist Iranian position would suggest. Future diplomatic signals should be weighted by whether they originate from: (a) Supreme Leader circle (Shamkhani = high authority), (b) FM/MOFА channel (Araghchi/Baghaei = formal diplomatic position), or (c) Parliament (Ghalibaf = political positioning). Contradictions between (a) and (b) are the highest-risk signal pattern for miscalculation.

Source reliability update: PGSA operational reporting (Lloyd's List via The Week, 11 May) — confirmed by multiple Tier 3+ sources. Lloyd's List maritime operational reporting confirmed as reliable Tier 3 signal for Hormuz access mechanics. Upweight to Tier 3 firm on maritime access/transit matters.
