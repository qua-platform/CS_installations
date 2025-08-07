# ======================================================================
#  t1_dashboard.py   
# ======================================================================
"""
Dash module for **T1 relaxation** calibration experiments
========================================================
* 1‑D sweep : Idle‑time [ns]  →  Readout amplitude (I / Q / |IQ|)
* Support multiple (≥10) qubits with 2-column × N-row scrollable layout
--------------------------------------------------------------------
"""
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
# Exponential decay
# ────────────────────────────────────────────────────────────────────
def decay_exp(t, a, offset, decay):
    """a*exp(t*decay) + offset  (decay<0 ⇒ decay)"""
    return a * np.exp(t * decay) + offset

# ────────────────────────────────────────────────────────────────────
# 1. Data Loading
# ────────────────────────────────────────────────────────────────────
def load_t1_data(folder):
    """
    Returns dict or None
      qubits, n, idle_time_ns, ds_raw, ds_fit,
      success, tau_ns, tau_err_ns,
      fit_a, fit_offset, fit_decay,
      vars_available, data_json, node_json
    """
    folder = os.path.normpath(folder)
    paths = {
        "ds_raw":  os.path.join(folder, "ds_raw.h5"),
        "ds_fit":  os.path.join(folder, "ds_fit.h5"),
        "data_js": os.path.join(folder, "data.json"),
        "node_js": os.path.join(folder, "node.json"),
    }
    if not all(os.path.exists(p) for p in paths.values()):
        print(f"[load_t1_data] missing files in {folder}")
        return None

    ds_raw = open_xr_dataset(paths["ds_raw"])
    ds_fit = open_xr_dataset(paths["ds_fit"])

    with open(paths["data_js"], "r", encoding="utf-8") as f:
        data_json = json.load(f)
    with open(paths["node_js"], "r", encoding="utf-8") as f:
        node_json = json.load(f)

    qubits    = ds_raw["qubit"].values
    n_q       = len(qubits)
    idle_time = ds_raw["idle_time"].values                   # ns

    success   = ds_fit["success"].values
    tau_ns    = ds_fit["tau"].values                         # ns
    tau_err   = ds_fit["tau_error"].values

    # ---------- fit parameters ----------
    if "fit_data" in ds_fit:
        fit_data = ds_fit["fit_data"]                        # dims: qubit, fit_vals
        fit_a      = fit_data.sel(fit_vals="a").values
        fit_offset = fit_data.sel(fit_vals="offset").values
        fit_decay  = fit_data.sel(fit_vals="decay").values
    else:   # fallback (individual variables)
        fit_a      = ds_fit["a"].values if "a" in ds_fit else np.full(n_q, np.nan)
        fit_offset = ds_fit["offset"].values if "offset" in ds_fit else np.full(n_q, np.nan)
        fit_decay  = ds_fit["decay"].values if "decay" in ds_fit else np.full(n_q, np.nan)

    # ---------- Data variable availability ----------
    vars_avail = [v for v in ("I", "Q") if v in ds_raw.data_vars]
    if all(v in vars_avail for v in ("I", "Q")):
        vars_avail.append("amp")    # |IQ|

    return dict(
        qubits=qubits, n=n_q, idle_time_ns=idle_time,
        ds_raw=ds_raw, ds_fit=ds_fit,
        success=success, tau_ns=tau_ns, tau_err_ns=tau_err,
        fit_a=fit_a, fit_offset=fit_offset, fit_decay=fit_decay,
        vars_available=vars_avail,
        data_json=data_json, node_json=node_json,
    )

# ────────────────────────────────────────────────────────────────────
# 2. Plot Generation
# ────────────────────────────────────────────────────────────────────
def create_t1_plot(data, var_key):
    """
    var_key ∈ {'I','Q','amp'}
    returns plotly.graph_objs.Figure
    """
    if not data or var_key not in data["vars_available"]:
        return go.Figure()

    qubits       = data["qubits"]
    n_q          = data["n"]
    t_ns         = data["idle_time_ns"]
    ds_raw       = data["ds_raw"]
    success      = data["success"]
    fit_a        = data["fit_a"]
    fit_offset   = data["fit_offset"]
    fit_decay    = data["fit_decay"]

    n_cols = 2
    n_rows = int(np.ceil(n_q / n_cols))

    fig = subplots.make_subplots(
        rows=n_rows,
        cols=n_cols,
        subplot_titles=[str(q) for q in qubits],
        vertical_spacing=0.08,
        horizontal_spacing=0.07,
    )

    for idx, q in enumerate(qubits):
        r, c = divmod(idx, n_cols)
        row, col = r + 1, c + 1

        I_raw = ds_raw["I"].sel(qubit=q).values
        Q_raw = ds_raw["Q"].sel(qubit=q).values if "Q" in ds_raw else np.zeros_like(I_raw)

        if var_key == "I":
            y = I_raw * 1e3                                            # mV
            ylabel = "Trans. amp I [mV]"
        elif var_key == "Q":
            y = Q_raw * 1e3
            ylabel = "Trans. amp Q [mV]"
        else:  # amp
            y = np.sqrt(I_raw**2 + Q_raw**2) * 1e3
            ylabel = "|IQ| [mV]"

        # Raw data
        fig.add_trace(
            go.Scatter(
                x=t_ns,
                y=y,
                mode="lines",
                line=dict(color="blue", width=1),
                name="Data" if idx == 0 else None,
                showlegend=(idx == 0),
            ),
            row=row, col=col,
        )

        # Fit curve
        if success[idx] and not np.isnan(fit_decay[idx]):
            y_fit = decay_exp(t_ns, fit_a[idx], fit_offset[idx], fit_decay[idx]) * 1e3
            fig.add_trace(
                go.Scatter(
                    x=t_ns,
                    y=y_fit,
                    mode="lines",
                    line=dict(color="red", dash="dash", width=1),
                    name="Fit" if idx == 0 else None,
                    showlegend=(idx == 0),
                ),
                row=row, col=col,
            )

        # Axis labels
        if row == n_rows:
            fig.update_xaxes(title_text="Idle time [ns]", row=row, col=col)
        if col == 1:
            fig.update_yaxes(title_text=ylabel, row=row, col=col)

    title_map = {"I": "I‑quadrature", "Q": "Q‑quadrature", "amp": "|IQ| magnitude"}
    fig.update_layout(
        title=f"T1 Relaxation – {title_map[var_key]}",
        height=350 * n_rows,
        template="dashboard_dark",
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1),
    )
    return fig

# ────────────────────────────────────────────────────────────────────
# 3. Summary Table
# ────────────────────────────────────────────────────────────────────
def create_summary_table(data):
    rows = []
    for i, q in enumerate(data["qubits"]):
        ok = bool(data["success"][i])
        rows.append(
            html.Tr(
                [
                    html.Td(q),
                    html.Td(f"{data['tau_ns'][i]/1e3: .1f}"    if ok else "—"),
                    html.Td(f"{data['tau_err_ns'][i]/1e3: .1f}" if ok else "—"),
                    html.Td("✓" if ok else "✗"),
                ],
                className="table-success" if ok else "table-warning",
            )
        )
    thead = html.Thead(html.Tr([html.Th(h) for h in
                                ["Qubit", "T1 [µs]", "Err [µs]", "Fit"]]))
    return dbc.Table([thead, html.Tbody(rows)],
                     bordered=True, striped=True, size="sm", responsive=True)

# ────────────────────────────────────────────────────────────────────
# 4. Layout
# ────────────────────────────────────────────────────────────────────
def create_t1_layout(folder):
    uid = folder.replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_t1_data(folder)
    if not data:
        return html.Div(
            [dbc.Alert("Failed to load data", color="danger"),
             html.Pre(folder)]
        )

    default_var = data["vars_available"][0]
    init_fig    = create_t1_plot(data, default_var)

    var_options = [{"label": f" {v.upper() if v!='amp' else '|IQ|'}", "value": v}
                   for v in data["vars_available"]]

    return html.Div(
        [
            dcc.Store(id={"type": "t1-data", "index": uid},
                      data={"folder": folder}),
            dbc.Row(
                dbc.Col(html.H3(f"T1 Relaxation – {Path(folder).name}")),
                className="mb-3",
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.RadioItems(
                                id={"type": "t1-var", "index": uid},
                                options=var_options,
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
                            children=[
                                dcc.Graph(
                                    id={"type": "t1-plot", "index": uid},
                                    figure=init_fig,
                                    config={"displayModeBar": True},
                                )
                            ],
                            type="default",
                        ),
                        md=8,
                    ),
                    dbc.Col(
                        [
                            html.H5("Summary"),
                            create_summary_table(data),
                            html.Hr(),
                            html.H6("Debug"),
                            html.Pre(
                                f"Folder: {folder}\nQubits: {data['n']}"
                            ),
                        ],
                        md=4,
                    ),
                ]
            ),
        ]
    )

# ────────────────────────────────────────────────────────────────────
# 5. Callbacks
# ────────────────────────────────────────────────────────────────────
def register_t1_callbacks(app: dash.Dash):
    @app.callback(
        Output({"type": "t1-plot", "index": MATCH}, "figure"),
        Input({"type": "t1-var",  "index": MATCH}, "value"),
        State({"type": "t1-data", "index": MATCH}, "data"),
    )
    def _update_plot(var_key, store):
        if not store:
            return go.Figure()
        data = load_t1_data(store["folder"])
        return create_t1_plot(data, var_key)
