"""Step 9: Figure 2 first-stage and reduced-form regressions.

Reimplements czone_plot_import_long_final.do on workfile_china_long.dta.
Also regenerates the added-variable plots (partialling out l_shind_manuf_cbp).
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from iv import ols

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'outputs')
os.makedirs(OUT, exist_ok=True)
df = pd.read_stata(os.path.join(HERE, '..', 'dta', 'workfile_china_long.dta'))

INSTR = 'd_tradeotch_pw_lag'
CTRL = 'l_shind_manuf_cbp'

rows = []
for label, dep in [('first_stage', 'd_tradeusch_pw'),
                   ('reduced_form', 'd_pct_manuf')]:
    r = ols(df, dep, [INSTR, CTRL])
    rows.append({'spec': label,
                 'coef_on_instrument': round(r['params'][INSTR], 4),
                 'robust_se': round(r['se'][INSTR], 4),
                 't_stat': round(r['tstat'][INSTR], 3),
                 'n': r['n']})
    print(f"{label}: coef={r['params'][INSTR]:.4f} se={r['se'][INSTR]:.4f} "
          f"t={r['tstat'][INSTR]:.2f} N={r['n']}")

pd.DataFrame(rows).to_csv(
    os.path.join(OUT, 'figure2_firststage_reducedform.csv'), index=False)
print("\nWrote outputs/figure2_firststage_reducedform.csv")


def wresid(y, X, w):
    """Weighted-OLS residuals of y on X (X includes constant)."""
    W = np.sqrt(w)
    Xw = X * W[:, None]
    yw = y * W
    beta, *_ = np.linalg.lstsq(Xw, yw, rcond=None)
    return y - X @ beta


# Added-variable plots: partial out CTRL (and constant) from both axes
d = df.dropna(subset=['d_tradeusch_pw', 'd_pct_manuf', INSTR, CTRL, 'timepwt48']).copy()
w = d['timepwt48'].to_numpy(float)
Z = np.column_stack([np.ones(len(d)), d[CTRL].to_numpy(float)])
x_res = wresid(d[INSTR].to_numpy(float), Z, w)

for label, dep, ylab, title in [
    ('firststage', 'd_tradeusch_pw',
     'Change in Import Exposure per Worker (kUSD)', 'First Stage Regression, 1990-2007'),
    ('reducedform', 'd_pct_manuf',
     'Change % Manufacturing Emp in Working Age Pop',
     'Change in Manufacturing Emp by Commuting Zone, 1990-2007')]:
    y_res = wresid(d[dep].to_numpy(float), Z, w)
    slope = np.polyfit(x_res, y_res, 1, w=np.sqrt(w))[0]
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.scatter(x_res, y_res, s=10, alpha=0.5)
    xs = np.linspace(x_res.min(), x_res.max(), 100)
    b = np.polyfit(x_res, y_res, 1, w=np.sqrt(w))
    ax.plot(xs, np.polyval(b, xs), 'r-', lw=2, label=f'slope={slope:.3f}')
    ax.set_xlabel('Chg in Predicted Import Exposure per Worker (kUSD)')
    ax.set_ylabel(ylab)
    ax.set_title(title)
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, f'fig2_{label}_av.png'), dpi=110)
    plt.close(fig)
    print(f"AV plot fig2_{label}_av.png slope={slope:.4f}")

print("\nWrote outputs/fig2_firststage_av.png and outputs/fig2_reducedform_av.png")
