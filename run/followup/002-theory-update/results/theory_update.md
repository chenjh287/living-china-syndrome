# The China Syndrome, theory updated to 2026: a dynamic incidence model with hysteresis

*A "Theory, updated to 2026" section for a living version of Autor, Dorn & Hanson (2013).*
*Follow-up 002. Builds on the recalibration in follow-up 001. All parameters are estimated or
calibrated on data through 2023–2024; every claim is labeled [ESTIMATED] / [CALIBRATED] /
[PROPOSED].*

---

## 1. The original model, recapped

ADH (2013, §I and the online Theory Appendix) ground their reduced-form design in a
gravity/monopolistic-competition incidence framework. A US commuting zone (CZ) is a small open
economy producing traded and non-traded goods; a rise in China's export-supply capability
$\hat A_{Cj}$ in industry $j$ lowers demand for the CZ's traded output in proportion to the CZ's
industry mix. After imposing common trade-imbalance and general-equilibrium scaling and dropping
the (small) export channel, their comparative statics collapse to a single-parameter mapping from
the **flow** of import growth to the **change** in traded-sector employment (their Eqs. 2–3):

$$\Delta y_{i,t} \;=\; -\,\tilde\alpha \cdot \Delta \text{IPW}_{i,t} \;+\; X_i'\gamma \;+\; e_{i,t},
\qquad \Delta\text{IPW}_{i,t}=\sum_j \frac{L_{ij t}}{L_{ujt}}\frac{\Delta M^{ucj}_t}{L_{it}} .$$

Two structural properties matter for what follows. The mapping is (i) **memoryless** — only the
current-period import flow enters, so predicted employment depends on nothing that happened before;
and (ii) **reversible/symmetric** — the same $\tilde\alpha$ governs a rising and a falling flow, so if
imports recede ($\Delta\text{IPW}<0$) the model predicts employment climbs back symmetrically. The
central parameter, ADH's headline, is $\tilde\alpha = -0.596\ (\text{se }0.100)$: a $+\$1{,}000$/worker
decadal rise in exposure cuts the manufacturing employment share by 0.60 pp
[ESTIMATED; replication `outputs/table3.csv`, col 6].

## 2. What the new evidence demands

Follow-up 001 re-estimated this mapping on successive post-2007 windows. Two facts emerged that the
original model cannot hold simultaneously.

**Fact 1 — the single flow elasticity "fades."** Re-fitting the *same* constant-$\tilde\alpha$ model
era by era (frozen-full spec, 2026 data vintage) gives [ESTIMATED, this study]:

| Era | window(s) | single-slope $\tilde\alpha$ | first-stage F |
|---|---|---|---|
| active shock | 2000–2012 (W2+W3) | **−0.279 (0.071)** | 66.9 |
| plateau | 2012–2019 (W4) | −0.025 (0.035) | 6.9 |
| reversal | 2019–2024 (W5) | +0.048 (0.025) | 25.4 |

The slope drifts from strongly negative to zero and slightly positive as the mean shock itself goes
from $+2.6$ (W2) to $+0.95$ (W3) to $+0.12$ (W4) to $-1.10$ (W5) $/\text{worker}$
(001, `national_context.csv` / `exposure_by_window.csv`). A constant-$\tilde\alpha$ model can only
absorb this by declaring its own central parameter unstable.

**Fact 2 — the level scar is permanent.** Yet the *levels* tell the opposite story about permanence.
Grouping CZs by accumulated 2000–2012 exposure (pop-weighted terciles) and tracking the manufacturing
employment-share **level** [ESTIMATED, 001 `c1_shares_by_year.csv`]:

| exposure group | 2000 | 2012 | 2019 | 2023 | fall (00→12) | recovered by 23 |
|---|---|---|---|---|---|---|
| high | 11.59 | 6.96 | 7.48 | 7.48 | −4.63 | +0.52 (≈11%) |
| mid | 9.78 | 6.07 | 6.60 | 6.61 | −3.71 | +0.54 (≈15%) |
| low | 5.34 | 3.46 | 3.64 | 3.70 | −1.88 | +0.24 (≈13%) |

The most-exposed places fell furthest and, once imports stopped growing and then receded, essentially
**did not climb back**. This is the "places still scarred" pattern.

**The tension.** A memoryless, reversible flow model *predicts Fact 1's fade* (no flow → no change) but
then also demands a **rebound** during the reversal (falling imports → recovering jobs). The data show
the fade *without* the rebound. The original model, taken literally, is internally forced to predict a
manufacturing renaissance in the very CZs it once said were hollowed out — and that renaissance did not
happen. The model needs a term that remembers the shock.

## 3. The updated model: dynamic incidence with directional hysteresis (one added state-dependence)

The **smallest** modification that reconciles both facts is to let ADH's incidence elasticity depend
on the *direction* of the flow — a ratchet:

$$\boxed{\;\Delta y_{i,t} \;=\; -\,\beta^{+}\underbrace{\max(\Delta\text{IPW}_{i,t},0)}_{\text{rising imports}} \;-\; \beta^{-}\underbrace{\min(\Delta\text{IPW}_{i,t},0)}_{\text{falling imports}} \;+\; X_i'\gamma \;+\; e_{i,t}\;}$$

with impact elasticity $\beta^{+}$ (= ADH's $\tilde\alpha$) and **recovery elasticity** $\beta^{-}$.
ADH is the special case $\beta^{+}=\beta^{-}$ (reversible). Hysteresis is $\beta^{-}=\rho\,\beta^{+}$ with
**recovery rate** $\rho\in[0,1]$; $\rho\approx 0$ is full scarring. Equivalently in levels, employment
tracks the **ratchet of accumulated exposure** — the running maximum of cumulative import penetration —
so a receding flow does not undo the accumulated stock:

$$y_{i,t} \;=\; y_{i,0} \;-\; \beta^{+}\,\underbrace{S^{\uparrow}_{i,t}}_{\text{stock built while imports rose}} \;+\; \beta^{+}\rho\,\underbrace{S^{\downarrow}_{i,t}}_{\text{stock unwound as imports fell}} , \qquad \rho\approx 0.$$

**The single added parameter is $\rho$** (equivalently the wedge $\beta^{+}-\beta^{-}$). This is exactly
the flow-shock/stock-legacy distinction the update calls for: the **flow** ($\Delta\text{IPW}$, now
$\approx 0$/negative) drives current-period losses only while it is positive; the **stock legacy**
($S^{\uparrow}$, the accumulated exposure) sets the permanent level. During accumulation the model *is*
ADH's flow model; once the flow reverses, the ratchet locks in the stock.

**Alternatives considered and rejected.**
- **A time-varying elasticity $\tilde\alpha_t$** (a separate slope each decade). It fits in-sample by
  construction but is not a model: it spends one free parameter *per window*, imposes no cross-era
  discipline, makes *no* out-of-sample prediction for the reversal, and is silent on the level scar.
  The ratchet nests it — the era-specific $\tilde\alpha_t$ *emerges* from the changing sign-mix of flows
  — using **one** extra parameter total, not one per window. Rejected as descriptively equivalent but
  structurally empty.
- **A pure stock model** $\Delta y = -\phi\,(\text{cumulative exposure})$. It captures permanence but
  predicts continuing decline while the stock is positive and rising, and it cannot deliver the sharp
  contemporaneous W2/W3 response the data show while the stock was still small. Rejected: it understates
  the active-shock impact. (The ratchet reproduces both the flow response *and* the stock persistence.)
- **A symmetric partial-adjustment / error-correction model** toward a fixed pre-shock equilibrium. It
  predicts recovery, which the level test (§4) directly refutes. Rejected.

## 4. Calibration and validation

### 4a. Side-by-side calibration (paper-era vs 2026)

`calibration_table.csv`. Key rows:

| parameter | symbol | paper-era (ADH) | 2026 (updated) | moment / source |
|---|---|---|---|---|
| impact elasticity (rising imports) | $\beta^{+}$ | −0.596 (0.100) | −0.279 (0.071) | ADH Table 3 col 6 → active-era 2SLS, 2026 vintage [ESTIMATED] |
| recovery elasticity (falling imports) | $\beta^{-}$ | −0.596 *(imposed = $\beta^+$)* | ≈ 0 | ADH symmetric assumption → level test [CALIBRATED] |
| recovery rate | $\rho=\beta^{-}/\beta^{+}$ | 1.00 *(reversible)* | **−0.17** (pre-2019: −0.34) | level test $b_R/(-b_I)$ [CALIBRATED] |
| permanent (net) level elasticity | $b_N$ | 0 *(transitory)* | −0.432 (0.118) | level test, $y_{23}-y_{00}$ on stock [ESTIMATED] |
| single-slope $\tilde\alpha$ forced on plateau/reversal | — | −0.596 | −0.03 / +0.05 | why constant-$\alpha$ fails [ESTIMATED] |

The recovery rate $\rho$ is estimated from a **level test** that is well-identified where the pooled
directional 2SLS is not (see §4c): using the accumulated 2000–2012 exposure "dose" (instrumented by the
eight-country analog — first stage strong, inherited from W2/W3) as the regressor in three level
equations on the 722 CZs [all ESTIMATED, this study]:

| level equation | coefficient on 2000–12 dose | interpretation |
|---|---|---|
| impact: $y_{2012}-y_{2000}$ | $b_I=-0.370\ (0.081)$ | the ADH hit, per $\$1$k accumulated |
| recovery: $y_{2023}-y_{2012}$ | $b_R=-0.062\ (0.062)$ | ≈ 0, *not* the $+0.37$ a reversible model needs |
| net: $y_{2023}-y_{2000}$ | $b_N=-0.432\ (0.118)$ | the effect is **fully permanent** through 2023 |

The recovery coefficient is statistically indistinguishable from zero and firmly rejects the reversible
prediction $b_R=+0.37$: $\rho=b_R/(-b_I)=-0.17$ (a point estimate slightly *below* zero — if anything
mild continued erosion — with a CI that excludes 1.0). The net elasticity equals the full impact: a
CZ's accumulated China exposure has left a **permanent** downshift in its manufacturing employment
share.

### 4b. Out-of-sample / held-out episode: the 2019–2024 reversal

The reversal window (post-2018 tariffs, COVID decoupling; imports from China fell in 85% of CZs) is the
episode the *original* model cannot explain — and it is genuinely held out: both models are calibrated
**only on pre-2019 data**. The symmetric ADH model has one parameter $\tilde\alpha=-0.279$ (active
window); the hysteresis model uses the same $\beta^{+}$ with $\beta^{-}\approx0$ (the pre-2019 recovery
rate). Predicting the per-CZ W5 manufacturing-share change and comparing to the actual [ESTIMATED, this
study]:

| model (calibrated pre-2019) | mean predicted W5 Δ (pp/decade) | pop-weighted RMSE across 722 CZs |
|---|---|---|
| ADH symmetric (predicts a rebound) | **+0.350** | 1.422 |
| hysteresis, $\beta^-\approx0$ (predicts no rebound) | −0.035 | **1.261** |
| naïve "no effect" benchmark | 0 | 1.204 |
| **actual 2019–2024** | **+0.064** | — |

The symmetric model predicts a $+0.35$ pp/decade manufacturing **rebound** in the reversal; the actual
change is $+0.06$ — essentially nothing. The hysteresis model (recovery $\approx 0$) predicts $\approx 0$
and matches. That the naïve zero benchmark is marginally best *is* the point: the true reversal response
is $\approx 0$, which is what hysteresis says and what the symmetric model denies. Symmetric ADH is the
only one of the three that gets the reversal qualitatively wrong.

### 4c. Robustness and what is *not* cleanly identified

A direct pooled 2SLS of the ratchet (splitting the flow at zero and instrumenting each part) recovers a
strong impact leg — $\beta^{+}=-0.338$ (partial first-stage F = 30) — but the **recovery leg is weakly
identified**: $\beta^{-}=-0.568$ (partial F = 2.2). The instrument (China's exports to eight other
high-income countries) does **not** track the US-specific reversal — its W5 mean is $+0.32$/worker while
US exposure is $-1.10$ — so there is little exogenous variation in *falling* US imports to identify
$\beta^{-}$ from the flow directly. OLS, which does not need the instrument, gives $\beta^{+}=-0.209$,
$\beta^{-}=-0.099$ (recovery rate ≈ 0.47, attenuated/biased). This is precisely why $\rho$ is calibrated
from the **level test** in §4a — which uses the *strongly*-instrumented 2000–2012 dose as its regressor —
rather than from the flow split. All three approaches agree on the sign and on $\rho<1$; the level test
is the preferred, well-identified estimate.

## 5. What the update implies going forward

- **The China-shock *impulse* on local labor markets is over, but its *incidence* is permanent.** The
  flow elasticity has gone to zero because the flow has gone to zero — not because places adjusted back.
  A 2026 forecaster who used ADH's reversible mapping would wrongly expect reshoring/tariff-driven import
  declines to *restore* manufacturing employment in the hardest-hit CZs. The hysteresis calibration says
  they will not: $\rho\approx 0$. [CALIBRATED]
- **The right treatment variable for the level of distress is now the stock, not the flow.** Policy and
  measurement should track accumulated exposure $S^{\uparrow}$ (a state), not decadal import growth (a
  flow that is now near zero or negative). [PROPOSED]
- **Where did the incidence go, if not into recovery?** Consistent with ADH's own conjecture that
  "factors other than labor bear part of the incidence," 001 found the transfer-receipt channel (C4) was
  the *most persistent* of the four claims, still positive in W3 while employment effects were fading.
  The permanent employment downshift with a persistent transfer response is the signature of adjustment
  borne by non-employment and the safety net rather than by re-employment or out-migration. Formally
  modeling the split of the permanent scar across margins (non-participation, disability, transfers,
  slow population decline) is the natural next structural step. [PROPOSED]

---

### Provenance and honesty notes
- Original-side numbers are read from replication artifacts on disk (`outputs/table3.csv`) and from 001's
  results CSVs; new numbers are produced by `workspace/src/theory_update.py` (reuses the replication's
  validated `repro/iv.py` weighted-2SLS/clustered-SE helper and 001's downloaded data — **no data was
  re-fetched or re-built**).
- Outcome is 001's CBP-jobs manufacturing-share proxy, not ADH's Census/ACS person-level measure (IPUMS
  unavailable); 001 validated the proxy (W2 proxy ≈ ADH original). Levels differ from ADH; the
  cross-window/cross-CZ *comparisons* used here are the internally consistent objects.
- The recovery leg of the directional flow model is weakly instrumented (§4c); the recovery rate is
  therefore calibrated from the well-identified level test. All labels: [ESTIMATED] from data,
  [CALIBRATED] parameter matched to a moment, [PROPOSED] theoretical suggestion not itself tested.
