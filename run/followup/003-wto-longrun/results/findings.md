# Findings — WTO entry as the shock, long-run impact (003-wto-longrun)

## Headline

**A commuting zone one interquartile step more exposed to China's WTO entry
(the Pierce–Schott NTR gap) still had ≈ 1.49 fewer manufacturing jobs per 100
working-age adults in 2023 (0.0149 per adult; per s.d.: 1.19 per 100).** The
25-year NTR-gap event study is flat before 2001, diverges sharply after WTO
accession (Dec 2001), and shows **no recovery through 2023** — the effect at
2023 (−1.49) is as large as at 2019 (−1.46), and larger than at 2012 (−1.22)
or 2007 (−0.80). All per an IQR move in NTRgap; full controls, simple-mean gap,
state-clustered SE. (`results/estimates_event_study.csv`, `fig1_wto_event_study.png`.)

This is the **living element**: PS 2016 ends 2007 and PS 2020 ~2015; ADH's BPEA 2021
(a realized-import, not NTR-gap, design) ends 2019, so the published NTR-gap
horizon is shorter still. A published NTR-gap event study running to 2023/24 does not
exist; the horizon here covers the post-2010 plateau, the 2018–19 tariff war,
and the post-COVID reshoring era. **Arm A is the Pierce–Schott identification
(removal of tariff *uncertainty*) transplanted into the ADH commuting-zone
frame — not a re-estimate of ADH's realized-import estimand.**

## Pre-trend verdict (load-bearing)

**Flat.** The load-bearing falsification is the LAUS unemployment rate
(unemp/LF), the one C2 series available continuously 1990–2024. Per-IQR θ_t for
every pre-accession year is a precise zero: 1991 +0.05 (0.29), 1993 −0.06
(0.24), 1995 −0.09 (0.17), 1997 +0.06 (0.23), 1999 −0.03 (0.18) — none within
2 SE of significance. θ first loads at 2001 (+0.28, the accession year) and
grows thereafter. The C1 1998/1999 *jobs-denominator* anchors load positively
(+1.35, +0.82) but are **contaminated**: NTRgap is built from mfg employment
shares, so a mfg-jobs/total-jobs outcome is mechanically tied to the regressor,
and China's imports were already surging pre-WTO under annual-renewal risk.
They are shown as open markers, flagged, and not used as a falsification test.
The clean persons-denominator and LAUS-rate pre-trends are flat.

**Spec-dependence of the pre-trend verdict (disclosure).** The flatness above holds under the primary (full-control) spec. In the pre-declared lean sensitivity spec (start-2000 mfg share + division dummies only), the C2 LAUS-rate pre-2000 coefficients load positively and significantly (9 of 10 pre-years |t|>2 (every pre-year except 1990), e.g. 1996 +0.96 (0.28), 1993 +0.94 (0.35)); the full-spec flatness means the frozen 2000 demographic controls absorb a converging pre-2000 trend in exposed CZs. The falsification is therefore conditional on the primary spec, and the lean-spec sensitivity row should be read with that caveat. The C1 headline is less affected: its lean and full estimates agree (-1.60 vs -1.49 at 2023).

**Anticipation caveat (pre-declared).** PNTR was partially anticipated during 1999-2000 (bilateral agreement Nov 1999, House vote May 2000), and 1990s annual-renewal risk means the pre-period baseline is threat-in-place rather than threat-free; any anticipation attenuates post-2001 estimates toward zero, a conservative bias for the headline.

## Arm agreement — is the permanent hit identification-robust? **Yes.**

| horizon | Arm A (reduced form, per IQR NTR gap) | Arm B (2SLS, per $1k accum. ΔIPW, other-hi IV) |
|---|---|---|
| 2019−2000 | −1.46 (0.47)\* | −0.497 (0.126)\* |
| 2023−2000 | −1.49 (0.43)\* | **−0.432 (0.118)\*** |

Units differ (IQR of the uncertainty shock vs $1k of realized imports), so
levels are not comparable, but **both arms agree in sign and in the key
qualitative fact: no recovery between 2019 and 2023.** Arm B reproduces 002's
permanent level effect **−0.432 (0.118)** to five decimals (read from
`002-theory-update/results/theory_metrics.json`, `level_test.net`). Two
different shocks, two different identification strategies, same verdict → **"the
manufacturing hit is permanent" is identification-robust.**

## Other outcomes (per IQR, full spec, 2007 / 2012 / 2019 / terminal)

| Outcome | 2007 | 2012 | 2019 | terminal | reading |
|---|---|---|---|---|---|
| C1 mfg/pop (pp) | −0.80\* | −1.22\* | −1.46\* | **−1.49\*** (2023) | permanent, no recovery |
| C2 unemp/pop (pp) | +0.15 | +0.43\* | −0.24\* | −0.00 (2024) | transient; gone/negative by tight-labor era |
| C2 NILF proxy (pp) | +0.59 | +1.02 | +1.88\* | +0.42 (2024) | non-participation elevated, esp. 2010s |
| C3 log wkly wage (×100) | −2.67\* | −2.66\* | −2.22\* | −2.23\* (2023) | wages persistently lower |
| C4 log real transfers pc (×100) | +2.03\* | +2.58\* | +2.06 | +2.05 (2022) | transfers up, significant through 2012 |

The employment scar is permanent and the wage penalty persists; unemployment
normalizes by 2019 while people exit the labor force (elevated NILF) — exposed
CZs "still don't recover" through *jobs*, consistent with the 2018–19 tariff
era reinstating NTR-gap-like risk (flagged on the figure) rather than helping
them rebound.

## Does WTO entry matter *beyond* realized imports? (Sec-4 variant — yes)

Adding contemporaneous accumulated ΔIPW to the C1 event-year regressions, **the
NTR gap stays large and significant**: 2007 −9.49 (4.75)\* raw, 2012 −16.14
(4.34)\* raw (per-IQR −0.63, −1.08); realized ΔIPW *also* loads (2012 −0.104
(0.028)\*). Both channels operate — Pierce–Schott's own finding that removing
tariff *uncertainty* matters on top of the import flow.

**Consequence for A4.** A4 (long diff on ΔIPW **instrumented by NTRgap**) has a
strong first stage (F = 11.8) but its exclusion restriction — NTRgap affecting
outcomes only via realized imports — is exactly what this variant rejects.
Per the pre-declared reconciliation rule, **A4 is reported as a descriptive
bridge linking the two literatures, not as a causal 2SLS, and is not
headlined** (A4 2023 = −1.12 (0.40) per $1k, larger than Arm B, as expected
when the instrument also has a direct effect).

## Deviations & limitations

1. **LAUS annual re-fetched.** 001's staged `laus_checkpoint.csv` held only the
   5 snapshot years, not the annual 1990–2024 the manifest described. Since the
   C2 1990–1999 pre-trend is load-bearing, annual LAUS was fetched fresh from
   the manifest-verified FRED pattern (`results/laus_annual.csv`, 3,105
   counties, 1990–2024). This is the only fetch performed.
2. **C2 pre-2000 denominator.** popest 15–64 begins in 2000, so the pre-2001
   falsification uses the LAUS unemployment *rate* (unemp/LF, LAUS-only). The
   headline C2 measures (unemp/pop, NILF proxy) use popest 15–64 and therefore
   start in 2000; their headline years (2007/12/19/24) are unaffected.
3. **C1 pre-2000 anchors are jobs-denominator and contaminated** (see pre-trend
   verdict); supporting only, not a test. Persons-denominator C1 starts 2000.
4. **C4 terminal 2022** (BEA CAINC35 ends 2022; HEAD re-probe 2026-09-17
   confirmed 1969–2022 vintage). **C3 snapshot years only** (2000/07/12/19/23);
   no extra QCEW years fetched.
5. **Employment weights (NTRgap) use the 1988 CBP vintage** as the pre-period
   (1990) proxy; 1988 and 1991 give near-identical 722-CZ coverage.
6. Gap aggregation sensitivity (import-weighted) and the lean control spec are
   carried through and agree with the headline (C1 2023: −1.46 import-weighted,
   −1.60 lean, vs −1.49 headline).
7. Proxy outcomes throughout (CBP jobs, LAUS, QCEW, BEA — not ACS/Census
   person-level; IPUMS unavailable), inherited from 001; levels differ from
   ADH but within-CZ changes are the object of interest.
