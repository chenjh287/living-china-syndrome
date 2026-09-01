"""Step 3: Table 4 (population) and Table 5 (employment/unemployment/non-employment).

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


# ---- Table 4: population (fully-controlled row) ----
pop_outcomes = ['lnchg_popworkage', 'lnchg_popworkage_edu_c',
                'lnchg_popworkage_edu_nc', 'lnchg_popworkage_age1634',
                'lnchg_popworkage_age3549', 'lnchg_popworkage_age5064']
pop = pd.DataFrame([fit(o) for o in pop_outcomes])
pop.to_csv(os.path.join(OUT, 'table4_pop.csv'), index=False)
print("=== Table 4 (population) ===")
print(pop.to_string(index=False))

# ---- Table 5 ----
# Panel A: log employment-count outcomes
panelA = ['lnchg_no_empl_mfg', 'lnchg_no_empl_nmfg', 'lnchg_no_unempl',
          'lnchg_no_nilf', 'lnchg_no_ssadiswkrs']
# Panel B: population-share outcomes and edu splits
panelB = ['d_sh_empl_mfg', 'd_sh_empl_nmfg', 'd_sh_unempl', 'd_sh_nilf',
          'd_sh_ssadiswkrs',
          'd_sh_empl_mfg_edu_c', 'd_sh_empl_nmfg_edu_c', 'd_sh_unempl_edu_c',
          'd_sh_nilf_edu_c',
          'd_sh_empl_mfg_edu_nc', 'd_sh_empl_nmfg_edu_nc', 'd_sh_unempl_edu_nc',
          'd_sh_nilf_edu_nc']
# Overall net employment rate (all/college/noncollege)
overall = ['d_sh_empl', 'd_sh_empl_edu_c', 'd_sh_empl_edu_nc']

rows = []
for o in panelA:
    r = fit(o); r['panel'] = 'A_count'; rows.append(r)
for o in panelB:
    r = fit(o); r['panel'] = 'B_share'; rows.append(r)
for o in overall:
    r = fit(o); r['panel'] = 'net_empl_rate'; rows.append(r)
emp = pd.DataFrame(rows)[['panel', 'outcome', 'coef', 'se', 'n']]
emp.to_csv(os.path.join(OUT, 'table5_emp.csv'), index=False)
print("\n=== Table 5 (employment) ===")
print(emp.to_string(index=False))
print("\nWrote outputs/table4_pop.csv and outputs/table5_emp.csv")
