# ======================================================================
#  ramsey_dashboard.py   (FULL / FIXED)
# ======================================================================
"""
Dash module for **Ramsey (T2*)** calibration experiments
========================================================
* Raw data : state (or I/Q) vs idle‑time, detuning_signs = ±1
* Fit      : exp‑cos(2πf t + φ) · exp(‑t/τ)
* Support ≥10 qubits with 2-column × N-row scrollable layout
--------------------------------------------------------------------
"""
from __future__ import annotations
import dash
from dash import dcc, html, Input, Output, State, MATCH
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.subplots as subplots
import xarray as xr
import numpy as np
import json, os
from pathlib import Path

# ────────────────────────────────────────────────────────────────────
# Safe xarray open_dataset
# ────────────────────────────────────────────────────────────────────
def open_xr_dataset(path, engines=("h5netcdf", "netcdf4", None)):
    last_err = None
    for eng in engines:
        try:
            return xr.open_dataset(path, engine=eng)
        except Exception as e:
            last_err = e
    raise last_err

# ────────────────────────────────────────────────────────────────────
# Ramsey model: exp‑decay × cos
# ────────────────────────────────────────────────────────────────────
def exp_cos_gamma(t_ns, a, f_cyc_per_ns, phi_rad, offset, gamma_1_over_ns):
    """offset + a·exp(‑γt)·cos(2πf t + φ)"""
    return offset + a * np.exp(-t_ns * gamma_1_over_ns) * np.cos(
        2.0 * np.pi * f_cyc_per_ns * t_ns + phi_rad
    )

# ────────────────────────────────────────────────────────────────────
# 1. Data Loading
# ────────────────────────────────────────────────────────────────────
def load_ramsey_data(folder: str | Path) -> dict | None:
    folder = os.path.normpath(str(folder))
    paths = {
        "ds_raw":  os.path.join(folder, "ds_raw.h5"),
        "ds_fit":  os.path.join(folder, "ds_fit.h5"),
        "data_js": os.path.join(folder, "data.json"),
        "node_js": os.path.join(folder, "node.json"),
    }
    if not all(os.path.exists(p) for p in paths.values()):
        print(f"[load_ramsey_data] missing files in {folder}")
        return None

    ds_raw = open_xr_dataset(paths["ds_raw"])
    ds_fit = open_xr_dataset(paths["ds_fit"])

    with open(paths["data_js"], "r", encoding="utf-8") as f:
        data_json = json.load(f)
    with open(paths["node_js"], "r", encoding="utf-8") as f:
        node_json = json.load(f)

    qubits   = ds_raw["qubit"].values
    n_q      = len(qubits)
    t_ns     = ds_raw["idle_time"].values
    signs    = ds_raw["detuning_signs"].values

    success = ds_fit["success"].values if "success" in ds_fit else np.full(n_q, True)

    # fit parameters
    if "fit" in ds_fit:
        fit_da = ds_fit["fit"]          # dims: (qubit, detuning_signs, fit_vals)
        has_det_dim = True
    else:
        fit_da = None
        has_det_dim = False

    def _param(key):
        if fit_da is not None:
            return fit_da.sel(fit_vals=key).values
        return ds_fit[key].values

    f_cyc = _param("f")
    gamma = _param("decay")

    if has_det_dim:
        idx_plus = list(signs).index(+1) if +1 in signs else 0
        f_det_mhz = f_cyc[:, idx_plus] * 1e3
        tau_ns    = np.where(gamma[:, idx_plus] != 0, 1.0 / gamma[:, idx_plus], np.nan)
    else:
        f_det_mhz = f_cyc * 1e3
        tau_ns    = np.where(gamma != 0, 1.0 / gamma, np.nan)

    vars_avail = [v for v in ("state", "I", "Q") if v in ds_raw.data_vars]
    if all(v in vars_avail for v in ("I", "Q")):
        vars_avail.append("amp")

    return dict(
        qubits=qubits, n=n_q, idle_time_ns=t_ns, det_signs=signs,
        ds_raw=ds_raw, ds_fit=ds_fit, success=success,
        f_det_mhz=f_det_mhz, tau_ns=tau_ns,
        vars_available=vars_avail,
        data_json=data_json, node_json=node_json,
    )

# ────────────────────────────────────────────────────────────────────
# 2. Plot Generation
# ────────────────────────────────────────────────────────────────────
def create_ramsey_plot(data: dict, var_key: str) -> go.Figure:
    if not data or var_key not in data["vars_available"]:
        return go.Figure()

    qubits   = data["qubits"]
    n_q      = data["n"]
    t_ns     = data["idle_time_ns"]
    signs    = data["det_signs"]
    ds_raw   = data["ds_raw"]
    ds_fit   = data["ds_fit"]
    success  = data["success"]

    if "fit" in ds_fit:
        fit_da = ds_fit["fit"]
        has_det_dim = True
    else:
        fit_da = None
        has_det_dim = False

    def _p(key):
        if fit_da is not None:
            return fit_da.sel(fit_vals=key).values
        return ds_fit[key].values

    A_arr    = _p("a")
    f_arr    = _p("f")
    phi_arr  = _p("phi")
    off_arr  = _p("offset")
    gam_arr  = _p("decay")

    n_cols = 2
    n_rows = int(np.ceil(n_q / n_cols))
    fig = subplots.make_subplots(
        rows=n_rows, cols=n_cols,
        subplot_titles=[str(q) for q in qubits],
        vertical_spacing=0.03, horizontal_spacing=0.07,
    )

    color_map = {+1: "blue", -1: "red"}
    legend_done = {"+": False, "-": False, "fit": False}

    for idx, q in enumerate(qubits):
        r, c = divmod(idx, n_cols)
        row, col = r + 1, c + 1

        for sgn in signs:
            color = color_map.get(int(sgn), "gray")
            s_lbl = "+" if sgn == +1 else "-"          # ← ASCII sign
            # ── y data ──────────────────────────────
            if var_key == "state":
                y = ds_raw["state"].sel(qubit=q, detuning_signs=sgn).values
                ylabel = "State population"
            elif var_key == "I":
                y = ds_raw["I"].sel(qubit=q, detuning_signs=sgn).values * 1e3
                ylabel = "Rot I [mV]"
            elif var_key == "Q":
                y = ds_raw["Q"].sel(qubit=q, detuning_signs=sgn).values * 1e3
                ylabel = "Rot Q [mV]"
            else:
                I = ds_raw["I"].sel(qubit=q, detuning_signs=sgn).values
                Q = ds_raw["Q"].sel(qubit=q, detuning_signs=sgn).values
                y = np.sqrt(I**2 + Q**2) * 1e3
                ylabel = "|IQ| [mV]"

            fig.add_trace(
                go.Scatter(
                    x=t_ns, y=y,
                    mode="markers",
                    marker=dict(size=5, color=color),
                    name=f"Δ={s_lbl}" if not legend_done[s_lbl] else None,
                    showlegend=not legend_done[s_lbl],
                ),
                row=row, col=col,
            )
            legend_done[s_lbl] = True

            # ── Fit curve ───────────────────────────
            if success[idx]:
                if has_det_dim:
                    j = list(signs).index(sgn)
                    a, f_cyc, phi, offset, gamma = (
                        A_arr[idx, j], f_arr[idx, j], phi_arr[idx, j],
                        off_arr[idx, j], gam_arr[idx, j]
                    )
                else:
                    a, f_cyc, phi, offset, gamma = (
                        A_arr[idx], f_arr[idx], phi_arr[idx],
                        off_arr[idx], gam_arr[idx]
                    )

                if not np.isnan(gamma):
                    y_fit = exp_cos_gamma(t_ns, a, f_cyc, phi, offset, gamma)
                    if var_key in ("I", "Q", "amp"):
                        y_fit *= 1e3
                    fig.add_trace(
                        go.Scatter(
                            x=t_ns, y=y_fit,
                            mode="lines",
                            line=dict(color=color, dash="dash", width=1),
                            name="Fit" if not legend_done["fit"] else None,
                            showlegend=not legend_done["fit"],
                        ),
                        row=row, col=col,
                    )
                    legend_done["fit"] = True

        if row == n_rows:
            fig.update_xaxes(title_text="Idle time [ns]", row=row, col=col)
        if col == 1:
            fig.update_yaxes(title_text=ylabel, row=row, col=col)

    ttl_map = {"state": "State population",
               "I": "I‑quadrature", "Q": "Q‑quadrature", "amp": "|IQ| magnitude"}
    fig.update_layout(
        title=f"Ramsey (T2*) – {ttl_map[var_key]}",
        height=380 * n_rows,
        template="dashboard_dark",
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1),
    )
    return fig

# ────────────────────────────────────────────────────────────────────
# 3. Summary Table
# ────────────────────────────────────────────────────────────────────
def create_summary_table(data: dict):
    rows = []
    for i, q in enumerate(data["qubits"]):
        ok = bool(data["success"][i])
        tau_us = data["tau_ns"][i] / 1e3 if ok else np.nan
        freq_mhz = data["f_det_mhz"][i] if ok else np.nan
        rows.append(
            html.Tr(
                [
                    html.Td(q),
                    html.Td(f"{freq_mhz: .3f}" if ok else "—"),
                    html.Td(f"{tau_us: .2f}"   if ok else "—"),
                    html.Td("✓" if ok else "✗"),
                ],
                className="table-success" if ok else "table-warning",
            )
        )
    thead = html.Thead(
        html.Tr([html.Th("Qubit"), html.Th("Δf [MHz]"),
                 html.Th("T2* [µs]"), html.Th("Fit")])
    )
    return dbc.Table([thead, html.Tbody(rows)],
                     bordered=True, striped=True, size="sm", responsive=True)

# ────────────────────────────────────────────────────────────────────
# 4. Layout
# ────────────────────────────────────────────────────────────────────
def create_ramsey_layout(folder: str | Path):
    uid = str(folder).replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_ramsey_data(folder)
    if not data:
        return html.Div([dbc.Alert("Failed to load data", color="danger"),
                         html.Pre(str(folder))])

    default_var = data["vars_available"][0]
    init_fig = create_ramsey_plot(data, default_var)

    var_opts = [{"label": f" {('|IQ|' if v=='amp' else v.upper()) if v!='state' else 'State'}",
                 "value": v}
                for v in data["vars_available"]]

    return html.Div(
        [
            dcc.Store(id={"type": "ramsey-data", "index": uid},
                      data={"folder": str(folder)}),
            dbc.Row(dbc.Col(html.H3(f"Ramsey (T2*) – {Path(folder).name}")),
                    className="mb-3"),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.RadioItems(
                                id={"type": "ramsey-var", "index": uid},
                                options=var_opts,
                                value=default_var,
                                inline=True,
                                className="dark-radio",
                                inputStyle={
                                    "margin-right": "8px",
                                    "margin-left":  "20px",
                                    "transform":    "scale(1.2)",
                                    "accentColor":  "#003366",
                                }
                            )
                        )
                    ),
                    md=12,
                ),
                className="mb-3",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Loading(
                            children=[dcc.Graph(
                                id={"type": "ramsey-plot", "index": uid},
                                figure=init_fig,
                                config={"displayModeBar": True})],
                            type="default",
                        ), md=8),
                    dbc.Col(
                        [
                            html.H5("Summary"),
                            create_summary_table(data),
                            html.Hr(),
                            html.H6("Debug"),
                            html.Pre(f"Folder: {folder}\nQubits: {data['n']}"),
                        ], md=4),
                ]
            ),
        ]
    )

# ────────────────────────────────────────────────────────────────────
# 5. Callbacks
# ────────────────────────────────────────────────────────────────────
def register_ramsey_callbacks(app: dash.Dash):
    @app.callback(
        Output({"type": "ramsey-plot", "index": MATCH}, "figure"),
        Input({"type": "ramsey-var",  "index": MATCH}, "value"),
        State({"type": "ramsey-data", "index": MATCH}, "data"),
    )
    def _update_plot(var_key, store):
        if not store:
            return go.Figure()
        data = load_ramsey_data(store["folder"])
        return create_ramsey_plot(data, var_key)
