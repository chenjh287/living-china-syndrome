# Living update spec — Autor, Dorn & Hanson (2013), "The China Syndrome" (AER 103(6))

**To the followup agent.** You are seeded from a completed replication of ADH 2013. The replication
codebase (ported from the Stata archive in `package/Autor-Dorn-Hanson-ChinaSyndrome-FileArchive/`)
and the original data (`dta/workfile_china.dta`, `dta/sic87dd_trade_data.dta`) are in your workspace.
Your job: re-estimate the paper's main claims on successive post-2007 windows through 2023/24 and
produce an over-time visualization showing how the China-shock estimates evolved from the paper's
1990–2007 sample to today. Every external URL below was probed and verified on 2026-08-23
(HTTP 200 + content inspected unless noted). You have full internet, FRED_API_KEY and
DATAVERSE_API_TOKEN. You do NOT have a Census API key, a BEA API key, IPUMS, or UN Comtrade access —
do not attempt those; the pipeline below avoids them entirely.

---

## 1. The claims to update

All are 2SLS on 722 commuting zones (CZs), stacked first differences (1990–2000, 2000–2007),
ten-year-equivalent changes, weighted by start-of-period CZ share of national population, SEs
clustered by state. Treatment: ΔIPW_uit = Σ_j (L_ijt/L_ujt)·ΔM_ucjt / L_it — decadal change in
Chinese imports per worker (k US$/worker, 2007 dollars), instrumented by the same measure built
from eight other high-income countries' imports from China (Australia, Denmark, Finland, Germany,
Japan, New Zealand, Spain, Switzerland) with employment lagged one decade (eq. 3–4 of the paper).

| # | Claim | Outcome | Headline (per +$1,000/worker decadal exposure) | Source |
|---|-------|---------|------------------------------------------------|--------|
| C1 | Import exposure reduces manufacturing employment | Δ mfg emp / working-age pop (pp) | **−0.596 (SE 0.099)**, full controls | Table 3, col 6 |
| C2 | Job loss shows up as unemployment and non-participation, not migration | Δ unemp/pop and Δ NILF/pop (pp) | **+0.221 (0.058)** unemp; **+0.553 (0.150)** NILF | Table 5, panel B |
| C3 | Import exposure lowers local wages | Δ mean log weekly earnings (log pts) | **−0.759 (0.253)** | Table 6, col 1 |
| C4 | Import exposure raises transfer receipts | Δ transfers per capita ($ and log pts) | **+$57.73 (18.41)**; log +1.01 (0.33) | Table 8, cols 1 |

Secondary anchors for benchmarking text: the paper attributes 33%/55%/44% of the 1990–2000 /
2000–2007 / full-period US mfg employment decline to import competition (21% for the supply-driven
component).

## 2. Update design

### Windows

| Window | Trade Δ years | Employment weights (t0) | Instrument lag weights | Status |
|--------|---------------|-------------------------|------------------------|--------|
| W1 1990–2000 | 1991→2000 | 1990 | 1980 | original — re-estimate from replication workfile |
| W2 2000–2007 | 2000→2007 | 2000 | 1990 | original — re-estimate from replication workfile |
| W3 2007–2012 | 2007→2012 | 2007 | 1999 | new |
| W4 2012–2019 | 2012→2019 | 2011 (see §4.2) | 1999 | new |
| W5 2019–2024 | 2019→2024 (outcomes to 2023 where a source stops there) | 2019 | 2007 | new |

Convert every Δ to ten-year equivalents (multiply by 10/n years: 10/9, 10/7, 10/5, 10/7, 10/5 —
for W5 use the actual outcome span, e.g. 10/4 if outcome is 2019–2023). Deflate all trade values to
2007 US$ with the annual-average PCE price index (FRED `PCEPI`, public CSV:
`https://fred.stlouisfed.org/graph/fredgraph.csv?id=PCEPI` — verified).

Also run one **pooled stacked regression** (all five windows, window dummies, exposure interacted
with window) as a compact statistical test of coefficient drift.

### Honest framing (write this into the findings note)
The economic question changes character across windows. Chinese import penetration surged 1991–2010,
plateaued after ~2010, and partially reversed after the 2018–19 tariffs and post-COVID decoupling
(ADH's own 2021 BPEA follow-up, "On the Persistence of the China Shock," found the shock plateaued
after 2010 and that *level* effects on exposed CZs persisted through 2019). So W3 still measures an
active shock; W4–W5 mostly measure adjustment/persistence under a stagnant-to-shrinking treatment
whose cross-CZ variance is far smaller. Expect: smaller ΔIPW dispersion, weaker first stages (report
first-stage F per window — if F < 10 in a window, flag the 2SLS estimate as weakly identified and
lean on the reduced form), and possibly sign flips in exposure for many CZs in W5 (negative import
growth is fine — the regressor is continuous). Interpret the IV in late windows as isolating China's
supply-driven push net of US-specific trade policy (the tariffs are precisely the kind of
US-specific demand/policy shock the instrument purges).

## 3. Data sources (all verified 2026-08-23)

### 3.1 Trade (exposure numerator)
- **CEPII BACI HS92, version 202601** — bilateral HS6 trade values 1995–2024, one CSV per year,
  single zip, no login:
  `https://www.cepii.fr/DATA_DOWNLOAD/baci/data/BACI_HS92_V202601.zip` (2,417,732,497 bytes;
  HTTP 200; supports Range requests). Contains `BACI_HS92_Y1995_V202601.csv` … `Y2024`. Columns:
  `t,i,j,k,v,q` = year, exporter (ISO numeric), importer, HS6 (1992 vintage), value (thousand
  current US$), quantity. I ranged-extracted Y2024 and parsed real rows — format confirmed.
  Country codes needed: exporter China = 156; importers USA = 842, AUS 36, DNK 208, FIN 246,
  DEU 276, JPN 392, NZL 554, ESP 724, CHE 756 (confirm codes against the `country_codes` CSV
  inside the zip).
  You only need years 2007, 2012, 2014, 2019, 2024 (plus 2000 if you validate further back), and
  only rows with i==156 and j in the 9 importers — stream-filter each year CSV, don't load whole
  files. If disk is tight, extract per-year members from the zip one at a time.
- **HS6 → SIC87dd crosswalk** (the same one ADH used):
  `https://www.ddorn.net/data/cw_hs6_sic87dd.zip` → `cw_hs6_sic87dd.dta`, 6,752 rows, columns
  `hs6, sic87dd, share, weights_method` (verified by reading the file). Apply value shares to map
  each HS6 flow into the 397 sic87dd manufacturing industries. Note `hs6` is numeric (e.g. 10110);
  zero-pad to 6 digits before matching BACI `k`.
- **ADH-cleaned trade through 2014 (validation + fallback)**:
  `https://www.ddorn.net/data/china9114.zip` → `china9114.dta`: `sic87dd, year, importer, exporter,
  imports` (nominal US$), years 1991–2014, importers include USA and the 8 comparison countries
  (verified by reading the file). **Validation step (required):** build ΔM_2007→2012 by sic87dd from
  BACI and from china9114; report the cross-industry correlation of US-from-China changes (expect
  r > 0.9; levels differ somewhat because BACI is FOB-harmonized). If BACI download fails entirely,
  fall back to china9114 (limits you to W3 + a 2012–2014 partial W4 — say so in the findings note).

### 3.2 Employment structure (exposure weights L_ijt, L_ujt, L_it)
- **CZ × sic87dd employment, precomputed by Dorn** (primary for W3, W4, and lags):
  `https://www.ddorn.net/data/cbp_czone_merged.zip` → `cbp_czone_merged.dta`: `year, sic87dd,
  czone, emp` for years **1988, 1991, 1999, 2007, 2011** (verified by reading the file). This is
  CBP already imputed, crosswalked and aggregated exactly in ADH space. Use: 2007 → W3 weights;
  2011 → W4 weights (one-year offset from the 2012 trade window start — precedented: ADH used 1990
  weights with 1991 trade; document it); 1999 → lag weights for W3 and W4; 2007 → lag weights for W5.
  L_it (total CZ employment) = sum over all sic87dd (it includes non-mfg rollups — inspect and, if
  it is mfg-only, take total CZ employment from raw CBP county totals `naics == "------"` instead;
  check against the replication's workfile `l_no_workers_totcbp` for 1991).
- **CBP 2019 raw** (W5 weights — the only new employment construction):
  `https://www2.census.gov/programs-surveys/cbp/datasets/2019/cbp19co.zip` (HTTP 200). County ×
  NAICS2017, no suppression post-2016 (noise-infused instead). Map NAICS2017 → NAICS2012 → NAICS2007
  → NAICS2002 → NAICS1997 with Census concordances (all verified HTTP 200):
  - `https://www.census.gov/naics/concordances/2017_to_2012_NAICS.xlsx`
  - `https://www.census.gov/naics/concordances/2012_to_2007_NAICS.xls`
  - `https://www.census.gov/naics/concordances/2007_to_2002_NAICS.xls`
  - `https://www.census.gov/naics/concordances/2002_NAICS_to_1997_NAICS.xls` (note: NOT
    `2002_to_1997_NAICS.xls`, which 404s)
  then NAICS1997 → SIC87 with the crosswalk **shipped in the replication package**:
  `package/.../other/cw_n97_s87.dta`, and SIC87 → sic87dd with the shipped
  `other/subfile_sic87dd.do` logic (already ported in your codebase). Where a code maps 1:m, split
  employment proportionally to national employment in the targets (same approach as ADH's cbp
  scripts in `other/`). County → CZ: `https://www.ddorn.net/data/cw_cty_czone.zip` →
  `cw_cty_czone.dta` (3,141 rows: `czone, cty_fips`; verified).
  **Fallback if the chain proves too lossy:** freeze W5 weights at 2011 (from cbp_czone_merged) —
  ADH's own BPEA follow-up freezes composition similarly; report which you used.
- **EFSY imputed CBP panel (optional helper, county × NAICS12, 1975 onward, suppressions imputed):**
  `https://github.com/fpeckert/website/releases/download/cbp-data/efsy_panel_naics.csv.zip`
  (1.3 GB CSV: `fipstate,fipscty,naics12,emp,year`; header verified). Use only if you need a lag
  year not in cbp_czone_merged.

### 3.3 Outcomes
- **C1, mfg employment share (primary, consistent across W2–W5):**
  numerator = CBP county manufacturing total employment (SIC years: sum SIC 20–39; NAICS years: the
  `31----` rollup row — no crosswalk needed), county→CZ via cw_cty_czone. Files (all HTTP 200):
  `https://www2.census.gov/programs-surveys/cbp/datasets/{YYYY}/cbp{yy}co.zip` for 2000, 2007,
  2012, 2019, 2023 (2023 is the latest; 12.9 MB). For 2007/2012 employment-flag suppression, apply
  the flag-midpoint imputation exactly as the ported `cbp*_imputations` logic does.
  Denominator = county working-age population (15–64), from Census popest (all HTTP 200, direct CSV):
  - 2000–2010: `https://www2.census.gov/programs-surveys/popest/datasets/2000-2010/intercensal/county/co-est00int-agesex-5yr.csv`
  - 2010–2020: `https://www2.census.gov/programs-surveys/popest/datasets/2010-2020/counties/asrh/CC-EST2020-AGESEX-ALL.csv`
  - 2020–2024: `https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/counties/asrh/cc-est2024-agesex-all.csv`
    (use the AGE15_64 or sum the 5-yr age buckets 15–64; watch the `YEAR` code column in the
    est-files — it indexes vintage years, read the file layout header).
  **Caveat to state prominently:** this is establishment *jobs* per resident working-age adult;
  ADH's original outcome is resident *workers* (Census/ACS persons). Both are plotted: re-estimate
  W1/W2 with the original workfile outcome (anchor points) AND with the CBP-based outcome for
  W2 (1998+ NAICS-consistent; W1 needs SIC-era CBP 1990 — include only if
  `https://www2.census.gov/programs-surveys/cbp/datasets/1990/cbp90co.zip` parses cleanly, else W1
  appears with the original outcome only). NAICS manufacturing excludes logging/publishing that SIC
  20–39 included — constant within 1998–2023, so window *changes* are consistent; note it.
- **C2, unemployment and non-participation (residents, consistent 1990–2024):** LAUS county annual
  data via **FRED** (bls.gov blocks this container's requests with 403; FRED mirrors LAUS fully —
  verified series with real 1990–2025 data):
  series IDs `LAUCN{5-digit county FIPS}00000000{3|4|5|6}A` = unemp rate | unemployment | employment
  | labor force. Example verified: `LAUCN250170000000003A/...4A/5A/6A`. Fetch with your
  FRED_API_KEY (`https://api.stlouisfed.org/fred/series/observations?series_id=...&api_key=...&file_type=json`),
  ~3,100 counties × 2 series (4A unemployment, 6A labor force) — batch politely (~120 req/min);
  budget ≈ 1 hour, checkpoint to disk as you go. Public no-key fallback:
  `https://fred.stlouisfed.org/graph/fredgraph.csv?id=ID1,ID2,...` (comma-join up to ~10 ids).
  Construct CZ-level: Δ(unemployed/pop15–64) and Δ(1 − laborforce/pop15–64) per window.
  **Caveat:** LAUS labor force is 16+ (includes 65+), popest denominator is 15–64; the NILF proxy is
  therefore level-shifted vs ADH — consistent across windows, so window-to-window comparisons stand;
  say so. Anchor W1/W2 with original workfile outcomes (`sh_unempl`, `sh_nilf` deltas).
- **C3, wages (jobs-based, consistent 1990–2024):** QCEW county average weekly wage. Annual
  singlefiles, no login (1990, 1992 and 2024 all verified HTTP 200):
  `https://data.bls.gov/cew/data/files/{YYYY}/csv/{YYYY}_annual_singlefile.zip`. Use
  `own_code == 5` (private) — or total covered `own_code == 0` — county rows
  (`agglvl_code` 70/71), field `annual_avg_wkly_wage`. CZ value = employment-weighted mean over
  counties; outcome = Δ log(avg weekly wage), deflated to real terms with PCEPI if you report real
  wages (ADH's outcome is nominal log weekly earnings within period — keep nominal deltas, the time
  dummies/window structure absorbs aggregate inflation; state the choice).
  **Caveat:** jobs-based mean weekly wage vs ADH's person-level composition-controlled log weekly
  earnings; no education/gender cuts. Anchor W1/W2 with workfile `avg_lnwkwage` deltas.
- **C4, transfers per capita (near-exact continuation of ADH's BEA source):** BEA CAINC35, county
  personal current transfer receipts, direct zip, no key (verified; contains
  `CAINC35__ALL_AREAS_1969_2022.csv`): `https://apps.bea.gov/regional/zip/CAINC35.zip`.
  LineCodes: 1000 total transfers (thousands $); also pull 2100 (retirement & disability insurance),
  2200 (medical), 2300 (income maintenance), 2400 (unemployment insurance). Per capita: divide by
  BEA's own population (CAINC30 line or use popest total). Deflate to 2007$ (PCEPI). Outcomes: Δ$
  per capita and Δ log, ten-year equivalents. Coverage ends 2022 → W5 for C4 is 2019–2022 (10/3
  scaling); **first check whether a fresher vintage exists** (probe the same URL's Last-Modified and
  `https://apps.bea.gov/regional/downloadzip.htm` for a CAINC35 file through 2023/24; use it if
  present). The persistence archive's `CA35_CZ.dta` (see §3.5) is a cross-check for pre-2019 values.
  **Caveat:** CAINC35 does not split SSDI from SSA retirement (ADH's SSDI-specific claim can't be
  updated without SSA county workbooks — skip SSDI specifically, update total/UI/income-assist/
  retirement+disability).

### 3.4 Controls and weights
- Extension windows (W3–W5), primary spec: ΔIPW + start-of-period mfg employment share (from the
  same CBP/popest construction, i.e. the lagged level of the C1 outcome variable) + Census division
  dummies (map `czone`→state→division; `https://www.ddorn.net/data/cw_czone_division.zip` exists,
  or use statefip from cw_cty_czone majority county). This mirrors ADH Table 3 col 3 (coef −0.538 vs
  −0.596 with full controls — quote that gap as the specification-sensitivity band).
- Also run a full-controls variant holding ADH's demographic controls fixed at their year-2000
  values (from the replication `workfile_china.dta` yr==2000 rows: `l_sh_popedu_c, l_sh_popfborn,
  l_sh_empl_f, l_sh_routine33, l_task_outsource`): this is what ADH's own BPEA follow-up does for
  2000–2019; frozen controls avoid needing ACS microdata (IPUMS unavailable).
- Regression weights: start-of-period CZ population share — popest county totals (2000-2010
  intercensal / CC-EST2020 / co-est2024-alldata.csv, all verified) aggregated to CZ; W1/W2 use the
  workfile's `timepwt48`.
- 2SLS, cluster SEs by state, `linearmodels.IV2SLS` (Python) or R `fixest::feols(..., iv)` /
  `ivreg`; report Kleibergen-Paap/robust first-stage F.

### 3.5 Validation anchors (required before trusting new numbers)
- Reproduce W1/W2 from the replication workfile: Table 3 col 6 ≈ −0.596 (0.099); Table 5B, 6, 8
  headline numbers above. Your replication run already did this — re-confirm in this session.
- ADH's own extension: `https://www.ddorn.net/data/Autor-Dorn-Hanson-Persistence-FileArchive.zip`
  (50.5 MB, verified; contains `Replication/data/czone_exposure_by_period_v6_rl.dta`,
  `ADH_control_vars.dta`, `czone_pop_all.dta`, `CA35_CZ.dta`, `ACS_pop_emp_inc.dta`). Correlate your
  constructed W3/W4 ΔIPW with their exposure-by-period measure (expect r ≳ 0.9 for overlapping
  periods; investigate before proceeding if r < 0.8 — likely a units, deflator, or crosswalk bug).
- BACI-vs-china9114 industry-level correlation (§3.1).
- Sanity: national sums — your US-from-China import total for 2007 should be ≈ $330B in 2007$
  (paper Table 1); mfg emp/pop should track FRED `MANEMP`/`CNP16OV`.

## 4. Estimation and outputs

Per window w ∈ {W1..W5}, per claim C1–C4 (C2 has two outcomes), estimate:

  Δy_iw (10-yr equiv) = γ_w + β_w · ΔIPW_uiw + X'_iw δ + e_iw,  ΔIPW instrumented by ΔIPW_oiw

primary spec + frozen-full-controls spec; weighted, state-clustered. N = 722 per window (drop AK/HI
consistent with mainland-only 722 CZs).

**Deliverables (write to `output/living_update/`):**
1. `estimates_by_window.csv` — tidy: `claim, outcome, outcome_def (original|proxy), window,
   years, spec, beta, se, ci_lo, ci_hi, first_stage_coef, first_stage_F, N, weight_year`.
   Include the W1/W2 original-outcome anchors and the pooled interaction model rows.
2. `exposure_by_window.csv` — czone, window, dipw_us, dipw_otherhi (for reuse/inspection).
3. `living_update_figure.(png|pdf)` — the flagship: 4 panels (C1, C2-unemp+NILF, C3, C4), x = time
   (window midpoints), y = ten-year-equivalent 2SLS coefficient with 95% CI band; shade the
   1990–2007 original sample region; dashed horizontal line at each original headline estimate with
   label (e.g. "ADH 2013: −0.60"); distinguish original-outcome anchors (solid markers) from
   proxy-outcome series (open markers) where both exist; add a small top strip showing the national
   context — China share of US goods imports (BACI) and US mfg emp/pop (FRED `MANEMP`/`CNP16OV`),
   1990–2024, so the reader sees the shock rise, plateau, and recede. Annotate first-stage F below
   any weakly identified point.
4. `findings.md` — ≤2 pages: what held, strengthened, faded, reversed; per-window first-stage
   strength; the framing from §2; every proxy caveat (jobs vs persons; LAUS 16+ vs 15–64; NAICS vs
   SIC mfg; CAINC35 ends 2022; BACI vs Comtrade levels); validation-check results.

## 5. Failure playbook
- BACI zip download fails/times out → retry with ranged/parallel download (server supports Range);
  if hard-fail, use `china9114.dta` (W3 + partial W4 only) and say so.
- CBP 2019 NAICS chain loses > ~5% of manufacturing employment unmatched → freeze W5 weights at
  2011 (cbp_czone_merged) and flag.
- FRED LAUS bulk pull throttled → halve request rate, checkpoint; it is resumable. Public
  fredgraph.csv (no key) is the backup path.
- BEA CAINC35 vintage still ends 2022 → W5-C4 = 2019–2022, scaled 10/3, flagged.
- Any single claim's pipeline fails → ship the figure with the remaining claims rather than
  blocking; C1 (manufacturing employment) is the must-have panel.
- Do NOT use: api.census.gov (returns "Missing Key" without a key we lack), www.bls.gov flat files
  (403 from this network), UN Comtrade (subscription), IPUMS (pending).

## 6. Compute budget
Everything is small-N econometrics (722 obs × ~60 regressions — seconds). The costs are downloads
(BACI 2.4 GB, EFSY 1.3 GB only if needed, QCEW ~5 years × ~80 MB, CBP ~6 × ~15 MB) and the FRED
LAUS pull (~1 h). Stream-filter BACI year-by-year; keep only the 9-importer/China slices
(a few MB each). Total session well under a day; prioritize C1 end-to-end first, then C4 (easiest
clean continuation), then C2, C3.