# Follow-up: A "living update" of Autor–Dorn–Hanson (2013), *The China Syndrome*

## Question

Autor, Dorn & Hanson (2013, AER) estimated the local-labor-market effects of Chinese import
competition across US commuting zones over 1990–2007, finding that a +$1,000/worker decadal
rise in import exposure cut the manufacturing employment share by 0.60 pp, raised unemployment
and non-participation, lowered wages, and raised transfer receipts. This follow-up **re-estimates
those four headline claims on successive post-2007 windows through 2023/24** — W3 (2007–2012),
W4 (2012–2019), W5 (2019–2024) — using the same 2SLS design (722 CZs, 10-yr-equivalent stacked
first differences, instrument = eight other high-income countries' China imports, state-clustered
SEs), and produces an over-time visualization of how the China-shock coefficients evolved. The
goal is to see whether the ADH effects persisted, strengthened, faded, or reversed as the shock
plateaued (~2010) and then reversed (post-2018 tariffs / COVID decoupling).

## Approach

**Reused from the replication** (`/workspace/eval/replication/codebase/`): the validated weighted-
2SLS / clustered-SE helper `repro/iv.py` (imported unchanged — it reproduces ADH Table 3 col 6 to
3 decimals), the original `workfile_china.dta` (W1/W2 exposure, anchor outcomes, frozen 2000
demographic controls, division dummies, state codes), and the ADH headline values read from the
replication's `outputs/table{3,5,6,8}*.csv`.

**Built new** (all under `workspace/`, data under `workspace/data/`):
- **Exposure (ΔIPW) for W3–W5.** Chinese exports to the US and to the 8 instrument countries from
  **CEPII BACI HS92 V202601** (2.4 GB; year slices 2007/2012/2019/2024 stream-filtered to China→
  9 importers), mapped HS6→sic87dd with Dorn's `cw_hs6_sic87dd` value shares, deflated to 2007$
  (FRED PCEPI). Combined with `cbp_czone_merged` CZ×industry employment weights (base years 2007,
  2011; lag years 1999, 2007) into per-CZ US and instrument exposure. `china9114` (ADH-cleaned
  trade) used as the validation anchor.
- **Outcomes rebuilt from primary sources**, county→CZ via `cw_cty_czone`, per-window 10-yr-equiv
  deltas on the 722 mainland CZs: **C1** CBP manufacturing jobs (`31----`) / popest working-age
  (15–64) population; **C2** FRED-mirrored LAUS county unemployment and labor force → unemp/pop and
  a (1−LF/pop) non-participation proxy; **C3** QCEW county average weekly wage (emp-weighted CZ mean,
  Δlog); **C4** BEA CAINC35 transfer receipts per capita (2007$, Δ$ and Δlog).
- **Estimation.** For each window×claim: weighted 2SLS in two specs — *primary* (ΔIPW + start-mfg-
  share + division dummies) and *frozen-full* (+ 5 ADH demographics frozen at 2000) — plus the
  W1/W2 original-outcome anchors (ADH full controls) and a **pooled** window-interaction model.
  Regression weights = start-of-period CZ population share (popest). First-stage F = robust
  single-instrument F.

## Results

**The shock itself** (mean constructed ΔIPW/worker, 10-yr-equiv 2007$k) rose then reversed:
**+1.18 (W1) → +2.64 (W2) → +0.95 (W3) → +0.12 (W4) → −1.10 (W5)** — mirroring China's share of
US goods imports (6%→21% peak 2017→13% 2024). The instrument weakens as dispersion shrinks
(first-stage F: 29.9, 20.8, **6.9**, 25.4 for W2–W5).

**Coefficients over time** (frozen-full spec, proxy outcome, per +$1,000/worker; SE in parens).
The "original" column is read from the replication artifacts on disk.

| Claim (outcome) | ADH'13 stacked *(replication CSV)* | W3 2007–12 | W4 2012–19 | W5 2019–24 |
|---|---|---|---|---|
| **C1** mfg emp share (pp) | −0.596 (0.099) `table3.csv` | **−0.417 (0.094)** | −0.025 (0.035) | +0.048 (0.025) |
| **C2** unemp/pop (pp) | +0.221 (0.058) `table5_emp.csv` | +0.005 (0.125) | +0.001 (0.020) | −0.002 (0.021) |
| **C2** NILF/pop (pp) | +0.553 (0.150) `table5_emp.csv` | −0.012 (0.387) | +0.026 (0.046) | −0.085 (0.068) |
| **C3** log wkly wage (log pts) | −0.759 (0.257) `table6_wage.csv` | −0.414 (0.416) | −0.002 (0.109) | −0.072 (0.174) |
| **C4** log transfers pc (log pts) | +1.013 (0.332) `table8_trans.csv` | +0.511 (0.487) | +0.020 (0.069) | +0.206 (0.186) |
| **C4** transfers pc (2007$) | +57.73 (18.41) `table8_trans.csv` | +45.0 (33.4) | +2.1 (5.2) | +7.6 (15.7) |

**Interpretation.**
- **C1 held through 2012, then vanished.** The manufacturing-employment effect is strongly
  negative and significant in **W3 (−0.42, F=20.8)** — the ADH result on fresh data while the shock
  was still active — then collapses to −0.03 (W4) and +0.05 (W5). A pooled interaction model
  confirms the drift is significant: base −0.617, **W4 +0.635 (0.105)**, **W5 +0.712 (0.103)**;
  the W3 interaction (−0.11) is insignificant (statistically the same as the ADH era).
- **C2/C3/C4 all fade the same way.** Unemployment, non-participation, wage, and transfer effects
  are near-zero and insignificant in W4–W5. Transfers (C4) show the most persistence into W3.
- This matches ADH's own 2021 *Persistence* paper: the shock plateaued after 2010; W4–W5 measure
  adjustment/persistence under a stagnant-to-shrinking treatment, not a new impulse.

**Anchoring / validation.** Constructed exposure correlates r=0.95 with the original workfile and
r=0.855 with the ADH Persistence archive's own per-worker measure (2000–07); BACI vs ADH-cleaned
china9114 trade correlates r=0.95 (industry) / 0.90 (CZ) for 2007–12; BACI US-from-China 2007 =
$319B vs paper's $330B. At W2 the proxy outcomes reproduce the originals (C2-NILF proxy +0.498 ≈
ADH +0.553), confirming the outcome substitutions are faithful.

**Figures.** `results/fig1_living_update.png` — flagship: national-context strip + 4 panels (C1;
C2 unemp+NILF; C3; C4) of the 2SLS coefficient vs time with 95% CI, the 1990–2007 sample shaded,
ADH headlines as dashed reference lines, original-outcome anchors as solid markers, proxy series as
open markers, first-stage F annotated where <10. `results/fig2_c1_drift.png` — compact card version
(constructed shock intensity + C1 coefficient drift). Also `living_update/living_update_figure.pdf`.

**Data artifacts.** `results/living_update/estimates_by_window.csv` (all 64 estimate rows incl.
primary/frozen-full/anchors/pooled), `exposure_by_window.csv` (per-CZ dipw_us & dipw_otherhi for
5 windows), plus outcome CSVs, national context, and the validation numbers above.

## Deviations & limitations

1. **W4 (2012–2019) is weakly identified** (first-stage F=6.9<10) — flagged on the figure; its
   near-zero point estimate is corroborated by the reduced form and the pooled model.
2. **Proxy outcomes, not ADH's Census/ACS person-level measures** (IPUMS unavailable): C1 is CBP
   establishment *jobs* per working-age *resident* (NAICS mfg excludes logging/publishing that
   SIC 20–39 included — constant within 1998–2023); C2 LAUS labor force is 16+ vs a 15–64
   denominator (NILF proxy level-shifted, consistent across windows); C3 is QCEW jobs-based mean
   weekly wage, nominal, no composition control; C4 is BEA total transfers (SSDI not separable).
   Levels differ from ADH; **window changes are consistent** and W2 proxy≈original confirms behavior.
3. **W5 employment weights frozen at 2011** (2019 CBP NAICS→SIC chain too lossy; sanctioned by the
   failure playbook and ADH's BPEA). **C4 W5 = 2019→2022** (CAINC35 ends 2022; no fresher vintage).
4. **BACI used for all new windows** (rather than mixing china9114 for W3), for a single internally-
   consistent trade source; china9114 retained as validation. **Switzerland corrected to BACI code
   757** (not 756). These choices are documented in `findings.md`.

Nothing in this report or the card is taken from memory or the paper's text where an executed number
exists; original-side values are read from the replication artifacts and cited to their file.
