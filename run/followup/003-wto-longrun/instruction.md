# Follow-up spec — WTO entry as the shock, long-run impact (003-wto-longrun)

**To the followup agent.** You are seeded from the completed replication of Autor, Dorn &
Hanson (2013), "The China Syndrome" (AER 103(6)), plus two finished follow-ups in this run
directory: `followup/001-living-update/` (window re-estimation through 2024) and
`followup/002-theory-update/` (hysteresis model; permanent level effect −0.432 (0.118)).
Read both studies' `report.md`, `result_card.json`, and `results/` before running anything.

Your job is a **third, complementary study**: bring the Pierce–Schott (AER 2016) WTO/PNTR
identification into the ADH commuting-zone frame and estimate the **long-term impact of
China's WTO entry** on US local labor markets, with outcomes through 2023/24 — 8+ years
past any published sample (PS 2016 ends 2007, PS AER: Insights 2020 ends ~2015, ADH's
BPEA 2021 Persistence follow-up ends 2019). The reader-facing target sentence: "A commuting
zone one standard deviation (or interquartile step) more exposed to China's WTO entry still
had X fewer manufacturing jobs per adult in 2023/24."

**Why this passes the judge gate (state this in your report):** a straight PNTR replication
with outcomes to 2007 would be robustness on data available to the original authors and
would rightly be rejected. The living element here is the **horizon**: the 25-year event
study covers the post-2010 plateau, the 2018–19 tariff war, and the post-COVID reshoring
era — nobody's published NTR-gap event study runs to 2024. Framing rule: Arm A is the
**Pierce–Schott identification in the ADH frame**, not "ADH's own shock" — PNTR measures
the effect of removing tariff *uncertainty*; ADH 2013 measures realized import competition.
Never present Arm A as a re-estimate of ADH's estimand.

**Deviation rule (pre-declared):** the estimands, specifications, weights, clustering, and
aggregation choices below are pre-declared. Any deviation you make — a different year set,
a dropped control, a changed weight base, an alternative aggregation, a descoped outcome —
must be logged explicitly in `report.md` ("Deviations & limitations"), in
`followup_summary.json.deviations`, and in the result card's `notes`. Silent substitution
is a failure of this study. This spec was written against the design doc
`econ2_papers/notes/china-shock-wto-extension-design.md`; if this spec and your judgment
conflict, do the closest defensible version and log it.

**Pre-staged data.** Everything you need is already under this study's
`workspace/data/` — new fetches verified 2026-09-17 plus relative symlinks into
`../001-living-update/workspace/data/` (see `workspace/DATA_MANIFEST.md` for sources,
URLs, checksums, and verification results). If your study directory is NOT the pre-staged
`003-wto-longrun/` (e.g. the launcher numbered you differently), first symlink the staged
tree into your own workspace:
`ln -s ../../003-wto-longrun/workspace/data workspace/data` — do not re-download.
You have internet + FRED_API_KEY, but the only fetch you should ever need is optional extra
QCEW years. Do NOT touch: api.census.gov (no key), www.bls.gov flat files (403 from this
network), UN Comtrade, IPUMS, and the **gated openICPSR PS 2016 archive (project 112965) —
gated resources are off-limits; report, never work around**.

---

## Workspace staging (do this first)

A verified, pre-staged data workspace for this study exists at
`../followup_staging/wto-longrun/workspace/` (relative to your study directory's
parent, i.e. `<run>/followup/followup_staging` is `<run>/followup_staging`).
Absolute path: `/data/haokunliu/veritas-workspace/econ2_papers/test-corpus/autor-dorn-hanson-2013-china-syndrome/run/followup_staging/wto-longrun/workspace`.
Your FIRST action: symlink or hardlink its contents into your own `workspace/`
(e.g. `cp -al` or per-entry `ln -s`), then verify DATA_MANIFEST.md md5s before any
analysis. Do not re-download anything listed in the manifest.

## 1. Pre-declared estimands

**Arm A (primary) — NTR-gap event study, reduced form in levels.** For each outcome y and
event year t, θ_t from:

  y_it − y_i,2000 = θ_t·NTRgap_i + X_i'δ_t + e_it,  estimated year-by-year (equivalently
  a stacked regression with year interactions; both are the same WLS),

with pre-2000 years as the falsification test (PNTR passed Oct 2000; accession Dec 2001;
θ_pre should be ≈ 0 — flat pre-trends are load-bearing, report them prominently).

Headline scalars (pre-declared, per **interquartile move in NTRgap_i**, also report per-sd).
**Scaling freeze**: the IQR and sd of NTRgap_i are computed once, unweighted across the 722
mainland CZs, from the headline (simple-mean-aggregation) gap after step 2.5, reported in
report.md, and those same two divisors are used for every outcome, arm, and year:
- **A1**: θ_2007, θ_2012, θ_2019, θ_2023 for C1 (mfg jobs / working-age pop, CBP-based).
- **A2**: θ_2007, θ_2012, θ_2019, θ_2024 for C2 (unemployment/pop and NILF proxy, LAUS-based).
- **A3**: same years for C3 (log weekly wage, QCEW, snapshot years only) and C4 (log real
  transfers pc, BEA, terminal 2022).
- **A4 (bridge 2SLS long difference)**: y_2019−y_2000 and y_2023−y_2000 on accumulated
  ΔIPW 2000–2012, **instrumented by NTRgap_i** — the "WTO entry → import surge → outcomes"
  chain linking the two literatures. Report the first stage (accumulated ΔIPW on NTRgap)
  and its F.
  **Reconciliation rule**: A4's exclusion restriction (NTRgap affects outcomes only via
  realized imports) is exactly what the §4 variant tests. If the variant shows NTRgap loading
  conditional on ΔIPW, report A4 as a descriptive bridge linking the two literatures, not as
  a causal 2SLS, and say so in findings.md; do not headline A4 in that case.

**Arm B (anchor) — accumulated-exposure long differences, ADH-2021 form.** Re-present
002's level result in ADH's Persistence style: y_2019−y_2000 and y_2023−y_2000 on
accumulated ΔIPW 2000–2012 instrumented by the comparison-country ΔIPW (001's instrument),
same controls/weights/clustering as Arm A. Pre-registered consistency target: this must
reproduce 002's permanent level effect (−0.432 (0.118) for mfg share through 2023, from
`002-theory-update/results/theory_metrics.json` — read the artifact, don't trust this
number from memory). Arm B costs almost nothing (001's panels exist) and anchors Arm A:
**the paper-level claim "the hit is permanent" is identification-robust only if both arms
agree in sign and rough magnitude at 2019 and 2023.** Say explicitly whether they do.

## 2. Shock construction (Arm A)

1. **Industry gap.** From `workspace/data/frs_tariff/tar_val.dta` (verified: 133,807 rows,
   HS8 × year 1989–2001, `spread = nonntr_rate − ntr_rate` to 1.5e-07): take **1999** lines
   (12,195 HS8; 9,997 with non-missing spread; mean 0.3168, sd 0.2304 — the PS anchor
   mean ≈ 0.32 / sd ≈ 0.15 in NAICS mfg space is your sanity check). gap at HS8 = `spread`.
2. **HS8 → HS6**: truncate hs8 to 6 digits; aggregate within HS6 both ways — (a) simple
   mean, (b) import-weighted by `v` — carry BOTH through to the end (pre-declared
   sensitivity; the headline uses (a) simple mean, mirroring PS's collapse (mean) — see
   `workspace/data/ps2020/programs/2_aeri_mortality_dataprep_06.do` lines ~1681–1727).
3. **HS6 → sic87dd** via `workspace/data/cw_hs6_sic87dd/cw_hs6_sic87dd.dta` value shares
   (zero-pad hs6 to 6 digits) → gap_j for the 397 sic87dd manufacturing industries.
4. **Industry validation (required before proceeding):** rebuild PS's own sic4-level s1999
   from tar_val using their recipe (merge on hs8num, collapse mean by sic — their sic link
   is in the PS input archive's `hs_sic_naics_imports_89_115_20160726.dta`; extract just
   that member from `20180396_input.zip`), and correlate with your sic87dd gap mapped to
   sic4. Expect r > 0.9; investigate below 0.8 (likely a padding/truncation or share bug)
   before any CZ work.
5. **CZ shock** (ADH eq. 3 skeleton, no instrument — Arm A is a reduced form):
   `NTRgap_i = Σ_j (L_ij,1990/L_i,1990)·gap_j` with employment from
   `workspace/data/cbp_czone_merged.dta` (use the **1988** vintage as the pre-period proxy
   for 1990, or 1991 if you determine 1988 coverage is worse — log the choice), 722
   mainland CZs. Reuse 001's apportionment code
   (`../001-living-update/workspace/src/exposure.py`, `build_exposure.py`) — the gap swap
   is ~30 lines; do not rewrite the machinery.
6. Report NTRgap_i distribution (mean, sd, IQR, top/bottom CZs) and its correlation with
   001's ΔIPW 2000–2012 (`../001-living-update/results/living_update/exposure_by_window.csv`)
   — expect strong positive but well below 1 (that gap is the point of Arm A).
   **Tripwire (pre-declared)**: if the 2000-population-weighted correlation between NTRgap_i
   and 001's accumulated ΔIPW 2000–2012 exceeds 0.85, drop the "two independent
   identifications" framing in favor of "complementary specifications", and accompany the
   §4 ΔIPW variant with collinearity diagnostics (partial R² / VIF), not a bare coefficient.

## 3. Outcomes (all CZ panels; 001's construction code is the starting point)

- **C1 mfg emp / working-age pop, ANNUAL 1998–2023**: CBP county files — snapshots in
  `workspace/data/cbp/`, all 21 intervening years pre-staged in `workspace/data/cbp_annual/`
  (verified: each has the `31----` mfg rollup, ~2,880–3,090 counties). Reuse 001's mfg
  extraction + flag-midpoint imputation; denominator popest 15–64 (`workspace/data/popest/`,
  interpolate intercensal years exactly as 001 did). Pre-2000 anchors: workfile 1990/2000
  outcomes + `cbp_czone_merged` 1988/1991 (levels; note the jobs-vs-persons proxy caveat).
- **C2 unemployment/pop and NILF proxy, ANNUAL 1990–2024**: `workspace/data/laus_checkpoint.csv`
  (already annual; LAUS LF is 16+ vs 15–64 denominator — same level-shift caveat as 001,
  consistent across years).
- **C3 log weekly wage**: QCEW snapshot years 2000/07/12/19/23 in `workspace/data/qcew/`
  (event-study points at snapshots only; fetch more years only if time permits — log it).
- **C4 log real transfers pc**: `workspace/data/bea/CAINC35__ALL_AREAS_1969_2022.csv`,
  annual, terminal 2022 (vintage re-probed 2026-09-17: unchanged since 2023-11-16; one
  fresh HEAD at run time is fine). Deflate with `workspace/data/pcepi_annual.csv` to 2007$.

County→CZ via `workspace/data/cw_cty_czone.dta` throughout, exactly as 001.

## 4. Specification details (pre-declared)

- **Controls X_i (frozen at 2000)**: ADH Table-3-col-6 controls from the replication
  workfile yr==2000 rows (`l_sh_popedu_c, l_sh_popfborn, l_sh_empl_f, l_sh_routine33,
  l_task_outsource`), start-of-period (2000) mfg employment share, + Census division
  dummies. Primary spec uses the full set; also run the lean spec (mfg share + division
  dummies only) as the sensitivity band, mirroring 001's primary-vs-frozen-full pair.
- **Anticipation caveat (state in findings)**: PNTR was partially anticipated during
  1999–2000 (bilateral agreement Nov 1999, House vote May 2000) and 1990s annual renewal
  risk means the pre-period baseline is "threat-in-place", so any anticipation attenuates
  post-2001 θ_t toward zero, a conservative bias worth stating.
- **Variant (required, PS 2016's own point)**: add contemporaneous ΔIPW (from 001's
  windows) to the 2007/2012 event-year regressions — does WTO entry matter *beyond*
  realized imports? Report as a variant row, not the headline.
- **Weights**: CZ share of national population in **2000** (001's popest-based weights;
  W1/W2-era anchors may use the workfile's `timepwt48` for cross-checks).
- **SEs**: clustered by state (48 mainland states), throughout, both arms.
- **Sample**: 722 mainland CZs, every regression; report N if any year drops CZs.
- **Estimator**: WLS via statsmodels/linearmodels (Arm A reduced form); linearmodels
  IV2SLS for A4 and Arm B. No Stata, no R needed. CPU-only, seconds per regression.
- **Interpretation caveat to carry into findings**: the 2018–19 tariff era partially
  reinstated NTR-gap-like risk; flag it on the figure, and note it predicts exposed CZs
  *still* don't recover (interesting, not fatal).

## 5. Validation gates (in order; do not proceed past a failed gate — debug or log)

1. Industry-level gap vs PS recipe: r > 0.9 (§2.4).
2. 1999 gap moments vs PS anchor (mean ≈ 0.32, sd 0.15–0.23 depending on space).
3. Pre-2000 θ_t flat (falsification): **C2 (LAUS, annual 1990–1999) is the load-bearing
   pre-trend test**; C1's 1988/1991/1998/1999 anchors are supporting evidence only (state
   their construction caveats). If pre-trends load, say so honestly and report
   trend-adjusted variants; do not quietly detrend.
4. Arm B reproduces 002's level effect from disk artifacts.
5. NTRgap_i vs ADH Persistence-archive exposure
   (`workspace/data/persistence/Replication/data/czone_exposure_by_period_v6_rl.dta`):
   report the correlation (001 validated its ΔIPW at 0.855; yours is a different shock —
   report, don't gate on a threshold).

## 6. Deliverables

To `results/`:
1. `estimates_event_study.csv` — tidy: `arm, claim, outcome, outcome_def, event_year,
   spec, gap_aggregation (simple|import_weighted), theta_or_beta, se, ci_lo, ci_hi,
   per (iqr|sd|unit), first_stage_F (A4/B only), N`.
2. **Flagship figure** (`fig1_wto_event_study.png/pdf`): event-study panel(s) — annual θ_t
   for C1 (and C2) with 95% CI, flat pre-2001 segment visible, sharp post-accession
   divergence, no recovery through 2023/24; vertical markers at PNTR (2000-10), accession
   (2001-12), tariff war (2018–19); reuse 001's national-context strip
   (`../001-living-update/results/living_update/national_context.csv`). Follow the
   result-presentation skill's figure style.
3. `fig2` (optional): Arm A vs Arm B long-run comparison at 2019/2023.
4. `findings.md` — ≤2 pages: the headline sentence with the actual number, pre-trend
   verdict, arm agreement, every §4 caveat, every deviation.

Plus the standard contract at the study root: `report.md`, `followup_summary.json`,
`result_card.json` (schema `sai.followup.result_card/v1`; metrics = the pre-declared
headline scalars with 002's level effect and PS 2016's published direction as baselines).
Result-card baseline provenance must cite disk artifacts (001/002 results files), never
memory.

## 7. Out of scope (pre-declared)

SSDI-specific transfers; person-level Census/ACS outcomes (IPUMS unavailable); mortality
outcomes (PS 2020's topic — their archive is here only as gap-construction input);
NAICS-space replication of PS 2016's industry regressions; the gated openICPSR archive.

## 8. Failure playbook

- HS8→sic87dd loses >10% of 1999 import value unmatched → check padding first; if real,
  report coverage and proceed with matched set, flagged.
- A CBP year parses badly → drop that event year, keep the panel (21 pre-staged years all
  passed `unzip -t` + spot parses).
- Event-study CIs explode in sparse years → report anyway; never smooth or drop silently.
- Anything long-running: FOREGROUND only (backgrounding kills the session — the #1 killer).

## 9. Compute budget

722 obs × ~35 years × ~6 outcomes × few specs — seconds each. Heaviest steps: parsing 26
CBP years (~minutes each, cache per-year mfg CSVs incrementally to results/ or workspace/)
and the one-time gap build. Target well under the followup wall clock; C1 Arm A end-to-end
first, then Arm B, then C2, then C3/C4.