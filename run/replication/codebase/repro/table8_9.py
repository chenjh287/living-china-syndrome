"""Step 5: Table 8 (transfer receipts) and Table 9 (household income per capita).

All fully-controlled 2SLS, weighted by timepwt48, clustered on statefip.
"""
import os
import pandas as pd
from iv import iv2sls, FULL_CONTROLS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'outputs')
os.makedirs(OUT, exist_ok=True)
df = pd.read_stata(os.path.join(HERE, '..', 'dta', 'workfile_china.dta'))


def fit(dep):
    r = iv2sls(df, dep, 'd_tradeusch_pw', ['d_tradeotch_pw_lag'], FULL_CONTROLS)
    return {'outcome': dep, 'coef': round(r['coef'], 4),
            'se': round(r['se'], 4), 'n': r['n']}


# ---- Table 8: transfer receipts (log-change then dollar-level) ----
t8_log = ['lnchg_trans_totindiv_pc', 'lnchg_trans_taaimp_pc',
          'lnchg_trans_unemp_pc', 'lnchg_trans_ssaret_pc',
          'lnchg_trans_ssadis_pc', 'lnchg_trans_totmed_pc',
          'lnchg_trans_fedinc_pc']
t8_lvl = ['d_trans_totindiv_pc', 'd_trans_taaimp_pc', 'd_trans_unemp_pc',
          'd_trans_ssaret_pc', 'd_trans_ssadis_pc', 'd_trans_totmed_pc',
          'd_trans_fedinc_pc']
rows = []
for o in t8_log:
    r = fit(o); r['form'] = 'log_change'; rows.append(r)
for o in t8_lvl:
    r = fit(o); r['form'] = 'dollar_level'; rows.append(r)
t8 = pd.DataFrame(rows)[['form', 'outcome', 'coef', 'se', 'n']]
t8.to_csv(os.path.join(OUT, 'table8_trans.csv'), index=False)
print("=== Table 8 (transfers) ===")
print(t8.to_string(index=False))

# ---- Table 9: household income per capita (relative-change then dollar-level) ----
t9_rel = ['relchg_avg_hhincsum_pc_pw', 'relchg_avg_hhincwage_pc_pw',
          'relchg_avg_hhinctrans_pc_pw']
t9_lvl = ['d_avg_hhincsum_pc_pw', 'd_avg_hhincwage_pc_pw',
          'd_avg_hhinctrans_pc_pw']
rows = []
for o in t9_rel:
    r = fit(o); r['form'] = 'rel_change'; rows.append(r)
for o in t9_lvl:
    r = fit(o); r['form'] = 'dollar_level'; rows.append(r)
t9 = pd.DataFrame(rows)[['form', 'outcome', 'coef', 'se', 'n']]
t9.to_csv(os.path.join(OUT, 'table9_hhinc.csv'), index=False)
print("\n=== Table 9 (household income) ===")
print(t9.to_string(index=False))
print("\nWrote outputs/table8_trans.csv and outputs/table9_hhinc.csv")
