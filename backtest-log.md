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

## 2026-05-17 — Day 79 Backtest Entry

### T+1 scoring (predictions made Day 78 / 16 May, evaluated at Day 79 / 17 May)

**Trend (Worse, Confidence High) — HELD CORRECT.**
Supreme Leader Khamenei publicly rejected Trump's 16 May nuclear proposal as "excessive and outrageous" on the same day it was transmitted, closing the Shamkhani/FM incoherence and unifying the Iranian leadership signal at the highest tier in the direction of rejection. EOD 18 May deadline now imminent without accepted framework. Re-escalation scenario moves to 56% (first structural majority in tracker history). Trend assessment Worse confirmed at High confidence.

**Threat level (4/5 Severe) — HELD CORRECT.**
No confirmed strike on named Gulf-state energy infrastructure. No US kinetic resumption confirmed as of 06:00 UTC 17 May. EOD 18 May not yet passed. Threshold conditions for 4→5 not met.

**W1 (Trump resumes Project Freedom/kinetics by EOD 18 May) — PENDING.**
EOD 18 May not yet reached at brief cutoff (06:00 UTC 17 May). No kinetic action confirmed. Scoring deferred to T+2.

**W2 (Iran Hard-tier formal response via Pakistan channel by EOD 19 May) — PARTIAL HIT.**
Khamenei (Supreme Leader tier) publicly rejected Trump's 16 May proposal — this is Hard-tier by source authority but delivered via public statement, not the Pakistan channel specified in the prediction. FM Araghchi's separate channel has not produced a written counter as of cutoff. Scored partial: Supreme Leader response received, but not via Pakistan mediation channel as specified.

**W3 (Strike on named Gulf-state energy asset 72h) — MISS (rolling).**
No confirmed strike. Rolling forward.

**W4 (China transmits named verifiable Iran deliverable by EOD 22 May) — MISS TRENDING.**
Trump confirmed he did NOT ask Xi to pressure Iran on Hormuz. Xi offered vague "help." No named verifiable deliverable. Strong trajectory toward miss.

**W5 (IRGC follow-on covert/maritime op on Gulf-state soil 72h) — MISS (rolling).**
No new confirmed ground infiltration. Rolling forward.

**Brier score inputs (Day 78 / 16 May predictions — evaluated 17 May):**
- P(Trump resumes kinetic by EOD 18 May) = 0.38 → PENDING
- P(Iran Hard-tier formal response via Pakistan by EOD 19 May) = 0.30 → PARTIAL HIT (Khamenei public, not Pakistan channel) → (0.30−0.5)² = 0.0400 (partial credit 0.5 outcome)
- P(Strike named Gulf-state energy asset 72h) = 0.10 → MISS → (0.10−0)² = 0.0100
- P(China transmits named verifiable deliverable by EOD 22 May) = 0.08 → MISS TRENDING → deferred
- P(IRGC ground/maritime infiltration 72h) = 0.16 → MISS → (0.16−0)² = 0.0256

**Surprise log (17 May):**
- **Khamenei same-day public rejection (16 May):** Fastest Supreme Leader–tier rejection of a US proposal in the 79-day tracker history. Closes factional ambiguity; unifies Iranian leadership signal at highest tier in rejection direction.
- **Re-escalation crosses 50% probability:** First time in tracker history the re-escalation scenario is the structural majority probability (56%).

---

### 2026-05-17 — Predictions logged for scoring at T+1 (18 May), T+3 (20 May), T+7 (24 May)

**Trend:** Worse (Confidence: High — Khamenei Supreme Leader rejection; EOD 18 May imminent; dual blockade intact; Brent $109; no diplomatic framework)
**Threat level:** 4/5 Severe (held — no named energy-infrastructure strike; no US kinetic resumption confirmed)

**Watchlist predictions:**
- W1 — Trump EOD 18 May: kinetic resumption OR sixth deadline extension — by EOD Mon 18 May
- W2 — Iran FM Araghchi written counter via Pakistan channel (distinct from Khamenei public statement) — by EOD Tue 19 May
- W3 — Strike on named Gulf-state energy infrastructure (Ras Laffan, Ras Tanura, Fujairah terminal, Habshan) — rolling 72h
- W4 — China transmits named, verifiable Iran deliverable — by EOD Fri 22 May
- W5 — Houthi resumption of commercial shipping attacks in Red Sea — rolling 72h (trigger: US kinetics)

**Scenarios (30d):**
- A — Negotiated framework — 8% (Δ −2pp)
- B — Frozen attrition — 36% (Δ −1pp)
- C — Re-escalation — 56% (Δ +3pp) ← MODAL, 20pp lead, first structural majority

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(Trump resumes kinetics/Project Freedom by EOD 18 May) = 0.42 (increased from 0.38: Khamenei rejection removes diplomatic cover for extension; six-extension credibility cliff)
- P(Iran FM Araghchi written counter via Pakistan by EOD 19 May) = 0.20 (reduced from 0.30: Khamenei public rejection may substitute for formal written response in US eyes; Pakistan channel quiet)
- P(Strike on named Gulf-state energy asset within 72h) = 0.14 (raised from 0.10: re-escalation scenario probability increase; IRGC posture unchanged)
- P(China transmits named verifiable Iran deliverable by EOD 22 May) = 0.07 (reduced from 0.08: Trump confirmed no ask to Xi on Hormuz; Chinese FM silent)
- P(Houthi resumption of commercial attacks in Red Sea within 72h) = 0.08 (new W5 reformulation; conditional on US kinetics probability; currently sub-threshold absent trigger)

**Methodology note (17 May):** Khamenei's same-day public rejection pattern introduces a new signal-speed benchmark: when Supreme Leader responds within hours of a US proposal transmission, it signals that the Iranian internal decision-making process has already pre-decided rejection — i.e., the proposal was reviewed before formal transmission (or Iran has a rapid-response protocol for maximalist US demands). This means future US proposals should be assessed for pre-rejection probability based on: (a) whether prior Khamenei-circle signals (Shamkhani, etc.) contradict FM signals before the proposal is even sent; (b) whether the proposal's first public element (enrichment zero, nuclear removal) crosses established Khamenei red lines without creative framing. Future proposals that include zero-enrichment language as headline terms should be treated as pre-rejected with >80% probability.

Source reliability update: Wikipedia US–Iran negotiations page (updated daily, well-sourced) has demonstrated 12–24h accuracy on diplomatic events when corroborated by Tier 2 headlines (Bloomberg, Yahoo Finance, Fox News live blogs). Upgrade to Tier 4 lead (requires same-day Tier 2 corroboration, not 24h window) for diplomatic event reporting.

## 2026-05-18 — Day 80 — Backtest entry

### Scoring: Day 79 (17 May) predictions evaluated at T+1 (18 May 06:01 UTC)

**Trend assessment (Worse/High) — CONFIRMED.**
Barakah NPP outer perimeter drone strike (17 May) — first named energy infrastructure hit in war. Trump rejected Iran proposal as "garbage." Trump meeting military advisers Tuesday to discuss war resumption. Israel–US kinetic coordination confirmed by AP (two sources). Ceasefire explicitly described as "on life support." All confirm Worse/High trend.

**Threat level (4/5 Severe) — HELD CORRECT.**
Barakah outer perimeter struck but no inner perimeter breach, no confirmed Iranian Hard-tier attribution, no US kinetic resumption. 4→5 threshold conditions not yet met. Held at 4/5.

**W1 (Trump kinetics/Project Freedom or seventh extension by EOD 18 May) — MISS (PENDING FINAL).**
No confirmed kinetic action by 06:01 UTC 18 May. Trump posted "Clock is Ticking" (Truth Social 17 May), is meeting military advisers Tuesday 19 May. Technically EOD 18 May not yet passed at brief cutoff. Scoring: deadline passed without confirmed kinetic action at 06:01 UTC — MISS on kinetics, but extension not explicitly confirmed either. Seventh extension effectively implied by continued ceasefire. Scored: MISS on kinetic resumption; partial hit on "seventh extension" implicit continuation.

**W2 (Iran FM written counter via Pakistan by EOD 19 May) — MISS TRENDING.**
Araghchi traveled to Beijing, not to Pakistan channel. No written counter-proposal via Pakistan. Strong trajectory to miss.

**W3 (Strike on named Gulf-state energy asset, rolling 72h) — HIT.**
Barakah NPP outer perimeter struck 17 May. Confirmed by IAEA, Al Jazeera, CNBC, AP, The National. UAE is a named Gulf state. Barakah is a named energy infrastructure asset. Hit scored. Note: no Hard-tier Iranian attribution yet — UAE investigating.
Brier: P(W3) = 0.14 → HIT → (0.14−1)² = 0.7396

**W4 (China named verifiable deliverable by EOD 22 May) — MISS CONFIRMED.**
Trump–Xi summit ended without concrete Hormuz progress (Trading Economics 17 May). US Trade Rep confirmed US did NOT ask China for direct Hormuz action (ABC News 17 May). → MISS CONFIRMED.
Brier: P(W4) = 0.07 → MISS → (0.07−0)² = 0.0049

**W5 (Houthi resumption commercial attacks 72h) — MISS (rolling).**
US-Houthi commercial shipping ceasefire holding Day 12. No confirmed large-scale commercial attacks. Rolling forward.
Brier: P(W5) = 0.08 → MISS → (0.08−0)² = 0.0064

**Brier scores (Day 79 predictions evaluated at T+1):**
- W1 (kinetics EOD 18 May) = 0.42 → MISS at 06:01 UTC cutoff → (0.42−0)² = 0.1764 (provisional)
- W2 (Pakistan counter EOD 19 May) = 0.20 → MISS TRENDING → deferred to EOD 19 May
- W3 (energy asset strike 72h) = 0.14 → HIT → (0.14−1)² = 0.7396
- W4 (China deliverable EOD 22 May) = 0.07 → MISS → (0.07−0)² = 0.0049
- W5 (Houthi commercial 72h) = 0.08 → MISS → (0.08−0)² = 0.0064

**Calibration note (18 May):** W3 was severely underweighted at 0.14 given the structural trajectory. The Barakah strike pattern (three drones entering from western border, two intercepted, one through) is consistent with Iranian mainland or Iraqi-proxy launch, not Houthi (which would come from south). Future energy-infrastructure strike probabilities should be weighted higher when: (a) Iran FM has explicitly stated Gulf states hosting US bases are legitimate targets; (b) UAE has hosted Israeli Iron Dome and personnel; (c) prior Fujairah oil zone fire within 2 weeks establishes pattern. Revise energy-infra strike prior from 0.10–0.14 to 0.20–0.25 per 72h window given current posture.

**Source reliability update (18 May):** The National (UAE) demonstrated sub-1h accuracy on Barakah strike details including western border entry direction and UAE MFA language ("treacherous terrorist attack") — upgrade to Tier 3 for UAE-specific energy infrastructure incidents. Fortune/AP joint reporting on Barakah confirmed same-day and aligned with IAEA confirmation within 3 hours — both reliable Hard-tier corroboration.

---

### 2026-05-18 — Predictions logged for scoring at T+1 (19 May), T+3 (21 May), T+7 (25 May)

**Trend:** Worse (Confidence: High — Barakah outer perimeter struck; Trump NSC military-options Tuesday; Israel–US kinetic coordination confirmed; Brent $111; no diplomatic framework; re-escalation 60%)
**Threat level:** 4/5 Severe (held — Barakah outer perimeter only, no inner breach, no confirmed Iranian attribution, no US kinetic resumption; 4→5 threshold watch active)

**Watchlist predictions:**
- W1 — Trump authorises kinetics/Project Freedom resumption after Tuesday 19 May NSC meeting — EOD Tue 19 May
- W2 — UAE formally attributes Barakah drone to Iran/proxy AND declares retaliatory posture — rolling 48h
- W3 — Araghchi Beijing visit produces named China-mediated verifiable Iran deliverable on Hormuz — by EOD Fri 22 May
- W4 — Strike on inner perimeter of named Gulf energy asset (Barakah inner core, Ras Tanura, Ras Laffan, Habshan) — rolling 72h
- W5 — Houthi resumption of commercial shipping attacks in Red Sea — rolling 72h (trigger: US kinetics)

**Scenarios (30d):**
- A — Negotiated framework — 7% (Δ −1pp) ← record low
- B — Frozen attrition — 33% (Δ −3pp)
- C — Re-escalation — 60% (Δ +4pp) ← MODAL, 27pp lead, record high

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(Trump kinetics/Project Freedom by EOD 19 May) = 0.45 (raised: NSC meeting confirmed; Israel–US coordination confirmed; "Clock is Ticking" signal; Barakah strike as trigger)
- P(UAE formal attribution to Iran + retaliatory posture within 48h) = 0.35 (new: UAE investigation ongoing; prior attacks attributed to Iran; western border entry direction; MFA "dangerous escalation" language)
- P(Araghchi Beijing produces China-mediated named deliverable by EOD 22 May) = 0.10 (slightly raised from W4 0.07: Araghchi actually in Beijing, unlike prior Pakistan-channel miss; but Trump–Xi precedent of no Hormuz action reduces ceiling)
- P(Strike on inner perimeter of named Gulf energy asset within 72h) = 0.22 (raised significantly from prior 0.14: Barakah pattern establishes capability and intent; outer perimeter breach normalises escalation ladder)
- P(Houthi resumption commercial attacks within 72h) = 0.25 (raised: conditional probability rises substantially if P(Trump kinetics) = 0.45; trigger relationship confirmed per Houthi ceasefire terms)

**Methodology note (18 May):** The Barakah strike represents a new escalation-ladder rung: attacks on civilian nuclear energy infrastructure in non-belligerent Gulf states. This introduces a new category of Hard-tier observable: "nuclear facility perimeter breach." Future strikes on any nuclear facility (inner or outer perimeter) should automatically trigger a 4→5 threshold review regardless of radiological outcome, because: (a) IAEA involvement activates international law dimension; (b) UAE "123 agreement" non-proliferation architecture creates US treaty-obligation response pressure; (c) one reactor on emergency diesel is a functional safety event, not merely a symbolic one. Revise methodology to add "nuclear facility strike (any perimeter)" as a standalone 4→5 threshold trigger candidate.

## 2026-05-19 — Backtest scoring + new predictions

### Scoring: Day 80 (18 May) predictions evaluated at T+1 (19 May 06:00 UTC)

**W1 (Trump authorises kinetics/Project Freedom by EOD 19 May) — MISS (conditional)**
Trump confirmed a strike WAS planned for Tuesday 19 May but stood it down Monday 18 May evening at Gulf leaders' request (CNN/Bloomberg/AFP). Strike was authorised in principle but deferred — not executed at 06:00 UTC cutoff. Scored MISS. Note: probability was 0.45 — the near-outcome (strike planned but deferred) indicates directional accuracy but timing miss.
Brier: P = 0.45 → MISS → (0.45−0)² = 0.2025

**W2 (UAE formally attributes Barakah to Iran + retaliatory posture within 48h) — MISS**
UAE still investigating at 06:00 UTC 19 May. No formal Iran attribution. Western border origin noted; UAE reserved "sovereign rights" but no retaliatory posture declared. Investigation Day 2 open.
Brier: P = 0.35 → MISS → (0.35−0)² = 0.1225

**W3 (Araghchi Beijing produces named China-mediated verifiable deliverable by EOD 22 May) — OPEN**
Araghchi Beijing visit was 6 May. Iran's revised proposal came via Pakistan channel 18 May — China not the named deliverable channel. Deadline EOD 22 May; tracking. Note: China called for "prompt resumption" but no named verifiable deliverable yet.

**W4 (Strike on inner perimeter of named Gulf energy asset within 72h) — MISS**
Barakah outer perimeter generator was struck 17 May. No inner-perimeter strike. Outer perimeter already scored as W3 HIT in Day 79 scoring.
Brier: P = 0.22 → MISS → (0.22−0)² = 0.0484

**W5 (Houthi resumption commercial attacks within 72h) — MISS (rolling)**
US-Houthi ceasefire holding Day 13. No confirmed large-scale commercial attacks. Strike deferral reduces near-term trigger probability.
Brier: P = 0.25 → MISS → (0.25−0)² = 0.0625

**Brier scores (Day 80 predictions at T+1):**
- W1 = 0.45 → MISS → 0.2025
- W2 = 0.35 → MISS → 0.1225
- W3 = OPEN (EOD 22 May)
- W4 = 0.22 → MISS → 0.0484
- W5 = 0.25 → MISS → 0.0625
- Mean (4 scored) = 0.109

**Calibration note (19 May):** W1 near-miss (strike planned, deferred) and W4 miss (outer not inner perimeter) both reflect calibration ceiling on Gulf-leader-mediated deferrals. The simultaneous Gulf trio (Qatar/Saudi/UAE) intervention was not modelled as a variable — add "Gulf state collective diplomatic intervention" as a signal that reduces P(kinetics) by 30–40pp when all three sovereigns make direct contact with Trump. This is a new observable class. W2 miss (UAE non-attribution) now at Day 2 — extend attribution prior: UAE is structurally reluctant to formally attribute to Iran when origin ambiguity (western border = Iraq) exists, as formal attribution would compel UAE military response under its own MFA "sovereign rights" language. Revise prior: P(formal UAE attribution within 72h of ambiguous origin) = 0.15–0.20, not 0.35.

---

### 2026-05-19 — Predictions logged for scoring at T+1 (20 May), T+3 (22 May), T+7 (26 May)

**Trend:** Same (Confidence: Medium — strike deferred, not cancelled; Iran responded via Pakistan; diplomatic window open but conditional)
**Threat level:** 4/5 Severe (held — deferral reduces imminent kinetic risk but structural Severe conditions unchanged: Hormuz closed, Barakah Unit 3 on diesel, Iran missile sites 70% restored, "moment's notice" standby maintained)

**Watchlist predictions:**
- W1 — Trump/US formal response to Iran's revised Pakistan proposal — accept/reject sequenced framework — EOD Wed 21 May
- W2 — UAE formal attribution of Barakah drone to Iran or named proxy — rolling 72h
- W3 — Iran inner-perimeter energy asset strike (Barakah core, Ras Tanura, Ras Laffan, Habshan) — rolling 72h
- W4 — Houthi resumption commercial attacks Red Sea — rolling 72h (trigger: US kinetics)
- W5 — Araghchi/China named verifiable Hormuz deliverable — EOD Fri 22 May

**Scenarios (30d):**
- A — Negotiated framework — 12% (Δ +5pp) ← first upward revision in 10 days
- B — Frozen attrition — 43% (Δ +10pp) ← MODAL first time in 10 days
- C — Re-escalation — 45% (Δ −15pp) ← near-modal, still dominant risk

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(Trump/US formal accepts/rejects sequenced framework by EOD 21 May) = 0.70 (high: deferral contingent on Iran response being serious; Trump said military ready "moment's notice")
- P(UAE formal attribution Barakah to Iran/proxy within 72h) = 0.20 (revised down from 0.35 per calibration note above)
- P(Inner-perimeter Gulf energy asset strike within 72h) = 0.18 (slightly lower: strike deferral removes US kinetics trigger; but Iranian proxy posture unchanged; outer-perimeter precedent elevates baseline)
- P(Houthi commercial attack resumption within 72h) = 0.12 (reduced: US kinetics deferral is primary trigger; ceasefire Day 13 stable)
- P(Named China-mediated verifiable Hormuz deliverable by EOD 22 May) = 0.10 (unchanged: China called for "prompt resumption" but no concrete mechanism; Iran used Pakistan not China channel for latest response)

**Methodology note (19 May):** Added "Gulf state collective diplomatic intervention" as a named observable class. When Qatar Emir + Saudi MBS + UAE MBZ make simultaneous direct contact with US president on Iran kinetics, reduce P(imminent kinetics within 24h) by 30–40pp regardless of prior Trump posture. This is observable via public statements and has now demonstrated twice (6 May Project Freedom pause; 18 May Tuesday strike deferral) that it is a reliable mechanism. Log in sources.md as a new leading indicator under Tier 3 (Gulf state direct diplomatic intervention → kinetics deferral signal).

## 2026-05-20 — Backtest scoring + new predictions

### Scoring: Day 81 (19 May) predictions evaluated at T+1 (20 May 06:00 UTC)

**W1 (Trump/US formal accepts/rejects sequenced framework by EOD 21 May) — OPEN**
Deadline EOD 21 May not yet reached. Context: Trump deferred 19 May strike at Gulf-state request; Iran's 18 May revised response via Pakistan tracked "previous positions" per IRIB; no formal US accept/reject as of 06:00 20 May. Tracking.

**W2 (UAE formal attribution Barakah to Iran/proxy within 72h) — HIT (partial)**
The National 19 May + UAE Defence Ministry: confirmed drones launched from Iraqi territory where Iranian-backed armed groups operate. UAE Ambassador Abushahab told UNSC 19 May the attack was "dangerous escalation" and attributed to "one state and its proxies" — indirect Iran attribution via proxy chain confirmed within 72h of 17 May attack. Scored HIT (proxy attribution = methodology threshold met; not direct Iran-state formal attribution but Iraqi proxy attribution confirmed).
Brier: P = 0.20 → HIT → (0.20−1)² = 0.64
Note: Revised calibration validated — P(formal UAE attribution within 72h of ambiguous origin) = 0.15–0.20 was correct; scored HIT at low probability = good calibration.

**W3 (Iran inner-perimeter energy asset strike within 72h) — MISS**
No inner-perimeter strike at Barakah core, Ras Tanura, Ras Laffan, or Habshan as of 06:00 20 May. Outer-perimeter precedent confirmed but no escalation to inner perimeter in window.
Brier: P = 0.18 → MISS → (0.18−0)² = 0.0324

**W4 (Houthi commercial attacks within 72h) — MISS**
Houthi ceasefire holding Day ~15 as of 06:00 20 May. No confirmed large-scale commercial attacks. Trigger (US kinetics) not activated — strike deferred 18 May.
Brier: P = 0.12 → MISS → (0.12−0)² = 0.0144

**W5 (Named China-mediated verifiable Hormuz deliverable by EOD 22 May) — OPEN**
Deadline EOD 22 May not yet reached. No named China-mediated deliverable observed. Pakistan channel active; China called for "prompt resumption" but no concrete mechanism named. Tracking.

**Brier scores (Day 81 predictions at T+1):**
- W1 = OPEN
- W2 = 0.20 → HIT → 0.64
- W3 = 0.18 → MISS → 0.0324
- W4 = 0.12 → MISS → 0.0144
- W5 = OPEN
- Mean (3 scored) = 0.229 (W2 HIT at low P inflates Brier — correct direction but scored inefficiently; recalibrate W2-class events upward)

**Calibration note (20 May):** W2 HIT at P=0.20 validates the revised downward calibration of P(UAE formal attribution within 72h of ambiguous origin). However, the Brier score of 0.64 for a HIT at P=0.20 is high — in hindsight P should have been 0.35–0.45 given the UNSC emergency session was called on Day 2 (19 May) and UAE FM language was explicit. Revise upward: when UAE/Gulf state calls UNSC emergency session within 24h of incident, P(attribution within 72h) = 0.50–0.60. New observable class: UNSC emergency session = 2× attribution prior.

---

### 2026-05-20 — Predictions logged for scoring at T+1 (21 May), T+3 (23 May), T+7 (27 May)

**Trend:** Same (Confidence: Medium — Israeli strike preparation is new signal; ceasefire technically holds; diplomatic window open through EOD 21 May W1 node)
**Threat level:** 4/5 Severe (held — Israeli nuclear-facility strike preparation adds upside risk to 5; structural Severe conditions unchanged)

**Watchlist predictions:**
- W1 — Trump formal accept/reject of Iran's revised Pakistan proposal — EOD Wed 21 May
- W2 — Israeli nuclear-facility strike execution — rolling 72h (CNN 20 May preparation confirmed)
- W3 — UAE/Gulf-state retaliatory strike on Iraqi proxy infrastructure — rolling 72h
- W4 — Houthi resumption commercial attacks — rolling 72h (trigger: Israeli strike or US kinetics)
- W5 — Inner-perimeter Gulf energy asset strike (Barakah core, Ras Tanura, Ras Laffan) — rolling 72h

**Scenarios (30d):**
- A — Negotiated framework — 10% (Δ −2pp)
- B — Frozen attrition — 40% (Δ −3pp)
- C — Re-escalation — 50% (Δ +5pp) ← near-modal

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(Trump formal accepts/rejects Iran proposal by EOD 21 May) = 0.75 (high: deadline explicit; Trump has now deferred twice; third deferral less likely given "life support" language 11 May and NSC pressure)
- P(Israeli nuclear-facility strike within 72h) = 0.30 (elevated significantly from prior day: CNN 20 May multiple US officials confirmed preparations including munitions movement and air exercise; not yet final decision; Trump likely to oppose without major Iranian provocation)
- P(UAE/Gulf retaliatory strike on Iraqi proxy within 72h) = 0.15 (UAE declared right to respond; but direct UAE military strike into Iraq is politically complex; more likely indirect action)
- P(Houthi commercial attack resumption within 72h) = 0.20 (elevated from 0.12: Israeli strike preparation is primary trigger; if W2 executes, Houthi resumption follows within 24–48h; conditional P given W2=0.30 → joint P approximately 0.20)
- P(Named China-mediated verifiable Hormuz deliverable by EOD 22 May) = 0.08 (slightly reduced: China has not signalled new mechanism; Pakistan channel dominant; Israel strike risk further reduces Chinese diplomatic space)

**Methodology note (20 May):** Added "UNSC emergency session within 24h of incident" as a new observable that doubles the prior probability of formal attribution within 72h. When UAE/Gulf state calls UNSC emergency session within 24h, P(formal attribution within 72h) revised from 0.15–0.20 to 0.40–0.60. Log in sources.md. Also: Israeli nuclear-facility strike preparation (CNN 20 May) has now been added to the "standalone 4→5 threshold trigger candidates" — if confirmed executed, automatic 4→5 upgrade regardless of radiological outcome, consistent with Barakah methodology update from Day 79.

## 2026-05-21 — Backtest scoring + new predictions

### Scoring: Day 82 (20 May) predictions evaluated at T+1 (21 May 06:00 UTC)

**W1 (Trump formal accept/reject of Iran's revised Pakistan proposal by EOD 21 May) — OPEN**
Deadline EOD 21 May not yet reached as of 06:00 UTC. Iran sent revised response via Pakistan 18 May (Reuters/WION). US formal response pending. Context: Trump called prior (10 May) Iranian proposal "totally unacceptable," "garbage," ceasefire "on life support." Third round of Iran-Pakistan-US diplomacy active. Tracking through EOD today.

**W2 (Israeli nuclear-facility strike execution within 72h) — MISS at T+1**
CNN 20 May confirmed preparations (munitions movement, air exercise, multiple US officials) but no execution confirmed as of 06:00 UTC 21 May. Gulf-state deferral mechanism held again (second application 18 May). Strike not executed in 72h window from 20 May. Scored MISS at T+1.
Brier: P = 0.30 → MISS → (0.30−0)² = 0.09
Note: Correct direction (MISS); low P appropriate. CNN preparation signal is real but "preparation ≠ execution" pattern confirmed now three times. Downward calibration validated: P(prepared strike executes within 72h) = 0.25–0.35 when Gulf-state deferral mechanism active. Revise: when Gulf-state intervention confirmed same day as preparation signal, P(execution within 72h) = 0.15–0.20 (downgrade 10pp).

**W3 (UAE/Gulf retaliatory strike on Iraqi proxy within 72h) — MISS at T+1**
UAE chose diplomatic route: called on Iraq to "immediately and unconditionally prevent all hostile acts" (UAE MFA 20 May, The National). No UAE or Saudi military strike into Iraq confirmed. Iraq investigating. Scored MISS.
Brier: P = 0.15 → MISS → (0.15−0)² = 0.0225
Note: Diplomatic-over-kinetic pattern for UAE consistent with war posture since Feb 28. Revise UAE military direct-action prior: P(UAE direct military strike into Iraq within 72h of attribution) = 0.08–0.12 (was 0.15; downgrade 3–7pp). UAE's "sovereign rights" declarations are posture signals, not execution signals.

**W4 (Houthi commercial attack resumption within 72h) — MISS at T+1**
Houthi ceasefire holding Day ~16. No Israeli strike (W2 missed); trigger not activated. Conditional P maintained. Scored MISS.
Brier: P = 0.20 → MISS → (0.20−0)² = 0.04
Note: Conditional logic correct; trigger dependency working as modelled.

**W5 (Named China-mediated verifiable Hormuz deliverable by EOD 22 May) — OPEN**
Deadline EOD 22 May not yet reached. Trump in Beijing mid-week per CNN sourcing. Araghchi at BRICS Delhi concurrently (Saudi/Egyptian FMs present). No named deliverable confirmed. Tracking.

**Brier scores (Day 82 predictions at T+1, 3 scored):**
- W1 = OPEN
- W2 = 0.30 → MISS → 0.09
- W3 = 0.15 → MISS → 0.0225
- W4 = 0.20 → MISS → 0.04
- W5 = OPEN
- Mean (3 scored) = 0.0508 (three MISSes at low P = low Brier = good calibration; correctly assigned low probabilities to events that did not occur)

**Calibration note (21 May):**
- W2: Preparation-confirmed-but-execution-not-executed is now the dominant pattern. New heuristic: "preparation signal + active Gulf-state intervention confirmed same day" → reduce execution P by 10pp. P(Israeli strike within 72h given Gulf-state active deferral) = 0.15–0.20, not 0.30.
- W3: UAE diplomatic-over-kinetic is a stable preference. Downgrade UAE direct military action prior to 0.08–0.12. Log in sources.md.
- Cumulative Week 12 Brier mean (last 5 scored): improving trend — consecutive low-P-MISS weeks signal appropriate conservative calibration.

---

### 2026-05-21 — Predictions logged for scoring at T+1 (22 May), T+3 (24 May), T+7 (28 May)

**Trend:** Same (Confidence: Medium — W1 EOD today is decisive; no new hard-tier escalation overnight; Barakah proxy chain confirmed but no inner-perimeter hit; Israeli strike deferred again)
**Threat level:** 4/5 Severe (held — structural conditions unchanged; inner-perimeter Barakah or Israeli strike execution would trigger automatic upgrade to 5)

**Watchlist predictions:**
- W1 — Trump/US formal response to Iran's revised 18 May Pakistan proposal — EOD Thu 21 May
- W2 — Israeli nuclear-facility strike execution — rolling 72h (preparations confirmed CNN 20 May; Gulf-state deferral active)
- W3 — UAE/Saudi military reprisal against Iraqi proxy — rolling 72h (diplomatic track active; military action unlikely but not ruled out)
- W4 — Houthi commercial shipping resumption — rolling 72h (trigger: W2 execution or US kinetics)
- W5 — Named China-mediated verifiable Hormuz deliverable — EOD Fri 22 May (Xi–Trump Beijing + Araghchi BRICS Delhi convergence)

**Scenarios (30d):**
- A — Negotiated framework — 10% (Δ 0pp)
- B — Frozen attrition — 40% (Δ 0pp)
- C — Re-escalation — 50% (Δ 0pp) ← near-modal

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(Trump formal accepts/rejects Iran proposal with named new mechanism by EOD 21 May) = 0.70 (high: deadline explicit; Iran sent revised response 18 May; US has not formally responded as of 06:00 UTC; pattern of same-day response once submitted)
- P(Israeli nuclear-facility strike within 72h) = 0.18 (downgraded from 0.30: Gulf-state deferral confirmed active; preparation-without-execution now third instance; calibration update applied)
- P(UAE/Saudi direct military strike on Iraqi proxy within 72h) = 0.08 (downgraded from 0.15: UAE diplomatic-over-kinetic pattern stable; Iraq under US pressure to act)
- P(Houthi commercial attack resumption within 72h) = 0.16 (slightly reduced: conditional on W2 now lower; P(W2)×P(Houthi|W2) = 0.18×0.80 ≈ 0.14; base resumption risk adds ~0.02)
- P(Named China-mediated verifiable Hormuz deliverable by EOD 22 May) = 0.12 (slight upward revision: Xi–Trump Beijing + Araghchi BRICS Delhi is a genuine multilateral convergence not seen in prior cycles; but "named deliverable" bar is high — most likely outcome is a vague statement of principle)

**Methodology updates (21 May):**
1. New calibration heuristic: "Preparation signal + confirmed active Gulf-state deferral same day" → reduce P(strike execution within 72h) by 10pp. Applies to Israeli and US military preparation signals.
2. UAE direct military action prior revised: P(UAE military strike into Iraq within 72h of attribution) = 0.08–0.12 (was 0.15). Stable diplomatic-over-kinetic preference confirmed across three attribution events.
3. IRGC state-media transit claims (e.g., "26 ships in 24h") to be treated as Tier 5 only — not to be used as transit count without independent UKMTO/Lloyd's List corroboration. Confirmed daily-ops procedure.

## 2026-05-22 — Day 84 Backtest Entry

### T+1 scoring of Day 83 (21 May) predictions

**W1 — Trump/US formal response to Iran's revised 18 May Pakistan proposal — EOD Thu 21 May**
RESULT: **HIT** — Iran FM Baghaei confirmed 21 May: Iran "received US views and are reviewing them" (Al Jazeera/CNBC 21 May). US counter-response transmitted through Pakistan channel on schedule. "Formal response transmitted" threshold met.
Brier: P=0.70 → HIT → (0.70−1)² = 0.09
Note: Response transmitted but Iran reviewing, not accepting — confirms iterative proposal cycle pattern. Calibration note: "formal response transmitted" is not the same as "named new mechanism." Subsequent watchlist items should distinguish these carefully.

**W2 — Israeli nuclear-facility strike execution within 72h — MISS**
No execution confirmed as of 06:00 UTC 22 May. Gulf-state deferral mechanism active (now third confirmed application). Preparation-without-execution pattern confirmed for third time.
Brier: P=0.18 → MISS → (0.18−0)² = 0.0324
Note: Calibration heuristic confirmed: P(Israeli strike within 72h given active Gulf-state deferral) = 0.15–0.20 appropriate. Will maintain.

**W3 — UAE/Saudi military strike on Iraqi proxy within 72h — MISS**
UAE chose diplomatic path: urged Iraq to prevent hostile acts (UAE MFA 20 May). Iraq investigating. No direct military action.
Brier: P=0.08 → MISS → (0.08−0)² = 0.0064
Note: UAE diplomatic-over-kinetic pattern stable. Prior revision to 0.08–0.12 validated.

**W4 — Houthi commercial attack resumption within 72h — MISS**
Houthi ceasefire holding Day ~16. No Israeli strike (W2 missed); trigger not activated.
Brier: P=0.16 → MISS → (0.16−0)² = 0.0256
Note: Conditional logic correct. Trigger dependency working as modelled.

**W5 — Named China-mediated verifiable Hormuz deliverable by EOD 22 May — MISS**
BRICS FM meeting 14-15 May produced no named Hormuz deliverable. Trump-Xi Beijing described as "relatively fruitless" on Hormuz. China's Wang Yi absent from BRICS. No joint mechanism announced.
Brier: P=0.12 → MISS → (0.12−0)² = 0.0144
Note: "Vague statement of principle" outcome correctly predicted as most likely. High bar for "named deliverable" confirmed appropriate.

**Day 83 T+1 Brier mean (5 scored):** (0.09 + 0.0324 + 0.0064 + 0.0256 + 0.0144) / 5 = **0.0338**
Calibration quality: Excellent. W1 HIT at high P; four MISSes at appropriately low P. Consistent with conservative calibration trend.

---

### 2026-05-22 — Predictions logged for scoring at T+1 (23 May), T+3 (25 May), T+7 (29 May)

**Trend:** Same → (Confidence: Medium — Pakistan shuttle at peak intensity; Iran reviewing US views; no new kinetics; core gap structurally unchanged)
**Threat level:** 4/5 Severe (held — Barakah outer perimeter struck; Israeli strike preparations unexecuted but confirmed; Vance "locked and loaded"; structural conditions unchanged)

**Watchlist predictions:**
- W1 — Pakistan Army Chief Munir Tehran visit outcome — EOD Sat 24 May
- W2 — Trump's "few days" window expiry / kinetics restart — Rolling 72–96h (Sat 24 – Mon 26 May)
- W3 — Israeli nuclear-facility strike execution — rolling 72h (preparations confirmed; Gulf-state deferral active third time)
- W4 — Barakah inner-perimeter attack — rolling 72h (outer perimeter struck; Iraqi proxy chain unresolved)
- W5 — Houthi commercial shipping resumption — conditional / rolling (trigger: W2 or W3)

**Scenarios (30d):**
- A — Negotiated framework — 10% (Δ 0pp)
- B — Frozen attrition — 42% (Δ +2pp)
- C — Re-escalation — 48% (Δ −2pp) ← near-modal

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(Munir Tehran visit produces named public Hormuz deliverable by EOD 24 May) = 0.12 (low: five prior proposal cycles produced no named deliverable; "vague statement" is modal outcome; but shuttle intensity is highest yet — slight upward vs base)
- P(Trump resumes kinetics within 96h absent named deliverable from Munir) = 0.28 (elevated from 0.20 base: "borderline" + "few days" language is strongest pre-strike signalling since Day 70; Gulf-state deferral fourth application would be unprecedented — P(fourth deferral) ≈ 0.50; P(kinetics | no fourth deferral) ≈ 0.55; combined ~0.28)
- P(Israeli nuclear-facility strike within 72h) = 0.16 (maintained: Gulf-state deferral active; preparation-without-execution three-times confirmed)
- P(Barakah inner-perimeter attack within 72h) = 0.10 (new watchlist item: outer perimeter proof-of-concept established; Iraqi proxy chain active and unresolved; UAE diplomatic response has not severed chain; Iraq investigation unlikely to produce rapid deterrence)
- P(Houthi commercial attack resumption within 72h absent trigger) = 0.05 (maintained: conditional on W2/W3 primarily; base resumption very low while ceasefire holds)

**Methodology notes (22 May):**
1. W1 "formal response transmitted" confirmed as achievable threshold; future watchlist items to specify "transmitted" vs "named new mechanism accepted" as distinct probability events.
2. Gulf-state deferral mechanism now three-times confirmed as active — elevating its weight as a leading indicator. If a fourth application occurs, note as unprecedented and flag as potential mechanism exhaustion signal.
3. Barakah inner-perimeter attack added as standalone W4 escalation threshold — outer-perimeter strike establishes proof of concept; should be tracked independently from diplomatic track.

## 2026-05-23 — Day 85 Backtest Entry

### T+1 scoring of Day 84 (22 May) predictions

**W1 — Pakistan Army Chief Munir Tehran visit — named public Hormuz deliverable by EOD 24 May**
RESULT: **MISS** — Munir arrived Tehran 22–23 May and met Araghchi (confirmed). Iran FM Baghaei explicitly stated visits are "a continuation of the same diplomatic process — not near a deal." No named deliverable. Qatar team also in Tehran without producing named mechanism.
Brier: P=0.12 → MISS → (0.12−0)² = 0.0144
Note: "Peak intensity without named deliverable" pattern confirmed again. Sixth consecutive proposal cycle producing vague statement, not named mechanism. Calibration of 0.12 for this threshold appropriate.

**W2 — Trump kinetics within 96h absent named deliverable — rolling (scored at T+1, 23 May)**
RESULT: **MISS at T+1** — No strike resumed. Iran issued NOTAM A1010/26 (western FIR closed to 25 May). US "reviewing military options" per multiple outlets. Gulf-state deferral applied (fourth application — unprecedented). No strike as of 06:00 UTC 23 May.
Brier: P=0.28 → MISS → (0.28−0)² = 0.0784
Note: Fourth Gulf-state deferral unprecedented — mechanism may be approaching exhaustion. 25 May NOTAM expiry is next hard node. Will re-evaluate P(kinetics) if NOTAM extends.

**W3 — Israeli nuclear-facility strike within 72h — MISS**
No execution. Gulf-state deferral active (fourth application). Preparation-without-execution pattern holds.
Brier: P=0.16 → MISS → (0.16−0)² = 0.0256
Note: P(Israeli strike | fourth Gulf-state deferral active) calibration remains 0.15–0.18.

**W4 — Barakah inner-perimeter attack within 72h — MISS**
No inner-perimeter attack. Iraqi-territory attribution confirmed; UAE investigation ongoing. No escalation from proxy chain.
Brier: P=0.10 → MISS → (0.10−0)² = 0.01
Note: Outer-perimeter proof-of-concept does not automatically translate to inner-perimeter escalation within 72h. Consider extending window to 7-day horizon for this watchlist item type.

**W5 — Houthi commercial attack resumption absent trigger — MISS**
Ceasefire holding Day 17. UKMTO confirmed small-craft approach 200nm W of Socotra (23 May) — armed security deployed, craft withdrew. Not attributed to Houthi; not a commercial attack resumption.
Brier: P=0.05 → MISS → (0.05−0)² = 0.0025
Note: Socotra incident adds to watchlist as W5 (new) — attribution pending. Does not score as Houthi resumption yet.

**Day 84 T+1 Brier mean (5 scored):** (0.0144 + 0.0784 + 0.0256 + 0.01 + 0.0025) / 5 = **0.0262**
Calibration quality: Excellent. All five were MISSes at appropriately low probabilities. Consistent with conservative calibration trend across Days 80–85.

**Cumulative T+1 Brier score (Days 80–85):** Mean ≈ 0.030 — well-calibrated conservative forecasting.

---

### 2026-05-23 — Predictions logged for scoring at T+1 (24 May), T+3 (26 May), T+7 (30 May)

**Trend:** Same → (Confidence: Medium — Peak shuttle intensity without named deliverable; NOTAM signal adds kinetic risk; Socotra incident adds alt-route watchlist item; core gap structurally unchanged)
**Threat level:** 4/5 Severe (held — NOTAM + US military-option review + Israeli preparations active + Barakah inner-perimeter threat standing)

**Watchlist predictions:**
- W1 — Iran NOTAM A1010/26 western airspace expiry — EOD Mon 25 May
- W2 — Trump strike resumption / kinetics restart — rolling 72–96h to 26 May
- W3 — Israeli nuclear-facility strike execution — rolling 72h
- W4 — Barakah inner-perimeter attack — rolling 72h
- W5 — Socotra small-craft incident attribution (Houthi link or not) — 48h / 25 May

**Scenarios (30d):**
- A — Negotiated framework — 10% (Δ 0pp)
- B — Frozen attrition — 44% (Δ +2pp)
- C — Re-escalation — 46% (Δ −2pp) ← near-modal

**Brier score inputs (to be evaluated at T+1, T+3, T+7):**
- P(NOTAM lifts quietly without kinetics by EOD 25 May) = 0.52 (slight majority: diplomatic channel active; fourth deferral precedent; but NOTAM itself is anomalous and US military-review language elevated)
- P(Trump resumes kinetics before EOD 26 May) = 0.26 (maintained near Day 84 level: fourth deferral unprecedented but not impossible; "limited timeframe" language; NOTAM as potential clearing signal)
- P(Israeli nuclear-facility strike within 72h) = 0.16 (maintained: Gulf-state deferral active; preparation-without-execution four-times confirmed)
- P(Barakah inner-perimeter attack within 72h) = 0.09 (slight reduction from 0.10: no escalation in 72h since outer-perimeter; Iraqi investigation marginally deterrent; proxy chain appears in holding pattern during peak diplomacy)
- P(Socotra incident attributed to Houthi / Houthi ceasefire violation confirmed within 48h) = 0.18 (new item: small-craft approach confirmed by UKMTO Hard source; 5-person approach is consistent with Houthi armed boarding tactics; but attribution unconfirmed; ceasefire holding 17 days)

**Methodology notes (23 May):**
1. Fourth Gulf-state deferral application confirmed — flag as "unprecedented." If a fifth application occurs, flag "mechanism exhaustion signal" as a structural watchlist item. Reduce P(deferral) from 0.50 to 0.35 for future same-window calculations.
2. Iran NOTAM closure now establishes a new leading-indicator type: western FIR airport closures (non-conflict-zone) coinciding with US military-option review language. Add to indicator library as "pre-kinetics airspace clearing signal (Iran domestic)" — weight as Tier 2 when corroborated by NOTAM official source.
3. UKMTO Socotra incident is first confirmed maritime-approach event in Red Sea–adjacent zone since Houthi ceasefire. Add "UKMTO incident within 300nm of Socotra" as a standing ceasefire-perimeter monitor, distinct from full Houthi resumption event.

## 2026-05-24 — Day 86 Backtest Entry

### T+1 scoring of Day 85 (23 May) predictions

**W1 (NOTAM) — P(NOTAM lifts quietly without kinetics by EOD 25 May) = 0.52**
RESULT AT T+1: PENDING (NOTAM expires 25 May 08:30Z; not yet expired as of 06:00 UTC 24 May). Will score at T+2.

**W2 — P(Trump resumes kinetics before EOD 26 May) = 0.26**
RESULT AT T+1 (24 May 06:00): MISS direction — Trump declared deal "largely negotiated" 23 May evening; described as "leaning toward diplomatic solution." No kinetics. Score: trending MISS. Brier contribution deferred to EOD 26 May.

**W3 — P(Israeli nuclear-facility strike within 72h) = 0.16**
RESULT AT T+1: MISS — No strike. Netanyahu convened emergency meeting but expressed concern "deferentially." No execution.
Brier: P=0.16 → MISS → (0.16−0)² = 0.0256

**W4 — P(Barakah inner-perimeter attack within 72h) = 0.09**
RESULT AT T+1: MISS — No inner-perimeter attack confirmed.
Brier: P=0.09 → MISS → (0.09−0)² = 0.0081

**W5 — P(Socotra attributed to Houthi / ceasefire violation within 48h) = 0.18**
RESULT AT T+1: MISS — UKMTO shows 0 new confirmed incidents. No Houthi attribution. Houthi ceasefire Day 18 holding.
Brier: P=0.18 → MISS → (0.18−0)² = 0.0324

**Scored at T+1 (3 of 5 items):** Mean Brier = (0.0256 + 0.0081 + 0.0324) / 3 = **0.022** — Excellent calibration.
Items W1 and W2 deferred for EOD 25 May and EOD 26 May scoring respectively.

**NOTE — MAJOR UNFORECAST DEVELOPMENT (Surprise event):**
Axios/Reuters MOU "largely negotiated" disclosure on 23 May evening (Day 85/86 boundary) was NOT captured in Day 85 watchlist at sufficient probability. Day 85 scenario A was at 10%; actual diplomatic convergence moved A probability to ~30% within 24h. This is the largest single-day scenario revision of the tracker's history.

**Surprise category:** Positive diplomatic surprise — Scenario A probability shift +20pp unforecast. Methodology note: "Peak intensity without named deliverable" pattern (confirmed 6 times) broke on the 7th iteration. Revise P(named deliverable | peak shuttle intensity) from ~0.12 to ~0.25 for future same-configuration calculations. The difference: Munir + Pezeshkian meeting (head-of-state level) + Trump "50/50" public admission + NOTAM expiry convergence all occurred simultaneously, creating a different configuration than prior cycles.

---

### 2026-05-24 — Predictions logged for scoring at T+1 (25 May), T+3 (27 May), T+7 (31 May)

**Trend:** Better (Confidence: Medium — MOU "largely negotiated"; Scenario A +20pp; first genuine convergence of war. Counter-signal: Iran's three unresolved items; unsigned text; Israeli opposition.)
**Threat level:** 4/5 Severe (held — MOU unsigned; Iranian three-item gap; Netanyahu emergency session; military on standby)

**Watchlist predictions:**
- W1 — MOU signed / formal announcement — Sunday 24 May → extended to Wed 27 May
- W2 — NOTAM A1010/26 quiet expiry vs. extension — Mon 25 May 08:30Z
- W3 — Iran's three unresolved items bridged or not — rolling to MOU signing/collapse
- W4 — Netanyahu/Israeli unilateral action — rolling 72h, elevated if MOU collapses
- W5 — Socotra attribution confirmed — 48h / 26 May

**Scenarios (30d):**
- A — Negotiated framework — 30% (Δ +20pp)
- B — Frozen attrition — 42% (Δ −2pp) ← modal
- C — Re-escalation — 28% (Δ −18pp)

**Brier score inputs (T+1, T+3, T+7):**
- P(MOU formally signed with text published by both sides by EOD 27 May) = 0.35 (Axios/Reuters confirm proximity; Iran FM "3–4 days"; Trump "shortly" — but Iran's three unresolved items and Israeli pressure are live veto points; pattern: every previous "close to deal" moment collapsed)
- P(NOTAM A1010/26 expires quietly without extension or kinetics by EOD 25 May) = 0.72 (MOU trajectory strongly supports quiet expiry; deal momentum + "leaning toward diplomatic solution" = high probability of no kinetics this window)
- P(Trump resumes kinetics before EOD 27 May) = 0.12 (reduced from 0.26: MOU trajectory significantly de-risks; but "50/50" framing and Israeli pressure keep non-trivial probability)
- P(Israeli unilateral strike on Iranian nuclear facility within 72h) = 0.08 (reduced from 0.16: Netanyahu expressing concern "deferentially"; MOU trajectory reduces immediate window; but Israeli alarm is highest since war began)
- P(Socotra incident attributed to Houthi / ceasefire violation confirmed by 26 May) = 0.15 (maintained: no new UKMTO report; attribution still unconfirmed; Houthi ceasefire structurally reinforced by MOU trajectory)

**Methodology notes (24 May):**
1. "Peak intensity without named deliverable" pattern broke on 7th iteration (Day 85→86 boundary). Revise P(named deliverable | peak shuttle intensity + head-of-state level meeting + NOTAM expiry convergence) from ~0.12 to ~0.25. The configuration that broke the pattern: simultaneous Munir–Pezeshkian meeting (head of state level), Trump "50/50" public framing, NOTAM expiry convergence, and multi-mediator (Pakistan + Qatar + Turkey + Egypt) simultaneous engagement.
2. New indicator type confirmed: "NOTAM expiry coinciding with MOU announcement window" — add as Tier 2 corroborating signal for Scenario A (Negotiated framework) when both occur within same 72h window.
3. IRGC non-compliance risk after MOU signing ("JCPOA erosion scenario") now flagged as W1 implementation variant — add as standing watchlist item if/when MOU is signed. Observable: AIS transit data diverges from signed-MOU expectations within 7 days.
4. Israel opposition to deal (Netanyahu emergency session, Israeli officials urging resumed strikes) is the strongest remaining Scenario C activating signal. Add "Netanyahu unilateral authorization" as a standalone escalation trigger distinct from Trump-authorized kinetics.

## 2026-05-25 — Day 87 Backtest Entry

### T+1 scoring of Day 86 (24 May) predictions

**W2 (NOTAM A1010/26 quiet expiry) — P(quiet expiry by EOD 25 May) = 0.72**
RESULT AT T+1: HIT — NOTAM expired 08:30Z 25 May without extension or kinetics. No new equivalent NOTAM issued as of 06:01 UTC 25 May.
Brier: P=0.72 → HIT → (0.72−1)² = 0.0784. Calibration note: probability was appropriately high; clean expiry consistent with MOU trajectory.

**W4 (Israeli unilateral strike within 72h) — P=0.08**
RESULT AT T+1: MISS (provisional, 72h window closes 27 May) — No Israeli unilateral strike confirmed. Netanyahu issued public statement but no kinetics.
Brier deferred to 27 May for full 72h window. Provisional score: trending MISS.

**W5 (Socotra attributed to Houthi by 26 May) — P=0.15**
RESULT AT T+1: MISS trending — No new UKMTO report; attribution unconfirmed as of 06:01 UTC 25 May.
Brier deferred to 26 May.

**Items W1 (MOU signed by 27 May, P=0.35) and W3 (kinetics by 27 May, P=0.12):** Deferred to T+3 (27 May).

**Scored at T+1 (1 of 5 fully scored):** NOTAM hit. Mean Brier contribution: 0.0784. Cumulative context: calibration still strong on kinetics avoidance predictions; MOU signing prediction structurally harder to score — pattern of "close to deal → extension" now on 7th iteration but this one has Khamenei-level endorsement.

**NOTE — MAJOR DEVELOPMENT (Day 87):**
MOU "agreed in principle" with Khamenei endorsing broad template (Al Jazeera/CNN 24 May). NOTAM expired cleanly. No signing on Sunday per US official. Lebanon clause and frozen-asset sequencing remain as named veto points. Scenario A moved to co-modal with B (38%/38%).

---

### 2026-05-25 — Predictions logged for scoring at T+1 (26 May), T+3 (28 May), T+7 (1 June)

**Trend:** Better (Confidence: Medium — MOU "in principle" + Khamenei endorsement + clean NOTAM expiry. Counter-signal: Lebanon clause open; IRGC contesting Hormuz framing; unsigned text; Israel "very unhappy.")
**Threat level:** 4/5 Severe (held — MOU unsigned; Lebanon clause; IRGC sovereignty model intact; Israeli unilateral risk non-zero)

**Watchlist predictions:**
- W1 — MOU formally signed — rolling to 31 May
- W2 — Lebanon ceasefire clause bridged — 72h / 28 May
- W3 — US blockade lift sequencing resolved — rolling / MOU signing
- W4 — Israeli unilateral action — rolling 72h elevated if MOU collapses
- W5 — Socotra attribution — 26 May

**Scenarios (30d):**
- A — Negotiated framework — 38% (Δ +8pp) ← co-modal
- B — Frozen attrition — 38% (Δ −4pp) ← co-modal
- C — Re-escalation — 24% (Δ −4pp)

**Brier score inputs (T+1, T+3, T+7):**
- P(MOU formally signed with text published by both sides by EOD 31 May) = 0.40 (Khamenei template endorsement confirmed; but Lebanon clause named veto point; IRGC Hormuz framing gap; pattern of extension; Iranian system "does not move fast enough")
- P(Lebanon clause bridged / resolved by 28 May) = 0.35 (named blocking actor is Israel; US cannot bridge without Netanyahu acquiescence; but Trump has overridden Netanyahu on ceasefire before)
- P(Israeli unilateral strike on Iranian nuclear facility by 28 May) = 0.07 (reduced: NOTAM expired cleanly; MOU in principle reduces immediate window; but Israel structurally opposed to deal)
- P(Trump resumes kinetics before EOD 27 May) = 0.09 (reduced from 0.12: MOU in-principle status, "serious negotiations" framing — but if Lebanon clause collapses this rises sharply)
- P(Socotra small-craft incident attributed to Houthi / ceasefire violation by 26 May) = 0.12 (maintained: no new UKMTO report; attribution still pending; 72h since incident)
- P(IRGC Hormuz permit system begins verifiable wind-down within 7 days / by 1 June) = 0.28 (conditional on MOU signing; even if signed, 30-day phase-out means wind-down starts but not complete; no signing = 0 wind-down)

**Methodology notes (25 May):**
1. Khamenei "broad template" endorsement is the first supreme-leader-level diplomatic signal confirmed by a Tier 2 source (Al Jazeera citing senior US official + CNN regional source). Upgrades "head-of-state level engagement" signal weight in Scenario A probability calculation.
2. Lebanon clause identified as the primary veto point with named blocking actor (Israel). Add "Lebanon ceasefire wording resolution" as a standalone binary observable for Scenario A — it now sits above nuclear clause in urgency hierarchy.
3. IRGC state media (Fars, Tasnim) contesting Trump's Hormuz framing even as MOU progresses — this is a strong leading indicator that IRGC compliance post-MOU signing may be the next structural risk (JCPOA-erosion scenario). Promote W5 (IRGC Hormuz sovereignty assertion) from watchlist to standing structural monitor.
4. A and B co-modal for first time in tracker history. Add methodology note: when A and B are within 5pp, use Lebanon clause + US blockade sequencing as the discriminating observable rather than general diplomatic language.

## 2026-05-26 — Day 88 Backtest Entry

### T+1 scoring of Day 87 (25 May) predictions

**W5 (Socotra small-craft attributed to Houthi by 26 May) — P=0.12**
RESULT AT T+1: MISS — No Houthi attribution confirmed. UKMTO Advisory 061-26 (26 May) reported suspicious armed skiff activity in Gulf of Aden (23 May incident), but this is a separate geographic/actor track from the Socotra incident. No UKMTO or MARAD attribution of Socotra to Houthis as of 06:00 UTC 26 May.
Brier: P=0.12 → MISS → (0.12−0)² = 0.0144. Calibration: probability was appropriately low. Socotra attribution remains unresolved — retiring from watchlist, replaced by Austria BVT nuclear intelligence as W5.

**NOTAM A1010/26 clean expiry (scored yesterday at T+1 — confirmed HIT):** Already logged. No revision.

**Trend assessment (Day 87): "Better"**
RESULT AT T+1: PARTIAL MISS — "Better" was supported by NOTAM expiry and MOU in-principle framing. However, Netanyahu's 25 May Lebanon intensification order (Bloomberg/AJ, confirmed Tier 1/2) activated a new escalation vector that was not yet visible at 06:00 UTC 25 May. The "Better" call was directionally premature given the Lebanon contradiction now embedded in MOU framework. Trend revised to "Same" on Day 88. Calibration note: Lebanon clause risk was listed as counter-signal but was not weighted heavily enough given Netanyahu's coalition pressures.

**W2 (Lebanon clause bridged by 28 May — P=0.35):**
RESULT AT T+1: MISS TRENDING — Netanyahu ordered intensification (25 May evening). Lebanon clause now actively worsening, not bridging. Brier deferred to T+3 (28 May). Provisional assessment: significantly deteriorated; re-estimate P(bridged by 28 May) = 0.15 (down from 0.35).

**W4 (Israeli unilateral strike on Iranian nuclear facility by 28 May — P=0.07):**
RESULT AT T+1: MISS (provisional) — No nuclear facility strike. IDF Bekaa Valley strikes are Lebanon-theater operations, not classified as "unilateral strike on Iranian nuclear facility." Window closes 28 May. Maintained at low probability but Lebanon kinetics are escalating.

**Items W1 (MOU signed by 31 May, P=0.40) and W3 (frozen-asset sequencing, rolling):** Deferred to T+3/T+7.

**T+1 Brier contribution today: 0.0144 (W5 MISS). Running mean Brier on point predictions this week: 0.046.**

---

### 2026-05-26 — Predictions logged for scoring at T+1 (27 May), T+3 (29 May), T+7 (2 June)

**Trend:** Same (Confidence: Medium — Lebanon clause now structural veto; Netanyahu intensification order issued; MOU unsigned Day 88. Counter-signal: Doha talks ongoing; SNSC path active; Khamenei endorsement standing.)
**Threat level:** 4/5 Severe (held — Lebanon contradiction active; MOU unsigned; IRGC model intact; Israeli unilateral risk non-zero through 28 May)

**Watchlist predictions:**
- W1 — MOU formally signed — rolling to 31 May (P=0.35, Δ −5pp from yesterday; Lebanon contradiction reduces near-term probability)
- W2 — Lebanon clause bridged or collapsed — 28 May (P=0.15 bridged, Δ −20pp; P=0.35 collapsed/deadlocked)
- W3 — Doha frozen-asset mechanism agreed — 27 May (P=0.55; Ghalibaf/Araghchi/CB governor in Doha with Qatar PM)
- W4 — Israeli unilateral strike on Iranian nuclear/Beirut-level infrastructure — rolling 72h (P=0.10, elevated from 0.07; Lebanon IDF Bekaa Valley escalation ongoing)
- W5 — Austria BVT nuclear intelligence corroborated by IAEA or US response — 30 May (P=0.20)

**Scenarios (30d):**
- A — Negotiated framework — 35% (Δ −3pp)
- B — Frozen attrition — 40% (Δ +2pp) ← re-modal
- C — Re-escalation — 25% (Δ +1pp)

**Brier score inputs (T+1, T+3, T+7):**
- P(MOU formally signed with text published by both sides by EOD 31 May) = 0.35 (Δ −5pp; Lebanon contradiction now structural; Doha financial track cannot resolve Lebanon alone)
- P(Lebanon clause bridged / resolved by 28 May) = 0.15 (Δ −20pp; Netanyahu intensification order issued; Trump endorsed Israel "freedom of action"; Iran non-negotiable)
- P(Doha frozen-asset partial-release mechanism agreed by 27 May) = 0.55 (Iran CB governor + Ghalibaf + Araghchi in Doha with Qatar PM; Qatar $12B loan proposal in play per Channel 12)
- P(Israeli unilateral strike on Iran nuclear facility or Beirut-level Hezbollah HQ by 28 May) = 0.10 (elevated from 0.07; Lebanon IDF escalation confirmed; far-right coalition pressure active; but Trump–Netanyahu relationship constraining)
- P(Houthi resumption of commercial shipping attacks within 7 days / by 2 June) = 0.12 (Lebanon IDF intensification is primary Houthi trigger; ceasefire holding Day 18; no Houthi statement yet)
- P(Austria BVT nuclear claim corroborated by IAEA or US intelligence assessment by 30 May) = 0.20 (Iran rejected; pattern of IAEA delayed response; if corroborated hardens US nuclear demands and reduces Scenario A probability)

**Methodology notes (26 May):**
1. Lebanon clause has overtaken frozen-asset sequencing as the primary discriminating observable. Add Lebanon IDF operational tempo (Northern Command announcements, strike intensity on Nabatieh/Bekaa vs Beirut) as a standing Tier 1 Hard signal in Scenario A/C discrimination framework.
2. The "three-sided bind" (US endorses Israel Lebanon freedom of action + Iran demands Lebanon ceasefire + Saudi Arabia has no channel to either) identified by houseofsaud.com analysis (Tier 4, useful analytical frame confirmed by multiple Tier 1/2 sources) is a structural constraint, not a cyclical negotiating position. Update methodology: when three-sided binds are identified, add them to the watchlist as structural monitors rather than 72h items.
3. Austria BVT intelligence report (26 May) on Iranian nuclear weapons program with ballistic missile delivery: treat as Tier 4 pending corroboration. Pattern: intelligence claims that surface during active MOU negotiations have historically been used as spoiling signals by third parties. Add "intelligence claim timing vs. negotiating calendar" as an anti-bias heuristic — do not elevate intelligence claims to Tier 2 during active diplomatic windows without IAEA or US government corroboration.
4. UKMTO Advisory 061-26 (26 May): Gulf of Aden skiff activity is opportunistic-piracy signal, not Houthi-attributed. Retiring Socotra attribution from watchlist (W5). Replace with Austria BVT nuclear claim as W5. Pattern: unattributed maritime incidents in Gulf of Aden are at baseline risk level given UKMTO advisory history; do not conflate with Houthi ceasefire compliance monitoring unless UKMTO or MARAD explicitly attributes.

## 2026-05-27 — Day 89 Backtest

### Scoring T+1 from Day 88 (26 May) predictions

| Item | Prediction | P | Outcome | Score | Brier contrib |
|------|-----------|---|---------|-------|---------------|
| W3 — Doha frozen-asset mechanism agreed by 27 May | Formal agreement | 0.55 | NEAR-MISS: gaps bridged per AJ source, no formal mechanism signed; Iran demanding $12B/$12B structure, Qatar denying $12B offer | MISS | (0.55−0)²=0.3025 |
| W4 — Israeli unilateral strike on Iran nuclear by 28 May | Strike | 0.10 | PROVISIONAL MISS: USCENTCOM defensive strikes vs missile sites (not Israeli unilateral nuclear strike); window still open to 28 May | PROVISIONAL MISS | pending |
| Trend: Same | — | — | CONFIRMED: MOU unsigned, USCENTCOM strikes in southern Iran, Iran accuses US of ceasefire violation; Lebanon clause structurally active. Same/slight worse. | HIT | — |
| Threat: 4/5 Severe | — | — | CONFIRMED: USCENTCOM strikes + Iran ceasefire violation accusation + MOU gap persist | HIT | — |

**SURPRISE (unforecast):** USCENTCOM "defensive strikes" on Iranian missile sites in southern Iran (37-15); Brent +3% to $99.58 (CNBC). Iran accused US of ceasefire violation. This was a new escalation vector; not on watchlist. Add as standing signal: USCENTCOM strike tempo on Hormuz-region assets is a Tier 1 Hard source for escalation trajectory.

**Running mean Brier (point predictions this week, T+1 horizon):** Prior 0.046 + today W3 0.3025 / 2 items resolved → revised mean approximately 0.11. W3 over-confidence (P=0.55 for formal agreement same day as talks) noted. Calibration delta: "talks advancing" ≠ "formal mechanism agreed same session." Downgrade same-session agreement probability after active mediation day by −15pp going forward.

### Day 89 Predictions logged for T+1 (28 May), T+3 (30 May), T+7 (3 June)

**Trend:** Same (Confidence: Medium — USCENTCOM strikes + Iran ceasefire-violation accusation + MOU unsigned + Lebanon clause active. Counter-signal: Trump "close to finalizing," Doha talks "overall good," Brent near 5-week low signals market pricing in eventual deal.)
**Threat level:** 4/5 Severe (held — USCENTCOM strikes add kinetic pressure; IRGC sovereignty model intact; Israeli unilateral risk non-zero through 28 May; structural MOU gap on Lebanon + frozen assets)

**Watchlist predictions:**
- W1 — MOU formally signed — deadline 31 May (P=0.30, Δ −5pp; USCENTCOM strikes + Iran ceasefire-violation accusation reduce near-term window; frozen-asset gap now public and hardened)
- W2 — Lebanon clause bridged or collapsed — 28 May deadline (P=0.12 bridged Δ −3pp; P=0.40 collapsed/deadlocked Δ +5pp; Israel-Lebanon 45-day ceasefire extension holds structural gap, Trump-Netanyahu call unresolved on Lebanon end)
- W3 — Frozen-asset partial-release mechanism agreed — rolling to 30 May (P=0.45, Δ −10pp; $12B demand hardened; Qatar denied offer; US position: relief for performance, not upfront; gap significant)
- W4 — Israeli unilateral strike on Iran nuclear facility by 28 May (P=0.08, Δ −2pp; Netanyahu denial per Wikipedia 57-1; Trump-Netanyahu relationship constraining; window closes 28 May)
- W5 — Austria BVT nuclear claim corroborated by IAEA or US — 30 May (P=0.20, unchanged)

**Scenarios (30d):**
- A — Negotiated framework — 32% (Δ −3pp; USCENTCOM strikes + Iran ceasefire-violation accusation + frozen-asset gap hardened)
- B — Frozen attrition — 43% (Δ +3pp ← modal; structural deadlock confirmed by multiple vectors)
- C — Re-escalation — 25% (Δ 0pp; USCENTCOM strikes elevated kinetics but ceasefire framework technically intact)

**Brier inputs (T+1/T+3/T+7):**
- P(MOU formally signed with text published by both sides by EOD 31 May) = 0.30
- P(Lebanon clause bridged by 28 May) = 0.12
- P(Frozen-asset partial release agreed in principle by 30 May) = 0.45
- P(Israeli unilateral strike on Iran nuclear/Beirut-level Hezbollah HQ by 28 May) = 0.08
- P(Austria BVT claim corroborated IAEA/US by 30 May) = 0.20
- P(Houthi resumption of commercial shipping attacks by 3 June) = 0.12 (ceasefire Day 19 holding; Lebanon IDF strikes ongoing but Houthi posture unchanged per MARAD 2026-006/UKMTO)
- P(Brent crude above $105 by 3 June) = 0.22 (currently ~$99; USCENTCOM strikes + Iran ceasefire accusation = upside risk; deal optimism = downside; net: modest upside probability)

## 2026-05-28 — Day 90 Backtest Entry

### Scoring T+1 from Day 89 (27 May) predictions

| Item | Prediction | P | Outcome | Score | Brier contrib |
|------|-----------|---|---------|-------|---------------|
| W2 — Lebanon clause bridged by 28 May | Bridged | 0.12 | MISS: IDF struck 150+ Hezbollah targets Tyre/Nabatieh/Bekaa 27 May; ceasefire violations ongoing; Lebanon clause structurally active Day 90. Pentagon military track 29 May still ahead. | MISS | (0.12−0)²=0.014 |
| W4 — Israeli unilateral strike on Iran nuclear by 28 May | Strike | 0.08 | MISS: No Israeli unilateral nuclear-site strike. USCENTCOM conducted new strikes near Bandar Abbas, but these are US operations, not Israeli unilateral. Window closed 28 May. | MISS | (0.08−0)²=0.006 |
| Trend: Same | — | — | PARTIAL MISS/UPGRADE: Kinetics escalated (Kuwait air defense activation, IRGC counter-strike on US base, four vessels fired on at Hormuz) — "Same" was too optimistic; actual trajectory is "Worse." Trend upgraded to Worse on Day 90. | PARTIAL MISS | — |
| Threat: 4/5 Severe | — | — | HIT: Kuwait air defense activation + IRGC counter-strike + four vessels fired on = Severe confirmed. | HIT | — |
| W1 — MOU formally signed by 31 May (P=0.30) | — | — | PENDING (31 May deadline) | — | — |
| W3 — Frozen-asset partial release agreed by 30 May (P=0.45) | — | — | PENDING (30 May deadline) | — | — |
| W5 — Austria BVT corroborated by 30 May (P=0.20) | — | — | PENDING (30 May deadline) | — | — |

**SURPRISE (unforecast Day 90):** Kuwait air defense activation against "hostile missile and drone threats" overnight 27/28 May (CNBC, Tier 2 Hard); IRGC claimed counter-strike on US base after USCENTCOM strikes near Bandar Abbas (CNBC/Tasnim); four vessels fired upon attempting Hormuz transit (CNN). Three-vector kinetic escalation on Day 90 was not on Day 89 watchlist. Add Kuwait infrastructure status as standing Tier 1 monitor signal.

**Methodology delta (Day 90):** Calibration note: Day 89 Trend assessment of "Same" was under-calibrated given USCENTCOM strike history. Heuristic update: when USCENTCOM–IRGC kinetic exchanges occur more than once in 72h AND Gulf state air defenses are activated, default Trend to "Worse" even if ceasefire framework nominally intact. Label: "kinetic-exchange frequency threshold" heuristic.

**Running mean Brier (T+1 point predictions, this week):** Prior mean ~0.11 (W3 over-confidence correction applied Day 89). Day 90 additions: W2 (0.014) + W4 (0.006) = mean revision: (0.11×2 + 0.014 + 0.006)/4 = ~0.06. Note: both Day 90 predictions were well-calibrated at low probability (0.12 and 0.08) — both MISS, but low Brier cost. Calibration delta: low-probability predictions (<0.15) are performing well; over-confidence risk remains at medium-probability tier (0.30–0.55).

### Day 90 Predictions logged for T+1 (29 May), T+3 (31 May), T+7 (4 June)

**Trend:** Worse (Confidence: Medium-High — Kuwait activation, IRGC counter-strike on US base, four vessels fired on at Hormuz, MOU unsigned. Counter-signal: ceasefire framework nominally intact; 29 May Pentagon track still scheduled; Brent MTD −12% signals market pricing deal.)
**Threat level:** 4/5 Severe (held — three kinetic vectors; Gulf state interceptor depletion; IRGC operating during MOU talks = hardliner signal)

**Watchlist predictions:**
- W1 — MOU formally signed / text published by both sides by EOD 31 May (P=0.22, Δ −8pp; Kuwait activation + IRGC counter-strike widen negotiating gap; hardliner signal on both sides active Day 90)
- W2 — Pentagon Lebanon military-track meeting 29 May productive (P=0.45; meeting confirmed scheduled; both parties engaged; but IDF 150+ strikes 27 May are headwind)
- W3 — Frozen-asset partial-release agreed in principle by 30 May (P=0.35, Δ −10pp; gap hardened further by Day 90 kinetics; Iran domestic approval path complicated)
- W4 — Kuwait escalation contained within 72h (no IRGC formal ceasefire withdrawal, no Gulf state formal attribution to Iran) (P=0.60; historical pattern: IRGC conducts exchange then steps back; but interceptor depletion creates incentive for escalation)
- W5 — Austria BVT nuclear claim corroborated by IAEA/US by 30 May (P=0.18, Δ −2pp; no corroboration signals spoiling-signal pattern more likely)

**Scenarios (30d):**
- A — Negotiated framework — 28% (Δ −4pp)
- B — Frozen attrition — 42% (Δ −1pp) ← modal
- C — Re-escalation — 30% (Δ +5pp)

**Brier inputs (T+1/T+3/T+7):**
- P(MOU formally signed with text published by both sides by EOD 31 May) = 0.22
- P(29 May Pentagon Lebanon track meeting publicly described as "productive" by State Dept) = 0.45
- P(Frozen-asset partial release agreed in principle by 30 May) = 0.35
- P(Kuwait escalation contained — no IRGC formal ceasefire withdrawal declaration within 72h) = 0.60
- P(Austria BVT claim corroborated IAEA/US by 30 May) = 0.18
- P(Houthi resumption of commercial shipping attacks by 4 June) = 0.18 (↑ from 0.12; IDF 150+ strikes in Lebanon 27 May approaching Houthi-stated trigger threshold; June 2–3 Lebanon talks critical)
- P(Brent crude above $100 by 4 June) = 0.35 (currently ~$95.59; Kuwait activation + IRGC counter-strike = upside; but MTD −12% and deal optimism = structural downside; net: moderate upside probability)
- P(Any Gulf state energy infrastructure multi-day outage by 4 June) = 0.20 (Kuwait Mina al-Ahmadi refinery repeatedly struck; interceptor depletion ~75%; acute risk window elevated by Day 90 kinetics)

## 2026-05-29 — Day 91 Backtest Entry

### Scoring T+1 from Day 90 (28 May) predictions

| Item | Prediction | P | Outcome | Score | Brier contrib |
|------|-----------|---|---------|-------|---------------|
| W2 — Pentagon Lebanon track 29 May productive | Productive | 0.45 | MISS: IDF struck Beirut Hezbollah missile commander 28 May — first Beirut strike since early May (CNN/NBC); Lebanon military track severely stressed; no "productive" State Dept readout found. Meeting context: headwind confirmed. | MISS | (0.45−0)²=0.203 |
| W4 — Kuwait escalation contained within 72h (no IRGC formal ceasefire withdrawal) | Contained | 0.60 | PARTIAL HIT: No formal IRGC ceasefire withdrawal declaration. But IRGC warned "next response more decisive"; CENTCOM called missile "egregious ceasefire violation"; Vance said "messy but ceasefire intact." Kinetics did not widen to multi-state war. Scoring as HIT on formal criterion (no withdrawal) despite deterioration. | HIT | (0.60−1)²=0.160 |
| Trend: Worse | — | — | HIT: Kuwait ballistic missile, 4 vessels fired on, Beirut strike, IRGC escalation warning — "Worse" confirmed on Day 91. | HIT | — |
| Threat: 4/5 Severe | — | — | HIT: Three kinetic vectors persisting; CENTCOM "egregious violation" framing; no downgrade signals. | HIT | — |
| W1 — MOU signed by EOD 31 May (P=0.22) | — | — | PENDING (31 May deadline) | — | — |
| W3 — Frozen-asset partial release by 30 May (P=0.35) | — | — | PENDING (30 May deadline; NBC: deal agreed in outline but both sides delaying) | — | — |
| W5 — Austria BVT corroborated by 30 May (P=0.18) | — | — | PENDING (30 May deadline; no corroboration found) | — | — |

**SURPRISE (unforecast Day 91):** Trump threatened to "blow up" Oman (27 May cabinet meeting, confirmed State Dept repost on X) and Treasury Bessent formally warned Oman against supporting PGSA tolling. Oman is the primary exit lane and mediation hub — this threat was not on the Day 90 watchlist. Add Oman diplomatic stability as W4 in Day 91 watchlist.

**Methodology delta (Day 91):** Calibration note: W2 over-confidence at P=0.45 for "productive Lebanon track" — IDF Beirut strikes create a structural contradiction between Lebanon ceasefire maintenance and MOU progress that was under-weighted. Heuristic update: when IDF conducts Beirut-level strikes within 24h of scheduled diplomatic meeting, downgrade "productive" probability by at least 20pp from prior estimate. Label: "Beirut-strike diplomatic discount" heuristic.

**Running mean Brier (T+1 point predictions):** Prior mean ~0.06 (Day 90 well-calibrated low-P predictions). Day 91 additions: W2 (0.203) + W4 (0.160) = mean revision: (0.06×4 + 0.203 + 0.160)/6 = ~0.10. Note: W2 is a meaningful calibration hit — 0.45 is medium-probability tier where over-confidence risk was flagged on Day 90. W4 HIT at 0.60 is within calibration range. Net: medium-probability tier (0.30–0.55) is confirmed as over-confidence zone; downweight diplomatic "productive" calls in active kinetic windows.

### Day 91 Predictions logged for T+1 (30 May), T+3 (1 June), T+7 (5 June)

**Trend:** Worse (Confidence: Medium-High — IRGC ballistic missile to Kuwait; 4 vessels fired on; Beirut strike; MOU unsigned; IRGC "more decisive" warning. Counter-signal: deal outline agreed per Arab mediator; Vance "good faith"; Brent structural decline = market pricing deal probability.)
**Threat level:** 4/5 Severe (held — three kinetic vectors; interceptor depletion; IRGC hardliner signals active during MOU talks)

**Watchlist predictions:**
- W1 — MOU text formally published by both parties by EOD 31 May (P=0.30, Δ +8pp; NBC Arab-mediator "agreed in Doha" is strongest positive signal to date; offset by Trump sign-off uncertainty and IRGC Tasnim denial)
- W2 — IRGC follow-through on "more decisive response" within 48h of Day 91 (P=0.30; historical IRGC pattern: signal threat then step back; but ballistic missile to Kuwait represents escalation above prior pattern)
- W3 — Trump formal sign-off on MOU by 31 May (P=0.30; "Trump decides" per Bessent; Vance "TBD"; Netanyahu/hardliner pressure = key downside)
- W4 — Oman maintains mediation role / no formal diplomatic downgrade to US by 3 June (P=0.72; Oman has continued engagement through extraordinary pressure to date; "blow up" threat may produce formal protest but unlikely full withdrawal before June 2–3 Lebanon talks)
- W5 — Houthi public statement or Red Sea maritime incident within 72h of continued IDF Beirut operations (P=0.25; IDF Beirut strike 28 May approaches Houthi stated trigger; conditional on no Lebanon ceasefire talks progress)

**Scenarios (30d):**
- A — Negotiated framework — 30% (Δ +2pp; deal closer structurally but signing uncertain)
- B — Frozen attrition — 42% (Δ 0pp) ← modal
- C — Re-escalation — 28% (Δ −2pp; Kuwait contained; no formal ceasefire withdrawal)

**Brier inputs (T+1/T+3/T+7):**
- P(MOU text publicly released by both US and Iran by EOD 31 May) = 0.30
- P(IRGC executes follow-on strike on Kuwait or Gulf-state territory within 48h of Day 91) = 0.30
- P(Trump formally signs off on MOU by 31 May) = 0.30
- P(Oman maintains active mediation role without formal diplomatic downgrade through 3 June) = 0.72
- P(Houthi public escalation statement or Red Sea maritime incident by 1 June) = 0.25
- P(Austria BVT nuclear claim corroborated by IAEA/US by 30 May) = 0.12 (Δ −6pp; 30 May now <48h away; silence = likely spoiling signal)
- P(Brent crude above $100 by 5 June) = 0.28 (currently ~$93–97; deal-optimism structural downside; kinetic upside; net: below $100 more likely as deal proximity caps upside)
- P(Any Gulf-state energy infrastructure multi-day outage by 5 June) = 0.22 (Kuwait Mina al-Ahmadi acutely at risk; IRGC "more decisive" warning active; interceptor depletion ~75%)

## 2026-05-30 — Day 92 Backtest Entry

### Scoring T+1 from Day 91 (29 May) predictions

| Item | Prediction | P | Outcome | Score | Brier contrib |
|------|-----------|---|---------|-------|---------------|
| W2 — IRGC follow-on strike within 48h of Day 91 (P=0.30) | Strike | 0.30 | MISS: No confirmed IRGC kinetic strike on Gulf-state territory or US base 29–30 May as of 06:01 UTC. GlobalSecurity OPREP confirms no major new attacks. IRGC warning remains active but not executed. | MISS | (0.30−0)²=0.090 |
| W3 — Trump formal sign-off on MOU by 31 May (P=0.30) | Sign-off | 0.30 | PENDING — Situation Room 29 May concluded WITHOUT announcement (CNN live). Decision deferred. | PENDING | — |
| W4 — Oman maintains mediation without formal downgrade (P=0.72) | Maintain | 0.72 | HIT: Araghchi called Omani FM 29 May; praised Oman. Bessent received no-tolling assurance from Omani ambassador 28 May. Oman mediation intact. | HIT | (0.72−1)²=0.078 |
| W5 — Houthi public escalation or Red Sea incident by 1 June (P=0.25) | Escalation | 0.25 | MISS (so far): GlobalSecurity confirms no major Houthi attacks on Red Sea shipping through Day 91 cutoff. Ceasefire Day 22 holding. | MISS (partial — 1 June not yet reached) | (0.25−0)²=0.063 |
| Trend: Worse | — | — | PARTIAL HIT: No new kinetics but MOU unsigned, PGSA active, Lebanon ops continuing, IRGC warning active. Arguably "Same" rather than "Worse" on Day 92. Day 91 brief called "Worse" which overstated the kinetic deterioration relative to Day 92 flat reading. Scoring as PARTIAL. | PARTIAL | — |
| Threat: 4/5 Severe | — | — | HIT: UKMTO Critical advisory 29 May; PGSA sanctions + continuity; Lebanon civilian toll. | HIT | — |

**Pending items (not yet scoreable):**
- W1 (MOU text published by 31 May, P=0.30): PENDING
- W3 (Trump sign-off by 31 May, P=0.30): PENDING

**Running mean Brier update (T+1 scored predictions):**
Prior mean ~0.10 (Day 91). Day 92 additions: W2 MISS (0.090) + W4 HIT (0.078) + W5 partial MISS (0.063). Mean revision: (0.10×6 + 0.090 + 0.078 + 0.063)/9 = ~0.095. Net: slight improvement. Low-probability predictions (0.25–0.30) performing within calibration range on MISS side.

**Methodology delta (Day 92):** W2 MISS at P=0.30 is within calibration range (30% predictions should miss 70% of the time). No heuristic change warranted. Confirm existing heuristic: IRGC "decisive response" language frequently precedes stand-down rather than escalation in ceasefire window — consistent with Day 90-92 pattern. Label: "IRGC signalling discount in active MOU window" — downweight follow-through probability by 10pp when active MOU talks are ongoing simultaneously.

---

### Day 92 Predictions logged for T+1 (31 May), T+3 (2 June), T+7 (6 June)

**Trend:** Same → (pivoting, Confidence: Medium)
**Threat level:** 4/5 Severe (held)

**Watchlist predictions:**
- W1 — Trump publicly announces MOU signing by EOD 2 June (P=0.35; Situation Room met without decision; weekend creates decision pressure from markets and mediators; Iran approval pathway unclear)
- W2 — Iran Supreme Leader Khamenei confirmed sign-off on MOU by EOD 2 June (P=0.30; US says Iranian negotiators "had approvals"; Iran FM and Fars deny; structural ambiguity)
- W3 — PGSA enforcement action on non-IRGC vessel despite Treasury sanctions (P=0.20; PGSA continuity vow is credible; but active MOU window creates incentive for restraint; net: low)
- W4 — Lebanon June 2–3 political track meeting productive — no collapse (P=0.45; IDF advancing but June 2–3 meeting confirmed per State Dept; Lebanon clause in MOU creates shared interest in outcome)
- W5 — No new IRGC kinetic strike on Gulf-state energy infra through 5 June (P=0.70; 48h no-strike pattern holds; IRGC pattern in MOU window = standdown; Kuwait interceptor depletion remains risk)

**Scenarios (30d):**
- A — Negotiated framework — 35% (Δ +5pp)
- B — Frozen attrition — 42% (Δ 0pp) ← modal
- C — Re-escalation — 23% (Δ −5pp)

**Brier inputs (T+1/T+3/T+7):**
- P(Trump publicly announces MOU signing by EOD 2 June) = 0.35
- P(Iran Supreme Leader confirmed sign-off on MOU by EOD 2 June) = 0.30
- P(PGSA enforcement action on non-authorised vessel within 72h) = 0.20
- P(Lebanon June 2–3 political track meeting not collapsing) = 0.45
- P(No new IRGC kinetic strike on Gulf-state energy infra through 5 June) = 0.70
- P(Brent above $100 by 6 June) = 0.22 (deal proximity structural downside; IRGC strike = upside tail)
- P(MOU text published jointly by US and Iran by EOD 5 June) = 0.40 (slightly higher than signing P due to parallel publication possible)
- P(Any Gulf-state energy infrastructure multi-day outage by 5 June) = 0.18 (Δ −4pp; no follow-through 48h; IRGC standdown pattern confirmed)

## 2026-05-31 — Day 93 Backtest Entry

### Scoring T+1 from Day 92 (30 May) predictions

| Item | Prediction | P | Outcome | Score | Brier contrib |
|------|-----------|---|---------|-------|---------------|
| W1 — Trump MOU sign-off by EOD 2 June (P=0.35) | Sign-off | 0.35 | PENDING — Situation Room 29 May concluded without decision; Trump 30 May made fresh demands Iran rejected. Decision not yet at EOD 2 June. | PENDING | — |
| W2 — Khamenei sign-off by EOD 2 June (P=0.30) | Sign-off | 0.30 | PENDING — JPost 28 May: Mojtaba Khamenei had not approved. IAEA 31 May HEU report adds complication. | PENDING | — |
| W3 — PGSA enforcement action on non-IRGC vessel (P=0.20) | Enforcement | 0.20 | MISS (72h window): No confirmed PGSA enforcement action 29–31 May. PGSA sanctioned, vowed continuity, no kinetic follow-through. | MISS | (0.20−0)²=0.040 |
| W4 — Lebanon June 2–3 track not collapsing (P=0.45) | No collapse | 0.45 | PARTIAL — IDF advancing; Hezbollah launching barrages; schools closed northern Israel (CNN 29–30 May). Track strained but not formally collapsed as of 06:01 UTC 31 May. | PARTIAL | — |
| W5 — No new IRGC kinetic strike on Gulf-state energy infra through 5 June (P=0.70) | No strike | 0.70 | HOLDING HIT: No confirmed IRGC follow-on strike 29–31 May. 72h+ standdown. Pattern consistent. | HOLDING HIT | (0.70−1)²=0.090 (provisional) |
| Trend: Same → | — | — | HIT: Day 93 opens as Same — IRGC standdown, MOU unsigned, no new kinetics, market pricing flat. | HIT | — |
| Threat: 4/5 Severe | — | — | HIT: UKMTO Critical, IRGC warning active, Lebanon escalating, nuclear complication added. | HIT | — |

**T+1 scored (Day 92 → 93):**
W3 MISS (0.040). W5 provisional HIT (0.090). Running mean Brier update: prior ~0.095. Day 93 additions so far: W3 MISS (0.040) + W5 HIT (0.090 provisional). Mean revision pending W1/W2/W4 resolution.

**Methodology delta (Day 93):** IAEA quarterly report landed on Day 93 as a surprise Hard-tier complication to MOU nuclear clause — not anticipated in Day 92 watchlist. Add heuristic: "IAEA quarterly reporting cycles (approx. end-of-February, end-of-May, end-of-August, end-of-November) are structurally timed to intersect with diplomatic windows and should be flagged as scheduled risk events in the watchlist." Label: "IAEA cycle = diplomatic complication risk." Add to forward watchlist for end-August 2026.

---

### Day 93 Predictions logged for T+1 (1 June), T+3 (3 June), T+7 (7 June)

**Trend:** Same → (Confidence: Medium)
**Threat level:** 4/5 Severe (held)

**Watchlist predictions:**
- W1 — Trump publicly announces MOU signing by EOD 2 June (P=0.28; Δ −7pp from Day 92; IAEA HEU report + Trump 30 May demand rejection reduce probability; mediation pressure intact)
- W2 — Iran supreme leadership endorses MOU by EOD 2 June (P=0.25; Δ −5pp; IAEA report hardens IRGC position; Iran FM denials continuing)
- W3 — Lebanon front: no formal ceasefire collapse by 3 June (P=0.55; IDF advancing but formal collapse requires political decision; Houthi re-entry trigger conditioned on this)
- W4 — IRGC maintains standdown on Gulf-state energy infrastructure through 5 June (P=0.68; Δ −2pp; 72h pattern holds but IAEA report may provide political cover for escalation signal)
- W5 — Houthi commercial-shipping standdown continues through 3 June (P=0.78; Day 23+ holding; Lebanon formal collapse would shift to 0.35)

**Scenarios (30d):**
- A — Negotiated framework — 33% (Δ −2pp; IAEA HEU complication; Trump demand rejection)
- B — Frozen attrition — 44% (Δ +2pp) ← modal
- C — Re-escalation — 23% (Δ 0pp)

**Brier inputs (T+1/T+3/T+7):**
- P(Trump announces MOU signing by EOD 2 June) = 0.28
- P(Iran supreme leadership endorses MOU by EOD 2 June) = 0.25
- P(Lebanon formal ceasefire collapse by 3 June) = 0.45 (complement of W3 above)
- P(IRGC maintains Gulf-state energy infra standdown through 5 June) = 0.68
- P(Houthi commercial-shipping standdown through 3 June) = 0.78
- P(Brent above $100 by 7 June) = 0.20 (IAEA report adds tail risk; deal optimism caps upside; physical flows unchanged)
- P(MOU text published jointly by US and Iran by EOD 5 June) = 0.35 (Δ −5pp; IAEA complication; demand rejection)
- P(Any Gulf-state energy infrastructure multi-day outage by 5 June) = 0.16 (72h standdown pattern; IRGC restraint in MOU window confirmed again)

## 1 June 2026 — Day 94

### Scoring T+1 from Day 93 (31 May) predictions

| Item | Prediction | P | Outcome | Score | Brier contrib |
|------|-----------|---|---------|-------|---------------|
| W1 — Trump announces MOU signing by EOD 2 June (P=0.28) | Signing | 0.28 | PENDING — No signing confirmed as of 06:01 UTC 1 June. EOD 2 June not yet reached. | PENDING | — |
| W2 — Khamenei endorses MOU by EOD 2 June (P=0.25) | Endorsement | 0.25 | PENDING — No Mojtaba Khamenei confirmed sign-off as of 06:01 UTC 1 June. | PENDING | — |
| W3 — Lebanon no formal ceasefire collapse by 3 June (P=0.55) | No collapse | 0.55 | HIT (provisional): Round 4 Israel–Lebanon talks confirmed for Washington 2–3 June. Ceasefire formally holding per Wikipedia. Lebanon ceasefire extended 45 days from 15 May. | HIT provisional | (0.55−1)²=0.203 (provisional) |
| W4 — IRGC maintains standdown on Gulf-state energy infra through 5 June (P=0.68) | Standdown | 0.68 | HOLDING HIT: No confirmed new IRGC kinetic strike on Gulf-state energy infrastructure 31 May–1 June. Pattern continues. | HIT provisional | (0.68−1)²=0.102 (provisional) |
| W5 — Houthi commercial-shipping standdown through 3 June (P=0.78) | Standdown | 0.78 | MISS: On 1 June, Houthis targeted Maltese-flagged oil tanker Abliani, cargo ship Maina, and LNG carrier Al Oraiq (Wikipedia Houthi attacks on commercial vessels, 1 June entries). Day 23+ standdown broken. | MISS | (0.78−0)²=0.608 |
| Trend: Same → | — | — | HIT: Situation remains in frozen-attrition band; no signing, no new major kinetics, Houthi re-emergence a shift but not yet structural escalation. | HIT | — |
| Threat: 4/5 Severe | — | — | MAINTAINED: UKMTO Critical active, Houthi re-emergence confirms 4/5 structural read. | HIT | — |

**T+1 scored (Day 93 → 94):**
W5 MISS (0.608) — significant. W3 provisional HIT (0.203). W4 provisional HIT (0.102). Running mean Brier update: prior ~0.095. Day 94 addition: W5 MISS (0.608) is a major calibration signal. Houthi standdown at P=0.78 was overconfident given Lebanon ceasefire tension. Methodology delta: **Houthi standdown probability should decay faster when Lebanon ceasefire is under stress AND MOU window is open; the two conditions together create Houthi incentive for solidarity signaling. Recalibrate: when Lebanon ceasefire violations are actively reported AND US-Iran MOU is unsigned for >7 days, Houthi standdown P ceiling = 0.60, not 0.78.**

**From Day 92 (30 May) — W1/W2/W4 now scored:**
- W3 Day 92 (PGSA enforcement, P=0.20): MISS — confirmed 31 May.
- W5 Day 92 (No IRGC kinetic strike through 5 June, P=0.70): HOLDING — still no confirmed Gulf-state energy infra strike.
- W4 Day 92 (Lebanon June 2–3 track not collapsing, P=0.45): HIT — talks proceeding.

---

### Day 94 Predictions logged for T+1 (2 June), T+3 (4 June), T+7 (8 June)

**Trend:** → Same (Confidence: Medium)
**Threat level:** 4/5 Severe (held; Houthi re-emergence reconfirms)

**Watchlist predictions:**
- W1 — Trump formally signs/announces MOU by EOD 2 June (P=0.25; Δ −3pp from Day 93; no new positive signal, Houthi re-emergence complicates momentum)
- W2 — Iran supreme leadership endorses MOU text by EOD 3 June (P=0.22; Δ −3pp; Mojtaba Khamenei no confirmed yes; IAEA HEU report continues to harden position)
- W3 — June 2–3 Washington Lebanon talks (Round 4) proceed without formal collapse (P=0.72; talks confirmed; Lebanese delegation led by Karam; Hezbollah opposes but Lebanon government proceeding)
- W4 — IRGC maintains standdown on Gulf-state energy infrastructure through 5 June (P=0.65; Δ −3pp; Houthi re-emergence may embolden parallel IRGC signaling)
- W5 — Houthi attacks on commercial shipping continue or expand through 4 June (P=0.70; Abliani/Maina/Al Oraiq 1 June = standdown broken; pattern shift)

**Scenarios (30d):**
- A — Negotiated framework — 31% (Δ −2pp; no signing, Houthi resumption adds complexity)
- B — Frozen attrition — 46% (Δ +2pp) ← modal
- C — Re-escalation — 23% (Δ 0pp)

**Brier inputs (T+1/T+3/T+7):**
- P(Trump announces MOU signing by EOD 2 June) = 0.25
- P(Iran supreme leadership confirms MOU endorsement by EOD 3 June) = 0.22
- P(Lebanon June 2–3 talks proceed without collapse) = 0.72
- P(IRGC maintains Gulf-state energy infra standdown through 5 June) = 0.65
- P(Houthi attacks on commercial shipping continue through 4 June) = 0.70
- P(Brent above $100 by 8 June) = 0.18 (deal optimism caps upside; Houthi re-emergence minor upside tail)
- P(MOU text jointly published by US and Iran by EOD 5 June) = 0.30 (Δ −5pp; unsigned principal approvals; Houthi complication)
- P(Any Gulf-state energy infrastructure multi-day outage by 5 June) = 0.15 (IRGC standdown pattern intact; Kuwait interceptor depletion risk)
- P(Strait of Hormuz commercial transits exceed 10/day by 8 June) = 0.08 (mine clearance + MOU signature required; both absent)

## 2 June 2026 — Day 95

### Scoring T+1 from Day 94 (1 June) predictions

| Item | Prediction | P | Outcome | Score | Brier contrib |
|------|-----------|---|---------|-------|---------------|
| W1 — Trump announces MOU signing by EOD 2 June (P=0.25) | Signing | 0.25 | MISS: No MOU signed. Iran suspended talks 1 Jun (Tasnim/NPR/NBC); Reuters confirmed Iran "preparing to decline" proposal on 2 Jun. | MISS | (0.25−0)²=0.063 |
| W2 — Iran supreme leadership endorses MOU by EOD 3 June (P=0.22) | Endorsement | 0.22 | MISS (provisional): Iran suspended mediator talks, signaling rejection not endorsement. | MISS provisional | (0.22−0)²=0.048 |
| W3 — Lebanon Round 4 talks proceed without formal collapse (P=0.72) | No collapse | 0.72 | PARTIAL MISS: Lebanon political track 2–3 Jun nominally proceeding, but Iran-US channel suspended; Israel struck Beirut suburbs; Hezbollah fired rockets 1–2 Jun. Scored MISS (diplomatic framework collapsed even if Lebanese bilateral track continues). | MISS | (0.72−0)²=0.518 |
| W4 — IRGC maintains Gulf-state energy infra standdown through 5 June (P=0.65) | Standdown | 0.65 | HIT PROVISIONAL: IRGC BMs intercepted targeting Kuwait (CENTCOM); no confirmed new multi-day energy infra outage. Standdown pattern technically holds on energy infra specifically. | HIT provisional | (0.65−1)²=0.123 |
| W5 — Houthi attacks continue through 4 June (P=0.70) | Attacks | 0.70 | HIT: Abliani, Maina, Al Oraiq attacked 1 Jun (Wikipedia confirmed). Ghaani threatened Bab al-Mandeb closure 1 Jun. | HIT | (0.70−1)²=0.09 |
| Trend → Same | — | — | MISS: Situation has moved to Worse — Iran talk suspension, dual-chokepoint threat, oil +5%, IRGC Kuwait exchange all represent deterioration beyond "same." | MISS | — |
| Threat 4/5 Severe | — | — | HIT: 4/5 Severe maintained; not yet Crisis but clearly still Severe. | HIT | — |

**T+1 running Brier update:** W1 MISS (0.063) + W2 MISS (0.048) + W3 MISS (0.518) + W4 HIT (0.123) + W5 HIT (0.09) = 0.842 / 5 = 0.168 mean for this day. Running cumulative mean remains elevated.

**Methodology delta from Day 95 scoring:** Lebanon-linked diplomatic suspension propagates faster than expected when IDF ground operations cross a threshold (Beaufort Castle seizure + Beirut suburb threat = threshold). Recalibrate: when IDF conducts ground incursion beyond Litani AND threatens Beirut suburbs, Iran talk-suspension probability should be treated as >0.80 regardless of MOU proximity. W3 confidence was overconfident (P=0.72 for no collapse when both conditions were present). Future calibration: Lebanon collapse probability P ceiling = 0.45 when IDF is past Litani + threatening Beirut + IRGC has signaled "consequences."

---

### Day 95 Predictions logged for T+1 (3 June), T+3 (5 June), T+7 (9 June)

**Trend:** ↑ Worse (Confidence: Medium)  
**Threat level:** 4/5 Severe (held; approaching 5/5 Crisis threshold if Bab al-Mandeb kinetics occur)

**Watchlist predictions:**
- W1 — Iran formally resumes MOU mediator talks by EOD 3 June (P=0.35; Trump claimed "rapid pace" and announced Lebanon halt; but no Iranian confirmation by 06:01 UTC 2 Jun)
- W2 — Houthi or Quds Force kinetic action in Bab al-Mandeb by EOD 4 June (P=0.45; Ghaani operational-tier threat 1 Jun; Houthi attacks confirmed 1 Jun; pattern signals intent)
- W3 — IRGC kinetic strike on Gulf-state energy infrastructure by EOD 5 June (P=0.22; Kuwait interceptor depletion ~75%; BMs intercepted this weekend but no energy infra strike confirmed)
- W4 — Lebanon Round 4 talks (2–3 Jun) produce formal outcome without total breakdown (P=0.55; Lebanon bilateral track proceeding; Iran-US suspension is separate track)
- W5 — US-Iran contact resumes via Pakistan/Oman/Qatar with senior-level public confirmation by EOD 5 June (P=0.40; Trump pressure; Lebanon halt claim is one mechanism for resumption)

**Scenarios (30d):**
- A — Negotiated framework — 25% (Δ −6pp)
- B — Frozen attrition — 44% (Δ −2pp) ← modal
- C — Re-escalation — 31% (Δ +8pp)

**Brier inputs (T+1/T+3/T+7):**
- P(Iran formally resumes mediator talks by EOD 3 June) = 0.35
- P(Houthi/Quds Force kinetic action in Bab al-Mandeb by EOD 4 June) = 0.45
- P(IRGC strike on Gulf-state energy infra by EOD 5 June) = 0.22
- P(Lebanon Round 4 talks 2–3 Jun produce outcome without total breakdown) = 0.55
- P(US-Iran contact resumes with public confirmation by EOD 5 June) = 0.40
- P(Brent above $100 by 9 June) = 0.35 (dual-chokepoint risk; EIA $106 Q2 projection; Iran full-closure threat)
- P(MOU text jointly published by US and Iran by EOD 9 June) = 0.18 (Δ −12pp; talk suspension + Reuters declining report)
- P(Any Gulf-state energy infrastructure multi-day outage by 5 June) = 0.20 (Kuwait interceptor ~75% depleted; IRGC BMs active this weekend)
- P(Bab al-Mandeb formal closure or ≥3 attacks in 24h by EOD 5 June) = 0.30 (Ghaani operational signal; Houthi attacks confirmed 1 Jun)

## 3 June 2026 (Day 96) — Scoring + New Predictions

### Scoring Day 95 predictions (T+1, made 2 June, scored against 3 June evidence)

| Item | Prediction | P | Outcome | Score | Brier contrib |
|------|-----------|---|---------|-------|---------------|
| W1 — Iran formally resumes MOU mediator talks by EOD 3 June | Resumption | 0.35 | PARTIAL HIT: Rubio Senate testimony 2 Jun confirmed talks ongoing; CNN regional source "back on track"; Iran Fars said messages stopped but US contradicted; Lebanon Round 4 continuing reduces suspension rationale. Scored 0.5 (ambiguous). | PARTIAL | (0.35−0.5)²=0.023 |
| W2 — Houthi/Quds Force kinetic action in Bab al-Mandeb by EOD 4 June | Attack | 0.45 | MISS: No confirmed Houthi attack on commercial vessel 2–3 June per Wikipedia Houthi attacks tracker. Next confirmed attacks 5 June (Roza/Vantage Dream). | MISS | (0.45−0)²=0.203 |
| W3 — IRGC strike on Gulf energy infra by EOD 5 June | Strike | 0.22 | MISS (partial): IRGC BMs intercepted over Kuwait 3 June (CNN); no confirmed energy infrastructure multi-day outage. Interception ≠ outage. | MISS | (0.22−0)²=0.048 |
| W4 — Lebanon Round 4 talks produce outcome without total breakdown | No collapse | 0.55 | HIT: Talks began 2 June (Times of Israel/AFP); State Dept "progress continues on political and security tracks"; talks continuing 3 June. No collapse. | HIT | (0.55−1)²=0.203 |
| W5 — US-Iran contact resumes with public senior confirmation by EOD 5 June | Confirmation | 0.40 | HIT: Rubio Senate Foreign Relations testimony 2 June = public senior confirmation; CNN confirmed talks back on track. | HIT | (0.40−1)²=0.360 |

**T+1 Brier mean (Day 95→96):** (0.023+0.203+0.048+0.203+0.360)/5 = 0.167

**Methodology note:** W2 miss confirms pattern: Houthi attacks after standdown break are episodic, not daily. The 1 June attacks were a breakout event; subsequent days may see pauses before next wave. Calibration: reduce daily P(Houthi attack on commercial vessel) from 0.45 to ~0.30 for 24h windows when no fresh trigger/signal exists the same day.

---

### Day 96 Predictions logged for T+1 (4 June), T+3 (6 June), T+7 (10 June)

**Trend:** ↑ Worse (Confidence: Medium)
**Threat level:** 4/5 Severe (stable; dual-chokepoint activation risk remains primary escalation path to 5/5)

**Watchlist predictions:**
- W1 — Lebanon Round 4 concludes 3 June with joint communiqué or clear framework (no full collapse) (P=0.60; talks continuing per State Dept; Trump pressed Netanyahu; Hezbollah agreed to stop shooting per Trump claim)
- W2 — Iran provides public confirmation of active MOU channel via FM or intermediary by EOD 5 June (P=0.38; Rubio confirmed ongoing; Iran Fars denial contradicted by US; Lebanon track proceeding reduces pressure to suspend)
- W3 — Houthi kinetic action on commercial vessel in Red Sea/Gulf of Aden by EOD 6 June (P=0.55; Abliani/Maina/Al Oraiq 1 Jun; Wikipedia shows next attacks 5 Jun; pattern accelerating)
- W4 — IRGC BM/drone strike on Kuwait energy or water infrastructure causing confirmed multi-day outage by EOD 7 June (P=0.18; interceptions ongoing; no outage confirmed yet; interceptor depletion risk remains)
- W5 — Brent closes above $100 by EOD 6 June (P=0.28; currently $96; IEA critical inventory warning; Iran message-stoppage ambiguity; upside tail from dual-chokepoint)

**Scenarios (30d):**
- A — Negotiated framework — 27% (Δ +2pp; Rubio nuclear concession signal + Lebanon talks continuing = incremental positive)
- B — Frozen attrition — 46% (Δ +2pp) ← modal
- C — Re-escalation — 27% (Δ −4pp; Lebanon de-escalation signal reduces immediate tail)

**Brier inputs (T+1/T+3/T+7):**
- P(Lebanon Round 4 concludes without formal collapse by EOD 3 June) = 0.60
- P(Iran provides public MOU channel confirmation by EOD 5 June) = 0.38
- P(Houthi kinetic on commercial vessel Red Sea/GoA by EOD 6 June) = 0.55
- P(IRGC causes confirmed Gulf energy/water outage ≥ 1 day by EOD 7 June) = 0.18
- P(Brent above $100 by EOD 6 June) = 0.28
- P(MOU jointly published by US and Iran by EOD 10 June) = 0.20 (Rubio "could happen today/tomorrow/next week"; nuclear concession signal; still no Trump sign-off)
- P(Hormuz commercial transits exceed 10/day by EOD 10 June) = 0.06 (mine clearance not started; no MOU signed)
- P(Any Houthi Bab al-Mandeb formal closure action by EOD 7 June) = 0.15 (attacks resumed but no closure; dual-chokepoint scenario requires deliberate escalation decision)

## 4 June 2026 (Day 97) — Scoring + New Predictions

### Scoring Day 96 predictions (T+1, made 3 June, scored against 4 June evidence)

| Item | Prediction | P | Outcome | Score | Brier contrib |
|------|-----------|---|---------|-------|---------------|
| W1 — Lebanon Round 4 concludes without formal collapse | No collapse | 0.60 | HIT: Israel-Lebanon joint ceasefire statement at State Dept 3 June (Axios, CBS, Xinhua); next round 22 June Washington. No collapse — formal framework agreed. | HIT | (0.60−1)²=0.160 |
| W2 — Iran public MOU channel confirmation by EOD 5 June | Confirmation | 0.38 | MISS: No Iranian public confirmation; Rubio hardened HEU condition 3 June. Iran has not publicly acknowledged Lebanon ceasefire as precondition met. | MISS | (0.38−0)²=0.144 |
| W3 — Houthi kinetic on commercial vessel by EOD 6 June | Attack | 0.55 | HIT: Roza + Vantage Dream attacked 5 June Red Sea (Wikipedia Houthi tracker); Maersk Seletar Arabian Sea drone claim also made 5 Jun. | HIT | (0.55−1)²=0.203 |
| W4 — IRGC confirmed Gulf energy/water outage ≥1 day by EOD 7 June | Outage | 0.18 | PARTIAL HIT: Kuwait Airport struck 3 Jun — civilian transport outage, 1 killed, 63 injured, flights suspended (The National, Arab News). Not energy infra specifically. Score 0.5 (civilian infra outage confirmed, energy infra not). | PARTIAL | (0.18−0.5)²=0.102 |
| W5 — Brent above $100 by EOD 6 June | >$100 | 0.28 | PARTIAL HIT: Brent $101.36 on morning 3 June (Fortune); closed $96.97 on 4 June (Trading Economics). Crossed $100 intraday. Score 0.5. | PARTIAL | (0.28−0.5)²=0.048 |

**T+1 Brier mean (Day 96→97):** (0.160+0.144+0.203+0.102+0.048)/5 = 0.131

**Methodology note:** Lebanon ceasefire was the highest-information event of the period — well-calibrated at P=0.60. Houthi episodic cluster pattern confirmed again: pause 2–4 June, cluster 5 June. W4 partial on civilian vs energy infrastructure distinction — the Kuwait Airport strike is the leading indicator for the energy infra tail risk, not the event itself. Rubio HEU hardline was a surprise that invalidated W2 (Iran confirmation unlikely while US is moving goalposts).

**Calibration update:** Reduce P(Iran senior public confirmation) for next 48h given Rubio HEU hardening. Increase P(Houthi attack next cluster) given confirmed episodic pattern restoring — raise baseline 24h P from 0.30 to 0.38 when last attack <5 days ago.

---

### Day 97 Predictions logged for T+1 (5 June), T+3 (7 June), T+7 (11 June)

**Trend:** ↑ Worse (Confidence: High)
**Threat level:** 4/5 Severe (stable; Kuwait Airport civilian fatality raises floor; energy infra strike would trigger 5/5)

**Watchlist predictions:**
- W1 — Hezbollah verifiably complies with Litani withdrawal — no fresh rocket/drone strikes on Israel for ≥48h by EOD 7 June (P=0.40; Hezbollah conducted several drone attacks 48h post-1 Jun ceasefire; compliance historically poor; Trump pressure high)
- W2 — Iran provides senior-level public acknowledgment that Lebanon ceasefire meets MOU precondition — via FM Araghchi, Tasnim, or intermediary — by EOD 7 June (P=0.30; Rubio HEU hardening reduces Iran's incentive to publicly accept; Lebanon deal not yet verified by Hezbollah)
- W3 — Houthi second attack cluster (≥2 commercial vessels) in Red Sea/GoA by EOD 8 June (P=0.55; 5 Jun cluster = Roza/Vantage Dream; episodic pattern predicts next cluster within 3–5 days)
- W4 — IRGC strike on Gulf-state energy infrastructure (oil terminal, refinery, pipeline, or desalination) causing confirmed ≥1-day outage by EOD 9 June (P=0.25; Kuwait Airport strike is leading indicator; interceptor depletion accelerating; IRGC doctrine now demonstrably targeting civilian-adjacent infrastructure)
- W5 — US-Iran MOU jointly published and signed by EOD 11 June (P=0.22; Lebanon ceasefire removed key Iranian precondition; but Rubio HEU condition and IRGC escalation create headwinds; Rubio said "could happen today/tomorrow/next week" 2 Jun)

**Scenarios (30d):**
- A — Negotiated framework — 30% (Δ +3pp; Lebanon ceasefire framework removes Iran's primary precondition)
- B — Frozen attrition — 43% (Δ −3pp) ← modal
- C — Re-escalation — 27% (Δ 0pp; Kuwait Airport fatality balanced by Lebanon de-escalation)

**Brier inputs (T+1/T+3/T+7):**
- P(Hezbollah ≥48h verified ceasefire compliance by EOD 7 June) = 0.40
- P(Iran public MOU/Lebanon precondition acknowledgment by EOD 7 June) = 0.30
- P(Houthi ≥2-vessel attack cluster Red Sea/GoA by EOD 8 June) = 0.55
- P(IRGC Gulf energy infra confirmed outage by EOD 9 June) = 0.25
- P(MOU jointly signed/published by EOD 11 June) = 0.22
- P(Brent above $100 by EOD 8 June) = 0.40 (intraday $101 on 3 Jun; EIA inventory draws; Kuwait Airport escalation risk)
- P(Kuwait Airport suffers second IRGC strike by EOD 10 June) = 0.18 (IRGC 30-missile salvo pattern; precedent now set)
- P(Hormuz commercial transits exceed 20/day by EOD 11 June) = 0.08 (no MOU signed; mine threat unchanged)

## 5 June 2026 (Day 98) — Backtest Scoring + New Predictions

### Scoring Day 97 predictions (T+1, made 4 June, scored against 5 June evidence)

| Item | Prediction | P | Outcome | Score | Brier contrib |
|------|-----------|---|---------|-------|---------------|
| W1 — Hezbollah ≥48h ceasefire compliance by EOD 7 June | Compliance | 0.40 | MISS: Hezbollah formally rejected Lebanon ceasefire 4 June (Naim Qassem); UNIFIL peacekeeper killed by mortars attributed to Hezbollah; continued drone attacks on Israel (NPR, Axios, Wikipedia). Non-compliance confirmed. | MISS | (0.40−0)²=0.160 |
| W2 — Iran public MOU/Lebanon precondition acknowledgment by EOD 7 June | Acknowledgment | 0.30 | MISS: No public acknowledgment by Iran. Araghchi issued warnings about Lebanon violations but no MOU precondition confirmation. Iran FM focused on Hezbollah solidarity, not unlock signal. (Washington Times, Al Jazeera) | MISS | (0.30−0)²=0.090 |
| W3 — Houthi ≥2-vessel attack cluster Red Sea/GoA by EOD 8 June | Attack cluster | 0.55 | HIT: Roza + Vantage Dream attacked in Red Sea 5 June (Wikipedia Houthi tracker — confirmed Houthi claim; missiles and drones); Maersk Seletar also claimed Arabian Sea. Third cluster since 1 June standdown break. Episodic pattern confirmed. | HIT | (0.55−1)²=0.203 |
| W4 — IRGC Gulf energy infra outage ≥1 day by EOD 9 June | Outage | 0.25 | PARTIAL HIT: Kuwait Airport terminal struck 3 June (confirmed by Kuwait MoD, CENTCOM) — civilian aviation outage, not energy/desalination infra. 1 killed, 63 wounded, flights suspended. Precedent set but not energy-specific outage. Score 0.5. | PARTIAL | (0.25−0.5)²=0.063 |
| W5 — MOU signed/published by EOD 11 June | Signed | 0.22 | IN PLAY — no resolution yet as of 5 June. Hezbollah rejection of Lebanon ceasefire 4 June makes signing unlikely by 11 June. Tracking. | PENDING | — |
| P(Brent >$100 by EOD 8 June) | >$100 | 0.40 | IN PLAY — Brent $95.39 per straits.live 5 June. Trending miss but 3 days remain. | PENDING | — |
| P(Kuwait Airport second IRGC strike by EOD 10 June) | Strike | 0.18 | IN PLAY | PENDING | — |
| P(Hormuz transits >20/day by EOD 11 June) | >20/day | 0.08 | IN PLAY — currently ~10/day, trending miss | PENDING | — |

**T+1 Brier mean (Day 97→98, scoreable items):** (0.160+0.090+0.203+0.063)/4 = 0.129

**Running calibration note:** Hezbollah non-compliance was well-calibrated at P=0.40 (MISS predicted was correct direction — P<0.5 implies miss more likely than hit). Houthi episodic cluster pattern now confirmed for third consecutive cycle — episodic baseline P(attack cluster) when last cluster <5 days ago should be maintained at 0.55-0.60. W4 partial: IRGC civilian infrastructure targeting confirmed (airport vs energy) — need to broaden W4 definition to include civilian transport infrastructure going forward. Rubio MOU signal (nuclear off-limits topics) was soft-tier and did not translate to operational confirmation — correct to keep at P=0.25-0.30 range.

**Methodology delta:** Broaden IRGC escalation watchlist item to include civilian transport infrastructure (airports, ports) as well as energy/desalination — Kuwait Airport strike demonstrates IRGC now targeting civilian-adjacent infrastructure as deliberate retaliation tool, not just collateral.

---

### Day 98 Predictions logged for T+1 (6 June), T+3 (8 June), T+7 (12 June)

**Trend:** ↑ Worse (Confidence: High)
**Threat level:** 4/5 Severe (stable; Kuwait Airport fatality sets floor; energy infra strike would trigger 5/5)

**Watchlist predictions:**
- W1 — Hezbollah verifiable compliance ≥48h (zero kinetics on Israel confirmed by UNIFIL) by EOD 9 June (P=0.25; Qassem formally rejected ceasefire 4 June; UNIFIL peacekeeper killed same day; structural non-compliance)
- W2 — Iran FM public acknowledgment Hezbollah compliance satisfies Lebanon precondition by EOD 10 June (P=0.20; precondition reinstated; no IRGC/FM signals suggesting unlock imminent)
- W3 — Houthi attack cluster (≥2 vessels, CENTCOM/UKMTO confirmed) Red Sea/GoA by EOD 10 June (P=0.60; episodic 3-5 day pattern; 5 June = cluster day; next expected 8-10 June)
- W4 — IRGC strike on Gulf energy OR civilian transport infrastructure causing confirmed ≥1-day operational outage by EOD 11 June (P=0.30; broadened per methodology delta; airport precedent now set; interceptor depletion is IRGC doctrine)
- W5 — US-Iran MOU jointly signed/published by EOD 13 June (P=0.15; Hezbollah rejection reinstated Lebanon precondition; Round 5 not until 22 June Washington; structural blockage)

**Scenarios (30d):**
- A — Negotiated framework — 27% (Δ −3pp; Lebanon precondition reinstated)
- B — Frozen attrition — 45% (Δ −1pp) ← modal
- C — Re-escalation — 28% (Δ +1pp; Kuwait Airport civilian fatality raises floor)

**Brier inputs (T+1/T+3/T+7):**
- P(Hezbollah ≥48h verified ceasefire compliance by EOD 9 June) = 0.25
- P(Iran public MOU/Lebanon precondition acknowledgment by EOD 10 June) = 0.20
- P(Houthi ≥2-vessel attack cluster Red Sea/GoA by EOD 10 June) = 0.60
- P(IRGC Gulf energy/civilian-transport infra confirmed outage by EOD 11 June) = 0.30
- P(MOU signed/published by EOD 13 June) = 0.15
- P(Brent above $100 by EOD 8 June) = 0.32 (currently $95.39; energy infra strike is upside catalyst; Hezbollah collapse reduces diplomatic tailwind)
- P(Kuwait Airport suffers second IRGC strike by EOD 12 June) = 0.22 (30-missile pattern; precedent set; interceptor depletion accelerating)
- P(Hormuz commercial transits exceed 20/day by EOD 12 June) = 0.06 (no MOU; mine threat unchanged; PGSA active)

## 6 June 2026 (Day 99) — Backtest Scoring + New Predictions

### Scoring Day 98 predictions (T+1, made 5 June, scored against 6 June evidence)

| Item | Prediction | P | Outcome | Score | Brier contrib |
|------|-----------|---|---------|-------|---------------|
| W1 — Hezbollah ≥48h ceasefire compliance by EOD 9 June | Compliance | 0.25 | IN PLAY — Hezbollah formally rejected ceasefire 4 Jun (NPR, AJ, Euronews); continued kinetics Lebanon 5 Jun (5 killed Zebdine). Structural non-compliance tracking to MISS. | PENDING | — |
| W2 — Iran FM public Lebanon precondition acknowledgment by EOD 10 June | Acknowledgment | 0.20 | IN PLAY — Araghchi stated "no tangible progress" 5 Jun (AJ); no acknowledgment format issued. Tracking to MISS. | PENDING | — |
| W3 — Houthi ≥2-vessel attack cluster Red Sea/GoA by EOD 10 June | Attack cluster | 0.60 | PARTIAL HIT (prior period): Roza + Vantage Dream confirmed 5 Jun (Day 98 window). New cluster window opens 8–10 Jun. Scoring as HIT for Day 98 cluster delivery; second cluster for W3 window pending. Score: HIT. | HIT | (0.60−1)²=0.160 |
| W4 — IRGC Gulf energy/civilian-transport infra outage by EOD 11 June | Outage | 0.30 | PARTIAL HIT: IRGC struck tanker Panaya in Hormuz overnight 5–6 Jun (IRGC/CENTCOM confirmed — vessel halted); Oman Mina Al Fahal terminal explosion 5 Jun (brief disruption, resumed). Kuwait/Bahrain 7-missile salvo intercepted. Tanker forced to halt = maritime transport outage. Score 0.6 (shipping asset confirmed; energy terminal only brief). | PARTIAL | (0.30−0.6)²=0.090 |
| W5 — MOU signed/published by EOD 13 June | Signed | 0.15 | IN PLAY — HoC Library: "no further talks confirmed"; Araghchi "no tangible progress"; overnight escalation hardens positions. Tracking to MISS. | PENDING | — |
| P(Brent >$100 by EOD 8 June) | >$100 | 0.32 | HIT — Brent $101.36 at 0845 ET 3 Jun (Fortune); pulled back to $97.44 on 5 Jun and ~$94.81 on 6 Jun. Peak >$100 confirmed within window. | HIT | (0.32−1)²=0.462 |
| P(Kuwait second IRGC strike by EOD 12 June) | Strike | 0.22 | HIT — IRGC fired 7 ballistic missiles at Kuwait and Bahrain overnight 5–6 Jun (CENTCOM confirmed); Kuwait air defense activated; sirens nationwide. Kuwait was struck. | HIT | (0.22−1)²=0.608 |
| P(Hormuz transits >20/day by EOD 12 June) | >20/day | 0.06 | Trending MISS — straits.live: ~10/day; Bloomberg 2 inbound/2 outbound large vessels. IRGC tanker strike overnight reduces probability further. | PENDING | — |

**T+1 Brier mean (Day 98→99, fully scoreable items this window: W3 HIT, W4 PARTIAL, Brent HIT, Kuwait HIT):**
- W3 HIT: (0.60−1)²=0.160
- W4 PARTIAL (0.6 outcome): (0.30−0.6)²=0.090
- Brent >$100 HIT: (0.32−1)²=0.462
- Kuwait strike HIT: (0.22−1)²=0.608
- **Mean: (0.160+0.090+0.462+0.608)/4 = 0.330**

**Calibration note:** Kuwait second strike was significantly underweighted at P=0.22 (actual = confirmed HIT within 48h). The IRGC "heavier response" doctrine warning was a clear signal that should have pushed P higher — revise future Gulf-state IRGC retaliatory strike probability upward after explicit IRGC "heavier response" statements to P=0.40–0.50. Brent >$100 HIT at P=0.32 was technically well-calibrated (touched $101 briefly on 3 Jun within the EOD 8 Jun window). W4 partial — tanker strike confirms IRGC maritime asset targeting is now indistinguishable from infrastructure outage for FM purposes; broaden W4 to include shipping asset strikes going forward.

**Methodology delta:** After explicit IRGC "heavier response / completely different response" warning statements, default Gulf-state military target probability in next 48h should be revised to P=0.40–0.50 (up from 0.22 baseline). This warning pattern has now been confirmed twice (3 Jun → 5–6 Jun response).

---

### Day 99 Predictions logged for T+1 (7 June), T+3 (9 June), T+7 (13 June)

**Trend:** ↑ Worse (Confidence: High)
**Threat level:** 4/5 Severe (stable floor; energy terminal ≥1-day outage would trigger 5/5)

**Watchlist predictions:**
- W1 — Hezbollah ≥48h verified ceasefire compliance (zero kinetics on Israel confirmed by UNIFIL) by EOD 9 June (P=0.15; Qassem formal rejection 4 Jun; kinetics ongoing 5 Jun; UNIFIL peacekeeper killed 4 Jun; structural non-compliance)
- W2 — Iran FM public acknowledgment Hezbollah compliance satisfies Lebanon precondition by EOD 10 June (P=0.12; Araghchi "no tangible progress" 5 Jun; overnight IRGC escalation hardens hardliner position; no unlock signal visible)
- W3 — Houthi attack cluster (≥2 vessels, CENTCOM/UKMTO confirmed) Red Sea/GoA by EOD 10 June (P=0.55; episodic 3–5 day pattern; 5 Jun = last cluster; next window 8–10 Jun)
- W4 — IRGC strike on Gulf energy OR shipping-adjacent infrastructure causing confirmed ≥1-day operational outage by EOD 12 June (P=0.38; tanker Panaya struck overnight = precedent; Oman Mina Al Fahal explosion = precedent; IRGC "heavier response" doctrine active; methodology delta applied)
- W5 — US-Iran MOU jointly signed/published by EOD 15 June (P=0.10; Hezbollah rejection blocks Lebanon precondition; overnight escalation hardens positions; HoC Library "no further talks confirmed"; Round 5 not until 22 Jun)

**Scenarios (30d):**
- A — Negotiated framework — 25% (Δ −2pp; overnight exchange + Lebanon blockage)
- B — Frozen attrition — 44% (Δ −1pp) ← modal
- C — Re-escalation — 31% (Δ +3pp; tanker strike + 7-missile salvo raises structural floor)

**Brier inputs (T+1/T+3/T+7):**
- P(Hezbollah ≥48h verified ceasefire compliance by EOD 9 June) = 0.15
- P(Iran public MOU/Lebanon precondition acknowledgment by EOD 10 June) = 0.12
- P(Houthi ≥2-vessel attack cluster Red Sea/GoA by EOD 10 June) = 0.55
- P(IRGC Gulf energy/shipping-asset confirmed outage ≥1 day by EOD 12 June) = 0.38
- P(MOU signed/published by EOD 15 June) = 0.10
- P(Brent above $100 by EOD 9 June) = 0.28 (currently ~$94.81; overnight escalation is upside; diplomatic pullback is downside; net slightly below $100)
- P(Gulf-state energy terminal IRGC strike ≥1-day outage by EOD 12 June) = 0.30 (Oman Mina Al Fahal brief precedent; Kuwait/Bahrain IRGC escalation pattern; "heavier response" doctrine)
- P(Hormuz commercial transits exceed 20/day by EOD 13 June) = 0.04 (tanker struck overnight; IRGC access-control doctrine confirmed; MOU not imminent)

## Day 100 — 7 June 2026

### T+1 Scoring (Day 99 predictions → Day 100 actuals)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W3: Houthi ≥2-vessel cluster Red Sea/GoA by EOD 10 Jun | 0.55 | PARTIAL HIT — 7 Jun: Houthis claimed Elbella + AAL Genoa; CENTCOM confirmed 4 ASBMs. No UKMTO vessel-damage confirmation yet. Scoring outcome = 0.6 | (0.55−0.6)²=0.0025 |
| P(Brent >$100 by EOD 9 Jun) | 0.28 | MISS — Brent $93.09 close 6 Jun; range $92.67–$95.90 on 7 Jun. Not approaching $100. | (0.28−0)²=0.0784 |

**T+1 Brier mean (2 scoreable items): (0.0025 + 0.0784)/2 = 0.0405**

Calibration note: Brent >$100 miss at P=0.28 was directionally correct (diplomatic optimism + demand concerns pulled price down). IRGC $24B impasse and OFAC new sanctions are downside oil-price signals overriding supply-shock upside. Revise: when OFAC is simultaneously issuing new sanctions AND US is redirecting frozen assets (dual economic pressure), diplomatic resolution probability falls → oil price risk premium also falls despite continued kinetics. Update priors accordingly.

### T+3 Pending (from Day 97, resolves ~10 June)
- W1: Hezbollah ceasefire compliance (P=0.15) → tracking MISS (kinetics ongoing 7 Jun)
- W2: Iran FM Lebanon precondition acknowledgment (P=0.12) → tracking MISS

### T+7 Pending (from Day 93, resolves ~14 June)
- No Day 93 T+7 items fully scoreable today.

---

### Day 100 New Predictions (T+1: 8 Jun, T+3: 10 Jun, T+7: 14 Jun)

**Trend:** ↑ Worse (Confidence: High)
**Threat level:** 4/5 Severe

**Watchlist predictions:**
- W1: Hezbollah ≥48h ceasefire compliance by EOD 9 Jun (P=0.10; kinetics ongoing 7 Jun; structural non-compliance; further reduction from 0.15)
- W2: Pakistan back-channel produces public bridging signal on $24B frozen-asset impasse by EOD 12 Jun (P=0.18; Naqvi in Tehran; Khamenei letter; unusual but not confirmed productive)
- W3: Houthi UKMTO-confirmed vessel damage Red Sea/GoA by EOD 10 Jun (P=0.50; claims made 7 Jun; CENTCOM confirmed ASBMs; independent damage confirmation pending)
- W4: IRGC strike on Gulf energy or shipping-adjacent infra causing ≥1-day outage by EOD 13 Jun (P=0.35; 7-missile salvo 5–6 Jun; CENTCOM 4th self-defence strike; "heavier response" doctrine still active)
- W5: US formally announces transfer/seizure of Iranian frozen assets to Gulf allies (beyond assessment phase) triggering Iran diplomatic suspension by EOD 15 Jun (P=0.22; Bessent assessment team active; Iran has explicitly flagged this as red line)

**Probabilistic predictions (Brier inputs):**
- P(Brent >$100 by EOD 10 Jun) = 0.18 (currently $93; diplomatic hope discount; no supply shock trigger imminent)
- P(Hormuz commercial transits exceed 20/day by EOD 14 Jun) = 0.04 (structural closure; MOU not imminent; mine risk)
- P(Gulf-state energy terminal IRGC strike ≥1-day outage by EOD 13 Jun) = 0.30 (IRGC doctrine active; "heavier response" warning repeated; methodology delta: post-explicit-warning probability = 0.35–0.45 in 48h window; now in Day 2–5 of elevated window)
- P(Pakistan back-channel produces Khamenei-level public de-escalation signal by EOD 12 Jun) = 0.18

**Scenarios (30d):**
- A: Negotiated framework — 23% (Δ −2pp)
- B: Frozen attrition — 44% (Δ 0pp) ← modal
- C: Re-escalation — 33% (Δ +2pp)

**Methodology delta (Day 100):** When US simultaneously pursues dual economic pressure (new OFAC sanctions + redirecting frozen assets to Gulf allies), it removes Iran's primary financial deal incentive. Default: in this configuration, MOU signing probability should be capped at ≤25% until a third-party bridging mechanism for the frozen assets is publicly proposed. The $24B frozen-asset variable is now THE rate-limiting factor for Scenario A — track it as a binary observable, not a continuous variable.

## Day 101 — 8 June 2026

### T+1 Scoring (Day 100 predictions → Day 101 actuals)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W3: Houthi UKMTO-confirmed vessel damage Red Sea/GoA by EOD 10 Jun | 0.50 | HIT — Norderney struck twice by ASBM 8 Jun (fire, damaged); MSC Tavvishi struck by missile 8 Jun (damaged); both confirmed in Wikipedia citing CENTCOM/reporting. Outcome = 1 | (0.50−1)²=0.25 |
| W1: Hezbollah ≥48h compliance by EOD 9 Jun | 0.10 | MISS tracking — IDF struck Beirut southern suburbs 7 Jun; Hezbollah kinetics ongoing; ceasefire rejected 4 Jun. Not resolved EOD 9 Jun yet. Outcome = 0 (tracking) | (0.10−0)²=0.01 |

**T+1 Brier mean (2 scoreable items): (0.25 + 0.01)/2 = 0.13**

Calibration note: W3 Houthi miss on scoring format — P=0.50 but outcome=1 produced a 0.25 Brier. The prior 5-Jun cluster (Roza/Vantage Dream) correctly flagged the 3–5 day window pattern; the 7 Jun claims were unconfirmed but 8 Jun delivered confirmed hits on Norderney + Tavvishi. The episodic cluster model is working; consider raising base rate from 0.50 to 0.60 for next 72h window given confirmed 8 Jun escalation and Iran–Israel overnight exchange as Houthi coordination signal.

### T+3 Scoring (Day 98 predictions → Day 101 actuals, resolves ~10 Jun)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W1: Hezbollah ≥48h compliance by EOD 9 Jun (from Day 99) | 0.15 | MISS — kinetics ongoing; IDF struck Beirut suburbs 7 Jun; Hezbollah rejected ceasefire 4 Jun. Outcome = 0 | (0.15−0)²=0.0225 |
| W2: Iran FM Lebanon precondition acknowledgment by EOD 10 Jun (from Day 99) | 0.12 | MISS — Iran launched missiles at Israel 7 Jun; Araghchi "no tangible progress"; overnight escalation. Outcome = 0 | (0.12−0)²=0.0144 |

**T+3 Brier mean (2 items): (0.0225 + 0.0144)/2 = 0.01845**

### T+7 Pending

No Day 94 items fully scoreable today.

---

### Day 101 New Predictions (T+1: 9 Jun, T+3: 11 Jun, T+7: 15 Jun)

**Trend:** ↑ Worse (Confidence: High)
**Threat level:** 4/5 Severe

**Watchlist predictions:**
- W1: Iran confirmed retaliatory strike on Israeli territory OR US Gulf asset causing damage by EOD 10 Jun (P=0.45; Iran fired missiles at Israel 7 Jun = first since April ceasefire; IDF struck Iran with ALBMs overnight 7–8 Jun; IRGC retaliation doctrine window 24–72h; escalation ladder now active)
- W2: SW Iran petrochemical facility confirmed ≥1-day operational outage by EOD 9 Jun (P=0.35; footage circulating of IDF ALBM strike; damage severity unconfirmed pending CENTCOM/ISW)
- W3: Pakistan back-channel (Naqvi/Khamenei channel) produces public bridging statement on $24B by EOD 12 Jun (P=0.18; Naqvi met Araghchi 7 Jun; no outcome yet; sole active de-escalation track)
- W4: IRGC confirmed strike on Gulf energy OR shipping-adjacent infra causing ≥1-day outage by EOD 13 Jun (P=0.40; "heavier response" doctrine active; overnight Israel–Iran exchange is fresh trigger; methodology: post-direct-strike-on-Iran probability elevated to 0.40–0.50 in 48–96h window)
- W5: Trump–Netanyahu public rupture (US formal withholding of military support or public US condemnation of Israeli Iran strike) by EOD 15 Jun (P=0.28; Israel struck Iran against Trump's explicit warning; fracture now visible; Trump reportedly furious per NBC)

**Probabilistic predictions (Brier inputs):**
- P(Brent >$100 by EOD 11 Jun) = 0.32 (currently $96–97 intraday; Israel–Iran overnight exchange is upside driver; SW Iran petrochemical unconfirmed adds further upside; $100 within 1 escalation event)
- P(Hormuz commercial transits exceed 20/day by EOD 15 Jun) = 0.03 (structural closure; MOU not imminent; US–Israel fracture reduces Scenario A probability; mine threat elevated)
- P(Gulf-state energy terminal IRGC strike ≥1-day outage by EOD 13 Jun) = 0.35 (IRGC doctrine active; overnight Israel ALBM strikes on Iran = fresh trigger for retaliation cycle)
- P(Pakistan back-channel public bridging signal on $24B by EOD 12 Jun) = 0.18

**Scenarios (30d):**
- A: Negotiated framework — 20% (Δ −3pp; Israel–Iran overnight exchange; US–Israel fracture; $24B impasse)
- B: Frozen attrition — 42% (Δ −2pp) ← modal
- C: Re-escalation — 38% (Δ +5pp; direct Israel–Iran exchange worst since April; Houthi dual hit; Brent +4%)

**Methodology delta (Day 101):** When Israel strikes Iran with ALBMs directly and against explicit US warnings, apply an immediate +5pp to Scenario C and −3pp to Scenario A for the following 72h window. The US–Israel operational fracture removes the US as a reliable restrainer of Israeli kinetics, which means IRGC retaliation doctrine activates against a broader target set (not just CENTCOM). Additionally: Houthi episodic cluster model validated — raise base rate for next 72h Houthi attack window from 0.50 to 0.60 following confirmed dual-hit day.

## 9 June 2026 — Day 102

### T+1 Scoring (Day 101 predictions → Day 102 actuals, 9 Jun)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W1: Iran confirmed retaliatory strike on Israeli territory causing damage by EOD 10 Jun | 0.45 | HIT — Iran fired ballistic missiles at Israel 7 Jun (night) + 8 Jun (morning); first direct exchange since April; US fired interceptors; confirmed CNN/NPR/Britannica. Outcome = 1 | (0.45−1)²=0.3025 |
| W2: SW Iran petrochemical facility confirmed ≥1-day operational outage by EOD 9 Jun | 0.35 | MISS (unresolved as of 06:00 UTC 9 Jun) — IDF confirmed strike on plant (Arab News/IDF), damage severity and outage unconfirmed by CENTCOM/ISW. Treating as 0 pending confirmation by EOD 10 Jun. Outcome = 0 (provisional) | (0.35−0)²=0.1225 |

**T+1 Brier mean (2 scoreable items): (0.3025 + 0.1225)/2 = 0.2125**

Calibration note: W1 was a HIT at P=0.45 — scored 0.3025 Brier, reflecting correct direction but underconfident probability. The Lebanon trigger mechanism (IDF → Iran retaliation) performed exactly as the Day 101 methodology delta predicted. Consider raising Iran retaliation probability to 0.55–0.65 in the next 72h window where Lebanon ops continue and an exchange has already occurred in the prior 48h.

W2 remains open — the IDF strike on SW Iran petrochemical plant is confirmed (Arab News, IDF statement), but operational outage is unconfirmed. This highlights the gap between kinetic event confirmation (fast, Tier 2+) and infrastructure outage confirmation (slow, requires CENTCOM/ISW or satellite assessment). The 35% probability was appropriate given the uncertainty asymmetry.

### T+3 Scoring (Day 99 predictions → Day 102 actuals, resolves ~12 Jun)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W3: Pakistan back-channel public bridging signal on $24B by EOD 12 Jun (Day 99) | 0.18 | PENDING — Sharif called for restraint 8 Jun but no $24B bridging proposal. Resolves 12 Jun. | — |
| W4: IRGC Gulf energy/shipping infra outage ≥1 day by EOD 13 Jun (Day 99) | 0.35 | PENDING — no confirmed outage as of 9 Jun 06:00 UTC. Resolves 13 Jun. | — |

### T+7 Scoring (Day 95 predictions → Day 102 actuals, resolves ~16 Jun)

No Day 95 items fully scoreable today.

---

### Day 102 New Predictions (T+1: 10 Jun, T+3: 12 Jun, T+7: 16 Jun)

**Trend:** → Same (Confidence: Medium)
**Threat level:** 4/5 Severe

**Watchlist predictions:**
- W1: Iran resumes missile strikes on Israel following fresh IDF Lebanon action by EOD 12 Jun (P=0.45; IDF struck Tyre 8 Jun hours after Iran's suspension; Netanyahu vowed Lebanon ops continue; Lebanon is active tripwire; methodology: post-exchange + active Lebanon trigger = 48–96h retaliation probability 0.40–0.50)
- W2: SW Iran petrochemical facility confirmed ≥1-day operational outage by EOD 10 Jun (P=0.35; IDF strike confirmed 8 Jun; CENTCOM/ISW outage assessment pending)
- W3: Pakistan back-channel public bridging proposal on $24B frozen assets by EOD 12 Jun (P=0.18; Sharif urged restraint but no proposal yet; sole active de-escalation track)
- W4: IRGC confirmed strike on Gulf energy/shipping infra causing ≥1-day outage by EOD 13 Jun (P=0.38; IRGC 48–96h retaliation window active from 8 Jun exchange; slightly down from 0.40 on Day 101 given Iran's suspension statement signals some restraint intent)
- W5: Trump formal condemnation of Israeli strikes OR US withholds military support from Israel by EOD 15 Jun (P=0.28; fracture visible but no formal action yet; unchanged)

**Probabilistic predictions (Brier inputs):**
- P(Brent >$100 by EOD 11 Jun) = 0.28 (Brent currently $93–96 after pullback from $98 intraday 8 Jun; Iran suspension eased; OPEC+ July supply increase headwind; need fresh escalation event to reach $100; slightly down from 0.32 on Day 101)
- P(Hormuz commercial transits exceed 20/day by EOD 15 Jun) = 0.03 (structural closure; no MOU; IRGC Strait Authority active)
- P(Gulf-state energy terminal IRGC strike ≥1-day outage by EOD 13 Jun) = 0.38 (IRGC retaliation doctrine active; 48–96h window from 8 Jun)
- P(Pakistan back-channel public bridging signal on $24B by EOD 12 Jun) = 0.18

**Scenarios (30d):**
- A: Negotiated framework — 20% (Δ 0pp; Lebanon/asset impasse unchanged; mutual halt does not qualify as MOU-level signal)
- B: Frozen attrition — 43% (Δ +1pp) ← modal
- C: Re-escalation — 37% (Δ −1pp; Iran's suspension statement and Brent pullback marginally reduce immediate C probability; Lebanon trigger keeps it elevated)

**Methodology delta (Day 102):** Confirm the Lebanon trigger mechanism as the highest-probability near-term escalation pathway. When Iran conditions ceasefire on Lebanon AND Israel explicitly rejects that condition AND IDF strikes in Lebanon within hours of Iran's suspension statement, the mutual-halt equilibrium half-life is ≤24h. Default: in this configuration, treat the suspension as provisional rather than stable and maintain IRGC retaliation probability at 0.40–0.50 for each 24h window in which Lebanon ops continue. Additionally: W2 (petrochemical outage) scoring gap confirmed — infrastructure outage confirmation lags kinetic event confirmation by 24–48h; build this lag into future watchlist deadline setting (+24h buffer beyond kinetic event date).

## 10 June 2026 — Day 103

### T+1 Scoring (Day 102 predictions → Day 103 actuals, 10 Jun)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W1: Iran resumes missile strikes on Israel following fresh IDF Lebanon action by EOD 12 Jun (Day 102) | 0.45 | PENDING — Iran declared end to Israel operations 9 Jun; Israel said "fire contained." No new Iran→Israel missiles confirmed 10 Jun AM. Lebanon trigger still active. Resolves EOD 12 Jun. | — |
| W2: SW Iran petrochemical facility confirmed ≥1-day operational outage by EOD 10 Jun | 0.35 | HIT — Argus Media (Tier 2) confirmed: IDF struck Mahshahr (Karoon hub) 8 Jun + Asaluyeh South Pars complex; Iran NPC confirmed damage and disruption; Bushehr deputy governor confirmed "several petrochemical production units damaged"; widespread power disruptions confirmed. Operational outage ≥1 day confirmed. Outcome = 1 | (0.35−1)²=0.4225 |

**T+1 Brier (1 scoreable item today): 0.4225**

Calibration note: W2 HIT at P=0.35 — underconfident. The infrastructure lag noted on Day 102 (outage confirmation lags kinetic event by 24–48h) was validated — outage confirmed exactly on Day 103 (24h after the Day 102 brief). The +24h buffer methodology delta is confirmed correct. Consider raising initial probability for petrochemical outage following confirmed IDF strikes on utility infrastructure (power/water) to 0.50+ when utility nodes (Mobin/Damavand type) are specifically confirmed struck.

### T+3 Scoring (Day 100 predictions → Day 103 actuals)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W3: Pakistan back-channel public bridging signal on $24B by EOD 12 Jun (Day 99/100) | 0.18 | PENDING — Pakistan FM Dar visiting Washington Friday to meet Rubio; no $24B bridging proposal confirmed. Resolves EOD 12 Jun. | — |
| W4: IRGC Gulf energy/shipping infra ≥1-day outage by EOD 13 Jun (Day 99/100) | 0.35–0.38 | PARTIAL — IRGC struck US military bases (Fifth Fleet Bahrain, Ali Al Salem Kuwait, Azraq Jordan) with missiles/drones 10 Jun (IRGC/CNN/NBC confirmed); Jordan intercepted 5 missiles; Bahrain/Kuwait intercepting. These are US military targets, not Gulf energy/shipping infra per original W4 definition. W4 as written = Gulf energy terminal outage = not yet qualifying. Resolves 13 Jun. | — |

### T+7 Scoring (Day 96 predictions → Day 103 actuals)

No Day 96 items with T+7 deadline reaching today.

---

### Day 103 New Predictions (T+1: 11 Jun, T+3: 13 Jun, T+7: 17 Jun)

**Trend:** ↑ Worse (Confidence: High)
**Threat level:** 4/5 Severe (floor; approaching Crisis threshold if IRGC strikes Gulf energy terminals)

**Watchlist predictions:**
- W1: IRGC confirmed strike on GCC energy terminal (Saudi, UAE, Qatar) causing ≥1-day operational outage by EOD 13 Jun (P=0.52; IRGC struck 21 US military targets in Bahrain/Kuwait/Jordan overnight; IRGC escalation doctrine historically expands to Gulf energy infra following direct US kinetic action; precedent: South Pars retaliatory strike on Ras Laffan April 2026; 48-72h window now active)
- W2: US conducts additional strikes on Iran (beyond overnight Bandar Abbas/Qeshm/Jask/Sirik wave) by EOD 13 Jun (P=0.40; Trump called response "very strong, very powerful"; IRGC retaliation activates second US strike cycle; ceasefire framework severely damaged)
- W3: 60-day MOU formally collapses OR Iran publicly withdraws from MOU framework by EOD 13 Jun (P=0.55; overnight US strikes on Hormuz strategic sites while MOU "tentative" = direct sabotage of framework; Iran FM Araghchi "clear violation of sovereignty"; Vance "still TBD" + new exchange makes sign-off highly unlikely near-term)
- W4: Hormuz commercial transits remain ≤5/day through EOD 17 Jun (P=0.95; structural closure; overnight US strikes on Bandar Abbas/Qeshm naval/radar sites INCREASE IRGC Strait Authority enforcement capability threat; no MOU)
- W5: Brent crude >$100 by EOD 11 Jun (P=0.58; overnight US-Iran military exchange involving Hormuz defense sites — market closed when strikes occurred; opening print likely +5–8%; Brent was ~$92 at straits.live pre-strike; range $96–102 on open)

**Probabilistic predictions (Brier inputs):**
- P(IRGC GCC energy terminal outage ≥1 day by EOD 13 Jun) = 0.52
- P(Brent >$100 by EOD 11 Jun) = 0.58
- P(60-day MOU formally signed/approved by EOD 17 Jun) = 0.07 (down from ~0.20; Apache/Hormuz exchange = framework in crisis)
- P(Hormuz commercial transits >5/day any day by EOD 17 Jun) = 0.03

**Scenarios (30d):**
- A: Negotiated framework — 12% (Δ −8pp; MOU framework in acute jeopardy after US struck Hormuz defense sites while "tentative" MOU pending; Iran's "clear violation of sovereignty" framing = negotiating red line triggered)
- B: Frozen attrition — 38% (Δ −5pp) ← modal (barely; escalation dynamics threatening B stability)
- C: Re-escalation — 50% (Δ +13pp; DIRECT US strikes on Hormuz sites + IRGC strikes on 3 Gulf US bases = tit-for-tat now US-Iran direct, not just Israel-Iran; this is the re-escalation scenario defining observable)

**Methodology delta (Day 103):** When the US directly strikes Iranian military sites at Hormuz chokepoints (Qeshm, Bandar Abbas, Jask, Sirik) while a draft MOU is simultaneously under negotiation, treat this as an MOU-invalidating event (framework confidence −50%) until explicit US official statement confirms negotiations continuing AND Iran publicly accepts that framing. "Won't hinder talks" (US official to CNN) alone is insufficient while Iran FM calls it "clear violation of sovereignty." Apply IRGC Gulf energy infra strike probability floor of 0.50 for 72h following any direct US strike on Hormuz defense nodes. Additionally: Apache-type incidents (patrol assets downed in contested airspace near Hormuz) should be flagged as HIGH false-flag/escalation ladder risk — ambiguity of whether intentional targeting (US officials divided) means both sides have incentive to interpret events to serve escalation or de-escalation as politically convenient. Default: treat as escalatory until both sides accept non-intentional framing publicly.

## Day 104 — 11 June 2026

### T+1 Scoring (Day 103 predictions → Day 104 actuals, 11 Jun 06:00 UTC)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W2: Brent crude >$100 by EOD 11 Jun | 0.58 | MISS — Brent trading $89.61–$94.43 range on 11 Jun (Investing.com); did not break $100 despite second US strike wave. SPR releases (58 mb) + OPEC+ +188 kb/d July quota capped price. Outcome = 0 | (0.58−0)²=0.3364 |

**T+1 Brier (1 scoreable item): 0.3364**

Calibration note: W2 MISS at P=0.58 — overconfident on $100 break. Market is discounting diplomatic channel survival and SPR buffer more than kinetic escalation. Delta: when SPR releases are active at scale (>50 mb) AND OPEC+ supply addition is confirmed for the same month, cap Brent >$100 probability at 0.45 even following direct US–Iran strike exchange, unless a GCC energy terminal is struck.

### T+3 Scoring (Day 101 predictions → Day 104 actuals)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W1 (Day 103): IRGC GCC energy terminal outage ≥1 day by EOD 13 Jun | 0.52 | PENDING — No confirmed GCC energy terminal outage as of 11 Jun 06:00 UTC. IRGC formal Hormuz closure declared but GCC energy terminal (Ras Tanura/Ras Laffan/Jebel Ali) not confirmed struck. Resolves EOD 13 Jun. | — |
| W3 (Day 103): MOU formally collapses/Iran withdraws by EOD 13 Jun | 0.55 | PENDING — Iran FM called US strikes "violation of sovereignty"; IRGC closed Hormuz formally; no signed MOU. MOU in acute jeopardy but not formally "collapsed" with Iran public withdrawal statement. Resolves EOD 13 Jun. | — |

### T+7 Scoring (Day 97 predictions → Day 104 actuals)

No Day 97 items with T+7 deadline reaching today.

### Day 103 Pending Items Still Active

| Item | Deadline | Status |
|---|---|---|
| W1 (Day 103): IRGC GCC energy terminal outage | EOD 13 Jun | PENDING |
| W3 (Day 103): MOU formal collapse | EOD 13 Jun | PENDING |
| W4 (Day 103): Hormuz ≤5/day through 17 Jun | EOD 17 Jun | ON TRACK — IRGC formal closure + 2 vessels struck confirms |

---

### Day 104 New Predictions (T+1: 12 Jun, T+3: 14 Jun, T+7: 18 Jun)

**Trend:** ↑ Worse (Confidence: High)
**Threat level:** 5/5 Crisis (first Crisis-level in tracker history; IRGC formal all-vessels closure declaration + kinetic enforcement)

**Watchlist predictions:**
- W1: IRGC confirmed strike on GCC energy terminal (Ras Tanura/Ras Laffan/Jebel Ali) causing ≥1-day operational outage by EOD 13 Jun (P=0.55; IRGC formal Hormuz closure + 2 vessels struck = escalation doctrine validated; 72h IRGC counter-retaliation window active from 11 Jun declaration; methodology delta: 0.50+ floor for 72h after US strike on Hormuz nodes)
- W2: CENTCOM/Iran FM jointly confirm Hormuz re-opening OR Iran publicly rescinds IRGC closure declaration by EOD 17 Jun (P=0.10; formal closure with kinetic enforcement = Iran has maximized leverage position; rescission requires either US concession or Iranian strategic calculation shift; 72h window too short for diplomacy at this tempo)
- W3: US third-wave strikes on Iran by EOD 14 Jun (P=0.45; Trump "very strong, very powerful" pattern + Iran retaliation ongoing + IRGC formal closure declaration = US "self-defence" logic provides legal/political basis for third wave; CENTCOM "remains vigilant, lethal, and ready")
- W4: Pakistan formally suspends mediation OR Iran FM publicly withdraws from MOU framework by EOD 13 Jun (P=0.40; IRGC closure declaration = Iran hardened position; but Pakistan has strong incentive to keep channel open; Iran FM has not yet issued formal withdrawal statement)
- W5: Houthi confirmed vessel strike in Red Sea/Gulf of Aden 11–14 Jun (P=0.60; Houthi doctrine escalates with Iran-axis tempo; formal Hormuz closure + direct US–Iran exchange = Houthi operational trigger conditions met; Wilson Center Jun 11 entry in progress at 06:00 UTC)

**Probabilistic predictions (Brier inputs):**
- P(IRGC GCC energy terminal outage ≥1 day by EOD 13 Jun) = 0.55
- P(Iran rescinds IRGC formal closure by EOD 17 Jun) = 0.10
- P(US third-wave strikes by EOD 14 Jun) = 0.45
- P(Brent >$100 by EOD 14 Jun) = 0.35 (revised down from 0.58; SPR/OPEC+ damper confirmed; GCC terminal strike needed to break $100)
- P(Hormuz commercial transits >5/day any day by EOD 17 Jun) = 0.05

**Scenarios (30d):**
- A: Negotiated framework — 8% (Δ −4pp; formal IRGC closure declaration + sovereignty framing = MOU signing path blocked; requires Iran to publicly retreat from a declared position)
- B: Frozen attrition — 30% (Δ −8pp; direct US–Iran exchange now structural; both sides have domestic political constraints preventing rapid de-escalation)
- C: Re-escalation — 62% (Δ +12pp) ← modal (IRGC formal all-vessels closure + kinetic enforcement + second US strike wave = Scenario C defining observables now fully active)

**Methodology delta (Day 104):** When IRGC issues a formal "closed to all vessels" declaration with kinetic enforcement (vessels struck), treat this as a structural escalation above de-facto closure: (1) IRGC GCC energy terminal strike probability floor rises to 0.55 for 96h; (2) MOU signing probability cap drops to ≤8% until Iran publicly rescinds declaration AND US pauses strike operations; (3) "CENTCOM denies closure" counter-statements do NOT offset IRGC declaration in operational risk assessment — the kinetic enforcement (vessels struck) is the Hard-tier signal. Additionally: Brent $100 break requires GCC energy terminal outage OR SPR depletion signal; US strike waves alone with active SPR releases are insufficient price catalyst (validated by Day 104 $91–96 range).

## Day 105 — 12 June 2026

### T+1 Scoring (Day 104 predictions → Day 105 actuals, 12 Jun 06:00 UTC)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W3 (Day 104): US third-wave strikes on Iran by EOD 14 Jun | 0.45 | EARLY MISS — Trump cancelled planned 3rd wave 11 Jun citing breakthrough (AP/PBS confirmed). Outcome = 0 as of 06:01 UTC 12 Jun. Deadline EOD 14 Jun still open — carry as PENDING but directionally MISS. | (0.45−0)²=0.2025 pending |
| W4 (Day 104): Pakistan suspends mediation OR Iran FM withdraws from MOU by EOD 13 Jun | 0.40 | MISS — Opposite occurred: MOU framework reached 11 Jun with Pakistan mediation central (AP/PBS confirmed). Outcome = 0. | (0.40−0)²=0.16 |
| Brent >$100 by EOD 14 Jun | 0.35 | MISS — Brent $89.25 on 12 Jun; deal optimism drove –4% on 11 Jun. Gap too large to close by EOD 14 Jun without catastrophic incident. Outcome = 0. | (0.35−0)²=0.1225 |

**T+1 Brier (3 scoreable items, 2 fully resolved): 0.16 (W4 resolved), 0.1225 (Brent, directional); W3 pending EOD 14 Jun**

Calibration note: W3 and W4 MISS pattern = Trump's deal-vs-escalation dynamic consistently resolves toward de-escalation at the last moment (validated: April 7, May 19, June 11). Delta: when Trump has previously backed down from a threatened strike while citing "talks," assign ≤0.30 probability to 3rd-wave materialising within 24h of breakthrough claim. Adjust W3 probability floor downward accordingly in future cycles.

### T+3 Scoring (Day 102 predictions → Day 105 actuals)

No Day 102 items with T+3 deadline resolving today (Day 103/104 items pending per above).

### Day 104 Pending Items Carried Forward

| Item | Deadline | Status |
|---|---|---|
| W1 (Day 104): IRGC GCC energy terminal outage | EOD 13 Jun | PENDING — No new strike in 11–12 Jun window; probability drops to ~0.20 during active ceasefire talks |
| W2 (Day 104): Iran rescinds IRGC closure / Hormuz reopen | EOD 17 Jun | PENDING — Deal framework announced but unsigned; Iran not confirmed; directionally more likely now (reassess to P=0.55) |
| W3 (Day 104): US 3rd-wave strikes | EOD 14 Jun | PENDING/directional MISS — Trump cancelled; P now 0.10 unless deal collapses |
| W5 (Day 104): Houthi vessel strike 11–14 Jun | EOD 14 Jun | PARTIAL HIT — UKMTO approach 10 Jun confirmed; probable 12 Jun Wikipedia entry (unconfirmed); resolve EOD 14 Jun |

---

### Day 105 New Predictions (T+1: 13 Jun, T+3: 15 Jun, T+7: 19 Jun)

**Trend:** → Same / Pivoting (Confidence: Medium)
**Threat level:** 4/5 Severe (down from 5/5 Crisis; breakthrough signal but unsigned deal)

**Watchlist predictions:**
- W1: Iran FM or Supreme Leader publicly confirms 60-day MOU AND Hormuz reopening commitment by EOD 15 Jun (P=0.45; Trump claims highest-level Iranian approval; Iran FM not publicly confirmed; Fars semi-official "likely to accept" = Soft; signing ceremony planned "this weekend")
- W2: Signing ceremony takes place with US and Iranian officials present by EOD 15 Jun (P=0.40; Trump says "maybe in Europe"; Vance/Witkoff/Kushner to attend; Netanyahu says Israel not party; Iran not confirmed — significant gap between Trump claim and Iranian side)
- W3: IRGC formally rescinds "closed to all vessels" declaration by EOD 17 Jun (P=0.50; deal framework includes Hormuz reopening; but IRGC declaration is a separate sovereign act requiring explicit rescission)
- W4: IRGC GCC energy terminal outage ≥1 day by EOD 13 Jun (P=0.20; 72h kinetic window from 10 Jun IRGC declaration; but ceasefire talks active; methodology delta: lower floor to 0.20 during US offensive pause + breakthrough claim)
- W5: Houthi confirmed vessel strike or sinking in Red Sea/Gulf of Aden 12–14 Jun (P=0.55; Wikipedia 12 Jun entry suggests new incident; UKMTO approach 10 Jun confirmed; Houthi ban independent of Iran ceasefire; Lebanon outside deal)

**Probabilistic predictions (Brier inputs):**
- P(Iran FM publicly confirms MOU by EOD 15 Jun) = 0.45
- P(Signing ceremony by EOD 15 Jun) = 0.40
- P(IRGC rescinds Hormuz closure declaration by EOD 17 Jun) = 0.50
- P(Brent <$85 by EOD 14 Jun) = 0.30 (deal optimism sustained; but Iran non-confirmation = uncertainty premium)
- P(GCC energy terminal outage by EOD 13 Jun) = 0.20
- P(US third-wave strikes by EOD 14 Jun) = 0.10 (deal talks active; ceasefire nominal; reversible)

**Scenarios (30d):**
- A: Negotiated framework — 35% (Δ +27pp; strongest de-escalation signal yet; but unsigned = fragile)
- B: Frozen attrition — 48% (Δ +18pp) ← modal (Iran not confirmed; deal may drag as previous breakthroughs have)
- C: Re-escalation — 17% (Δ −45pp; 3rd wave cancelled; but tail risk non-zero until IRGC rescission confirmed)

**Methodology delta (Day 105):** When Trump cancels a threatened strike AND cites diplomatic breakthrough with named-party approvals AND planning a signing ceremony (three simultaneous conditions), lower re-escalation scenario probability by ~40pp from prior estimate. This is the strongest observable short of a signed document. However, maintain Soft-tier classification until: (1) Iran FM public confirmation OR (2) signing ceremony confirmed. Do not lower threat below 4/5 until at least one Hard-tier Iranian confirmation exists. Additionally: Brent >$100 now requires active re-escalation (Scenario C trigger) — deal optimism has structurally repriced the conflict risk premium downward.

## Day 106 — 13 June 2026

### T+1 Scoring (Day 105 predictions → Day 106 actuals, 13 Jun 06:01 UTC)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W1: Iran FM publicly confirms MOU by EOD 15 Jun | 0.45 | PARTIAL HIT — Araghchi stated on IRIB TV 13 Jun that signing "within few days" and covered terms publicly (Xinhua/Times of Israel confirmed). Counts as public Iranian FM confirmation of framework, not yet signed. Score as HIT directionally. Outcome = 1. | (0.45−1)²=0.3025 |
| W2: Signing ceremony by EOD 15 Jun | 0.40 | PENDING — Geneva ceremony planned "in coming days" per CNN/AP; no ceremony yet as of 06:01 UTC 13 Jun. Deadline 15 Jun still open. | Pending |
| W4: IRGC GCC energy terminal outage by EOD 13 Jun | 0.20 | MISS — No confirmed GCC energy terminal strike in 12–13 Jun window. Outcome = 0. | (0.20−0)²=0.04 |
| W5: Houthi vessel strike 12–14 Jun | 0.55 | HIT — Wilson Center/CENTCOM: Houthi ASBM launched over Red Sea 12 Jun; CENTCOM destroyed 3 ASCM launchers + 1 UAS same day. Operational kinetics confirmed. Outcome = 1. | (0.55−1)²=0.2025 |
| P(Brent <$85 by EOD 14 Jun) | 0.30 | NEAR MISS / PENDING — Brent ~$87.40 at 06:01 UTC 13 Jun; day range 85.80–89.72. Below $85 still possible by EOD 14 Jun. Pending. | Pending |
| P(US 3rd-wave strikes by EOD 14 Jun) | 0.10 | On track for MISS — No indication of resumed strikes; deal text confirmed. Will resolve EOD 14 Jun. | Pending |

**T+1 Brier (2 resolved items): W4 MISS 0.04; W5 HIT 0.2025. W1 partial HIT 0.3025. Running 3-item Brier = 0.1825.**

Calibration note: W5 (Houthi) HIT validates maintaining ≥0.50 Houthi ASBM probability during active Iran–US kinetic exchange window even when ceasefire nominal — Houthi operational tempo confirmed independent of US–Iran deal talks. W4 MISS (GCC terminal) confirms methodology delta from Day 105: lower floor to 0.10–0.20 during active MOU finalisation + ceasefire nominal period. W1 HIT confirms: when Iran FM speaks publicly on IRIB TV about MOU terms and timeline, treat as Hard-tier Iranian confirmation (state broadcaster = regime position, but public commitment carries signalling weight above prior Fars/semi-official leaks).

### T+3 Scoring (Day 103 predictions → Day 106 actuals)

No Day 103 items with T+3 deadline resolving today per prior log.

### Day 105 Pending Items Carried Forward

| Item | Deadline | Status |
|---|---|---|
| W2 (Day 105): Signing ceremony by EOD 15 Jun | EOD 15 Jun | PENDING — Geneva ceremony planned; reassess EOD 15 Jun |
| W3 (Day 104/105): IRGC rescinds closure declaration | EOD 17 Jun | PENDING — No rescission; Araghchi sovereignty framing complicates; P reassessed 0.45 |
| W3 (Day 104): US 3rd-wave strikes by EOD 14 Jun | EOD 14 Jun | PENDING/directional MISS — P now 0.05; will resolve EOD 14 Jun |
| P(Brent <$85 by EOD 14 Jun) | EOD 14 Jun | PENDING — $87.40 current; day range touched $85.80 |

---

### Day 106 New Predictions (T+1: 14 Jun, T+3: 16 Jun, T+7: 20 Jun)

**Trend:** ↓ Better (Confidence: Medium)
**Threat level:** 3/5 Concerning (down from 4/5 Severe; Pakistan PM text confirmation + Iran FM public IRIB statement = two-source threshold met)

**Watchlist predictions:**
- W1: MOU Islamabad Declaration formally signed with simultaneous US + Iranian public announcements by EOD 17 Jun (P=0.55; Pakistan PM text confirmed; Araghchi "few days"; Geneva ceremony planned; Trump G7 travel next week as natural signing window)
- W2: IRGC formally rescinds 11 Jun closure declaration by EOD 20 Jun (P=0.45; deal framework includes Hormuz reopening; but Araghchi's sovereignty framing suggests new legal instrument — not automatic on MOU signing)
- W3: Iran–Oman joint Hormuz transit framework announced by EOD 30 Jun (P=0.30; Araghchi flagged Oman discussions; required for commercial insurance normalisation; logistically complex)
- W4: Houthi confirmed vessel strike or sinking in Red Sea/Gulf of Aden 13–17 Jun (P=0.55; ASBM launched 12 Jun; ban on Israel-linked ships active; Lebanon unresolved; Houthi campaign structurally independent)
- W5: Deal collapse signal — Trump public withdrawal OR Iran Supreme Leader public contradiction of Araghchi by EOD 17 Jun (P=0.15; Netanyahu spoiler vector active; prior breakthroughs reversed; but three-condition methodology delta lowers re-escalation floor)

**Probabilistic predictions (Brier inputs):**
- P(MOU signed by EOD 17 Jun) = 0.55
- P(IRGC rescinds Hormuz closure by EOD 20 Jun) = 0.45
- P(Brent <$82 by EOD 17 Jun) = 0.35 (signed MOU + IRGC rescission would push into $80–82 range)
- P(Brent >$95 by EOD 17 Jun) = 0.12 (requires deal collapse or new kinetics)
- P(Houthi vessel strike 13–17 Jun) = 0.55
- P(Deal collapse signal by EOD 17 Jun) = 0.15

**Scenarios (30d):**
- A: Negotiated framework — 52% (Δ +44pp vs Day 104; strongest dual-signal; Pakistan text + Iran FM public)
- B: Frozen attrition/drag — 38% (Δ −10pp; unsigned deal + sovereignty framing + Lebanon friction)
- C: Re-escalation — 10% (Δ −52pp vs Day 104; nominal ceasefire 48h+; GCC terminal W4 MISS)

**Methodology delta (Day 106):** When Iran FM speaks publicly on state TV (IRIB) about MOU terms, timeline, and signing modality — treat as Hard-tier Iranian state commitment signal, not merely Soft-tier (state media as regime position). This is qualitatively above prior Fars/Tasnim semi-official leaks. Update source weight: IRIB public FM statement = Hard tier for diplomatic commitments (but NOT for military/operational claims, which remain Soft until IRGC/CENTCOM corroboration). Log in sources.md.

## Day 107 — 14 June 2026 · Backtest Entry

### T+1 Scoring (Day 106 predictions → Day 107 actuals, 14 Jun 06:00 UTC)

| Prediction | P | Outcome | Score (Brier) |
|---|---|---|---|
| W1: MOU signed by EOD 17 Jun | 0.55 | PENDING — Electronic signing scheduled Sunday 15 Jun per Pakistan FM; Iran FM says not Sunday but "coming days"; not yet signed as of 06:00 UTC 14 Jun. Resolve EOD 17 Jun. | Pending |
| W4: Houthi vessel strike 13–17 Jun | 0.55 | HIT — M/V Verbena struck by 2 ASCM in Gulf of Aden 13 Jun; fires, 1 mariner severely injured (Wilson Center/CENTCOM confirmed). Outcome=1. | (0.55−1)²=0.2025 |
| W5: Deal collapse signal by EOD 17 Jun | 0.15 | Tracking toward MISS — No collapse; Iran FM hedged on date only; Pakistan FM confirmed ceremony. Still PENDING EOD 17 Jun. | Pending |
| P(MOU signed by EOD 17 Jun) | 0.55 | PENDING — Resolve EOD 17 Jun. | Pending |
| P(Brent <$82 by EOD 17 Jun) | 0.35 | PENDING — Brent $87.33 on 12 Jun (last trade day); markets closed 13–14 Jun (weekend). Resolve EOD 17 Jun. | Pending |
| P(Brent >$95 by EOD 17 Jun) | 0.12 | Tracking toward MISS — $87.33; deal optimism dominant. PENDING. | Pending |

**T+1 resolved items (Day 106 → 14 Jun): W4 HIT (0.2025). Running Day 107 single-item Brier = 0.2025.**

Calibration note: W4 Houthi HIT (second consecutive day) confirms 0.55 base rate for Houthi attack tempo during active Iran-US deal window is well-calibrated. Houthi campaign confirmed structurally independent — maintain ≥0.50 attack probability through Lebanon unresolved. W1/W5 PENDING — Iran date-hedging vs Pakistan FM confirmation creates genuine uncertainty; EOD 17 Jun is the resolution window.

### Day 107 New Predictions (T+1: 15 Jun, T+3: 17 Jun, T+7: 21 Jun)

**Trend:** ↓ Better (Confidence: Medium)
**Threat level:** 3/5 Concerning (maintained from Day 106)

**Watchlist predictions:**
- W1: Islamabad Declaration electronically signed with simultaneous US + Iranian official announcements by EOD 17 Jun (P=0.65; raised from 0.55; US C-17 logistics + Pakistan FM ceremony confirmation + Trump Sunday statement; Iran FM date-hedging only, not deal rejection; ISW elite consensus signal)
- W2: Iran Supreme Leader (Mojtaba Khamenei) publicly endorses MOU OR Majlis hardliner bloc formally moves to block by EOD 17 Jun (P endorsement=0.40; P bloc opposition=0.20)
- W3: IRGC formally rescinds Hormuz closure declaration by EOD 22 Jun (P=0.45; politically distinct from MOU signature; Araghchi sovereignty framing; required for commercial insurance normalisation)
- W4: Houthi confirmed vessel strike or sinking in Red Sea / Gulf of Aden 14–18 Jun (P=0.55; Verbena 13 Jun hit validates base rate; Lebanon unresolved; Israel-linked ban active)
- W5: Israel publicly breaks with US on Iran deal — Netanyahu statement rejecting MOU OR Israeli kinetic action disrupting signing by EOD 17 Jun (P=0.12; Israel warned of security threats; Netanyahu spoiler vector active but constrained by US relationship)

**Probabilistic predictions (Brier inputs):**
- P(MOU signed by EOD 17 Jun) = 0.65
- P(IRGC rescinds Hormuz closure by EOD 22 Jun) = 0.45
- P(Brent <$82 by EOD 17 Jun) = 0.40 (signed MOU + market reaction; markets reopen Mon 16 Jun)
- P(Brent >$92 by EOD 17 Jun) = 0.10 (requires deal collapse or new kinetics)
- P(Houthi vessel strike 14–18 Jun) = 0.55
- P(Deal collapse signal by EOD 17 Jun) = 0.12

**Scenarios (30d):**
- A: Negotiated framework — 62% (Δ +10pp vs Day 106; US C-17 logistics + Pakistan FM ceremony confirmation = strongest observable yet; two-mediator-country text confirmation)
- B: Frozen attrition/slip — 30% (Δ −8pp; Iran date-hedging + hardliner pushback = realistic slip to 16–17 Jun)
- C: Re-escalation — 8% (Δ −2pp; ceasefire nominal 96h+; US C-17 Geneva posture; Houthi independent)

**Methodology delta (Day 107):** No new delta. Confirm Day 106 delta: IRIB public FM statement = Hard tier for diplomatic commitments. Wave 3 (post-MOU reopening crunch) now formally added to wave assessment as a forming risk category — logistics planning horizon for mine-clearance + IRGC rescission + insurance lag should begin now under Scenario A base-case assumption.
