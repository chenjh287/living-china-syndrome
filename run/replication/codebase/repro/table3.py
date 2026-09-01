"""Step 2: Table 3 -- headline manufacturing-employment-share 2SLS.

Reimplements czone_analysis_ipw_final.do lines 119-126: six IV2SLS
specifications adding controls cumulatively.
"""
import os
import pandas as pd
from iv import iv2sls, REG_DUMMIES

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'outputs')
os.makedirs(OUT, exist_ok=True)

df = pd.read_stata(os.path.join(HERE, '..', 'dta', 'workfile_china.dta'))

SPECS = {
    'col1': ['t2'],
    'col2': ['l_shind_manuf_cbp', 't2'],
    'col3': ['l_shind_manuf_cbp'] + REG_DUMMIES + ['t2'],
    'col4': ['l_shind_manuf_cbp'] + REG_DUMMIES +
            ['l_sh_popedu_c', 'l_sh_popfborn', 'l_sh_empl_f', 't2'],
    'col5': ['l_shind_manuf_cbp'] + REG_DUMMIES +
            ['l_sh_routine33', 'l_task_outsource', 't2'],
    'col6': ['l_shind_manuf_cbp'] + REG_DUMMIES +
            ['l_sh_popedu_c', 'l_sh_popfborn', 'l_sh_empl_f',
             'l_sh_routine33', 'l_task_outsource', 't2'],
}

rows = []
for name, controls in SPECS.items():
    r = iv2sls(df, 'd_sh_empl_mfg', 'd_tradeusch_pw',
               ['d_tradeotch_pw_lag'], controls)
    rows.append({'spec': name,
                 'coef_d_tradeusch_pw': round(r['coef'], 4),
                 'se': round(r['se'], 4),
                 'first_stage_coef': round(r['first_stage_coef'], 4),
                 'n': r['n']})
    print(f"{name}: coef={r['coef']:.3f} se={r['se']:.3f} "
          f"first_stage={r['first_stage_coef']:.3f} N={r['n']}")

res = pd.DataFrame(rows)
res.to_csv(os.path.join(OUT, 'table3.csv'), index=False)
print("\nWrote outputs/table3.csv")

# col-2 coefficient scaled by 2000-2007 interquartile exposure range (~1.06)
col2_coef = res.loc[res.spec == 'col2', 'coef_d_tradeusch_pw'].iloc[0]
print(f"\ncol-2 coefficient (for interquartile differential): {col2_coef}")
print(f"75th-vs-25th differential (col2 x 1.06): {col2_coef * 1.06:.3f} pp")
print(f"headline col-6 estimate: {res.loc[res.spec=='col6','coef_d_tradeusch_pw'].iloc[0]}")
