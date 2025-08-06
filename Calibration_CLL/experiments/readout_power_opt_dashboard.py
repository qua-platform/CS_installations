# ======================================================================
#  readout_power_dashboard.py   (FULL / NEW FILE)
# ======================================================================
"""
Dash module for **Readout‑Power‑Optimization** experiments
=========================================================
* View‑1 : Assignment‑fidelity & non‑outlier vs relative‑power
* View‑2 : Confusion‑matrix (2×2 per qubit)
* View‑3 : IQ‑blob scatter (rotated Ig/Qg, Ie/Qe) + thresholds
--------------------------------------------------------------------
* ≥10 qubits support, 2 columns × N rows pagination (1 page = 8 qubits)
* Data structure : ds_raw.h5, ds_fit.h5, data.json, node.json (+ ds_iq_blobs.h5 optional)
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
# Global: layout/sizing
# ────────────────────────────────────────────────────────────────────
N_COLS = 2                   # All subplot column count
PER_PAGE = 16                # 2 columns × 8 rows
PLOT_H_UNIT = {              # Fixed height per row (px)  ── adjust if needed
    "assign": 340,
    "conf":   260,
    "blob":   360,
}
V_SPACE = 0.04               # Subplot vertical spacing
H_SPACE = 0.07               # Subplot horizontal spacing

# ────────────────────────────────────────────────────────────────────
# Safe xarray.open_dataset
# ────────────────────────────────────────────────────────────────────
def open_xr_dataset(path, engines=("h5netcdf", "netcdf4", None)):
    last = None
    for eng in engines:
        try:
            return xr.open_dataset(path, engine=eng)
        except Exception as e:
            last = e
    raise last

# ────────────────────────────────────────────────────────────────────
# 1. Data loader
# ────────────────────────────────────────────────────────────────────
def load_rpo_data(folder: str | Path) -> dict | None:
    """
    Return dict
      qubits, n,
      amp, fidelity, non_out, opt_amp,
      gg, ge, eg, ee,
      Ig, Ie, Qg, Qe, rus_thr, ge_thr,
      readout_fidelity, success, has_iq
    """
    folder = os.path.normpath(str(folder))
    paths = {
        "ds_raw":  os.path.join(folder, "ds_raw.h5"),
        "ds_fit":  os.path.join(folder, "ds_fit.h5"),
        "data_js": os.path.join(folder, "data.json"),
        "node_js": os.path.join(folder, "node.json"),
        "ds_iq":   os.path.join(folder, "ds_iq_blobs.h5"),     # optional
    }
    if not all(os.path.exists(p) for p in paths.values() if p.endswith((".h5", ".json")) and "ds_iq" not in p):
        print(f"[load_rpo_data] missing core files in {folder}")
        return None

    ds_raw = open_xr_dataset(paths["ds_raw"])
    ds_fit = open_xr_dataset(paths["ds_fit"])
    with open(paths["data_js"], "r", encoding="utf-8") as f:
        data_json = json.load(f)

    # ── Common metadata ───────────────────────────────────────────────
    qubits = ds_raw["qubit"].values
    n_q    = len(qubits)
    success = ds_fit["success"].values if "success" in ds_fit else np.full(n_q, True)

    # ── 1) Assignment‑fidelity / non‑outliers ─────────────────
    amp = ds_raw["readout_amplitude"].values            # shape (q, A)
    fit_data = ds_fit["fit_data"].values                # (q, A, 2)
    fidelity   = fit_data[:, :, 0]
    non_out    = fit_data[:, :, 1]
    opt_amp    = ds_fit["optimal_amp"].values
    readout_fidelity = ds_fit["readout_fidelity"].values if "readout_fidelity" in ds_fit \
                       else np.nanmax(fidelity, axis=1)

    # ── 2) Confusion‑matrix ───────────────────────────────────
    if all(k in ds_fit for k in ("gg", "ge", "eg", "ee")):
        gg, ge, eg, ee = (ds_fit[k].values for k in ("gg", "ge", "eg", "ee"))
    else:
        # fallback → data_json["fit_results"][qubit]['confusion_matrix']
        gg = np.zeros(n_q); ge = np.zeros(n_q); eg = np.zeros(n_q); ee = np.zeros(n_q)
        for i, q in enumerate(qubits):
            cm = np.array(data_json["fit_results"][str(q)]["confusion_matrix"])
            gg[i], ge[i], eg[i], ee[i] = cm[0, 0], cm[0, 1], cm[1, 0], cm[1, 1]

    # ── 3) IQ‑blob (optional ds_iq_blobs.h5) ───────────────────
    has_iq = os.path.exists(paths["ds_iq"])
    if has_iq:
        ds_iq = open_xr_dataset(paths["ds_iq"])
        Ig = ds_iq["Ig_rot"].values * 1e3
        Ie = ds_iq["Ie_rot"].values * 1e3
        Qg = ds_iq["Qg_rot"].values * 1e3
        Qe = ds_iq["Qe_rot"].values * 1e3
        rus_thr = ds_iq["rus_threshold"].values * 1e3
        ge_thr  = ds_iq["ge_threshold"].values  * 1e3
    else:
        # Minimal size placeholder (skip scatter plot)
        Ig = Ie = Qg = Qe = rus_thr = ge_thr = None

    return dict(
        qubits=qubits, n=n_q,
        amp=amp, fidelity=fidelity, non_out=non_out, opt_amp=opt_amp,
        gg=gg, ge=ge, eg=eg, ee=ee,
        Ig=Ig, Ie=Ie, Qg=Qg, Qe=Qe, rus_thr=rus_thr, ge_thr=ge_thr,
        readout_fidelity=readout_fidelity, success=success, has_iq=has_iq,
    )

# ────────────────────────────────────────────────────────────────────
# 1‑B. Pagination helper
# ────────────────────────────────────────────────────────────────────
def slice_page(data: dict, page: int) -> dict:
    s = slice((page-1)*PER_PAGE, min(page*PER_PAGE, data["n"]))
    copy = {k: (v[s] if isinstance(v, np.ndarray) else v) for k, v in data.items()}
    copy["qubits"] = data["qubits"][s]
    copy["n"]      = len(copy["qubits"])
    return copy

# ────────────────────────────────────────────────────────────────────
# 2‑A. Assignment‑plot
# ────────────────────────────────────────────────────────────────────
def plot_assignment(d: dict) -> go.Figure:
    qbs, n_q = d["qubits"], d["n"]
    n_rows = int(np.ceil(n_q / N_COLS))
    fig = subplots.make_subplots(
        rows=n_rows, cols=N_COLS,
        subplot_titles=[str(q) for q in qbs],
        vertical_spacing=V_SPACE, horizontal_spacing=H_SPACE,
    )

    for i, q in enumerate(qbs):
        r, c = divmod(i, N_COLS); row, col = r+1, c+1
        x = d["amp"][i]
        fig.add_trace(go.Scatter(x=x, y=d["fidelity"][i], mode="lines",
                                 line=dict(color="blue", width=1.5),
                                 name="readout fidelity" if i==0 else None,
                                 showlegend=i==0),
                      row=row, col=col)
        fig.add_trace(go.Scatter(x=x, y=d["non_out"][i], mode="lines",
                                 line=dict(color="red", width=1.5),
                                 name="non‑outliers" if i==0 else None,
                                 showlegend=i==0),
                      row=row, col=col)
        fig.add_vline(x=d["opt_amp"][i], line=dict(color="black", dash="dash"),
                      row=row, col=col)
        if i==0:
            fig.add_trace(go.Scatter(x=[None], y=[None], mode="lines",
                                     line=dict(color="black", dash="dash"),
                                     name="optimal readout amplitude"),
                          row=row, col=col)
        if row==n_rows:
            fig.update_xaxes(title_text="Relative power", row=row, col=col)
        if col==1:
            fig.update_yaxes(title_text="Fidelity / outliers", row=row, col=col)
        fig.update_yaxes(range=[0.5, 1.02], row=row, col=col)

    fig.update_layout(
        title="Assignment fidelity and non‑outlier probability",
        height=PLOT_H_UNIT["assign"]*n_rows,
        template="dashboard_dark",
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1),
    )
    return fig

# ────────────────────────────────────────────────────────────────────
# 2‑B. Confusion‑matrix
# ────────────────────────────────────────────────────────────────────
def plot_confusion(d: dict) -> go.Figure:
    qbs, n_q = d["qubits"], d["n"]
    n_rows = int(np.ceil(n_q / N_COLS))
    fig = subplots.make_subplots(
        rows=n_rows, cols=N_COLS,
        subplot_titles=[str(q) for q in qbs],
        vertical_spacing=V_SPACE, horizontal_spacing=H_SPACE,
    )
    for i, q in enumerate(qbs):
        r, c = divmod(i, N_COLS); row, col = r+1, c+1
        z = np.array([[d["gg"][i], d["ge"][i]],
                      [d["eg"][i], d["ee"][i]]])
        txt = np.vectorize(lambda p:f"{p*100:.1f}%")(z)
        fig.add_trace(go.Heatmap(
            z=z[::-1], text=txt[::-1], texttemplate="%{text}",
            textfont=dict(size=18),
            coloraxis="coloraxis", showscale=i==0, zmin=0, zmax=1),
            row=row, col=col)
        fig.update_xaxes(showticklabels=False,
                         title_text="Measured" if row==n_rows else None,
                         row=row, col=col)
        fig.update_yaxes(showticklabels=False,
                         title_text="Prepared" if col==1 else None,
                         row=row, col=col)
    fig.update_layout(
        coloraxis=dict(colorbar=dict(title="Prob.")),
        title="g.s. and e.s. fidelity",
        height=PLOT_H_UNIT["conf"]*n_rows,
        template="dashboard_dark",
    )
    return fig

# ────────────────────────────────────────────────────────────────────
# 2‑C. IQ‑blob scatter
# ────────────────────────────────────────────────────────────────────
def plot_blob(d: dict) -> go.Figure:
    if not d["has_iq"]:
        return go.Figure(layout=dict(
            title="IQ data unavailable in this run – ds_iq_blobs.h5 not found"))
    qbs, n_q = d["qubits"], d["n"]
    n_rows = int(np.ceil(n_q / N_COLS))
    fig = subplots.make_subplots(
        rows=n_rows, cols=N_COLS,
        subplot_titles=[str(q) for q in qbs],
        vertical_spacing=V_SPACE, horizontal_spacing=H_SPACE,
    )
    for i, q in enumerate(qbs):
        all_I = np.concatenate([d["Ig"], d["Ie"]]) if d["has_iq"] else np.array([0])
        all_Q = np.concatenate([d["Qg"], d["Qe"]]) if d["has_iq"] else np.array([0])
        x_min, x_max = float(all_I.min())*1.05, float(all_I.max())*1.05
        y_min, y_max = float(all_Q.min())*1.05, float(all_Q.max())*1.05
        r, c = divmod(i, N_COLS); row, col = r+1, c+1
        fig.add_trace(go.Scatter(x=d["Ig"][i], y=d["Qg"][i], mode="markers",
                                 marker=dict(color="blue", size=3, opacity=0.25),
                                 name="Ground" if i==0 else None,
                                 showlegend=i==0),
                      row=row, col=col)
        fig.add_trace(go.Scatter(x=d["Ie"][i], y=d["Qe"][i], mode="markers",
                                 marker=dict(color="orange", size=3, opacity=0.25),
                                 name="Excited" if i==0 else None,
                                 showlegend=i==0),
                      row=row, col=col)
        fig.add_vline(x=d["rus_thr"][i], line=dict(color="black", dash="dash"),
                      row=row, col=col)
        fig.add_vline(x=d["ge_thr"][i], line=dict(color="red", dash="dash"),
                      row=row, col=col)
        if i==0:
            fig.add_trace(go.Scatter(x=[None], y=[None], mode="lines",
                                     line=dict(color="black", dash="dash"),
                                     name="RUS Threshold"), row=row, col=col)
            fig.add_trace(go.Scatter(x=[None], y=[None], mode="lines",
                                     line=dict(color="red", dash="dash"),
                                     name="Threshold"), row=row, col=col)
        fig.update_xaxes(range=[x_min, x_max], row=row, col=col)
        fig.update_yaxes(range=[y_min, y_max],
                         scaleanchor=f"x{i+1}", scaleratio=1,
                         row=row, col=col)
        if row==n_rows:
            fig.update_xaxes(title_text="I [mV]", row=row, col=col)
        if col==1:
            fig.update_yaxes(title_text="Q [mV]", row=row, col=col)
    fig.update_layout(
        title="g.s. and e.s. discriminators (rotated)",
        height=PLOT_H_UNIT["blob"]*n_rows,
        template="dashboard_dark",
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1),
    )
    return fig

# ────────────────────────────────────────────────────────────────────
# 2‑wrapper
# ────────────────────────────────────────────────────────────────────
def make_plot(data: dict, mode: str, page: int) -> go.Figure:
    if not data:
        return go.Figure()
    d_page = slice_page(data, page)
    if mode == "assign":
        return plot_assignment(d_page)
    if mode == "conf":
        return plot_confusion(d_page)
    return plot_blob(d_page)    # "blob"

# ────────────────────────────────────────────────────────────────────
# 3. Summary Table
# ────────────────────────────────────────────────────────────────────
def summary_table(d: dict):
    rows = []
    for i, q in enumerate(d["qubits"]):
        rows.append(
            html.Tr(
                [
                    html.Td(q),
                    html.Td(f"{d['opt_amp'][i]:.4f}"),
                    html.Td(f"{d['readout_fidelity'][i]*100: .1f}%"),
                    html.Td("✓" if d["success"][i] else "✗"),
                ],
                className="table-success" if d["success"][i] else "table-warning",
            )
        )
    head = html.Thead(html.Tr(
        [html.Th(h) for h in ("Qubit", "opt. amp", "Fidelity", "Fit")]))
    return dbc.Table([head, html.Tbody(rows)],
                     bordered=True, striped=True, size="sm", responsive=True)

# ────────────────────────────────────────────────────────────────────
# 4. Layout
# ────────────────────────────────────────────────────────────────────
def create_rpo_layout(folder: str | Path):
    uid = str(folder).replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_rpo_data(folder)
    if not data:
        return html.Div([dbc.Alert("Data loading failed", color="danger"), html.Pre(str(folder))])

    n_pages = int(np.ceil(data["n"]/PER_PAGE))
    init_fig = make_plot(data, "assign", 1)

    page_sel = dbc.Pagination(
        id={"type": "rpo-page", "index": uid},
        active_page=1, max_value=n_pages,
        fully_expanded=False, first_last=True, size="lg",
        className="my-2",
        style=None if n_pages > 1 else {"display": "none"},
    )

    return html.Div(
        [
            dcc.Store(id={"type": "rpo-data", "index": uid}, data={"folder": str(folder)}),
            dbc.Row(dbc.Col(html.H3(f"Readout Power Optimization – {Path(folder).name}")),
                    className="mb-3"),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                dcc.RadioItems(
                                    id={"type": "rpo-view", "index": uid},
                                    options=[
                                        {"label": " Assignment", "value": "assign"},
                                        {"label": " Confusion Mtx", "value": "conf"},
                                        {"label": " Scatter (blob)", "value": "blob"},
                                    ],
                                    value="assign",
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
                        ), md=8),
                    dbc.Col(page_sel, md=4,
                            className="d-flex align-items-center justify-content-end"),
                ], className="mb-3"
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Loading(
                            children=[dcc.Graph(id={"type": "rpo-plot", "index": uid},
                                                figure=init_fig,
                                                config={"displayModeBar": True})],
                            type="default",
                        ), md=8),
                    dbc.Col(
                        [
                            html.H5("Summary"),
                            summary_table(data),
                            html.Hr(),
                            html.H6("Debug"),
                            html.Pre(f"Folder: {folder}\nQubits: {data['n']}\nPages: {n_pages}"
                                     f"\nIQ‑data: {data['has_iq']}"),
                        ], md=4),
                ]
            ),
        ]
    )

# ────────────────────────────────────────────────────────────────────
# 5. Callback registration
# ────────────────────────────────────────────────────────────────────
def register_rpo_callbacks(app: dash.Dash):
    @app.callback(
        Output({"type": "rpo-plot", "index": MATCH}, "figure"),
        Input({"type": "rpo-view",  "index": MATCH}, "value"),
        Input({"type": "rpo-page",  "index": MATCH}, "active_page"),
        State({"type": "rpo-data",  "index": MATCH}, "data"),
    )
    def _update(view, page, store):
        if not store:
            return go.Figure()
        data = load_rpo_data(store["folder"])
        return make_plot(data, view, page or 1)
