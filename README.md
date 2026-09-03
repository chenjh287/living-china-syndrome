# The China Syndrome (Autor, Dorn and Hanson, AER 2013)

This repository holds the working directory of an automated replication and
extension of the paper, produced by [SAI](https://sai.science) agents. It is
the same file tree a signed-in user can browse in the run's workspace, and it
backs the public living-paper page:

**https://sai.science/econ/living-china-syndrome**

## What is here

- `run/` — the replication working directory: `analyze/` (extracted claims),
  `replication/` (the ported and executed codebase), `verify/` (per-claim
  verdicts and the replication score), `report/` (the run's own report), and
  `followup/` (the extension studies: a re-estimation of the paper's main
  claims on data through 2024-2026, and a refit of the paper's model to the
  combined evidence, each with its report, result card, and figures).
- `referee_report.md` — the referee-style report synthesized from the run.
- Some large input data files are omitted; where that happened,
  `run/LARGE_FILES_OMITTED.md` lists them.

## The paper

Autor, D., Dorn, D., and Hanson, G. (2013). The China Syndrome: Local Labor Market Effects of Import Competition in the United States. American Economic Review 103(6), 2121-2168.

Replication materials from David Dorn's data archive (ddorn.net). Files under `run/replication/codebase/` derive from those materials
(possibly modified by the replication agent) and remain under their original
authors' terms. Everything else in this repository is generated output from
the SAI pipeline.

## Caveats

Replication scores measure whether claims reproduce under our agents' effort,
not whether authors did anything wrong. Read the referee report's Notes and
the per-claim verdicts in `run/verify/verdicts.json` before quoting any
number.

## Data sources for the extension studies

The extension studies pulled fresh public data on August 23, 2026. In full:

- CEPII, BACI International Trade Database at the Product Level, HS92 revision, version 202601 (1995 to 2024), downloaded from cepii.fr.
- David Dorn's data archive for Autor, Dorn and Hanson (2013): the HS6-to-SIC87dd crosswalk, SIC87dd bilateral trade 1991 to 2014, County Business Patterns commuting-zone employment, and the county-to-commuting-zone crosswalk, downloaded from ddorn.net.
- Autor, Dorn and Hanson, replication archive for "On the Persistence of the China Shock" (Brookings Papers on Economic Activity, 2021), ddorn.net, used for validation only.
- U.S. Census Bureau, County Business Patterns, county files for 2000, 2007, 2012, 2019 and 2023.
- U.S. Census Bureau, Population Estimates Program, county population by age and sex (intercensal 2000 to 2010, Vintage 2020, and Vintage 2024).
- U.S. Bureau of Labor Statistics, Local Area Unemployment Statistics, county unemployment and labor force, retrieved via FRED, Federal Reserve Bank of St. Louis.
- U.S. Bureau of Labor Statistics, Quarterly Census of Employment and Wages, annual county files for 2000, 2007, 2012, 2019 and 2023.
- U.S. Bureau of Economic Analysis, CAINC35: Personal Current Transfer Receipts by County (1969 to 2022 vintage).
- Federal Reserve Bank of St. Louis, FRED series PCEPI, MANEMP and CNP16OV (deflator and national context).
- The paper's own replication package (workfile_china.dta and derived tables), reused for the original-period anchors and controls.

The theory update fetched no new data; it works entirely from the living update's artifacts and the replication package.
