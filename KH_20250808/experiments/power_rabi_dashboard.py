"""
Dash module for **Power‑Rabi** calibration experiments
=====================================================
* 1‑D  : nb_of_pulses has length 1  –> line graph
* 2‑D  : nb_of_pulses length ≥ 2 –> Heat‑map (colormesh)
* Assumes up to 10+ qubits, using 2-column × N-row scrollable layout
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
# Common helper: H5 file loader
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
# 1. Data Loader
# -------------------------------------------------------------------
def load_prabi_data(folder):
    """
    folder (str | Path) → dict or None
    Returned dict contents:
      qubits, n, is_1d, nb_pulses, full_amp_mV, ds_raw, ds_fit,
      success, opt_amp_mV, vars_available (['I','Q','state'] existing items)
    """
    folder = os.path.normpath(folder)
    paths = {k: os.path.join(folder, k) for k in
             ("ds_raw.h5", "ds_fit.h5", "data.json", "node.json")}
    if not all(os.path.exists(p) for p in paths.values()):
        print(f"[load_prabi_data] missing files in {folder}")
        return None

    ds_raw = open_xr_dataset(paths["ds_raw.h5"])
    ds_fit = open_xr_dataset(paths["ds_fit.h5"])

    # Main common variables
    qubits = ds_raw["qubit"].values
    n_q    = len(qubits)

    nb_of_pulses = ds_raw["nb_of_pulses"].values          # (P,)   int
    is_1d        = len(nb_of_pulses) == 1

    full_amp_mV  = ds_raw["full_amp"].values * 1e3        # (q, A) or (A,)   mV
    success      = ds_fit["success"].values
    opt_amp_mV   = (ds_fit["opt_amp"].values * 1e3
                    if "opt_amp" in ds_fit else np.full(n_q, np.nan))

    # Check which data variables exist
    vars_avail = [v for v in ("I", "Q", "state") if v in ds_raw.data_vars]

    # JSONs are stored for debugging purposes only
    with open(paths["data.json"], "r", encoding="utf-8") as f:
        data_json = json.load(f)
    with open(paths["node.json"], "r", encoding="utf-8") as f:
        node_json = json.load(f)

    return dict(
        qubits=qubits, n=n_q, is_1d=is_1d, nb_pulses=nb_of_pulses,
        full_amp_mV=full_amp_mV, ds_raw=ds_raw, ds_fit=ds_fit,
        success=success, opt_amp_mV=opt_amp_mV, vars_available=vars_avail,
        data_json=data_json, node_json=node_json,
    )


# -------------------------------------------------------------------
# 2. Plot Generation
# -------------------------------------------------------------------
def create_prabi_plot(data, var_key):
    """
    var_key ∈ {'I','Q','state'}
    Returns: plotly.graph_objs.Figure
    """
    if not data or var_key not in data["vars_available"]:
        return go.Figure()

    qubits      = data["qubits"]
    n_q         = data["n"]
    nb_pulses   = data["nb_pulses"]
    is_1d       = data["is_1d"]
    ds_raw      = data["ds_raw"]
    full_amp_mv = data["full_amp_mV"]
    opt_amp_mv  = data["opt_amp_mV"]
    success     = data["success"]

    n_cols = 2
    n_rows = int(np.ceil(n_q / n_cols))

    fig = subplots.make_subplots(
        rows=n_rows, cols=n_cols,
        subplot_titles=[str(q) for q in qubits],
        vertical_spacing=0.03, horizontal_spacing=0.07,
    )

    show_cbar = True   # Show colorbar only for first heat‑map
    for idx, q in enumerate(qubits):
        r, c = divmod(idx, n_cols)
        row, col = r + 1, c + 1

        # x-axis: full_amp (per‑qubit or 1D)
        x_amp = (full_amp_mv[idx] if full_amp_mv.ndim == 2 else
                 full_amp_mv)  # (A,)

        da = ds_raw[var_key].sel(qubit=q)   # dims: amp_prefactor[, nb_of_pulses]
        if var_key in ("I", "Q"):
            da = da * 1e3                   # → mV

        if is_1d:
            y = da.squeeze().values
            fig.add_trace(
                go.Scatter(x=x_amp, y=y[::-1], mode="lines",
                           line=dict(width=1, color="blue"),
                           name="Data" if idx == 0 else None,
                           showlegend=(idx == 0)),
                row=row, col=col,
            )
            ylabel = {"I": "Rot I [mV]", "Q": "Rot Q [mV]",
                      "state": "State"}[var_key]
            fig.update_yaxes(title_text=ylabel if col == 1 else None,
                             row=row, col=col)

            # Optimal amplitude
            if success[idx] and not np.isnan(opt_amp_mv[idx]):
                fig.add_vline(x=opt_amp_mv[idx],
                              line=dict(color="red", dash="dash", width=1),
                              row=row, col=col)
                if idx == 0:
                    fig.add_trace(go.Scatter(
                        x=[None], y=[None], mode="lines",
                        line=dict(color="red", dash="dash", width=1),
                        name="opt. amp"), row=row, col=col)

        else:   # 2‑D colormesh
            z = da.transpose("nb_of_pulses", "amp_prefactor").values  # (P, A)

            hm = go.Heatmap(
                x=x_amp, y=nb_pulses, z=z[::-1],
                coloraxis="coloraxis", showscale=show_cbar,
            )
            fig.add_trace(hm, row=row, col=col)
            show_cbar = False   # Hide colorbar for subsequent subplots

            # Optimal amplitude line
            if success[idx] and not np.isnan(opt_amp_mv[idx]):
                fig.add_trace(
                    go.Scatter(
                        x=[opt_amp_mv[idx]] * len(nb_pulses),
                        y=nb_pulses,
                        mode="lines",
                        line=dict(color="white", dash="dash", width=1),
                        hoverinfo="skip",
                        showlegend=False,
                    ),
                    row=row, col=col,
                )

            fig.update_yaxes(title_text="# pulses" if col == 1 else None,
                             autorange="reversed", row=row, col=col)

        # Common X‑label
        if row == n_rows:
            fig.update_xaxes(title_text="Pulse amp. [mV]", row=row, col=col)

    title_var = {"I": "I‑quadrature", "Q": "Q‑quadrature",
                 "state": "State"}[var_key]
    fig.update_layout(
        title=f"Power Rabi – {title_var}",
        height=400 * n_rows,
        template="dashboard_dark",
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1),
        coloraxis=dict(
                colorbar=dict(title=var_key),
                colorscale="Viridis"  
    ),
    )
    return fig


# -------------------------------------------------------------------
# 3. Summary Table
# -------------------------------------------------------------------
def create_summary_table(data):
    rows = []
    for i, q in enumerate(data["qubits"]):
        ok = bool(data["success"][i])
        rows.append(
            html.Tr(
                [
                    html.Td(q),
                    html.Td(f"{data['opt_amp_mV'][i]:.3f}" if ok else "—"),
                    html.Td("✓" if ok else "✗"),
                ],
                className="table-success" if ok else "table-warning",
            )
        )
    head = html.Thead(html.Tr([html.Th("Qubit"),
                               html.Th("opt. amp [mV]"),
                               html.Th("Fit")]))
    return dbc.Table([head, html.Tbody(rows)],
                     bordered=True, striped=True, size="sm", responsive=True)


# -------------------------------------------------------------------
# 4. Layout
# -------------------------------------------------------------------
def create_prabi_layout(folder):
    uid = folder.replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_prabi_data(folder)
    if not data:
        return html.Div([dbc.Alert("Failed to load data", color="danger"),
                         html.Pre(folder)])

    default_var = data["vars_available"][0]
    init_fig = create_prabi_plot(data, default_var)

    var_options = [{"label": f" {v}", "value": v} for v in data["vars_available"]]

    return html.Div(
        [
            dcc.Store(id={"type": "prabi-data", "index": uid},
                      data={"folder": folder}),
            dbc.Row(dbc.Col(html.H3(f"Power Rabi – {Path(folder).name}")),
                    className="mb-3"),

            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.RadioItems(
                                id={"type": "prabi-var", "index": uid},
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
                    ), md=12
                ), className="mb-3"
            ),

            dbc.Row(
                [
                    dbc.Col(
                        dcc.Loading(
                            children=[dcc.Graph(id={"type": "prabi-plot",
                                                    "index": uid},
                                                figure=init_fig,
                                                config={"displayModeBar": True})],
                            type="default",
                        ), md=8
                    ),
                    dbc.Col(
                        [
                            html.H5("Summary"),
                            create_summary_table(data),
                            html.Hr(),
                            html.H6("Debug"),
                            html.Pre(f"Folder: {folder}\nQubits: {data['n']}"
                                     f"\n1‑D: {data['is_1d']}"),
                        ], md=4
                    ),
                ]
            ),
        ]
    )

# -------------------------------------------------------------------
# 5. Callbacks
# -------------------------------------------------------------------
def register_prabi_callbacks(app: dash.Dash):

    @app.callback(
        Output({"type": "prabi-plot", "index": MATCH}, "figure"),
        Input({"type": "prabi-var",  "index": MATCH}, "value"),
        State({"type": "prabi-data", "index": MATCH}, "data"),
    )
    def _update_plot(var_key, store):
        if not store:
            return go.Figure()
        data = load_prabi_data(store["folder"])
        return create_prabi_plot(data, var_key)
