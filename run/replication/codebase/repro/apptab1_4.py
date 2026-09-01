"""Step 7: Appendix Table 1 descriptives + Appendix Table 4 OLS estimate.

(a) weighted percentiles of d_tradeusch_pw by year (Stata summ, detail);
(b) fully-controlled OLS of d_sh_empl_mfg on d_tradeusch_pw.
"""
import os
import pandas as pd
from iv import ols, wpercentile, FULL_CONTROLS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'outputs')
os.makedirs(OUT, exist_ok=True)
df = pd.read_stata(os.path.join(HERE, '..', 'dta', 'workfile_china.dta'))

# (a) Appendix Table 1: weighted percentiles of d_tradeusch_pw by year
rows = []
for yr in (1990, 2000):
    sub = df[df['yr'] == yr]
    p25 = wpercentile(sub['d_tradeusch_pw'], sub['timepwt48'], 25)
    p50 = wpercentile(sub['d_tradeusch_pw'], sub['timepwt48'], 50)
    p75 = wpercentile(sub['d_tradeusch_pw'], sub['timepwt48'], 75)
    rows.append({'year': yr, 'p25': round(p25, 4), 'p50': round(p50, 4),
                 'p75': round(p75, 4), 'iqr': round(p75 - p25, 4)})
    print(f"yr={yr}: p25={p25:.4f} p50={p50:.4f} p75={p75:.4f} IQR={p75-p25:.4f}")
imp = pd.DataFrame(rows)
imp.to_csv(os.path.join(OUT, 'apptab1_importgrowth.csv'), index=False)

# (b) Appendix Table 4: fully-controlled OLS of mfg share on gross exposure
r = ols(df, 'd_sh_empl_mfg', ['d_tradeusch_pw'] + FULL_CONTROLS)
coef = r['params']['d_tradeusch_pw']
se = r['se']['d_tradeusch_pw']
print(f"\nAppendix Table 4 OLS: coef={coef:.4f} se={se:.4f} N={r['n']}")
pd.DataFrame([{'outcome': 'd_sh_empl_mfg', 'coef_d_tradeusch_pw': round(coef, 4),
               'se': round(se, 4), 'n': r['n']}]).to_csv(
    os.path.join(OUT, 'apptab4_ols.csv'), index=False)
print("\nWrote outputs/apptab1_importgrowth.csv and outputs/apptab4_ols.csv")
