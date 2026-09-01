"""Step 10: Table 1 trade statistics + Figure 1 time series.

(a) import_levels.dta / export_levels.dta: US imports-from-China and
    exports-to-China levels and growth 1991-2007, plus China's share of US
    manufacturing imports from low-income countries in 1991/2007.
(b) figure1_data.dta: China import-penetration (impr) and mfg-emp/pop series.
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'outputs')
os.makedirs(OUT, exist_ok=True)

imp = pd.read_stata(os.path.join(HERE, '..', 'dta', 'import_levels.dta'))
exp = pd.read_stata(os.path.join(HERE, '..', 'dta', 'export_levels.dta'))
fig1 = pd.read_stata(os.path.join(HERE, '..', 'dta', 'figure1_data.dta'))

# Aggregate trade totals (constant across industry rows -> take the value)
def v(df, col):
    return float(df[col].iloc[0])

# US imports from China (billion USD)
usch = {y: v(imp, f'l_totimp_usch_{y}') for y in (1991, 2000, 2007)}
# US imports from other low-income countries
uslw = {y: v(imp, f'l_totimp_uslw_{y}') for y in (1991, 2000, 2007)}
# US exports to China (billion USD)
usexp = {y: v(exp, f'l_totexp_usch_{y}') for y in (1992, 2000, 2007)}

# China share of low-income mfg imports = China / (China + other low-income)
china_share = {y: usch[y] / (usch[y] + uslw[y]) for y in (1991, 2000, 2007)}

rows = [
    {'series': 'US_imports_from_China_bnUSD',
     'y1991_1992': round(usch[1991], 3), 'y2000': round(usch[2000], 3),
     'y2007': round(usch[2007], 3), 'growth_2007_over_start': round(usch[2007] / usch[1991], 3)},
    {'series': 'US_exports_to_China_bnUSD',
     'y1991_1992': round(usexp[1992], 3), 'y2000': round(usexp[2000], 3),
     'y2007': round(usexp[2007], 3), 'growth_2007_over_start': round(usexp[2007] / usexp[1992], 3)},
    {'series': 'China_share_of_lowincome_imports',
     'y1991_1992': round(china_share[1991], 4), 'y2000': round(china_share[2000], 4),
     'y2007': round(china_share[2007], 4), 'growth_2007_over_start': np.nan},
]
t1 = pd.DataFrame(rows)
t1.to_csv(os.path.join(OUT, 'table1_trade.csv'), index=False)
print("=== Table 1 (trade statistics) ===")
print(t1.to_string(index=False))
# China's share of the GROWTH in low-income imports 2000->2007 (paper: 89%)
gshare = (usch[2007] - usch[2000]) / ((usch[2007] + uslw[2007]) - (usch[2000] + uslw[2000]))
print(f"\nChina share of low-income import GROWTH 2000-2007: {gshare:.3f} (paper ~0.89)")

# (b) Figure 1 series
f1 = fig1[['year', 'impr', 'cpsmanufemppop']].rename(
    columns={'impr': 'import_penetration_impr',
             'cpsmanufemppop': 'mfg_emp_pop_cpsman'})
f1.to_csv(os.path.join(OUT, 'figure1_series.csv'), index=False)
print("\n=== Figure 1 series (endpoints) ===")
print(f1[f1.year.isin([1991, 2000, 2007])].to_string(index=False))

# Regenerate figure1.png
m = (fig1.year > 1986) & (fig1.year < 2008)
d = fig1[m]
fig, ax1 = plt.subplots(figsize=(7, 5))
ax1.plot(d.year, d.impr, 'b-', label='China import penetration ratio')
ax1.set_xlabel('Year'); ax1.set_ylabel('Import penetration')
ax2 = ax1.twinx()
ax2.plot(d.year, d.cpsmanufemppop, 'r--', label='Manufacturing employment/Population')
ax2.set_ylabel('Manufacturing emp/pop')
lines = ax1.get_lines() + ax2.get_lines()
ax1.legend(lines, [l.get_label() for l in lines], loc='center left')
fig.tight_layout()
fig.savefig(os.path.join(OUT, 'figure1.png'), dpi=110)
plt.close(fig)
print("\nWrote outputs/table1_trade.csv, outputs/figure1_series.csv, outputs/figure1.png")
