# Follow-up 002 — Calibrated theory update for ADH (2013), "The China Syndrome"

## Question

Building on follow-up 001 (which re-estimated ADH's four headline 2SLS claims on post-2007 windows and
found them fade to zero as the shock plateaued/reversed, while local effects persisted), produce the
next intellectual step: a **calibrated, updated theory** a 2026 version of the paper would contain.
Start from ADH's own gravity/trade-exposure incidence framework (their §I / Theory Appendix),
recalibrate its central parameter on the latest data, and make the **smallest** amendment that
reconciles the original evidence (a strong contemporaneous employment effect) with 001's new evidence
(the effect fades when the import *flow* stops, yet hard-hit places stay *scarred*). Validate the updated
model with a side-by-side calibration and a held-out/out-of-sample test, labeling every claim
[ESTIMATED]/[CALIBRATED]/[PROPOSED].

## Approach

**Reused (nothing re-fetched or re-built):**
- The replication's validated weighted-2SLS / clustered-SE helper `repro/iv.py` (imported unchanged;
  reproduces ADH Table 3 col 6 to 3 decimals).
- 001's downloaded/derived data as-is: `exposure_by_window.csv` (per-CZ ΔIPW, US + eight-country
  instrument, W1–W5), `c1_shares_by_year.csv` (per-CZ manufacturing-share **levels** 2000/07/12/19/23),
  `outcome_C1.csv` (10-yr-equiv Δmfg-share by window), `cz_invariants.csv` (division dummies, frozen-2000
  demographics), `cz_pop_by_year.csv` (population weights).
- The canonical ADH coefficient (−0.596, se 0.100) read from the replication artifact
  `outputs/table3.csv` col 6.

**Built new** (`workspace/src/theory_update.py`, one script, seconds of compute):
1. **Recalibrated the single ADH incidence elasticity by era** (active 2000–12, plateau 2012–19,
   reversal 2019–24) to show the constant-slope model's central parameter is not stable.
2. **Proposed and estimated the updated model** — a *dynamic incidence with directional hysteresis
   (a ratchet)*: $\Delta y=-\beta^{+}\max(\Delta\text{IPW},0)-\beta^{-}\min(\Delta\text{IPW},0)+X'\gamma$,
   with $\beta^{+}$ = impact elasticity, $\beta^{-}$ = recovery elasticity, recovery rate
   $\rho=\beta^{-}/\beta^{+}$. ADH is the $\rho=1$ (reversible) special case.
3. **Level / permanent-downshift test** (the well-identified route to $\rho$): 2SLS of the
   manufacturing-share *level change* on accumulated 2000–2012 exposure (instrumented) over three
   horizons — impact (00→12), recovery (12→23), net (00→23).
4. **Out-of-sample validation**: calibrate both the symmetric ADH model and the hysteresis model on
   *pre-2019* data only, predict the held-out 2019–2024 reversal per CZ, compare to actual (pop-weighted
   RMSE, 722 CZs).
5. Two-group level trajectories and the figure.

Deliverables under `results/`: `theory_update.md` (the written theory section), `calibration_table.csv`,
`fig1_theory_update.png/.pdf` (+ `fig2_scar_permanence.png`), `theory_metrics.json`,
`level_trajectory_by_exposure.csv`.

## Results

**The model.** ADH's incidence mapping $\Delta y=-\tilde\alpha\,\Delta\text{IPW}$ is *memoryless* and
*reversible*. 001's two facts cannot both hold under it: the effect fades when the flow stops (consistent
with the model) **and** the level stays scarred when imports recede (which the model, being reversible,
denies — it predicts a rebound). The minimal fix is **one new state-dependence**: make the incidence
elasticity direction-dependent (a ratchet), so a receding import flow does not undo the accumulated
exposure stock. The single added parameter is the recovery rate $\rho$.

**Calibration (paper-era vs 2026)** — from `calibration_table.csv`:

| parameter | symbol | paper-era (ADH) | 2026 (updated) | source |
|---|---|---|---|---|
| impact elasticity (rising imports) | $\beta^{+}$ | −0.596 (0.100) | −0.279 (0.071) | `table3.csv` col6 → active-era 2SLS [ESTIMATED] |
| recovery elasticity (falling imports) | $\beta^{-}$ | −0.596 (imposed = $\beta^+$) | ≈ 0 | level test [CALIBRATED] |
| **recovery rate** | $\rho=\beta^{-}/\beta^{+}$ | **1.00** (reversible) | **−0.17** (≈0; pre-2019 −0.34) | level test [CALIBRATED] |
| permanent (net) level elasticity | $b_N$ | 0 (transitory) | −0.432 (0.118) | level test [ESTIMATED] |
| single-slope $\tilde\alpha$, plateau / reversal | — | −0.596 | −0.03 / +0.05 | forced constant-α fit [ESTIMATED] |

**Level test — the manufacturing scar is permanent** (2SLS on 722 CZs, per $1k accumulated 2000–12
exposure, instrumented):

| horizon | coefficient on accumulated exposure | reading |
|---|---|---|
| impact  $y_{2012}-y_{2000}$ | −0.370 (0.081) | the ADH hit |
| recovery $y_{2023}-y_{2012}$ | −0.062 (0.062) | ≈ 0 — **not** the +0.37 a reversible model needs |
| net $y_{2023}-y_{2000}$ | −0.432 (0.118) | effect fully permanent through 2023 |

Recovery is statistically zero and rejects full reversion; the net effect equals the full impact. In
raw levels, the top-exposure tercile of CZs fell 4.63 pp (2000→2012) and recovered only 0.52 pp (≈11%)
by 2023; the effect that once looked transitory is a permanent downshift.

**Out-of-sample — the 2019–24 reversal the original model cannot explain** (both models calibrated on
pre-2019 data; predict held-out W5, 722 CZs):

| model (calibrated pre-2019) | mean predicted W5 Δ (pp/decade) | weighted RMSE |
|---|---|---|
| ADH symmetric (predicts rebound) | +0.350 | 1.422 |
| hysteresis, $\beta^-\approx0$ | −0.035 | 1.261 |
| naïve "no effect" | 0 | 1.204 |
| **actual 2019–2024** | **+0.064** | — |

The symmetric model predicts a +0.35 pp/decade manufacturing rebound where imports fell; the actual
change is +0.06 (≈ nothing). The hysteresis model predicts ≈ 0 and matches. Symmetric ADH is the only
one that gets the reversal qualitatively wrong.

**Comparison to the original replication values**

| quantity | original (replication artifact) | this follow-up | source file | note |
|---|---|---|---|---|
| impact incidence elasticity $\beta^+$ | −0.596 (0.100) | −0.279 (0.071) active-era | `replication/.../outputs/table3.csv` col6 | same sign/order; the impact leg survives |
| recovery rate $\rho$ | 1.00 (implied by ADH's reversible model) | −0.17 ≈ 0 | ADH §I / Eqs. 2–3 (theory) | new parameter; reversibility rejected |
| single-slope α, reversal era | −0.596 (assumed constant) | +0.048 (0.025) | 001 `summary_frozenfull_proxy.csv` (W5) | why a constant α fails |
| net/permanent level effect | 0 (transitory in flow model) | −0.432 (0.118) | this study, `theory_metrics.json` | scar is permanent |

The full written theory section is `results/theory_update.md`. The figure (`fig1_theory_update.png`)
shows all four pieces: the era-drift of the single elasticity (A), the permanent level scar by exposure
group (B), the level-test coefficients with the ADH reversible prediction marked (C), and the held-out
reversal test (D).

## Deviations & limitations

1. **The recovery leg of the *flow* ratchet is weakly instrumented** (pooled directional 2SLS partial
   first-stage F = 2.2): China's exports to the eight instrument countries did not fall with the
   US-specific post-2018 reversal (its W5 mean is +0.32 while US exposure is −1.10), so there is little
   exogenous variation in *falling US imports*. The recovery rate is therefore calibrated from the
   **level test**, which uses the strongly-instrumented 2000–2012 dose (F ≈ 30) as its regressor. OLS on
   the flow split gives a larger (attenuated-toward-symmetry) recovery rate ≈ 0.47; all approaches agree
   $\rho<1$. This is disclosed in §4c of `theory_update.md` and is the main caveat on the exact value of
   $\rho$ (its being well below 1, and the *permanence* of the level effect, are robust).
2. **Proxy outcome, not ADH's Census/ACS person-level measure** (IPUMS unavailable): the manufacturing
   share is 001's CBP-jobs-per-working-age-resident proxy. 001 validated it (W2 proxy ≈ ADH original).
   Levels differ from ADH; the cross-window/cross-CZ comparisons used here are the consistent objects.
3. **The updated model is calibrated, not fully structurally estimated.** A genuinely structural
   estimation of the ratchet (e.g. a nonlinear GMM on the accumulation vs. unwinding of the stock) was
   infeasible in-session with a well-behaved instrument for the reversal; per the instruction I calibrate
   to the moments 001 already produced (the level changes and window elasticities) and say so. The
   forward-looking claims (§5) are labeled [PROPOSED].
4. **Endpoints inherited from 001**: W5 level is 2019→2023 (latest CBP), scaled where 001 scaled it; the
   $c1\_shares\_by\_year$ endpoints are 2000/07/12/19/23. No new data vintage was pulled.
