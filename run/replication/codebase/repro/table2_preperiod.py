"""Step 8: Table 2 (2SLS by period) + falsification test.

Reimplements czone_analysis_preperiod_final.do on workfile_china_preperiod.dta.
Contemporaneous 2SLS by period, plus falsification on FUTURE exposure.
All weighted by timepwt48, clustered on statefip.
"""
import os
import pandas as pd
from iv import iv2sls

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'outputs')
os.makedirs(OUT, exist_ok=True)
df = pd.read_stata(os.path.join(HERE, '..', 'dta', 'workfile_china_preperiod.dta'))

rows = []


def add(label, data, endog, instr, controls):
    r = iv2sls(data, 'd_sh_empl_mfg', endog, instr, controls)
    rows.append({'spec': label, 'coef': round(r['coef'], 4),
                 'se': round(r['se'], 4), 'n': r['n']})
    print(f"{label}: coef={r['coef']:.3f} se={r['se']:.3f} N={r['n']}")


# Contemporaneous import exposure (claim C3)
add('1990-2000', df[df.yr == 1990], 'd_tradeusch_pw', ['d_tradeotch_pw_lag'], [])
add('2000-2007', df[df.yr == 2000], 'd_tradeusch_pw', ['d_tradeotch_pw_lag'], [])
add('stacked_1990-2007', df[df.yr >= 1990], 'd_tradeusch_pw',
    ['d_tradeotch_pw_lag'], ['t2000'])

# Falsification: pre-period mfg change on FUTURE exposure (claim C4)
add('falsification_1970-1980', df[df.yr == 1970], 'd_tradeusch_pw_future',
    ['d_tradeotch_pw_lag_future'], [])
add('falsification_1980-1990', df[df.yr == 1980], 'd_tradeusch_pw_future',
    ['d_tradeotch_pw_lag_future'], [])
add('falsification_stacked_1970-1990', df[(df.yr >= 1970) & (df.yr < 1990)],
    'd_tradeusch_pw_future', ['d_tradeotch_pw_lag_future'], ['t1980'])

t2 = pd.DataFrame(rows)
t2.to_csv(os.path.join(OUT, 'table2_byperiod.csv'), index=False)
print("\nWrote outputs/table2_byperiod.csv")
