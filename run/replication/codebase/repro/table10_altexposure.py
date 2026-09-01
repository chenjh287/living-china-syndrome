"""Step 6: Table 10 -- alternative trade-exposure measures for mfg employment share.

d_sh_empl_mfg regressed on alternative exposure measures. All fully-controlled,
weighted by timepwt48, clustered on statefip.
"""
import os
import pandas as pd
from iv import iv2sls, ols, FULL_CONTROLS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'outputs')
os.makedirs(OUT, exist_ok=True)
df = pd.read_stata(os.path.join(HERE, '..', 'dta', 'workfile_china.dta'))

DEP = 'd_sh_empl_mfg'
rows = []

# (baseline) gross exposure -- Table 3 col-6 comparator
r = iv2sls(df, DEP, 'd_tradeusch_pw', ['d_tradeotch_pw_lag'], FULL_CONTROLS)
rows.append({'measure': 'gross_baseline', 'coef_on_exposure': round(r['coef'], 4),
             'se': round(r['se'], 4), 'n': r['n']})

# (a) domestic + international exposure
r = iv2sls(df, DEP, 'd_tradex_usch_pw', ['d_tradex_otch_pw_lag'], FULL_CONTROLS)
rows.append({'measure': 'dom_intl', 'coef_on_exposure': round(r['coef'], 4),
             'se': round(r['se'], 4), 'n': r['n']})

# (b) net-of-intermediate-inputs
r = iv2sls(df, DEP, 'd_tradeusch_netinput_pw',
           ['d_tradeotch_pw_lag', 'd_inputotch_pw_lag'], FULL_CONTROLS)
rows.append({'measure': 'net_intermediates', 'coef_on_exposure': round(r['coef'], 4),
             'se': round(r['se'], 4), 'n': r['n']})

# (c) net imports
r = iv2sls(df, DEP, 'd_netimpusch_pw',
           ['d_tradeotch_pw_lag', 'd_expotch_pw_lag'], FULL_CONTROLS)
rows.append({'measure': 'net_imports', 'coef_on_exposure': round(r['coef'], 4),
             'se': round(r['se'], 4), 'n': r['n']})

# (d) gravity-residual reduced-form OLS
r = ols(df, DEP, ['d_traderes_pw_lag'] + FULL_CONTROLS)
rows.append({'measure': 'gravity_residual',
             'coef_on_exposure': round(r['params']['d_traderes_pw_lag'], 4),
             'se': round(r['se']['d_traderes_pw_lag'], 4), 'n': r['n']})

# (e) factor content of net imports
r = iv2sls(df, DEP, 'd_nettradefactor_usch_io',
           ['d_tradefactor_otch_lag_io', 'd_expfactor_otch_lag_io'], FULL_CONTROLS)
rows.append({'measure': 'factor_content', 'coef_on_exposure': round(r['coef'], 4),
             'se': round(r['se'], 4), 'n': r['n']})

t10 = pd.DataFrame(rows)
t10.to_csv(os.path.join(OUT, 'table10_altexposure.csv'), index=False)
print("=== Table 10 (alternative exposure measures) ===")
print(t10.to_string(index=False))
print("\nWrote outputs/table10_altexposure.csv")
