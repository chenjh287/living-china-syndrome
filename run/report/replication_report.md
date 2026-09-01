# Replication Report

**Generated:** 2026-08-23 22:33:57

---

## Executive Summary

**Mode:** full

**Replication Score: 80.0%** (25/28 claims counted)

*Coverage: scored over 25 attempted/blocked claim(s); 3 out-of-scope (not targeted by the plan — excluded, not counted as failures).*

## Tier Breakdown

| Tier | Match | Partial | No match | Not attempted | n/a | Missing | Total |
|---|---|---|---|---|---|---|---|
| Headline | 4 | 0 | 0 | 1 | 0 | 0 | 5 |
| Supporting | 15 | 2 | 0 | 3 | 0 | 0 | 23 |

## Per-Claim Verdicts

| ID | Tier | Type | Status | Rationale | Evidence |
|---|---|---|---|---|---|
| C1 | headline | scalar | match | The produced table log/tab_ipw_manuf_2.scsv (Table 3, fully-controlled specification) shows in column (6) the coefficient on the import exposure regressor d_t~eusch_pw = -0.596 ... | 1 file(s) |
| C2 | supporting | table | match | All cells of Table 3 (2SLS estimates) match the paper values to the reported precision. The main d_tradeusch_pw coefficients in log/tab_ipw_manuf_2.scsv (line 5) are -0.746, -0.... | 3 file(s) |
| C3 | supporting | scalar | match | The evidence file log/tab_ipw_mfg_byperiod.scsv (Table 2) reports the d_tradeusc~w (Chinese import exposure) 2SLS coefficients in columns 1-3 as -0.888, -0.718, and -0.746, with... | 1 file(s) |
| C4 | supporting | scalar | match | log/tab_ipw_mfg_byperiod.scsv (Table 2) reports the coefficients on future-period import exposure (d_tradeusc~e) in columns 4-6: 0.431 (SE 0.149) for 1970-1980, -0.130 (SE 0.126... | 2 file(s) |
| C5 | headline | scalar | not attempted | No plan step targeted this claim; the planner marked it BLOCKED (counts as a reproducibility gap): Headline aggregate counterfactual (% of national mfg-employment decline explai... | 0 file(s) |
| C6 | supporting | scalar | not attempted | No plan step targeted this claim; the planner marked it BLOCKED (counts as a reproducibility gap): Supply-driven (48%) counterfactual worker-count decomposition (548k/982k). No ... | 0 file(s) |
| C7 | headline | scalar | match | This headline economic-magnitude summary follows directly from the reproduced fully-controlled 2SLS coefficients scaled by the 2000-2007 interquartile exposure differential. The... | 7 file(s) |
| C8 | supporting | scalar | partial | The preferred-specification baseline OLS is reproduced essentially exactly: outputs/apptab4_ols.csv reports coef_d_tradeusch_pw = -0.1711 (se 0.0278, n=1444) for d_sh_empl_mfg, ... | 3 file(s) |
| C9 | supporting | scalar | match | The run reproduced Figure 2's first-stage and reduced-form regressions (N=722) and the added-variable-plot .gph files exist (gph/mfg_imppw_9007long_2sls1_av.gph, gph/mfg_imppw_9... | 4 file(s) |
| C10 | supporting | scalar | out of scope | No plan step targeted this claim; treated as out_of_scope (excluded from the score, not a failure): Appendix robustness dropping specific industries (steel/glass/cement, compute... | 0 file(s) |
| C11 | supporting | table | match | log/tab_ipw_pop.scsv reproduces Table 4 with 18 columns: cols 1-6 = Panel A (no controls), 7-12 = Panel B (regional controls), 13-18 = Panel C (full controls), across All/Colleg... | 2 file(s) |
| C12 | supporting | table | match | The produced Table 5 (log/tab_ipw_empl.scsv) matches the paper exactly. In the treatment row `d_t~eusch_pw` (the $1,000 import exposure per worker coefficient), Panel A log-coun... | 1 file(s) |
| C13 | headline | table | match | The evidence file log/tab_ipw_empl.scsv contains Table 5 panel B. In the d_t~eusch_pw ($1,000 import shock) row, the five share columns match the paper exactly: d_sh_em~_mfg = -... | 1 file(s) |
| C14 | supporting | scalar | match | log/tab_ipw_empl.scsv (Table 5 panel B) reports d_t~eusch_pw coefficients per education group. The noncollege nonmanufacturing employment-share coefficient (col 16, d_sh_empl_..... | 1 file(s) |
| C15 | supporting | table | match | The evidence file log/tab_ipw_wage.scsv reproduces Table 6 exactly. The d_t~eusch_pw (import exposure per worker) coefficient row reads -0.759/-0.892/-0.614 for all/male/female ... | 1 file(s) |
| C16 | supporting | table | match | The produced output file log/tab_ipw_mfgnmfg.scsv contains Table 7 with the change-in-average-log-wage coefficients on d_t~eusch_pw (Chinese import exposure per worker). Column ... | 1 file(s) |
| C17 | headline | table | match | The replicated Table 8 output at log/tab_ipw_trans.scsv reports coefficients on d_t~eusch_pw (the $1,000 Chinese import exposure regressor) that match the paper's reported value... | 2 file(s) |
| C18 | supporting | table | match | The evidence file log/tab_ipw_hhinc_pw.scsv (Table 9) reports coefficients on the import-exposure regressor (row 'd_t~eusch_pw'). Columns 1-6 are the percent-change specificatio... | 2 file(s) |
| C19 | supporting | table | partial | All five Table 10 output files were produced and their panel assignments confirmed from the do-file (do/czone_analysis_ipw_final.do, lines 284-290 d_tradex_usch_pw -> tab_expoff... | 12 file(s) |
| C20 | supporting | scalar_range | not attempted | No plan step targeted this claim; the planner marked it BLOCKED (counts as a reproducibility gap): Deadweight-loss-of-transfers welfare calculation ($13/$21; $22-44 range) apply... | 0 file(s) |
| C21 | supporting | scalar_range | not attempted | No plan step targeted this claim; the planner marked it BLOCKED (counts as a reproducibility gap): Deadweight-loss-of-nonparticipation welfare calculation ($43/$69; $87-137 rang... | 0 file(s) |
| C22 | supporting | table | match | The run produced log/import_stats_final.log (via do/import_stats_final.do), which summarizes trade levels in BN 2007 US$. US imports from China (l_totimp_usch): 1991=26.27168, 2... | 3 file(s) |
| C23 | supporting | scalar | match | The reproduced Figure 1 series in outputs/figure1_series.csv (produced by repro/table1_fig1.py from dta/figure1_data.dta) yields all four values. Import penetration (import_pene... | 4 file(s) |
| C24 | supporting | scalar | match | The reproduced Appendix Table 1 percentiles (outputs/apptab1_importgrowth.csv) give weighted percentiles of ten-year-equivalent d_tradeusch_pw (in kUSD/worker): for 1990 (1990-2... | 3 file(s) |
| C25 | supporting | scalar | out of scope | No plan step targeted this claim; treated as out_of_scope (excluded from the score, not a failure): External cited statistics (China's ~3/4 share of LMIC manufacturing-VA growth... | 0 file(s) |
| C26 | supporting | figure | match | Both the expected .gph file (gph/mfg_imppw_9007long_olsred_av.gph, reduced form) and its first-stage counterpart (gph/mfg_imppw_9007long_2sls1_av.gph) were produced, along with ... | 6 file(s) |
| C27 | supporting | scalar | match | The claim is a magnitude interpretation of Table 3 column 2: the column-2 (manufacturing-share-controlled) coefficient on import exposure times the 2000-2007 interquartile expos... | 1 file(s) |
| C28 | supporting | scalar | out of scope | No plan step targeted this claim; treated as out_of_scope (excluded from the score, not a failure): The distinctive number ($113.18, SE 41.53) is a re-estimate normalizing trans... | 0 file(s) |

## Flags

- 3 claim(s) marked out_of_scope (planner did not target them) — excluded from the score, not counted as failures. Score is over the 25 attempted/blocked claim(s).

## Replication Attempt

**Environment:** Python 3.12.8, GPU: NVIDIA RTX A6000 (x4, 49140 MiB each), Packages: pandas 3.0.5, numpy 2.5.2, scipy 1.18.1, linearmodels 7.0, statsmodels 0.14.6
**Duration:** 0s
**Steps completed:** 10/10

| Step | Description | Result | Duration |
|------|-------------|--------|----------|
| 1 | Set up environment, validate inputs, build reusable weighted-2SLS helper with state-clustered SEs. | Success | 0s |
| 2 | Table 3: six cumulative-control 2SLS specs of d_sh_empl_mfg on instrumented d_tradeusch_pw. | Success | 0s |
| 3 | Table 4 (population) and Table 5 (employment/unemployment/non-employment), fully controlled. | Success | 0s |
| 4 | Table 6 (wage changes) and Table 7 (mfg vs non-mfg), fully controlled. | Success | 0s |
| 5 | Table 8 (per-capita transfer receipts) and Table 9 (household income per capita), fully controlled. | Success | 0s |
| 6 | Table 10: alternative trade-exposure measures for the mfg employment share. | Success | 0s |
| 7 | Appendix Table 1 weighted import-growth percentiles + Appendix Table 4 preferred-spec OLS. | Success | 0s |
| 8 | Table 2 (2SLS by period) + falsification test on future exposure (preperiod file). | Success | 0s |
| 9 | Figure 2 first-stage and reduced-form regressions (+ added-variable plots). | Success | 0s |
| 10 | Table 1 trade statistics + Figure 1 time series. | Success | 0s |


## Limitations & Code Quality

**Fixes the replication agent applied to make the work run:** 1 (1 minor, 0 major, 0 critical). These are evidence about the provided code/paper, not the replication.

The fix burden is essentially negligible. Only a single fix was required: installing matplotlib, an omitted but extremely common plotting dependency, via a one-line package install with no code modifications. This is a minor, routine reproducibility issue that reflects an incomplete dependency manifest rather than any problem with the paper's algorithms, data, or methodology. No major or critical fixes were needed, suggesting the repository is in good reproducible shape and the published results are readily achievable from the provided code.

| # | Description | Severity | Impact |
|---|-------------|----------|--------|
| 1 | Installed matplotlib, which was missing from the initial dependency set, to render the added-variable plots. | minor | Indicates an incomplete dependency specification (e.g., matplotlib omitted from requirements/pyproject/environment file) rather than any flaw in the paper's methodology. Common in research repos where plotting dependencies are assumed to be present. Trivial to fix and does not undermine confidence in the reported results. |


---

*Report generated by Veritas Replication Agent*
