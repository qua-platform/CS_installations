# ======================================================================
#  iq_dashboard.py
# ======================================================================
"""
Dash module for **IQ‑Discrimination / Readout‑Fidelity** analysis
=================================================================
Views  :
  • Confusion‑matrix  (2×2 per qubit)  
  • Rotated‑I histograms with dual thresholds  
  • Rotated‑IQ “blob” scatter (optional pagination)
All views share 2‑column × N‑row layout with automatic pagination.
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
# 0. Global settings (rows·cols, pagination, size)
# ────────────────────────────────────────────────────────────────────
N_COLS             = 2      # Common number of columns for all views
PER_PAGE           = 16     # Maximum qubits per page (2 cols × 8 rows)
PLOT_HEIGHT_UNIT = {        # Height per row [px]  ### TUNE HERE
    "conf": 360,            # confusion‑matrix
    "hist": 360,            # histogram
    "blob": 360,            # scatter (blob)
}
SUBPLOT_VSPACE     = 0.05   #   │ vertical spacing      ### TUNE HERE
SUBPLOT_HSPACE     = 0.07   #   └─horizontal spacing

# ────────────────────────────────────────────────────────────────────
# Common: Safe xarray.open_dataset
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
# 1. Data Loader
# ────────────────────────────────────────────────────────────────────
def load_iq_data(folder: str | Path) -> dict | None:
    """
    Returns dict (keys):
      qubits, n, ds_raw, ds_fit,
      success, readout_fidelity,
      gg, ge, eg, ee,
      Ig, Ie, Qg, Qe,
      rus_thr, ge_thr
    """
    folder = os.path.normpath(str(folder))
    paths = {
        "ds_raw":  os.path.join(folder, "ds_raw.h5"),
        "ds_fit":  os.path.join(folder, "ds_fit.h5"),
        "data_js": os.path.join(folder, "data.json"),
        "node_js": os.path.join(folder, "node.json"),
    }
    if not all(os.path.exists(p) for p in paths.values()):
        print(f"[load_iq_data] missing files in {folder}")
        return None

    ds_raw = open_xr_dataset(paths["ds_raw"])
    ds_fit = open_xr_dataset(paths["ds_fit"])
    with open(paths["data_js"], "r", encoding="utf-8") as f:
        data_json = json.load(f)
    with open(paths["node_js"], "r", encoding="utf-8") as f:
        node_json = json.load(f)

    qubits   = ds_fit["qubit"].values if "qubit" in ds_fit else ds_raw["qubit"].values
    n_q      = len(qubits)
    success  = ds_fit["success"].values if "success" in ds_fit else np.full(n_q, True)
    fidelity = ds_fit["readout_fidelity"].values if "readout_fidelity" in ds_fit else np.full(n_q, np.nan)

    gg = ds_fit["gg"].values; ge = ds_fit["ge"].values
    eg = ds_fit["eg"].values; ee = ds_fit["ee"].values

    Ig = ds_fit["Ig_rot"].values * 1e3
    Ie = ds_fit["Ie_rot"].values * 1e3
    Qg = ds_fit["Qg_rot"].values * 1e3 if "Qg_rot" in ds_fit else np.zeros_like(Ig)
    Qe = ds_fit["Qe_rot"].values * 1e3 if "Qe_rot" in ds_fit else np.zeros_like(Ie)

    rus_thr = ds_fit["rus_threshold"].values * 1e3
    ge_thr  = ds_fit["ge_threshold"].values * 1e3

    return dict(
        qubits=qubits, n=n_q,
        ds_raw=ds_raw, ds_fit=ds_fit,
        success=success, readout_fidelity=fidelity,
        gg=gg, ge=ge, eg=eg, ee=ee,
        Ig=Ig, Ie=Ie, Qg=Qg, Qe=Qe,
        rus_thr=rus_thr, ge_thr=ge_thr,
    )

# ────────────────────────────────────────────────────────────────────
# 1‑B. Data slicer for pagination
# ────────────────────────────────────────────────────────────────────
def slice_data_for_page(data: dict, page: int, per_page: int = PER_PAGE) -> dict:
    """Return new dict with only index portion for requested page (1‑based)"""
    start = (page - 1) * per_page
    stop  = min(page * per_page, data["n"])
    sel   = slice(start, stop)
    sliced = {k: (v[sel] if isinstance(v, np.ndarray) else v)
              for k, v in data.items()
              if isinstance(v, np.ndarray)}
    # Non‑array items remain as is
    for k, v in data.items():
        if k not in sliced:
            sliced[k] = v
    sliced["qubits"] = data["qubits"][sel]
    sliced["n"]      = len(sliced["qubits"])
    return sliced

# ────────────────────────────────────────────────────────────────────
# 2‑A. Confusion‑matrix plot  (2×N, enlarged number font)
# ────────────────────────────────────────────────────────────────────
def plotconfusion(data: dict) -> go.Figure:
    qbs = data["qubits"]; n_q = data["n"]
    n_rows = int(np.ceil(n_q / N_COLS))
    fig = subplots.make_subplots(
        rows=n_rows, cols=N_COLS,
        subplot_titles=[str(q) for q in qbs],
        vertical_spacing=SUBPLOT_VSPACE, horizontal_spacing=SUBPLOT_HSPACE,
    )
    for idx, q in enumerate(qbs):
        r, c = divmod(idx, N_COLS); row, col = r + 1, c + 1
        z = np.array([[data["gg"][idx], data["ge"][idx]],
                      [data["eg"][idx], data["ee"][idx]]])
        txt = np.vectorize(lambda x: f"{x*100:.1f}%")(z)
        fig.add_trace(
            go.Heatmap(
                z=z[::-1], text=txt[::-1], texttemplate="%{text}",
                textfont={"size": 18},                 
                colorscale="Greys", zmin=0, zmax=1,
                showscale=(idx == 0), coloraxis="coloraxis"),
            row=row, col=col,
        )
        fig.update_xaxes(showticklabels=False, title_text="Measured" if row == n_rows else None,
                         row=row, col=col)
        fig.update_yaxes(showticklabels=False, title_text="Prepared" if col == 1 else None,
                         row=row, col=col)

    fig.update_layout(
        coloraxis=dict(colorbar=dict(title="Prob.")),
        title="IQ Readout – Confusion Matrix",
        height=PLOT_HEIGHT_UNIT["conf"] * n_rows,  
        template="dashboard_dark",
    )
    return fig

# ────────────────────────────────────────────────────────────────────
# 2‑B. Histogram plot
# ────────────────────────────────────────────────────────────────────
def plothistogram(data: dict) -> go.Figure:
    qbs = data["qubits"]; n_q = data["n"]
    Ig, Ie = data["Ig"], data["Ie"]
    rus, ge_thr = data["rus_thr"], data["ge_thr"]
    n_rows = int(np.ceil(n_q / N_COLS))
    fig = subplots.make_subplots(
        rows=n_rows, cols=N_COLS,
        subplot_titles=[str(q) for q in qbs],
        vertical_spacing=SUBPLOT_VSPACE, horizontal_spacing=SUBPLOT_HSPACE,
    )
    for idx, q in enumerate(qbs):
        r, c = divmod(idx, N_COLS); row, col = r + 1, c + 1
        bins = np.linspace(min(Ig[idx].min(), Ie[idx].min()),
                           max(Ig[idx].max(), Ie[idx].max()), 90)
        fig.add_trace(go.Histogram(
            x=Ig[idx], nbinsx=len(bins)-1, name="|g⟩" if idx == 0 else None,
            marker_color="skyblue", opacity=0.7, showlegend=(idx == 0)),
            row=row, col=col)
        fig.add_trace(go.Histogram(
            x=Ie[idx], nbinsx=len(bins)-1, name="|e⟩" if idx == 0 else None,
            marker_color="lightsalmon", opacity=0.7, showlegend=(idx == 0)),
            row=row, col=col)
        fig.add_vline(x=rus[idx], line=dict(color="black", dash="dash"), row=row, col=col)
        fig.add_vline(x=ge_thr[idx], line=dict(color="red",   dash="dash"), row=row, col=col)
        if row == n_rows: fig.update_xaxes(title_text="I‑rot [mV]", row=row, col=col)
        if col == 1:      fig.update_yaxes(title_text="Counts",     row=row, col=col)

    fig.update_layout(
        barmode="overlay",
        title="IQ Readout – Rotated‑I Histograms",
        height=PLOT_HEIGHT_UNIT["hist"] * n_rows,
        template="dashboard_dark",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig

# ────────────────────────────────────────────────────────────────────
# 2‑C. Scatter (blob) plot
# ────────────────────────────────────────────────────────────────────
def plotblob(data: dict) -> go.Figure:
    qbs = data["qubits"]; n_q = data["n"]
    Ig, Ie, Qg, Qe = data["Ig"], data["Ie"], data["Qg"], data["Qe"]
    rus, ge_thr = data["rus_thr"], data["ge_thr"]
    n_rows = int(np.ceil(n_q / N_COLS))
    fig = subplots.make_subplots(
        rows=n_rows, cols=N_COLS,
        subplot_titles=[str(q) for q in qbs],
        vertical_spacing=SUBPLOT_VSPACE, horizontal_spacing=SUBPLOT_HSPACE,
    )
    for idx, q in enumerate(qbs):
        r, c = divmod(idx, N_COLS); row, col = r + 1, c + 1
        fig.add_trace(go.Scatter(
            x=Ig[idx], y=Qg[idx], mode="markers",
            marker=dict(color="skyblue", size=4, opacity=0.3),
            name="|g⟩" if idx == 0 else None, showlegend=(idx == 0)),
            row=row, col=col)
        fig.add_trace(go.Scatter(
            x=Ie[idx], y=Qe[idx], mode="markers",
            marker=dict(color="lightsalmon", size=4, opacity=0.3),
            name="|e⟩" if idx == 0 else None, showlegend=(idx == 0)),
            row=row, col=col)
        fig.add_vline(x=rus[idx], line=dict(color="black", dash="dash"), row=row, col=col)
        fig.add_vline(x=ge_thr[idx], line=dict(color="red",   dash="dash"), row=row, col=col)
        fig.update_yaxes(scaleanchor=f"x{idx+1}", scaleratio=1, row=row, col=col)
        if row == n_rows: fig.update_xaxes(title_text="I‑rot [mV]", row=row, col=col)
        if col == 1:      fig.update_yaxes(title_text="Q‑rot [mV]", row=row, col=col)

    fig.update_layout(
        title="IQ Readout – Rotated‑IQ Blob",
        height=PLOT_HEIGHT_UNIT["blob"] * n_rows,
        template="dashboard_dark",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig

# ────────────────────────────────────────────────────────────────────
# 2. Plot wrapper (mode + page)
# ────────────────────────────────────────────────────────────────────
def create_iq_plot(data: dict, mode: str, page: int = 1) -> go.Figure:
    if not data:
        return go.Figure()
    data_page = slice_data_for_page(data, page)
    if mode == "conf": return plotconfusion(data_page)
    if mode == "hist": return plothistogram(data_page)
    return plotblob(data_page)          # "blob"

# ────────────────────────────────────────────────────────────────────
# 3. Summary Table (based on all qubits)
# ────────────────────────────────────────────────────────────────────
def create_summary_table(data: dict):
    rows = []
    for i, q in enumerate(data["qubits"]):
        ok = bool(data["success"][i])
        rows.append(
            html.Tr(
                [
                    html.Td(q),
                    html.Td(f"{data['readout_fidelity'][i]: .1f} %" if ok else "—"),
                    html.Td("✓" if ok else "✗"),
                ],
                className="table-success" if ok else "table-warning",
            )
        )
    head = html.Thead(html.Tr([html.Th("Qubit"),
                               html.Th("Readout Fidelity"),
                               html.Th("Fit")]))
    return dbc.Table([head, html.Tbody(rows)],
                     bordered=True, striped=True, size="sm", responsive=True)

# ────────────────────────────────────────────────────────────────────
# 4. Layout
# ────────────────────────────────────────────────────────────────────
def create_iq_layout(folder: str | Path):
    uid  = str(folder).replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_iq_data(folder)
    if not data:
        return html.Div([dbc.Alert("Failed to load data", color="danger"),
                         html.Pre(str(folder))])

    n_pages = int(np.ceil(data["n"] / PER_PAGE))
    init_fig = create_iq_plot(data, "conf", page=1)

    # Pagination component
    page_selector = dbc.Pagination(
        id={"type": "iq-page", "index": uid},
        active_page=1, max_value=n_pages,
        fully_expanded=False, first_last=True, size="lg",
        className="my-2",
    ) if n_pages > 1 else html.Div()

    return html.Div(
        [
            dcc.Store(id={"type": "iq-data", "index": uid},
                      data={"folder": str(folder)}),

            # ── Title ────────────────────────────────────────────
            dbc.Row(dbc.Col(html.H3(f"IQ Discrimination – {Path(folder).name}")),
                    className="mb-3"),

            # ── View selection + Page selection ─────────────────
            dbc.Row(
                dbc.Col(
                    dbc.Row([
                        dbc.Col(page_selector, width="auto"),
                        dbc.Col(
                            dcc.RadioItems(
                                id={"type": "iq-view", "index": uid},
                                options=[
                                    {"label": " Confusion Mtx", "value": "conf"},
                                    {"label": " Histogram",     "value": "hist"},
                                    {"label": " Scatter (blob)", "value": "blob"},
                                ],
                                value="conf",
                                inline=True,
                                className="dark-radio",
                                inputStyle={
                                    "margin-right": "8px",
                                    "margin-left":  "20px",
                                    "transform":    "scale(1.2)",
                                    "accentColor":  "#003366",
                                }
                            ),
                            width="auto"
                        ),
                    ], className="align-items-center g-2"),
                ),
                className="mb-3",
            ),

            # ── Graph + Summary ─────────────────────────────────
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Loading(
                            children=[
                                dcc.Graph(
                                    id={"type": "iq-plot", "index": uid},
                                    figure=init_fig,
                                    config={"displayModeBar": True},
                                )
                            ],
                            type="default",
                        ), md=8),
                    dbc.Col(
                        [
                            html.H5("Summary"),
                            create_summary_table(data),
                            html.Hr(),
                            html.H6("Debug"),
                            html.Pre(f"Folder: {folder}\nQubits: {data['n']}\nPages: {n_pages}"),
                        ], md=4),
                ]
            ),
        ]
    )

# ────────────────────────────────────────────────────────────────────
# 5. Callbacks (update figure when view or page changes)
# ────────────────────────────────────────────────────────────────────
def register_iq_callbacks(app: dash.Dash):
    @app.callback(
        Output({"type": "iq-plot", "index": MATCH}, "figure"),
        Input({"type": "iq-view",  "index": MATCH}, "value"),
        Input({"type": "iq-page",  "index": MATCH}, "active_page"),
        State({"type": "iq-data",  "index": MATCH}, "data"),
    )
    def updateplot(view_mode, page, store):
        if not store:
            return go.Figure()
        data = load_iq_data(store["folder"])
        return create_iq_plot(data, view_mode, page or 1)
