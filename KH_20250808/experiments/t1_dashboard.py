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

def decay_exp(t, a, offset, decay):
    """Exponential decay function: a * exp(t * decay) + offset"""
    return a * np.exp(t * decay) + offset

def fit_t1_decay(time_ns, amplitude_data):
    """
    Fit T1 decay to the data
    Returns: (success, tau_us, tau_error_us, fit_params)
    """
    try:
        # Initial guesses
        a_guess = amplitude_data[0] - amplitude_data[-1]  # Initial amplitude
        offset_guess = amplitude_data[-1]  # Final value as offset
        
        # Estimate decay rate from the data
        # Find where signal drops to ~1/e of initial amplitude
        target_val = offset_guess + a_guess / np.e
        idx_1e = np.argmin(np.abs(amplitude_data - target_val))
        if idx_1e > 0:
            tau_guess = time_ns[idx_1e]
            decay_guess = -1.0 / tau_guess
        else:
            decay_guess = -1.0 / 50000  # Default guess: 50 μs
        
        # Perform the fit
        popt, pcov = curve_fit(
            decay_exp, 
            time_ns, 
            amplitude_data,
            p0=[a_guess, offset_guess, decay_guess],
            bounds=(
                [0, 0, -np.inf],  # Lower bounds
                [np.inf, np.inf, 0]  # Upper bounds (decay must be negative)
            ),
            maxfev=5000
        )
        
        a_fit, offset_fit, decay_fit = popt
        
        # Calculate tau and its error
        tau_ns = -1.0 / decay_fit
        tau_us = tau_ns / 1000.0
        
        # Calculate tau error from covariance matrix
        decay_error = np.sqrt(pcov[2, 2])
        tau_error_ns = tau_ns * (decay_error / abs(decay_fit))
        tau_error_us = tau_error_ns / 1000.0
        
        # Success criteria
        success = (tau_us > 0.016) and (tau_error_us / tau_us < 1.0)
        
        return success, tau_us, tau_error_us, {'a': a_fit, 'offset': offset_fit, 'decay': decay_fit}
        
    except Exception as e:
        print(f"Fit failed: {e}")
        return False, np.nan, np.nan, None

# --------------------------------------------------------------------
# Common helper: xarray open_dataset with multiple engine attempts
# --------------------------------------------------------------------
def open_xr_dataset(path, engines=("h5netcdf", "netcdf4", None)):
    last_err = None
    for eng in engines:
        try:
            return xr.open_dataset(path, engine=eng)
        except Exception as e:
            last_err = e
    raise last_err

# --------------------------------------------------------------------
# 1. Data Loader for T1 measurements
# --------------------------------------------------------------------
def load_t1_data(folder):
    folder = os.path.normpath(folder)
    paths = {
        "ds_raw":  os.path.join(folder, "ds_raw.h5"),
        "ds_fit":  os.path.join(folder, "ds_fit.h5"),
        "data_js": os.path.join(folder, "data.json"),
        "node_js": os.path.join(folder, "node.json"),
    }
    if not all(os.path.exists(p) for p in paths.values()):
        print(f"[load_t1_data] missing file in {folder}")
        return None
    
    ds_raw = open_xr_dataset(paths["ds_raw"])
    ds_fit = open_xr_dataset(paths["ds_fit"])
    
    with open(paths["data_js"], "r", encoding="utf-8") as f:
        data_json = json.load(f)
    with open(paths["node_js"], "r", encoding="utf-8") as f:
        node_json = json.load(f)
    
    # Extract T1-specific data
    qubits = ds_raw["qubit"].values
    idle_time_ns = ds_raw["idle_time"].values  # in nanoseconds
    idle_time_us = idle_time_ns / 1000.0  # convert to microseconds
    
    # Get I and Q data (shape: n_qubits x n_idle_times)
    I_data = ds_raw["I"].values
    Q_data = ds_raw["Q"].values
    
    # Calculate transmission amplitude in mV
    trans_amp = np.sqrt(I_data**2 + Q_data**2) * 1e3
    
    # Perform our own fitting for each qubit
    success_list = []
    tau_list = []
    tau_error_list = []
    fit_params_list = []
    
    for i in range(len(qubits)):
        # Get the amplitude data for this qubit (already in mV)
        amp_data = trans_amp[i]
        
        # Convert back to original scale for fitting (divide by 1e3)
        amp_data_for_fit = amp_data / 1e3
        
        # Fit the decay
        success, tau_us, tau_error_us, fit_params = fit_t1_decay(idle_time_ns, amp_data_for_fit)
        
        success_list.append(success)
        tau_list.append(tau_us)
        tau_error_list.append(tau_error_us)
        fit_params_list.append(fit_params)
        
        print(f"Qubit {qubits[i]}: T1 = {tau_us:.1f} ± {tau_error_us:.1f} μs, Success = {success}")
        if fit_params:
            print(f"  Fit params: a={fit_params['a']:.3e}, offset={fit_params['offset']:.3e}, decay={fit_params['decay']:.3e}")
    
    return dict(
        qubits=qubits, 
        n=len(qubits),
        idle_time_ns=idle_time_ns,
        idle_time_us=idle_time_us,
        trans_amp=trans_amp,
        I=I_data,
        Q=Q_data,
        success=np.array(success_list),
        tau=np.array(tau_list),
        tau_error=np.array(tau_error_list),
        fit_params=fit_params_list,
        fit_results={}  # We're not using the JSON results anymore
    )
# --------------------------------------------------------------------
# 2. Exponential decay function for T1
# --------------------------------------------------------------------
def exponential_decay_with_params(t, a, offset, decay):
    """
    Exponential decay function using the parameters from fit_data
    t: time in nanoseconds
    a: amplitude
    offset: baseline offset
    decay: decay rate (should be negative for decay, but we'll handle both cases)
    """
    # Ensure decay is negative for proper exponential decay
    # If decay is positive, make it negative
    if decay > 0:
        decay = -decay
    
    # Standard exponential decay: a * exp(decay * t) + offset
    # where decay should be negative (= -1/tau)
    return a * np.exp(decay * t) + offset

# --------------------------------------------------------------------
# 3. Plot Generation for T1 measurements
# --------------------------------------------------------------------
def create_t1_plots(
    data,
    n_cols: int = 2,
    fig_width: int = None,
    fig_height: int = None,
    vertical_spacing_px: int = 20,
    legend_x: float = 0.98,
    legend_y: float = 1.0,
    legend_xanchor: str = "right",
    legend_yanchor: str = "bottom",
    legend_orientation: str = "h"
):
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
    
    # Create subplot titles with qubit names
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
        
        # Use nanoseconds for x-axis (matching the reference image)
        x_ns = data["idle_time_ns"]
        y_mv = data["trans_amp"][idx]
        
        # Add data points
        fig.add_trace(
            go.Scatter(
                x=x_ns, 
                y=y_mv,
                mode="lines+markers",
                marker=dict(size=3, color="blue"),
                line=dict(color="blue", width=1),
                name="Data",
                legendgroup="raw_data",
                showlegend=(idx == 0),  # Show legend only for first subplot
            ),
            row=r, col=c
        )
        
        # Add fit if successful
        if data["success"][idx] and data["fit_params"][idx] is not None:
            # Get fit parameters
            fit_p = data["fit_params"][idx]
            
            # Generate smooth fit curve
            x_fit_ns = np.linspace(x_ns.min(), x_ns.max(), 500)
            
            # Calculate fitted values using our fit parameters
            # Note: fit was done on data/1e3, so params are in that scale
            y_fit = decay_exp(x_fit_ns, fit_p['a'], fit_p['offset'], fit_p['decay'])
            
            # Convert back to mV for display
            y_fit = y_fit * 1e3
            
            fig.add_trace(
                go.Scatter(
                    x=x_fit_ns,
                    y=y_fit,
                    mode="lines",
                    line=dict(color="darkblue", width=2, dash="solid"),
                    name="Fit",
                    legendgroup="fit_curve",
                    showlegend=(idx == 0),  # Show legend only for first subplot
                ),
                row=r, col=c
            )
            
            # Add T1 value and success indicator as text box
            t1_val = data['tau'][idx]
            t1_err = data['tau_error'][idx]
            
            # Format T1 with error
            if not np.isnan(t1_err) and t1_err > 0:
                t1_str = f"T1 = {t1_val:.1f} ± {t1_err:.1f} μs"
            else:
                t1_str = f"T1 = {t1_val:.1f} μs"
            
            annotation_text = f"{t1_str}\nFit: ✓"
            bg_color = "rgba(144, 238, 144, 0.3)"  # Light green
            border_color = "green"
            
            fig.add_annotation(
                text=annotation_text,
                xref=f"x{idx+1 if idx > 0 else ''}",
                yref=f"y{idx+1 if idx > 0 else ''}",
                x=x_ns.max() - (x_ns.max() - x_ns.min()) * 0.02,
                y=y_mv.min() + (y_mv.max() - y_mv.min()) * 0.98,
                xanchor="right",
                yanchor="top",
                showarrow=False,
                font=dict(size=9),
                bgcolor=bg_color,
                bordercolor=border_color,
                borderwidth=1,
                align="left"
            )

        else:
            # Add failure indicator
            annotation_text = "Fit Failed\nFit: ✗"
            bg_color = "rgba(255, 200, 200, 0.3)"  # Light red
            border_color = "red"
            
            fig.add_annotation(
                text=annotation_text,
                xref=f"x{idx+1 if idx > 0 else ''}",
                yref=f"y{idx+1 if idx > 0 else ''}",
                x=x_ns.max() - (x_ns.max() - x_ns.min()) * 0.02,
                y=y_mv.min() + (y_mv.max() - y_mv.min()) * 0.98,
                xanchor="right",
                yanchor="top",
                showarrow=False,
                font=dict(size=9, color="red"),
                bgcolor=bg_color,
                bordercolor=border_color,
                borderwidth=1,
                align="left"
            )
        
        # Update axes labels
        fig.update_xaxes(
            title_text="Idle time [ns]" if r == n_rows else None,
            row=r, col=c,
            showgrid=True,
        )
        fig.update_yaxes(
            title_text="Trans. amp. [mV]" if c == 1 else None,
            row=r, col=c,
            showgrid=True,
        )
    
    # Global styling (updated to match reference)
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
    layout_args = dict(
        title="T1 vs. idle time",
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
# 4. Summary Table for T1 measurements
# --------------------------------------------------------------------
def create_t1_summary_table(data):
    rows = []
    for i, q in enumerate(data["qubits"]):
        ok = bool(data["success"][i])
        tau_val = data["tau"][i]
        tau_err = data["tau_error"][i]
        
        # Format T1 value
        if ok and not np.isnan(tau_val):
            t1_str = f"{tau_val:.1f} ± {tau_err:.1f}"
        else:
            t1_str = "—"
        
        rows.append(
            html.Tr([
                html.Td(str(q)),
                html.Td(t1_str),
                html.Td("✓" if ok else "✗"),
            ], className="table-success" if ok else "table-warning")
        )
    
    header = html.Thead(html.Tr([
        html.Th("Qubit"), 
        html.Th("T1 [μs]"),
        html.Th("Fit Success")
    ]))
    
    return dbc.Table(
        [header, html.Tbody(rows)],
        bordered=True, 
        striped=True,
        size="sm", 
        responsive=True
    )

# --------------------------------------------------------------------
# 5. Layout + Callbacks for T1 measurements
# --------------------------------------------------------------------
def create_t1_layout(folder):
    uid = folder.replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_t1_data(folder)
    if not data:
        return html.Div([
            dbc.Alert("Failed to load T1 data", color="danger"), 
            html.Pre(folder)
        ])
    
    default_height = 400 * ceil(data["n"] / 2)  # 2 columns by default
    init_fig = create_t1_plots(data, n_cols=2, fig_height=default_height)
    
    # Controls
    controls_accordion = dbc.Accordion(
        [
            dbc.AccordionItem(
                title="Display Options",
                children=[
                    dbc.Row([
                        dbc.Col(html.Div([
                            html.Label("Columns per Row"),
                            dcc.Dropdown(
                                id={"type": "t1-cols", "index": uid},
                                options=[{"label": i, "value": i} for i in range(1, 5)],
                                value=2, 
                                clearable=False
                            )
                        ]), width=4),
                        dbc.Col(html.Div([
                            html.Label("Figure Width (px)"),
                            dcc.Slider(
                                id={"type": "t1-width", "index": uid},
                                min=600, max=2000, step=100, value=1200,
                                marks={i: str(i) for i in range(600, 2001, 400)},
                                tooltip={"placement": "bottom", "always_visible": True}
                            )
                        ]), width=4),
                        dbc.Col(html.Div([
                            html.Label("Figure Height (px)"),
                            dcc.Slider(
                                id={"type": "t1-height", "index": uid},
                                min=300, max=2000, step=100, value=default_height,
                                marks={i: str(i) for i in range(300, 2001, 500)},
                                tooltip={"placement": "bottom", "always_visible": True}
                            )
                        ]), width=4),
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
        id={"type": "copy-t1-plot", "index": uid},
        color="secondary",
        size="sm",
        className="mb-2"
    )
    
    # Store for base64 encoded image
    image_store = dcc.Store(id={"type": "t1-plot-image-store", "index": uid})
    
    # Summary section
    summary_content = html.Div([
        html.Div([
            html.H6("T1 Summary Table", style={"display": "inline-block", "marginRight": "10px"}),
            dcc.Clipboard(
                id={"type": "copy-t1-summary", "index": uid},
                target_id={"type": "t1-summary-table-content", "index": uid},
                title="Copy summary to clipboard",
                style={"display": "inline-block", "verticalAlign": "middle"}
            )
        ], style={"marginBottom": "10px"}),
        html.Div(
            create_t1_summary_table(data),
            id={"type": "t1-summary-table-content", "index": uid}
        )
    ])
    
    # Side panel
    side_panel = html.Div(
        id={"type": "t1-side-panel", "index": uid},
        children=[
            html.Div(
                dbc.Button(
                    "◀ Info",
                    id={"type": "toggle-t1-side-panel", "index": uid},
                    color="primary",
                    size="sm",
                    style={
                        "writingMode": "vertical-rl",
                        "textOrientation": "mixed",
                        "height": "100px",
                        "padding": "10px 5px"
                    }
                ),
                id={"type": "t1-side-toggle-container", "index": uid},
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
                id={"type": "t1-side-panel-content", "index": uid},
                children=[
                    summary_content,
                    html.Hr(),
                    html.H6("Measurement Info"),
                    html.Pre(f"Folder: {folder}\nQubits: {data['n']}"),
                    html.Hr(),
                    html.H6("T1 Measurement Description"),
                    html.P([
                        "The T1 relaxation time measurement consists of preparing ",
                        "the qubit in the excited state using a π-pulse and then ",
                        "measuring the qubit state after a variable idle time. ",
                        "The exponential decay of the excited state population ",
                        "gives the T1 relaxation time."
                    ], style={"fontSize": "12px"})
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
        dcc.Store(id={"type": "t1-data", "index": uid}, data={"folder": folder}),
        dcc.Store(id={"type": "t1-side-panel-state", "index": uid}, data={"is_open": False}),
        image_store,
        dbc.Row(dbc.Col(html.H3(f"T1 Measurement – {Path(folder).name}")), className="mb-3"),
        controls_accordion,
        dbc.Row([
            dbc.Col([
                copy_plot_btn,
                dcc.Loading(
                    dcc.Graph(
                        id={"type": "t1-plot", "index": uid},
                        figure=init_fig,
                        config={"displayModeBar": True}
                    )
                )
            ], width=12)
        ]),
        side_panel
    ])

def register_t1_callbacks(app):
    @app.callback(
        [Output({"type": "t1-plot", "index": MATCH}, "figure"),
         Output({"type": "t1-summary-table-content", "index": MATCH}, "children")],
        Input({"type": "t1-cols", "index": MATCH}, "value"),
        Input({"type": "t1-width", "index": MATCH}, "value"),
        Input({"type": "t1-height", "index": MATCH}, "value"),
        State({"type": "t1-data", "index": MATCH}, "data"),
    )
    def update_t1_plot(n_cols, fig_w, fig_h, store):
        data = load_t1_data(store["folder"])
        fig = create_t1_plots(
            data,
            n_cols=n_cols,
            fig_width=fig_w,
            fig_height=fig_h
        )
        summary_table = create_t1_summary_table(data)
        return fig, summary_table
    
    # Toggle side panel callback
    @app.callback(
        [Output({"type": "t1-side-panel-content", "index": MATCH}, "style"),
         Output({"type": "t1-side-toggle-container", "index": MATCH}, "style"),
         Output({"type": "toggle-t1-side-panel", "index": MATCH}, "children"),
         Output({"type": "t1-side-panel-state", "index": MATCH}, "data")],
        Input({"type": "toggle-t1-side-panel", "index": MATCH}, "n_clicks"),
        State({"type": "t1-side-panel-state", "index": MATCH}, "data"),
        prevent_initial_call=True
    )
    def toggle_t1_side_panel(n_clicks, state_data):
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
        Output({"type": "t1-plot-image-store", "index": MATCH}, "data"),
        Input({"type": "copy-t1-plot", "index": MATCH}, "n_clicks"),
        State({"type": "t1-plot", "index": MATCH}, "figure"),
        prevent_initial_call=True
    )
    def update_t1_image_store(n_clicks, current_figure):
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
                                        const btn = document.querySelector('[id*="copy-t1-plot"]');
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
        Output({"type": "copy-t1-plot", "index": MATCH}, "children"),
        Input({"type": "t1-plot-image-store", "index": MATCH}, "data"),
        State({"type": "copy-t1-plot", "index": MATCH}, "n_clicks"),
    )

# --------------------------------------------------------------------
# 6. Main app integration example
# --------------------------------------------------------------------
if __name__ == "__main__":
    # Example usage
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    # Example folder path - replace with your actual T1 data folder
    folder_path = "path/to/your/t1/data/folder"
    
    app.layout = html.Div([
        create_t1_layout(folder_path)
    ])
    
    register_t1_callbacks(app)
    
    app.run_server(debug=True)