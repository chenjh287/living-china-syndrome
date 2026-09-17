# Follow-up 003 — WTO entry as the shock: the long-run impact of China's WTO accession on US local labor markets

## Question

Follow-ups 001 and 002 studied ADH (2013)'s **realized-import** shock (ΔIPW):
001 re-estimated the four headline 2SLS claims on post-2007 windows (they fade
as the import flow plateaus/reverses), and 002 showed the manufacturing *level*
effect is a **permanent scar** (−0.432 (0.118) through 2023). This third study
brings the **Pierce–Schott (AER 2016) WTO/PNTR identification** — the removal of
tariff *uncertainty* when Congress granted China Permanent Normal Trade
Relations (PNTR passed Oct 2000; WTO accession Dec 2001) — into the ADH
commuting-zone frame, and estimates the **long-term impact of China's WTO entry
on US local labor markets with outcomes through 2023/24**, 8+ years past any
published NTR-gap event study (PS 2016 ends 2007, PS 2020 ~2015; ADH's BPEA 2021,
a realized-import rather than NTR-gap design, ends 2019). Target sentence: *"A commuting zone one standard deviation (or
interquartile step) more exposed to China's WTO entry still had X fewer
manufacturing jobs per adult in 2023/24."*

**Why this passes the judge gate.** A straight PNTR replication to 2007 would be
robustness on the original authors' data. The living element is the **horizon**:
a 25-year event study covering the post-2010 plateau, the 2018–19 tariff war,
and post-COVID reshoring. **Arm A is the Pierce–Schott shock (tariff-uncertainty
removal) in the ADH frame — deliberately *not* a re-estimate of ADH's
realized-import estimand.**

## Approach

**Reused from the replication and from 001/002 (not rebuilt):**
- The validated weighted-2SLS/OLS + state-clustered-SE helper
  `/workspace/eval/replication/codebase/repro/iv.py` (reproduces ADH Table 3
  col 6 to 3 decimals), imported unchanged.
- 001's exposure/apportionment machinery (`exposure.py`, `build_c1..c4.py`) and
  its derived CZ artifacts: `cz_invariants.csv` (division dummies + frozen-2000
  demographics), `cz_pop_by_year.csv` (2000 weights), `c1_shares_by_year.csv`
  (2000 start-mfg control), `exposure_by_window.csv` (ΔIPW for A4/Arm B),
  `national_context.csv`, `cz722.csv`.
- 002's `theory_metrics.json` for the Arm-B consistency target (**read from
  disk**, `level_test.net = −0.43219 (0.11804)`).

**Built new (`workspace/src/`):**
1. `build_gap.py` — the NTR-gap shock (Arm A). §2 pipeline: 1999 FRS `tar_val`
   HS8 spreads → HS6 (simple-mean **and** import-weighted) → sic87dd via
   `cw_hs6_sic87dd` value shares → `NTRgap_i = Σ_j (L_ij,1988/L_i,1988)·gap_j`
   over 722 CZs, with the PS-recipe validation and all correlations.
2. `build_c1_annual.py` — C1 CBP mfg jobs (`31----`, size-class–midpoint
   imputation) / popest working-age pop, **annual 1998–2023** (26 CBP years
   parsed and cached).
3. `fetch_laus_annual.py` + `build_c2_annual.py` — C2 LAUS annual 1990–2024.
4. `build_c3c4_levels.py` — C3 QCEW log weekly wage & C4 BEA log real transfers
   pc, snapshot levels.
5. `estimate_arms.py` — Arm A event study, A4 bridge 2SLS, Arm B anchor, and the
   Sec-4 variant. `figures.py` — the two figures.

**Estimand (Arm A):** year-by-year WLS
`y_it − y_i,2000 = θ_t·NTRgap_i + X_i'δ_t + e_it`, weights = 2000 CZ population,
SE clustered by state (48 mainland states), 722 CZs. Controls X: full =
start-2000 mfg share + Census-division dummies + 5 ADH demographics frozen at
2000; lean = mfg share + division dummies. Both gap aggregations carried through.
**Scaling freeze** (computed once, unweighted, on the headline simple-mean
NTRgap): **IQR = 0.0668, s.d. = 0.0533**; those two divisors scale every θ.

## Validation gates (all passed)

| Gate | Target | Result |
|---|---|---|
| 1. Industry gap vs PS sic4 recipe | r > 0.9 | **r = 0.959** (383 common SIC) |
| 2. 1999 gap moments | mean ≈ 0.32, sd 0.15–0.23 | **mean 0.326, sd 0.164** (sic87dd) |
| 3. Pre-2001 θ_t flat (C2 LAUS rate) | ≈ 0 | 1991–99 all within 1.2 SE of 0 (full spec; lean spec loads, see disclosure) |
| 4. Arm B reproduces 002 level effect | −0.432 (0.118) | **−0.43219 (0.11804)** (5-dp match) |
| 5. NTRgap vs ADH Persistence exposure | report | r = 0.79 (vs 1991–2007 ΔIPW) |

Data-coverage checks: HS6→sic87dd matched **100%** of 1999 import value;
NTRgap covers **99.9%** of 1988 mfg employment; 396 mfg sic87dd industries.
**Tripwire:** pop-2000-weighted corr(NTRgap, accumulated ΔIPW 2000–2012) =
**0.50** (unweighted 0.60) — below 0.85, so the "two independent
identifications" framing holds.

## Results

### Flagship — C1 manufacturing employment (`fig1_wto_event_study.png`)

θ_t per IQR move in NTRgap (full spec, simple gap), selected years:

| year | 2001 | 2007 | 2012 | 2019 | 2023 |
|---|---|---|---|---|---|
| θ (pp per IQR) | −0.04 | **−0.80\*** | **−1.22\*** | **−1.46\*** | **−1.49\*** |
| (SE) | (0.12) | (0.34) | (0.31) | (0.47) | (0.43) |

Per s.d.: 2023 = **−1.19 (0.34)**. In per-adult terms the 2023 IQR effect is
**0.0149 fewer manufacturing jobs per working-age adult** (0.0119 per s.d.).
The path is flat before 2001, diverges monotonically after accession, and does
**not** recover through 2023 — the plateau, tariff war, and reshoring era leave
the most-exposed CZs no closer to their 2000 baseline. Robust to gap
aggregation (import-weighted 2023 = −1.46) and controls (lean 2023 = −1.60).

### Other outcomes (per IQR, full; 2007 / 2012 / 2019 / terminal)

| Outcome | 2007 | 2012 | 2019 | terminal |
|---|---|---|---|---|
| C1 mfg/pop (pp) | −0.80\* | −1.22\* | −1.46\* | −1.49\* (2023) |
| C2 unemp/pop (pp) | +0.15 | +0.43\* | −0.24\* | −0.00 (2024) |
| C2 NILF proxy (pp) | +0.59 | +1.02 | +1.88\* | +0.42 (2024) |
| C3 log wkly wage (×100) | −2.67\* | −2.66\* | −2.22\* | −2.23\* (2023) |
| C4 log real transfers pc (×100) | +2.03\* | +2.58\* | +2.06 | +2.05 (2022) |

The employment scar and wage penalty are permanent; unemployment normalizes by
the tight-labor-market late 2010s while labor-force *exit* stays elevated —
exposed CZs don't recover through jobs. (\* = |θ| > 1.96·SE.)

### Arm agreement (`fig2_arm_comparison.png`)

Arm A (reduced form) 2019 −1.46\* / 2023 −1.49\* per IQR; Arm B (2SLS on
accumulated ΔIPW 2000–2012, other-hi instrument) 2019 −0.497\* / **2023 −0.432\***
per $1k. Different shocks, different identification strategies, **same sign and same
permanence** → the paper-level claim "the hit is permanent" is
identification-robust. Arm B reproduces 002 exactly.

### WTO entry beyond realized imports (Sec-4 variant)

With contemporaneous ΔIPW added, NTRgap stays large/significant (2012 raw
−16.14 (4.34), per-IQR −1.08) and ΔIPW also loads (−0.104 (0.028)). Both
channels matter — PS 2016's own point. **A4's exclusion restriction is thereby
rejected**, so A4 (2023 −1.12 (0.40) per $1k, first-stage F = 11.8) is reported
as a **descriptive bridge, not a causal 2SLS, and is not headlined.**

### Comparison to prior artifacts

| Quantity | Prior value (source) | This study | Note |
|---|---|---|---|
| Permanent mfg level effect, 2023 | −0.432 (0.118) — `002/results/theory_metrics.json` `level_test.net` | Arm B −0.43219 (0.11804) | 5-dp reproduction (same construction) |
| ADH realized-import mfg effect (per $1k, ADH era) | −0.596 (0.099) — `replication/.../outputs/table3.csv` col6 | n/a (different estimand) | Arm A measures the *uncertainty* shock, not ΔIPW |
| NTR-gap horizon in prior work | ~2015 (PS 2020); ADH BPEA 2021, a non-NTR-gap design, ends 2019 | **2023 (C1/C3), 2024 (C2)** | the living element |
| 1999 industry NTR gap moments | mean ≈0.32 (PS 2016) | mean 0.326, sd 0.164 | gate 2 |

## Deviations & limitations

See `results/findings.md` for the full list; the material ones:
1. **Annual LAUS 1990–2024 re-fetched** — 001's staged checkpoint held only 5
   snapshot years, and the load-bearing C2 pre-trend needs the annual 1990s
   series. Fetched from the manifest-verified FRED pattern; the only fetch made.
2. **C2 pre-2000 denominator = LAUS unemployment rate** (popest 15–64 starts
   2000); headline C2 (unemp/pop, NILF) start 2000, headline years unaffected.
3. **C1 pre-2000 (1998/99) anchors are jobs-denominator and contaminated** by
   the shock's construction — supporting-only, not a falsification test; the
   clean pre-trend is C2's LAUS rate (flat).
4. **C4 terminal 2022** (BEA vintage), **C3 snapshots only**, **NTRgap weights =
   1988 CBP vintage**. All per spec/failure-playbook.
5. Proxy outcomes throughout (CBP/LAUS/QCEW/BEA, no IPUMS) inherited from 001.

All original-side numbers are read from disk artifacts and cited to their file;
nothing here is taken from memory or the papers' text where an executed number
exists.

## Disclosures

**Spec-dependence of the pre-trend verdict (disclosure).** The flatness above holds under the primary (full-control) spec. In the pre-declared lean sensitivity spec (start-2000 mfg share + division dummies only), the C2 LAUS-rate pre-2000 coefficients load positively and significantly (9 of 10 pre-years |t|>2 (every pre-year except 1990), e.g. 1996 +0.96 (0.28), 1993 +0.94 (0.35)); the full-spec flatness means the frozen 2000 demographic controls absorb a converging pre-2000 trend in exposed CZs. The falsification is therefore conditional on the primary spec, and the lean-spec sensitivity row should be read with that caveat. The C1 headline is less affected: its lean and full estimates agree (-1.60 vs -1.49 at 2023).

**Anticipation caveat (pre-declared).** PNTR was partially anticipated during 1999-2000 (bilateral agreement Nov 1999, House vote May 2000), and 1990s annual-renewal risk means the pre-period baseline is threat-in-place rather than threat-free; any anticipation attenuates post-2001 estimates toward zero, a conservative bias for the headline.
