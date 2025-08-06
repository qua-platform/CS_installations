# ======================================================================
#  qspec_dashboard.py   
# ======================================================================
"""
Dash module for **Qubit Spectroscopy** experiments
==================================================
* Displays rotated‑I response vs RF frequency **or** vs detuning
* Overlays Lorentzian fit (res freq, width, π‑pulse amplitude)
* Scales to many qubits with 2‑column × N‑row subplots
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

# -------------------------------------------------------------------
# Safe xarray loading
# -------------------------------------------------------------------
def open_xr_dataset(path, engines=("h5netcdf", "netcdf4", None)):
    last_err = None
    for eng in engines:
        try:
            return xr.open_dataset(path, engine=eng)
        except Exception as e:
            last_err = e
    raise last_err

# -------------------------------------------------------------------
# 1. Data Loading
# -------------------------------------------------------------------
def load_qspec_data(folder):
    folder = os.path.normpath(folder)
    req = [Path(folder, f) for f in ("ds_raw.h5", "ds_fit.h5", "data.json", "node.json")]
    if not all(p.exists() for p in req):
        print(f"[load_qspec_data] missing file in {folder}")
        return None

    ds_raw = open_xr_dataset(req[0])
    ds_fit = open_xr_dataset(req[1])

    with open(req[2], "r", encoding="utf-8") as f:
        data_json = json.load(f)
    with open(req[3], "r", encoding="utf-8") as f:
        node_json = json.load(f)

    qubits   = ds_raw["qubit"].values if "qubit" in ds_raw else ds_fit["qubit"].values
    n_q      = len(qubits)
    success  = ds_fit["success"].values

    detuning_hz = ds_fit["detuning"].values             # 1D
    detuning_mhz = detuning_hz / 1e6

    full_freq_ghz = ds_fit["full_freq"].values / 1e9    # shape (n_q, N)
    I_rot_mv      = ds_fit["I_rot"].values * 1e3        # mV, same shape

    # fit params (shape n_q)
    amplitude  = ds_fit["amplitude"].values
    position   = ds_fit["position"].values
    width      = ds_fit["width"].values
    base_line  = ds_fit["base_line"].values
    res_freq   = ds_fit["res_freq"].values / 1e9        # GHz
    fwhm_mhz   = ds_fit["fwhm"].values / 1e6            # MHz
    x180_amp   = ds_fit["x180_amplitude"].values if "x180_amplitude" in ds_fit else np.full(n_q, np.nan)

    return dict(
        qubits=qubits, n=n_q, success=success,
        det_mhz=detuning_mhz, det_hz=detuning_hz,
        freq_ghz=full_freq_ghz, I_rot=I_rot_mv,
        amp=amplitude, pos=position, width=width, base_line=base_line,
        res_freq=res_freq, fwhm=fwhm_mhz, x180=x180_amp,
        ds_raw=ds_raw, ds_fit=ds_fit, data_json=data_json, node_json=node_json,
    )

# -------------------------------------------------------------------
# 2. Lorentzian Peak
# -------------------------------------------------------------------
def lorentzian_peak(x, A, center, width, offset):
    return offset + A * (1 / (1 + ((x - center) / width) ** 2))

# -------------------------------------------------------------------
# 3. Plot Generation
# -------------------------------------------------------------------
def create_qspec_plot(data, view="rf"):
    """view='rf' → RF frequency axis,  view='det' → Detuning axis + fit"""
    if not data:
        return go.Figure()

    n_cols = 2  # Changed from 1 to 2
    n_rows = int(np.ceil(data["n"] / n_cols))  # Calculate rows needed for 2 columns
    fig = subplots.make_subplots(rows=n_rows, cols=n_cols, shared_xaxes=False,
                                 subplot_titles=[f"{q}" for q in data["qubits"]],
                                 vertical_spacing=0.04)

    for i, q in enumerate(data["qubits"]):
        row = i // n_cols + 1  # Calculate row position
        col = i % n_cols + 1   # Calculate column position
        
        if view == "rf":
            x = data["freq_ghz"][i]
            y = data["I_rot"][i]
            fig.add_trace(go.Scatter(x=x, y=y, mode="lines",
                                     line=dict(color="blue", width=1),
                                     name="Data" if i == 0 else None,
                                     showlegend=(i == 0)),
                          row=row, col=col)
            fig.update_xaxes(title_text="RF frequency [GHz]" if row == n_rows else None, row=row, col=col)
            fig.update_yaxes(title_text="Rotated I [mV]", row=row, col=col)
        else:  # detuning
            x_det = data["det_mhz"]
            y_det = data["I_rot"][i]
            fig.add_trace(go.Scatter(x=x_det, y=y_det, mode="lines",
                                     line=dict(color="blue", width=1),
                                     name="Data" if i == 0 else None,
                                     showlegend=(i == 0)),
                          row=row, col=col)

            # fit
            if data["success"][i]:
                x_fit = data["det_hz"]
                offset_interp = np.interp(x_fit, data["det_hz"], data["base_line"][i])
                y_fit = lorentzian_peak(x_fit,
                                        data["amp"][i],
                                        data["pos"][i],
                                        data["width"][i]/2,      # HWHM
                                        offset_interp) * 1e3
                fig.add_trace(go.Scatter(x=x_fit/1e6, y=y_fit, mode="lines",
                                         line=dict(color="red", dash="dash"),
                                         name="Fit" if i == 0 else None,
                                         showlegend=(i == 0)),
                              row=row, col=col)

            fig.update_xaxes(title_text="Detuning [MHz]" if row == n_rows else None, row=row, col=col)
            fig.update_yaxes(title_text="Rotated I [mV]", row=row, col=col)

    title = "Qubit Spectroscopy – RF frequency" if view == "rf" else "Qubit Spectroscopy – Detuning / Fit"
    fig.update_layout(title=title, height=400*n_rows,  # Changed from 250 to 400
                      template="dashboard_dark",
                      legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
    return fig

# -------------------------------------------------------------------
# 4. Summary Table
# -------------------------------------------------------------------
def create_summary_table(data):
    rows = []
    for i, q in enumerate(data["qubits"]):
        ok = bool(data["success"][i])
        rows.append(
            html.Tr(
                [
                    html.Td(q),
                    html.Td(f"{data['res_freq'][i]:.4f}" if ok else "—"),
                    html.Td(f"{data['fwhm'][i]:.3f}"     if ok else "—"),
                    html.Td(f"{data['x180'][i]:.4f}"     if ok else "—"),
                    html.Td("✓" if ok else "✗"),
                ],
                className="table-success" if ok else "table-warning",
            )
        )
    thead = html.Thead(html.Tr([html.Th(h) for h in ["Qubit", "Res Freq [GHz]", "FWHM [MHz]", "π‑pulse amp", "Fit"]]))
    return dbc.Table([thead, html.Tbody(rows)], bordered=True, striped=True, size="sm", responsive=True)

# -------------------------------------------------------------------
# 5. Layout
# -------------------------------------------------------------------
def create_qspec_layout(folder):
    uid = folder.replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_qspec_data(folder)
    if not data:
        return html.Div([dbc.Alert("Failed to load data", color="danger"), html.Pre(folder)])

    init_fig = create_qspec_plot(data, "rf")
    return html.Div(
        [
            dcc.Store(id={"type": "qspec-data", "index": uid}, data={"folder": folder}),
            dbc.Row(dbc.Col(html.H3(f"Qubit Spectroscopy – {Path(folder).name}")), className="mb-3"),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.RadioItems(
                                id={"type": "qspec-view", "index": uid},
                                options=[
                                    {"label": " RF frequency", "value": "rf"},
                                    {"label": " Detuning + Fit", "value": "det"},
                                ],
                                value="rf",
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
                            children=[dcc.Graph(id={"type": "qspec-plot", "index": uid},
                                                figure=init_fig,
                                                config={"displayModeBar": True})],
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
                            html.Pre(f"Folder: {folder}\nQubits: {data['n']}"),
                        ],
                        md=4,
                    ),
                ]
            ),
        ]
    )

# -------------------------------------------------------------------
# 6. Callback Registration
# -------------------------------------------------------------------
def register_qspec_callbacks(app):
    @app.callback(
        Output({"type": "qspec-plot", "index": MATCH}, "figure"),
        Input({"type": "qspec-view",  "index": MATCH}, "value"),
        State({"type": "qspec-data",  "index": MATCH}, "data"),
    )
    def _update(view, store):
        if not store:
            return go.Figure()
        data = load_qspec_data(store["folder"])
        return create_qspec_plot(data, view)
