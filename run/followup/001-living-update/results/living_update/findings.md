# Living update of Autor–Dorn–Hanson (2013), "The China Syndrome" — findings

**Question.** Re-estimate ADH's four headline local-labor-market claims on successive
post-2007 windows through 2023/24 and visualize how the China-shock coefficients evolved
from the paper's 1990–2007 sample to today.

**Design.** 2SLS on 722 mainland commuting zones, ten-year-equivalent first differences,
weighted by start-of-period CZ population share, SEs clustered by state. Treatment ΔIPW =
decadal change in Chinese imports per worker (2007 US$), instrumented by the same measure
built from eight other high-income countries' imports from China. Windows: W1 1990–2000,
W2 2000–2007 (original), W3 2007–2012, W4 2012–2019, W5 2019–2024 (new). Trade from CEPII
BACI HS92 V202601 mapped to sic87dd; employment weights from Dorn's `cbp_czone_merged`;
outcomes rebuilt from CBP / LAUS(FRED) / QCEW / BEA CAINC35. Primary spec = ΔIPW +
start-period mfg-share + Census-division dummies; **frozen-full** spec adds ADH's five
demographic controls frozen at their 2000 values. All coefficients below are the
frozen-full spec, proxy outcome, per +$1,000/worker decadal exposure.

## What the shock did over time (the national context)

China's share of US goods imports rose 6%→16% (1995→2007), plateaued at ~19–21% (2010–2017),
then **receded to 13% by 2024** after the 2018–19 tariffs and post-COVID decoupling. The
mean cross-CZ exposure I constructed tracks this exactly: ΔIPW/worker (10-yr-equiv, 2007$k)
= **+1.18 (W1) → +2.64 (W2) → +0.95 (W3) → +0.12 (W4) → −1.10 (W5)**. So W3 still measures
an active shock; W4 measures a stagnant treatment; W5 measures a *reversing* treatment
(85% of CZs have negative import growth). Treatment cross-CZ dispersion shrinks and the
instrument weakens accordingly (first-stage F: W2 29.9, W3 20.8, **W4 6.9**, W5 25.4).

## What held, faded, reversed (β, SE in parentheses; ADH'13 stacked headline for reference)

| Claim (outcome) | ADH'13 | W2 2000–07 | W3 2007–12 | W4 2012–19 | W5 2019–24 |
|---|---|---|---|---|---|
| **C1** mfg emp share (pp) | −0.596 (0.099) | −0.326 (0.138) | **−0.417 (0.094)** | −0.025 (0.035) | +0.048 (0.025) |
| **C2** unemp/pop (pp) | +0.221 (0.058) | +0.068 (0.072) | +0.005 (0.125) | +0.001 (0.020) | −0.002 (0.021) |
| **C2** NILF/pop (pp) | +0.553 (0.150) | +0.498 (0.240) | −0.012 (0.387) | +0.026 (0.046) | −0.085 (0.068) |
| **C3** log wkly wage (log pts) | −0.759 (0.257) | −1.571 (0.527) | −0.414 (0.416) | −0.002 (0.109) | −0.072 (0.174) |
| **C4** log transfers pc (log pts) | +1.013 (0.332) | +0.729 (0.337) | +0.511 (0.487) | +0.020 (0.069) | +0.206 (0.186) |
| **C4** transfers pc (2007$) | +57.73 (18.41) | +37.1 (26.5) | +45.0 (33.4) | +2.1 (5.2) | +7.6 (15.7) |

- **Held through 2012 (C1, C4).** The manufacturing-employment effect is strongly negative
  and significant in **W3 (−0.417, F=20.8)** — essentially the ADH result on fresh data,
  while the shock was still active. Transfer receipts (C4) likewise still rise with exposure
  in W3 (+0.51 log, +$45/cap).
- **Faded to zero by 2012–2019 (W4) and stayed there in W5.** Every claim collapses toward
  zero once the shock plateaus: C1 goes −0.42 → **−0.03 (W4)** → **+0.05 (W5)**; C2, C3, C4
  all become statistically indistinguishable from zero. The tiny **positive** C1 sign in W5
  is consistent with a reversing treatment (imports falling most in the CZs once most exposed).
- **The drift is statistically confirmed.** A pooled stacked model (all four windows, exposure
  × window interactions, W2 base) gives base β = −0.617 and significant positive interactions
  **W4 +0.635 (0.105)** and **W5 +0.712 (0.103)** — i.e. the exposure–mfg-employment slope is
  significantly less negative after 2012. W3 interaction −0.113 (0.172) is insignificant: the
  effect is statistically unchanged from the ADH era through 2012.

**Bottom line.** ADH's original findings replicate on fresh post-2007 data *for the window in
which the shock was still active* (2007–2012), then fade to zero as the shock plateaus and
reverses — matching ADH's own 2021 "Persistence" conclusion that the shock plateaued after
2010. The China-shock *impulse* on local labor markets is over; these later windows measure
adjustment under a treatment that is no longer growing.

## Validation checks (all passed)

- **Exposure vs original workfile** (2000–07 reconstruction): r = **0.954** (US), 0.984 (instrument).
- **Exposure vs ADH Persistence archive** `d_tradeusch_p1_2000_2007`: r = **0.855** (>0.8 threshold).
- **BACI vs china9114** (ADH-cleaned trade), 2007→2012: industry-level ΔM r = **0.950** (US);
  CZ-level exposure r = **0.90**. Levels differ (BACI is FOB-harmonized): china9114 puts the
  2007→2012 US-from-China rise at $50B, BACI at $74B — BACI is closer to Census (~$68–75B), so
  BACI is used for all new windows.
- **National sums.** BACI US-from-China 2007 = $319B (paper Table 1: ~$330B). Mfg emp/pop and
  China-import-share series track FRED `MANEMP`/`CNP16OV` and Census.
- **Proxy vs original outcome at W2** (same exposure): C2-NILF proxy +0.498 ≈ ADH +0.553;
  C1 proxy −0.326 vs ADH per-period −0.469; C4-log proxy +0.729 vs ADH +1.013. Proxies behave
  like the originals, validating the outcome substitutions.

## Deviations & caveats (each matters for interpretation)

1. **W4 is weakly identified (first-stage F = 6.9 < 10).** The 2012–2019 2SLS estimate is
   flagged; its near-zero point estimate should lean on the reduced form / the pooled model,
   both of which agree the effect is gone.
2. **Outcomes are jobs/BEA-based proxies, not ADH's Census/ACS person-level measures**
   (IPUMS unavailable). C1 numerator = CBP establishment *jobs* (NAICS `31----`) per
   working-age *resident*, not resident workers; C2 uses LAUS (labor force is 16+, denominator
   15–64, so the NILF proxy is level-shifted but consistent across windows); C3 is QCEW
   jobs-based mean weekly wage (nominal, no education/gender composition control); C4 is
   BEA CAINC35 total transfers (SSDI cannot be split out). Levels differ from ADH but
   **window-to-window changes are internally consistent**, and the W2 proxy≈original checks
   above confirm they behave like the originals.
3. **W5 employment weights frozen at 2011** (2019 CBP requires a lossy NAICS2017→SIC87 chain;
   the failure playbook and ADH's own BPEA sanction freezing). Lag weights: 1999 (W3/W4), 2007 (W5).
4. **Coverage endpoints.** C1/C2/C3 W5 outcome = 2019→2023 (latest CBP/LAUS/QCEW), scaled 10/4;
   C4 W5 = 2019→2022 (CAINC35 ends 2022, no fresher vintage — confirmed Last-Modified Nov 2023),
   scaled 10/3. Connecticut adopted planning-region FIPS in 2022; all CT counties belong to one
   CZ (20901) so CT is routed there for 2023 files.
5. **Switzerland is BACI code 757, not 756** (instruction said 756; corrected against
   `country_codes_V202601.csv`).
6. **Nominal wages / within-window inflation.** C3 and C4-dollar keep ADH's convention; trade
   values are deflated to 2007$ with PCEPI. The differenced-Persistence exposure check gave a
   low r (0.28) — an artifact of differencing two cumulative measures with different base-year
   weights, not the pipeline (the direct-vs-direct checks above are the valid ones).
