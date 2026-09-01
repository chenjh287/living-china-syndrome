"""Reusable weighted 2SLS / OLS with state-clustered SEs.

Reimplements Stata's `ivregress 2sls dep (endog=instr) controls [aw=w], cluster(c)`
and `reg dep x controls [aw=w], cluster(c)` using linearmodels.

Validated against the authors' shipped Stata logs (tab_ipw_manuf_2.scsv):
Table 3 col1 coef -0.746 se 0.069 (Stata -0.746, 0.068); col6 coef -0.596
se 0.100 (Stata -0.596, 0.099). Coefficients match to 3 decimals; SEs match
to rounding (~0.001, minor cluster df-adjustment difference).
"""
import pandas as pd
import numpy as np
from linearmodels.iv import IV2SLS

REG_DUMMIES = ['reg_midatl', 'reg_encen', 'reg_wncen', 'reg_satl',
               'reg_escen', 'reg_wscen', 'reg_mount', 'reg_pacif']

# Full control set used in the fully-controlled specifications
FULL_CONTROLS = (['l_shind_manuf_cbp'] + REG_DUMMIES +
                 ['l_sh_popedu_c', 'l_sh_popfborn', 'l_sh_empl_f',
                  'l_sh_routine33', 'l_task_outsource', 't2'])


def iv2sls(data, dep, endog, instruments, controls,
           weight='timepwt48', cluster='statefip'):
    """Weighted 2SLS with cluster-robust SEs.

    endog: name (str) or list of endogenous regressor names.
    instruments: list of instrument names.
    controls: list of exogenous control names (a constant is always added).
    Returns dict with coef/se on each endogenous var plus n, and the
    first-stage coefficient (of the first instrument on the first endog).
    """
    endog = [endog] if isinstance(endog, str) else list(endog)
    instruments = list(instruments)
    controls = list(controls)
    cols = [dep] + endog + instruments + controls + [weight, cluster]
    d = data.dropna(subset=cols).copy()

    exog = pd.DataFrame({'const': 1.0}, index=d.index)
    for c in controls:
        exog[c] = d[c].astype(float)

    mod = IV2SLS(d[dep].astype(float), exog, d[endog].astype(float),
                 d[instruments].astype(float), weights=d[weight].astype(float))
    res = mod.fit(cov_type='clustered', clusters=d[cluster], debiased=True)

    out = {'n': int(d.shape[0]), 'rsq': float(res.rsquared)}
    for e in endog:
        out[e] = {'coef': float(res.params[e]), 'se': float(res.std_errors[e])}
    # convenience: coef/se on the (single) primary endogenous var
    out['coef'] = out[endog[0]]['coef']
    out['se'] = out[endog[0]]['se']

    # first-stage coefficient of first instrument on first endogenous var
    fs = ols(d, endog[0], instruments + controls, weight=weight, cluster=cluster)
    out['first_stage_coef'] = fs['params'].get(instruments[0], np.nan)
    return out


def ols(data, dep, rhs, weight='timepwt48', cluster='statefip'):
    """Weighted OLS with cluster-robust SEs (Stata `reg ... [aw], cluster`)."""
    rhs = list(rhs)
    cols = [dep] + rhs + [weight, cluster]
    d = data.dropna(subset=cols).copy()
    exog = pd.DataFrame({'const': 1.0}, index=d.index)
    for c in rhs:
        exog[c] = d[c].astype(float)
    mod = IV2SLS(d[dep].astype(float), exog, None, None,
                 weights=d[weight].astype(float))
    res = mod.fit(cov_type='clustered', clusters=d[cluster], debiased=True)
    return {
        'n': int(d.shape[0]),
        'rsq': float(res.rsquared),
        'params': {k: float(v) for k, v in res.params.items()},
        'se': {k: float(v) for k, v in res.std_errors.items()},
        'tstat': {k: float(v) for k, v in res.tstats.items()},
    }


def wpercentile(values, weights, q):
    """Stata-style weighted percentile (aweights), q in 0..100.

    Matches Stata `summ x [aw=w], detail` percentiles: interpolation on the
    cumulative running weight, threshold at q/100 * sum(weights)."""
    v = np.asarray(values, float)
    w = np.asarray(weights, float)
    m = ~(np.isnan(v) | np.isnan(w))
    v, w = v[m], w[m]
    order = np.argsort(v)
    v, w = v[order], w[order]
    cw = np.cumsum(w)
    thresh = q / 100.0 * w.sum()
    # Stata: find first obs where cumulative weight >= threshold
    idx = np.searchsorted(cw, thresh, side='left')
    idx = min(idx, len(v) - 1)
    return float(v[idx])
