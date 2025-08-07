# ======================================================================
#  drag_dashboard.py   (FULL / UPDATED)
# ======================================================================
"""
Dash module for **DRAG‑coefficient calibration** experiments
============================================================
* 2‑D sweep  : (#‑pulses , α‑prefactor) → state population  **or** I‑quadrature
* 1‑D view   : α‑prefactor → ⟨state⟩  or ⟨I⟩
* Summary    : per‑qubit optimal α  +  fit‑success
* Support  ≥10 qubits with 2‑column × N‑row scrollable layout
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
# Utility : safe xarray.open_dataset
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
# 1. Data Loading 
# ────────────────────────────────────────────────────────────────────
def load_drag_data(folder: str | Path) -> dict | None:
    """
    Returns dict (None on failure)
      qubits, n,
      alpha, nb_pulses,
      Z_heat      (q, P, A)   – heat‑map data (state prob. **or** I[mV])
      Z_avg       (q, A)      – pulse‑averaged
      z_label     str         – for axes / colorbar
      var_key     'state'|'I'
      opt_alpha, success,
      ds_raw, ds_fit, data_json, node_json
    """
    folder = os.path.normpath(str(folder))
    paths = {
        "ds_raw":  os.path.join(folder, "ds_raw.h5"),
        "ds_fit":  os.path.join(folder, "ds_fit.h5"),
        "data_js": os.path.join(folder, "data.json"),
        "node_js": os.path.join(folder, "node.json"),
    }
    if not all(os.path.exists(p) for p in paths.values()):
        print(f"[load_drag_data] missing files in {folder}")
        return None

    ds_raw = open_xr_dataset(paths["ds_raw"])
    ds_fit = open_xr_dataset(paths["ds_fit"])

    with open(paths["data_js"], "r", encoding="utf-8") as f:
        data_json = json.load(f)
    with open(paths["node_js"], "r", encoding="utf-8") as f:
        node_json = json.load(f)

    qubits = ds_raw["qubit"].values
    n_q    = len(qubits)

    # ── coordinates ────────────────────────────────────────────────
    alpha = (
        ds_raw["alpha"].values
        if "alpha" in ds_raw.coords
        else ds_raw["alpha_prefactor"].values
    )
    nb_pulses = ds_raw["nb_of_pulses"].values

    # ── variable detection : state  ↔  I ────────────────────────────
    if "I" in ds_raw.data_vars:
        var_key   = "I"
        z_raw     = ds_raw["I"].values * 1e3            # mV
        z_label   = "I [mV]"
    elif "state" in ds_raw.data_vars:
        var_key   = "state"
        z_raw     = ds_raw["state"].values              # probability (0‑1)
        z_label   = "State population"
    else:
        raise KeyError("Neither 'I' nor 'state' variable found in ds_raw")

    # Shape adapt (ensure (q,P,A))
    Z_heat = z_raw if z_raw.ndim == 3 else z_raw[np.newaxis, ...]

    # Averaged (1‑D)
    if "averaged_data" in ds_raw:
        Z_avg = ds_raw["averaged_data"].values
        if var_key == "I":
            Z_avg = Z_avg * 1e3
    else:
        Z_avg = Z_heat.mean(axis=1)

    # ── fit results ────────────────────────────────────────────────
    fit_results = data_json.get("fit_results", {})
    opt_alpha = np.full(n_q, np.nan, dtype=float)
    success   = np.full(n_q, False,  dtype=bool)
    for i, q in enumerate(qubits):
        info = fit_results.get(str(q), {})
        opt_alpha[i] = info.get("alpha", np.nan)
        success[i]   = bool(info.get("success", False))

    return dict(
        qubits=qubits, n=n_q,
        alpha=alpha, nb_pulses=nb_pulses,
        Z_heat=Z_heat, Z_avg=Z_avg,
        var_key=var_key, z_label=z_label,
        opt_alpha=opt_alpha, success=success,
        ds_raw=ds_raw, ds_fit=ds_fit,
        data_json=data_json, node_json=node_json,
    )


# ────────────────────────────────────────────────────────────────────
# 2‑A. Summary Figure
# ────────────────────────────────────────────────────────────────────
def create_summary_figure(d: dict) -> go.Figure:
    qbs = d["qubits"]
    colors = ["seagreen" if ok else "firebrick" for ok in d["success"]]

    fig = subplots.make_subplots(
        rows=2, cols=1, shared_xaxes=True,
        row_heights=[0.7, 0.3], vertical_spacing=0.03,
    )
    fig.add_trace(go.Bar(x=qbs, y=d["opt_alpha"],
                         marker_color=colors, name="optimal α"),
                  row=1, col=1)
    fig.add_hline(y=0, line=dict(color="black", dash="dash"), row=1, col=1)
    fig.add_trace(go.Bar(x=qbs, y=d["success"].astype(int),
                         marker_color=colors, name="fit OK"),
                  row=2, col=1)
    fig.update_yaxes(range=[-0.1, 1.1], row=2, col=1)
    fig.update_layout(
        title="DRAG Calibration – per‑qubit results",
        height=400, showlegend=False, template="dashboard_dark",
    )
    return fig


# ────────────────────────────────────────────────────────────────────
# 2‑B. Detailed Plot  (avg | heat)
# ────────────────────────────────────────────────────────────────────
def create_drag_plot(d: dict, mode: str = "avg") -> go.Figure:
    qbs      = d["qubits"]; n_q = d["n"]
    alpha    = d["alpha"];   nb_p = d["nb_pulses"]
    Z_avg    = d["Z_avg"];   Z_hm = d["Z_heat"]
    optα     = d["opt_alpha"]; success = d["success"]
    label_z  = d["z_label"]; var_key = d["var_key"]

    n_cols = 2
    n_rows = int(np.ceil(n_q / n_cols))
    fig = subplots.make_subplots(
        rows=n_rows, cols=n_cols,
        subplot_titles=[str(q) for q in qbs],
        vertical_spacing=0.03, horizontal_spacing=0.07,
    )

    show_cbar = True
    for i, q in enumerate(qbs):
        r, c = divmod(i, n_cols)
        row, col = r + 1, c + 1

        if mode == "avg":
            x = alpha if alpha.ndim == 1 else alpha[i]
            fig.add_trace(
                go.Scatter(x=x, y=Z_avg[i], mode="lines",
                           line=dict(color="blue", width=1),
                           name="Data" if i == 0 else None,
                           showlegend=(i == 0)),
                row=row, col=col,
            )
            if success[i] and not np.isnan(optα[i]):
                fig.add_vline(x=optα[i],
                              line=dict(color="red", dash="dash", width=1),
                              row=row, col=col)
                if i == 0:
                    fig.add_trace(go.Scatter(x=[None], y=[None], mode="lines",
                                             line=dict(color="red", dash="dash"),
                                             name="optimal α"),
                                  row=row, col=col)

        else:  # heat‑map
            x = alpha if alpha.ndim == 1 else alpha[i]
            z = Z_hm[i]                                  # (P, A)
            fig.add_trace(
                go.Heatmap(x=x, y=nb_p, z=z[::-1],
                           coloraxis="coloraxis",
                           showscale=show_cbar),
                row=row, col=col,
            )
            show_cbar = False
            if success[i] and not np.isnan(optα[i]):
                fig.add_vline(x=optα[i],
                              line=dict(color="white", dash="dash", width=1),
                              row=row, col=col)
            fig.update_yaxes(title_text="# pulses" if col == 1 else None,
                             autorange="reversed", row=row, col=col)

        # axis labels
        if row == n_rows:
            fig.update_xaxes(title_text="DRAG coefficient α",
                             row=row, col=col)
        if col == 1 and mode == "avg":
            fig.update_yaxes(title_text=f"⟨{label_z}⟩", row=row, col=col)

    title_mode = "Averaged" if mode == "avg" else "Heat‑map"
    fig.update_layout(
        title=f"DRAG Calibration – {title_mode} ({label_z})",
        height=280 * n_rows,
        template="dashboard_dark",
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1),
        coloraxis=dict(colorbar=dict(title=label_z), colorscale="Viridis") if mode == "heat" else None,
    )
    return fig
                  
# ────────────────────────────────────────────────────────────────────
# 3. Summary Table
# ────────────────────────────────────────────────────────────────────
def create_summary_table(d: dict):
    rows = []
    for i, q in enumerate(d["qubits"]):
        ok = bool(d["success"][i])
        rows.append(
            html.Tr(
                [
                    html.Td(q),
                    html.Td(f"{d['opt_alpha'][i]: .3f}" if ok else "—"),
                    html.Td("✓" if ok else "✗"),
                ],
                className="table-success" if ok else "table-warning",
            )
        )
    thead = html.Thead(html.Tr([html.Th("Qubit"),
                                html.Th("optimal α"),
                                html.Th("Fit")]))
    return dbc.Table([thead, html.Tbody(rows)],
                     bordered=True, striped=True, size="sm", responsive=True)


# ────────────────────────────────────────────────────────────────────
# 4. Layout
# ────────────────────────────────────────────────────────────────────
def create_drag_layout(folder: str | Path):
    uid = str(folder).replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_drag_data(folder)
    if not data:
        return html.Div([dbc.Alert("Failed to load data", color="danger"),
                         html.Pre(str(folder))])

    init_mode  = "avg"
    summary_fig = create_summary_figure(data)
    detail_fig  = create_drag_plot(data, init_mode)

    return html.Div(
        [
            dcc.Store(id={"type": "drag-data", "index": uid},
                      data={"folder": str(folder)}),

            dbc.Row(dbc.Col(html.H3(f"DRAG Calibration – {Path(folder).name}")),
                    className="mb-3"),

            dbc.Row(dbc.Col(
                dcc.Graph(figure=summary_fig, config={"displayModeBar": True}),
                md=12), className="mb-4"),

            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.RadioItems(
                                id={"type": "drag-view", "index": uid},
                                options=[
                                    {"label": " Averaged", "value": "avg"},
                                    {"label": " Heat‑map", "value": "heat"},
                                ],
                                value=init_mode,
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
                    ), md=12
                ), className="mb-3"
            ),

            dbc.Row(
                [
                    dbc.Col(
                        dcc.Loading(
                            children=[dcc.Graph(
                                id={"type": "drag-plot", "index": uid},
                                figure=detail_fig,
                                config={"displayModeBar": True})],
                            type="default",
                        ), md=8),
                    dbc.Col(
                        [
                            html.H5("Summary"),
                            create_summary_table(data),
                            html.Hr(),
                            html.H6("Debug"),
                            html.Pre(f"Folder: {folder}\nQubits: {data['n']}"
                                     f"\nVar: {data['var_key']}"),
                        ], md=4),
                ]
            ),
        ]
    )


# ────────────────────────────────────────────────────────────────────
# 5. Callbacks
# ────────────────────────────────────────────────────────────────────
def register_drag_callbacks(app: dash.Dash):
    @app.callback(
        Output({"type": "drag-plot", "index": MATCH}, "figure"),
        Input({"type": "drag-view", "index": MATCH}, "value"),
        State({"type": "drag-data", "index": MATCH}, "data"),
    )
    def _update_plot(view_mode, store):
        if not store:
            return go.Figure()
        d = load_drag_data(store["folder"])
        return create_drag_plot(d, view_mode)
