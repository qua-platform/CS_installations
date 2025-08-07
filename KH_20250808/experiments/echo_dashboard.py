import dash
from dash import dcc, html, Input, Output, State, MATCH, ClientsideFunction, ctx
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.subplots as subplots
import xarray as xr
import numpy as np
import json, os
import base64
import io
from pathlib import Path
from math import ceil
from scipy.optimize import curve_fit
from scipy import signal
import warnings

# --------------------------------------------------------------------
# Common helper: xarray open_dataset with multiple engine attempts
# --------------------------------------------------------------------
def open_xr_dataset(path, engines=("h5netcdf", "netcdf4", None)):
    """Try multiple engines to open xarray dataset"""
    last_err = None
    for eng in engines:
        try:
            return xr.open_dataset(path, engine=eng)
        except Exception as e:
            last_err = e
    raise last_err

# --------------------------------------------------------------------
# T2 Echo fitting functions
# --------------------------------------------------------------------
def decay_exp(t, a, offset, decay):
    """
    T2 Echo decay model: offset + a·exp(decay·t)
    Note: decay parameter is typically negative for exponential decay
    
    Parameters:
    - t: time (in same units as used during fitting)
    - a: amplitude
    - offset: baseline offset
    - decay: decay rate (typically negative, decay = -1/T2_echo)
    """
    return offset + a * np.exp(decay * t)

# --------------------------------------------------------------------
# 1. Data Loader for T2 Echo measurements
# --------------------------------------------------------------------
def load_t2_echo_data(folder):
    """Load T2 Echo data from folder"""
    folder = os.path.normpath(folder)
    paths = {
        "ds_raw": os.path.join(folder, "ds_raw.h5"),
        "ds_fit": os.path.join(folder, "ds_fit.h5"),
        "data_js": os.path.join(folder, "data.json"),
        "node_js": os.path.join(folder, "node.json"),
    }
    
    # Check if all files exist
    if not all(os.path.exists(p) for p in paths.values()):
        print(f"[load_t2_echo_data] missing file in {folder}")
        return None
    
    # Load datasets
    ds_raw = open_xr_dataset(paths["ds_raw"])
    ds_fit = open_xr_dataset(paths["ds_fit"])
    
    # Load JSON files
    with open(paths["data_js"], "r", encoding="utf-8") as f:
        data_json = json.load(f)
    with open(paths["node_js"], "r", encoding="utf-8") as f:
        node_json = json.load(f)
    
    # Extract basic data
    qubits = ds_raw["qubit"].values
    n_q = len(qubits)
    
    # Check the actual units of idle_time in the dataset
    # Based on the data structure analysis, idle_time values go up to 200000
    # and are stored as integers, suggesting they are in nanoseconds
    idle_time_ns = ds_raw["idle_time"].values.astype(float)  # Ensure float for calculations
    idle_time_us = idle_time_ns / 1000.0  # Convert to microseconds for display
    
    # Get I and Q data
    I_data = ds_raw["I"].values  # Shape: (n_qubits, n_time_points)
    Q_data = ds_raw["Q"].values  # Shape: (n_qubits, n_time_points)
    
    # Check original success flags from ds_fit
    original_success = ds_fit["success"].values if "success" in ds_fit else np.full(n_q, True)
    
    # Extract T2 echo and error from ds_fit (already calculated)
    T2_ns = ds_fit["T2_echo"].values if "T2_echo" in ds_fit else np.full(n_q, np.nan)
    T2_err = ds_fit["T2_echo_error"].values if "T2_echo_error" in ds_fit else np.full(n_q, np.nan)
    
    # T2_echo in ds_fit is already in nanoseconds, convert to microseconds
    # T2_echo = -1/decay (where decay is negative for exponential decay)
    T2_us = np.abs(T2_ns) * 1e-3  # Convert ns to μs, take absolute value
    T2_err_us = np.abs(T2_err) * 1e-3
    
    # Extract existing fit parameters if available
    fit_a = np.full(n_q, np.nan)
    fit_offset = np.full(n_q, np.nan)
    fit_decay = np.full(n_q, np.nan)
    
    if "fit_data" in ds_fit:
        fit_da = ds_fit["fit_data"]  # dims: qubit, fit_vals
        try:
            fit_a = fit_da.sel(fit_vals="a").values
            fit_offset = fit_da.sel(fit_vals="offset").values
            fit_decay = fit_da.sel(fit_vals="decay").values
        except:
            pass
    else:
        # Fallback: check if individual arrays exist
        fit_a = ds_fit["a"].values if "a" in ds_fit else fit_a
        fit_offset = ds_fit["offset"].values if "offset" in ds_fit else fit_offset
        fit_decay = ds_fit["decay"].values if "decay" in ds_fit else fit_decay
    
    # Store fit parameters for each qubit
    fit_results_custom = {}
    for i, q in enumerate(qubits):
        if original_success[i] and not np.isnan(fit_decay[i]):
            fit_results_custom[str(q)] = {
                'a': fit_a[i],
                'offset': fit_offset[i],
                'decay': fit_decay[i],
                't2_echo_us': T2_us[i],
                't2_error_us': T2_err_us[i],
                'r_squared': np.nan  # Not calculated in original fit
            }
        else:
            fit_results_custom[str(q)] = None
    
    # Calculate transmission amplitude in mV
    trans_amp = np.sqrt(I_data**2 + Q_data**2) * 1e3
    
    # Extract T2 echo values from original fit if available in JSON
    original_t2_echo = {}
    if "fit_results" in data_json:
        for q_str, fit_info in data_json["fit_results"].items():
            if "T2_echo" in fit_info:
                # Convert from seconds to microseconds
                original_t2_echo[q_str] = fit_info["T2_echo"] * 1e6
    
    # Check which variables are available
    vars_available = []
    for v in ("state", "I", "Q"):
        if v in ds_raw.data_vars:
            vars_available.append(v)
    if all(v in vars_available for v in ("I", "Q")):
        vars_available.append("amp")  # |IQ|
    
    return dict(
        qubits=qubits,
        n=n_q,
        idle_time_ns=idle_time_ns,
        idle_time_us=idle_time_us,
        trans_amp=trans_amp,
        I=I_data,
        Q=Q_data,
        original_success=original_success,
        success=original_success,  # Use original success flags
        t2_echo_us=T2_us,
        t2_error_us=T2_err_us,
        original_t2_echo=original_t2_echo,
        fit_params=fit_results_custom,
        fit_a=fit_a,
        fit_offset=fit_offset,
        fit_decay=fit_decay,
        vars_available=vars_available,
        data_json=data_json,
        node_json=node_json,
        ds_raw=ds_raw,
        ds_fit=ds_fit
    )

# --------------------------------------------------------------------
# 2. Plot Generation for T2 Echo measurements
# --------------------------------------------------------------------
def create_t2_echo_plots(
    data,
    n_cols: int = 2,
    fig_width: int = None,
    fig_height: int = None,
    vertical_spacing_px: int = 20,
    legend_x: float = 0.98,
    legend_y: float = 1.0,
    legend_xanchor: str = "right",
    legend_yanchor: str = "bottom",
    legend_orientation: str = "h",
    plot_variable: str = "I"  # Default to I quadrature
):
    """Create T2 Echo plots with fits for multiple qubits"""
    
    if not data:
        return go.Figure()
    
    n_q = data["n"]
    n_cols = max(1, min(n_cols, n_q))
    n_rows = ceil(n_q / n_cols)
    
    # Compute ideal height
    SUBPLOT_HEIGHT_PX = 300
    TITLE_MARGIN_PX = 80
    BOTTOM_MARGIN_PX = 50
    total_spacing_px = vertical_spacing_px * (n_rows - 1) if n_rows > 1 else 0
    ideal_height = (
        SUBPLOT_HEIGHT_PX * n_rows +
        total_spacing_px +
        TITLE_MARGIN_PX +
        BOTTOM_MARGIN_PX
    )
    effective_height = fig_height if fig_height else ideal_height
    
    # Compute Plotly fraction for vertical spacing
    if n_rows > 1 and effective_height > 0:
        content_height = effective_height - TITLE_MARGIN_PX - BOTTOM_MARGIN_PX
        vs_fraction = vertical_spacing_px / content_height
        max_allowed = 1.0 / (n_rows - 1)
        if vs_fraction > max_allowed:
            vs_fraction = max_allowed * 0.9
        vs_fraction = max(0.001, vs_fraction)
    else:
        vs_fraction = 0.02
    
    # Create subplot titles
    subplot_titles = [str(q) for q in data["qubits"]]
    
    fig = subplots.make_subplots(
        rows=n_rows, cols=n_cols,
        subplot_titles=subplot_titles,
        vertical_spacing=vs_fraction,
        horizontal_spacing=0.08
    )
    
    # Add traces for each qubit
    for idx, q in enumerate(data["qubits"]):
        r, c = divmod(idx, n_cols)
        r += 1
        c += 1
        
        x_us = data["idle_time_us"]
        
        # Get y data based on plot variable
        if plot_variable == "amp":
            y_data = data["trans_amp"][idx, :]
            ylabel = "|IQ| [mV]"
        elif plot_variable == "I":
            y_data = data["I"][idx, :] * 1e3
            ylabel = "I [mV]"
        elif plot_variable == "Q":
            y_data = data["Q"][idx, :] * 1e3
            ylabel = "Q [mV]"
        elif plot_variable == "state" and "state" in data.get("vars_available", []):
            y_data = data["ds_raw"]["state"].sel(qubit=q).values
            ylabel = "State"
        else:
            y_data = data["trans_amp"][idx, :]
            ylabel = "Signal"
        
        # Add raw data points
        fig.add_trace(
            go.Scatter(
                x=x_us,
                y=y_data,
                mode="lines+markers",
                marker=dict(size=3, color="blue"),
                line=dict(color="blue", width=1),
                name="Data",
                legendgroup="raw",
                showlegend=(idx == 0),  # Show legend only for first subplot
            ),
            row=r, col=c
        )
        
        # Add fit if successful and parameters are available
        if data["success"][idx] and not np.isnan(data["fit_decay"][idx]):
            # Use the existing fit parameters from ds_fit
            fit_a = data["fit_a"][idx]
            fit_offset = data["fit_offset"][idx]
            fit_decay = data["fit_decay"][idx]
            
            # Generate fit curve
            x_fit_ns = np.linspace(data["idle_time_ns"].min(), data["idle_time_ns"].max(), 500)
            x_fit_us = x_fit_ns / 1000.0  # Convert to microseconds for plotting
            
            # Calculate fit based on the variable being plotted
            # The fit parameters are from fitting the raw data (not scaled)
            y_fit_raw = decay_exp(x_fit_ns, fit_a, fit_offset, fit_decay)
            
            # Apply appropriate scaling based on plot variable
            if plot_variable == "state" and "state" in data.get("vars_available", []):
                y_fit = y_fit_raw
            elif plot_variable in ("I", "Q", "amp"):
                # Scale to mV for display
                y_fit = y_fit_raw * 1e3
            else:
                y_fit = y_fit_raw * 1e3
            
            # Debug: Check if fit is reasonable
            if idx == 0:  # Only print for first qubit to avoid clutter
                print(f"Debug - Qubit {q}:")
                print(f"  Fit params: a={fit_a:.6e}, offset={fit_offset:.6e}, decay={fit_decay:.6e}")
                print(f"  T2_echo = {data['t2_echo_us'][idx]:.1f} μs = {data['t2_echo_us'][idx]*1000:.1f} ns")
                print(f"  Expected decay = -1/T2_echo = {-1/(data['t2_echo_us'][idx]*1000):.6e}")
                print(f"  Time range: {x_fit_ns.min():.0f} to {x_fit_ns.max():.0f} ns")
                print(f"  Decay factor at end: exp({fit_decay:.6e} * {x_fit_ns.max():.0f}) = {np.exp(fit_decay * x_fit_ns.max()):.4f}")
            
            fig.add_trace(
                go.Scatter(
                    x=x_fit_us,
                    y=y_fit,
                    mode="lines",
                    line=dict(color="red", width=2, dash="solid"),
                    name="Fit",
                    legendgroup="fit",
                    showlegend=(idx == 0),  # Show legend only for first subplot
                ),
                row=r, col=c
            )
        
        # Add T2 echo value and success indicator as annotation
        if data["success"][idx]:
            t2_val = data["t2_echo_us"][idx]
            t2_err = data["t2_error_us"][idx]
            
            if not np.isnan(t2_val):
                # Format T2 echo with error
                if not np.isnan(t2_err) and t2_err > 0:
                    t2_str = f"T2 echo = {t2_val:.1f} ± {t2_err:.1f} μs"
                else:
                    t2_str = f"T2 echo = {t2_val:.1f} μs"
                
                # Add original T2 echo value if available
                original_str = ""
                if str(q) in data.get("original_t2_echo", {}):
                    orig_val = data["original_t2_echo"][str(q)]
                    original_str = f"\nOriginal: {orig_val:.1f} μs"
                
                annotation_text = f"{t2_str}{original_str}\nFit: ✓"
            else:
                annotation_text = "Fit parameters invalid\nFit: ✗"
            
            bg_color = "rgba(144, 238, 144, 0.3)"  # Light green
            border_color = "green"
        else:
            annotation_text = "Fit Failed\nFit: ✗"
            bg_color = "rgba(255, 200, 200, 0.3)"  # Light red
            border_color = "red"
        
        # Determine y position for annotation
        y_max = np.nanmax(y_data)
        y_min = np.nanmin(y_data)
        
        fig.add_annotation(
            text=annotation_text,
            xref=f"x{idx+1 if idx > 0 else ''}",
            yref=f"y{idx+1 if idx > 0 else ''}",
            x=x_us.max() - (x_us.max() - x_us.min()) * 0.02,
            y=y_min + (y_max - y_min) * 0.98,
            xanchor="right",
            yanchor="top",
            showarrow=False,
            font=dict(size=9),
            bgcolor=bg_color,
            bordercolor=border_color,
            borderwidth=1,
            align="left"
        )
        
        # Update axes labels
        fig.update_xaxes(
            title_text="Idle time [μs]" if r == n_rows else None,
            row=r, col=c,
            showgrid=True,
        )
        fig.update_yaxes(
            title_text=ylabel if c == 1 else None,
            row=r, col=c,
            showgrid=True,
        )
    
    # Global styling
    fig.update_xaxes(
        gridcolor="rgba(0,0,0,0.1)",
        griddash="solid",
        zerolinecolor="rgba(0,0,0,0.2)",
        zerolinewidth=0.5,
        ticks="outside",
        ticklen=4,
        showline=True,
        linecolor="black",
        mirror=False,
    )
    fig.update_yaxes(
        gridcolor="rgba(0,0,0,0.1)",
        griddash="solid",
        zerolinecolor="rgba(0,0,0,0.2)",
        zerolinewidth=0.5,
        ticks="outside",
        ticklen=4,
        showline=True,
        linecolor="black",
        mirror=False,
    )
    
    # Layout
    var_title_map = {
        "amp": "Amplitude |IQ|",
        "I": "I-quadrature",
        "Q": "Q-quadrature",
        "state": "State",
    }
    
    layout_args = dict(
        title=f"T2 Echo Measurement – {var_title_map.get(plot_variable, 'Signal')}",
        legend=dict(
            orientation=legend_orientation,
            yanchor=legend_yanchor,
            y=legend_y,
            xanchor=legend_xanchor,
            x=legend_x,
            bgcolor="rgba(255, 255, 255, 0.9)",
            bordercolor="black",
            borderwidth=1,
            font=dict(size=10),
        ),
        font=dict(size=11),
        title_font_size=14,
        autosize=True,
        margin=dict(
            t=TITLE_MARGIN_PX,
            b=BOTTOM_MARGIN_PX,
            l=80,
            r=60
        ),
        height=effective_height,
        showlegend=True,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )
    if fig_width:
        layout_args["width"] = fig_width
    
    fig.update_layout(**layout_args)
    return fig

# --------------------------------------------------------------------
# 3. Summary Table for T2 Echo measurements
# --------------------------------------------------------------------
def create_t2_echo_summary_table(data):
    """Create summary table showing T2 echo and fit success"""
    rows = []
    
    for i, q in enumerate(data["qubits"]):
        # Check both original and our fitting success
        original_ok = bool(data["original_success"][i])
        our_ok = bool(data["success"][i])
        
        t2_val = data["t2_echo_us"][i]
        t2_err = data["t2_error_us"][i]
        
        # Format T2 echo value
        if our_ok and not np.isnan(t2_val):
            if not np.isnan(t2_err) and t2_err > 0:
                t2_str = f"{t2_val:.1f} ± {t2_err:.1f}"
            else:
                t2_str = f"{t2_val:.1f}"
        else:
            t2_str = "—"
        
        # Add original value if available
        original_str = "—"
        if str(q) in data.get("original_t2_echo", {}):
            orig_val = data["original_t2_echo"][str(q)]
            original_str = f"{orig_val:.1f}"
        
        # Determine row class based on success
        if not original_ok:
            row_class = "table-danger"  # Original fit failed
            status = "✗ (original)"
        elif our_ok:
            row_class = "table-success"  # Both succeeded
            status = "✓"
        else:
            row_class = "table-warning"  # Our fit failed but original passed
            status = "⚠ (refit failed)"
        
        rows.append(
            html.Tr([
                html.Td(str(q)),
                html.Td(t2_str),
                html.Td(original_str),
                html.Td(status),
            ], className=row_class)
        )
    
    header = html.Thead(html.Tr([
        html.Th("Qubit"),
        html.Th("T2 Echo [μs]"),
        html.Th("Original [μs]"),
        html.Th("Fit Status")
    ]))
    
    return dbc.Table(
        [header, html.Tbody(rows)],
        bordered=True,
        striped=True,
        size="sm",
        responsive=True
    )

# --------------------------------------------------------------------
# 4. Layout + Callbacks for T2 Echo measurements
# --------------------------------------------------------------------
def create_t2_echo_layout(folder):
    """Create the complete layout for T2 Echo visualization"""
    uid = folder.replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_t2_echo_data(folder)
    
    if not data:
        return html.Div([
            dbc.Alert("Failed to load T2 Echo data", color="danger"),
            html.Pre(folder)
        ])
    
    default_height = 400 * ceil(data["n"] / 2)  # 2 columns by default
    init_fig = create_t2_echo_plots(data, n_cols=2, fig_height=default_height, plot_variable="I")
    
    # Build variable options based on available data
    var_options = []
    if "I" in data.get("vars_available", []):
        var_options.append({"label": "I-quadrature", "value": "I"})
    if "Q" in data.get("vars_available", []):
        var_options.append({"label": "Q-quadrature", "value": "Q"})
    if "amp" in data.get("vars_available", []):
        var_options.append({"label": "Amplitude |IQ|", "value": "amp"})
    if "state" in data.get("vars_available", []):
        var_options.append({"label": "State", "value": "state"})
    
    # Controls
    controls_accordion = dbc.Accordion(
        [
            dbc.AccordionItem(
                title="Display Options",
                children=[
                    dbc.Row([
                        dbc.Col(html.Div([
                            html.Label("Plot Variable"),
                            dcc.Dropdown(
                                id={"type": "t2e-var", "index": uid},
                                options=var_options,
                                value=var_options[0]["value"] if var_options else "I",
                                clearable=False
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Columns per Row"),
                            dcc.Dropdown(
                                id={"type": "t2e-cols", "index": uid},
                                options=[{"label": i, "value": i} for i in range(1, 5)],
                                value=2,
                                clearable=False
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Figure Width (px)"),
                            dcc.Slider(
                                id={"type": "t2e-width", "index": uid},
                                min=600, max=2000, step=100, value=1200,
                                marks={i: str(i) for i in range(600, 2001, 400)},
                                tooltip={"placement": "bottom", "always_visible": True}
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Figure Height (px)"),
                            dcc.Slider(
                                id={"type": "t2e-height", "index": uid},
                                min=300, max=2000, step=100, value=default_height,
                                marks={i: str(i) for i in range(300, 2001, 500)},
                                tooltip={"placement": "bottom", "always_visible": True}
                            )
                        ]), width=3),
                    ], align="center", className="mb-3"),
                ]
            ),
        ],
        start_collapsed=True,
        flush=True,
        className="mb-4"
    )
    
    # Copy button
    copy_plot_btn = dbc.Button(
        "Copy Plot to Clipboard",
        id={"type": "copy-t2e-plot", "index": uid},
        color="secondary",
        size="sm",
        className="mb-2"
    )
    
    # Store for base64 encoded image
    image_store = dcc.Store(id={"type": "t2e-plot-image-store", "index": uid})
    
    # Summary section
    summary_content = html.Div([
        html.Div([
            html.H6("T2 Echo Summary", style={"display": "inline-block", "marginRight": "10px"}),
            dcc.Clipboard(
                id={"type": "copy-t2e-summary", "index": uid},
                target_id={"type": "t2e-summary-table-content", "index": uid},
                title="Copy summary to clipboard",
                style={"display": "inline-block", "verticalAlign": "middle"}
            )
        ], style={"marginBottom": "10px"}),
        html.Div(
            create_t2_echo_summary_table(data),
            id={"type": "t2e-summary-table-content", "index": uid}
        )
    ])
    
    # Side panel
    side_panel = html.Div(
        id={"type": "t2e-side-panel", "index": uid},
        children=[
            html.Div(
                dbc.Button(
                    "◀ Info",
                    id={"type": "toggle-t2e-side-panel", "index": uid},
                    color="primary",
                    size="sm",
                    style={
                        "writingMode": "vertical-rl",
                        "textOrientation": "mixed",
                        "height": "100px",
                        "padding": "10px 5px"
                    }
                ),
                id={"type": "t2e-side-toggle-container", "index": uid},
                style={
                    "position": "fixed",
                    "right": "0",
                    "top": "50%",
                    "transform": "translateY(-50%)",
                    "zIndex": "1000",
                    "transition": "right 0.3s ease-in-out"
                }
            ),
            html.Div(
                id={"type": "t2e-side-panel-content", "index": uid},
                children=[
                    summary_content,
                    html.Hr(),
                    html.H6("Measurement Info"),
                    html.Pre(f"Folder: {folder}\nQubits: {data['n']}"),
                    html.Hr(),
                    html.H6("T2 Echo Description"),
                    html.P([
                        "The T2 Echo measurement consists of playing an echo sequence ",
                        "(x90 - idle_time - x180 - idle_time - -x90 - measurement) for ",
                        "different idle times. The qubit T2 echo is extracted by fitting ",
                        "the exponential decay of the measured quadratures/state. ",
                        "This measurement removes the effects of slow frequency fluctuations ",
                        "and measures the intrinsic decoherence rate T2."
                    ], style={"fontSize": "12px"}),
                    html.Hr(),
                    html.H6("Fit Status Legend"),
                    html.Ul([
                        html.Li("✓ : Fit successful"),
                        html.Li("✗ (original) : Original fit failed, no refit attempted"),
                        html.Li("⚠ (refit failed) : Original passed but refit failed"),
                    ], style={"fontSize": "11px"})
                ],
                style={
                    "position": "fixed",
                    "right": "-400px",
                    "top": "0",
                    "width": "400px",
                    "height": "100vh",
                    "backgroundColor": "white",
                    "boxShadow": "-2px 0 5px rgba(0,0,0,0.1)",
                    "padding": "20px",
                    "overflowY": "auto",
                    "transition": "right 0.3s ease-in-out",
                    "zIndex": "999"
                }
            )
        ]
    )
    
    # Main layout
    return html.Div([
        dcc.Store(id={"type": "t2e-data", "index": uid}, data={"folder": folder}),
        dcc.Store(id={"type": "t2e-side-panel-state", "index": uid}, data={"is_open": False}),
        image_store,
        dbc.Row(dbc.Col(html.H3(f"T2 Echo Measurement – {Path(folder).name}")), className="mb-3"),
        controls_accordion,
        dbc.Row([
            dbc.Col([
                copy_plot_btn,
                dcc.Loading(
                    dcc.Graph(
                        id={"type": "t2e-plot", "index": uid},
                        figure=init_fig,
                        config={"displayModeBar": True}
                    )
                )
            ], width=12)
        ]),
        side_panel
    ])

def register_t2_echo_callbacks(app):
    """Register callbacks for T2 Echo visualization"""
    
    @app.callback(
        [Output({"type": "t2e-plot", "index": MATCH}, "figure"),
         Output({"type": "t2e-summary-table-content", "index": MATCH}, "children")],
        Input({"type": "t2e-var", "index": MATCH}, "value"),
        Input({"type": "t2e-cols", "index": MATCH}, "value"),
        Input({"type": "t2e-width", "index": MATCH}, "value"),
        Input({"type": "t2e-height", "index": MATCH}, "value"),
        State({"type": "t2e-data", "index": MATCH}, "data"),
    )
    def update_t2e_plot(plot_var, n_cols, fig_w, fig_h, store):
        """Update T2 Echo plot based on user inputs"""
        data = load_t2_echo_data(store["folder"])
        fig = create_t2_echo_plots(
            data,
            n_cols=n_cols,
            fig_width=fig_w,
            fig_height=fig_h,
            plot_variable=plot_var
        )
        summary_table = create_t2_echo_summary_table(data)
        return fig, summary_table
    
    # Toggle side panel callback
    @app.callback(
        [Output({"type": "t2e-side-panel-content", "index": MATCH}, "style"),
         Output({"type": "t2e-side-toggle-container", "index": MATCH}, "style"),
         Output({"type": "toggle-t2e-side-panel", "index": MATCH}, "children"),
         Output({"type": "t2e-side-panel-state", "index": MATCH}, "data")],
        Input({"type": "toggle-t2e-side-panel", "index": MATCH}, "n_clicks"),
        State({"type": "t2e-side-panel-state", "index": MATCH}, "data"),
        prevent_initial_call=True
    )
    def toggle_t2e_side_panel(n_clicks, state_data):
        """Toggle the side information panel"""
        is_open = state_data.get("is_open", False) if state_data else False
        
        if n_clicks:
            is_open = not is_open
        
        if is_open:
            panel_style = {
                "position": "fixed",
                "right": "0",
                "top": "0",
                "width": "400px",
                "height": "100vh",
                "backgroundColor": "white",
                "boxShadow": "-2px 0 5px rgba(0,0,0,0.1)",
                "padding": "20px",
                "overflowY": "auto",
                "transition": "right 0.3s ease-in-out",
                "zIndex": "999"
            }
            toggle_style = {
                "position": "fixed",
                "right": "400px",
                "top": "50%",
                "transform": "translateY(-50%)",
                "zIndex": "1000",
                "transition": "right 0.3s ease-in-out"
            }
            button_text = "▶ Info"
        else:
            panel_style = {
                "position": "fixed",
                "right": "-400px",
                "top": "0",
                "width": "400px",
                "height": "100vh",
                "backgroundColor": "white",
                "boxShadow": "-2px 0 5px rgba(0,0,0,0.1)",
                "padding": "20px",
                "overflowY": "auto",
                "transition": "right 0.3s ease-in-out",
                "zIndex": "999"
            }
            toggle_style = {
                "position": "fixed",
                "right": "0",
                "top": "50%",
                "transform": "translateY(-50%)",
                "zIndex": "1000",
                "transition": "right 0.3s ease-in-out"
            }
            button_text = "◀ Info"
        
        return panel_style, toggle_style, button_text, {"is_open": is_open}
    
    # Copy plot to clipboard callback
    @app.callback(
        Output({"type": "t2e-plot-image-store", "index": MATCH}, "data"),
        Input({"type": "copy-t2e-plot", "index": MATCH}, "n_clicks"),
        State({"type": "t2e-plot", "index": MATCH}, "figure"),
        prevent_initial_call=True
    )
    def update_t2e_image_store(n_clicks, current_figure):
        """Convert plot to base64 image for clipboard copying"""
        if n_clicks and current_figure:
            try:
                fig = go.Figure(current_figure)
                width = current_figure.get('layout', {}).get('width', 800)
                height = current_figure.get('layout', {}).get('height', 600)
                
                if width is None:
                    width = 800
                if height is None:
                    height = 600
                
                try:
                    image_bytes_io = fig.to_image(
                        format="png",
                        engine="kaleido",
                        width=width,
                        height=height
                    )
                except:
                    import plotly.io as pio
                    image_bytes_io = pio.to_image(
                        fig,
                        format="png",
                        width=width,
                        height=height
                    )
                
                encoded_image = base64.b64encode(image_bytes_io).decode('utf-8')
                return encoded_image
            except Exception as e:
                print(f"Error converting figure to image: {e}")
                return ""
        return ""
    
    # Clientside callback for copying image
    app.clientside_callback(
        """
        function(stored_image_data, n_clicks) {
            if (n_clicks && stored_image_data) {
                const img = new Image();
                img.src = 'data:image/png;base64,' + stored_image_data;
                
                img.onload = function() {
                    const canvas = document.createElement('canvas');
                    canvas.width = this.naturalWidth;
                    canvas.height = this.naturalHeight;
                    
                    const ctx = canvas.getContext('2d');
                    ctx.drawImage(this, 0, 0);
                    
                    canvas.toBlob(function(blob) {
                        if (blob) {
                            const item = new ClipboardItem({'image/png': blob});
                            navigator.clipboard.write([item]).then(
                                function() {
                                    console.log('Image copied to clipboard successfully');
                                    setTimeout(function() {
                                        const btn = document.querySelector('[id*="copy-t2e-plot"]');
                                        if (btn) {
                                            btn.textContent = "Copy Plot to Clipboard";
                                        }
                                    }, 2000);
                                },
                                function(error) {
                                    console.error('Failed to copy image: ', error);
                                }
                            );
                        }
                    }, 'image/png');
                };
                
                return "Copied!";
            }
            return "Copy Plot to Clipboard";
        }
        """,
        Output({"type": "copy-t2e-plot", "index": MATCH}, "children"),
        Input({"type": "t2e-plot-image-store", "index": MATCH}, "data"),
        State({"type": "copy-t2e-plot", "index": MATCH}, "n_clicks"),
    )

# --------------------------------------------------------------------
# Example usage
# --------------------------------------------------------------------
if __name__ == "__main__":
    # Example: Create a simple Dash app to test the T2 Echo plotting tool
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    # Example folder path - replace with your actual data folder
    test_folder = "path/to/your/t2_echo_data"
    
    # Create layout
    app.layout = html.Div([
        create_t2_echo_layout(test_folder)
    ])
    
    # Register callbacks
    register_t2_echo_callbacks(app)
    
    # Run the app
    app.run_server(debug=True)