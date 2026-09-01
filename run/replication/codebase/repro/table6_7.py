"""Step 4: Table 6 (wage changes) and Table 7 (manufacturing vs non-manufacturing).

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


# ---- Table 6: wage changes ----
wage_outcomes = ['d_avg_lnwkwage', 'd_avg_lnwkwage_m', 'd_avg_lnwkwage_f',
                 'd_avg_lnwkwage_c', 'd_avg_lnwkwage_c_m', 'd_avg_lnwkwage_c_f',
                 'd_avg_lnwkwage_nc', 'd_avg_lnwkwage_nc_m', 'd_avg_lnwkwage_nc_f']
t6 = pd.DataFrame([fit(o) for o in wage_outcomes])
t6.to_csv(os.path.join(OUT, 'table6_wage.csv'), index=False)
print("=== Table 6 (wages) ===")
print(t6.to_string(index=False))

# ---- Table 7: mfg vs nmfg (counts then wages) ----
t7_outcomes = ['lnchg_no_empl_mfg', 'lnchg_no_empl_mfg_edu_c',
               'lnchg_no_empl_mfg_edu_nc', 'lnchg_no_empl_nmfg',
               'lnchg_no_empl_nmfg_edu_c', 'lnchg_no_empl_nmfg_edu_nc',
               'd_avg_lnwkwage_mfg', 'd_avg_lnwkwage_mfg_c',
               'd_avg_lnwkwage_mfg_nc', 'd_avg_lnwkwage_nmfg',
               'd_avg_lnwkwage_nmfg_c', 'd_avg_lnwkwage_nmfg_nc']
t7 = pd.DataFrame([fit(o) for o in t7_outcomes])
t7.to_csv(os.path.join(OUT, 'table7_mfgnmfg.csv'), index=False)
print("\n=== Table 7 (mfg vs nmfg) ===")
print(t7.to_string(index=False))
print("\nWrote outputs/table6_wage.csv and outputs/table7_mfgnmfg.csv")
