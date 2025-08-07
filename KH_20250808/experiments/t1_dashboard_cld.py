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
    idle_time_us = idle_time_ns / 1000.0  # convert to microseconds for display
    
    # Get I and Q data (shape: n_qubits x n_idle_times)
    I_data = ds_raw["I"].values
    Q_data = ds_raw["Q"].values
    
    # Calculate transmission amplitude
    scale_ = 1e3 # Convert to mV
    trans_amp = np.sqrt(I_data**2 + Q_data**2) * scale_
    
    # Get fit parameters from ds_fit
    success = ds_fit["success"].values
    tau = ds_fit["tau"].values if "tau" in ds_fit else np.full(len(qubits), np.nan)
    tau_error = ds_fit["tau_error"].values if "tau_error" in ds_fit else np.full(len(qubits), np.nan)
    
    # Get fit data if available
    fit_data = ds_fit["fit_data"].values if "fit_data" in ds_fit else None
    
    # Also check data.json for fit_results
    fit_results = data_json.get("fit_results", {})
    
    # If tau not in ds_fit, try to get from data.json
    if np.all(np.isnan(tau)):
        for i, q in enumerate(qubits):
            q_str = str(q)
            if q_str in fit_results:
                tau[i] = fit_results[q_str].get("t1", np.nan) / 1000.0  # Convert ns to μs
                tau_error[i] = fit_results[q_str].get("t1_error", np.nan) / 1000.0
                success[i] = fit_results[q_str].get("success", False)
    
    return dict(
        qubits=qubits, 
        n=len(qubits),
        idle_time_ns=idle_time_ns,
        idle_time_us=idle_time_us,
        trans_amp=trans_amp,
        I=I_data,
        Q=Q_data,
        success=success,
        tau=tau,
        tau_error=tau_error,
        fit_data=fit_data,
        fit_results=fit_results
    )

# --------------------------------------------------------------------
# 2. Exponential decay function for T1
# --------------------------------------------------------------------
def exponential_decay(t, A, tau, offset):
    """Exponential decay function: A * exp(-t/tau) + offset"""
    return A * np.exp(-t / tau) + offset

# --------------------------------------------------------------------
# 3. Plot Generation for T1 measurements
# --------------------------------------------------------------------
def create_t1_plots(
    data,
    n_cols: int = 2,
    fig_width: int = None,
    fig_height: int = None,
    vertical_spacing_px: int = 20,
    legend_x: float = 0.02,
    legend_y: float = 0.98,
    legend_xanchor: str = "left",
    legend_yanchor: str = "top",
    legend_orientation: str = "v"
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
        
        x_us = data["idle_time_us"]
        y_mv = data["trans_amp"][idx]
        
        # Add data points
        fig.add_trace(
            go.Scatter(
                x=x_us, 
                y=y_mv,
                mode="lines+markers",
                line=dict(color="blue", width=1),
                marker=dict(size=3),
                name=f"{q} Data",
                legendgroup=f"q{idx}",
                showlegend=True,
            ),
            row=r, col=c
        )
        
        # Add fit if successful
        if data["success"][idx] and not np.isnan(data["tau"][idx]):
            # Generate smooth fit curve
            x_fit = np.linspace(x_us.min(), x_us.max(), 500)
            
            # If we have fit_data from the dataset, use it to reconstruct the fit
            # Otherwise, estimate the fit parameters
            if data["fit_data"] is not None and idx < len(data["fit_data"]):
                fit_params = data["fit_data"][idx]
                # fit_vals dimension should contain parameters like 'a', 'offset', etc.
                # For now, we'll estimate from the data
                A_est = y_mv[0] - y_mv[-1]
                offset_est = y_mv[-1]
                tau_val = data["tau"][idx]
            else:
                # Estimate fitting parameters
                A_est = y_mv[0] - y_mv[-1]
                offset_est = y_mv[-1]
                tau_val = data["tau"][idx]
            
            # Generate fit curve using exponential decay
            y_fit = exponential_decay(x_fit * 1000, A_est, tau_val * 1000, offset_est)  # Convert μs to ns for calculation
            
            # Format T1 value with error for legend
            tau_str = f"T1 = {data['tau'][idx]:.1f} ± {data['tau_error'][idx]:.1f} μs"
            
            fig.add_trace(
                go.Scatter(
                    x=x_fit,
                    y=y_fit,
                    mode="lines",
                    line=dict(color="red", width=2, dash="solid"),
                    name=tau_str,
                    legendgroup=f"q{idx}",
                    showlegend=True,
                ),
                row=r, col=c
            )
            
            # Add success indicator in subplot title
            fig.add_annotation(
                text=f"Success: {data['success'][idx]}",
                xref=f"x{idx+1}" if idx > 0 else "x",
                yref=f"y{idx+1}" if idx > 0 else "y",
                x=x_us.max() * 0.95,
                y=y_mv.max() * 0.95,
                showarrow=False,
                font=dict(size=10),
                bgcolor="rgba(255, 255, 255, 0.8)",
                bordercolor="green" if data["success"][idx] else "red",
                borderwidth=1
            )
        else:
            # Add failure indicator
            fig.add_annotation(
                text="Fit Failed",
                xref=f"x{idx+1}" if idx > 0 else "x",
                yref=f"y{idx+1}" if idx > 0 else "y",
                x=x_us.max() * 0.95,
                y=y_mv.max() * 0.95,
                showarrow=False,
                font=dict(size=10, color="red"),
                bgcolor="rgba(255, 255, 255, 0.8)",
                bordercolor="red",
                borderwidth=1
            )
        
        # Update axes labels
        fig.update_xaxes(
            title_text="idle_time [ns]" if r == n_rows else None,
            row=r, col=c,
            showgrid=True,
        )
        fig.update_yaxes(
            title_text="Trans. amp. [mV]" if c == 1 else None,
            row=r, col=c,
            showgrid=True,
        )
    
    # Global styling
    fig.update_xaxes(
        gridcolor="rgba(0,0,0,0.2)", 
        griddash="dash",
        zerolinecolor="rgba(0,0,0,0.2)", 
        zerolinewidth=0.5,
        ticks="inside", 
        ticklen=6,
        showline=True, 
        linecolor="black", 
        mirror=False,
    )
    fig.update_yaxes(
        gridcolor="rgba(0,0,0,0.2)", 
        griddash="dash",
        zerolinecolor="rgba(0,0,0,0.2)", 
        zerolinewidth=0.5,
        ticks="inside", 
        ticklen=6,
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
            bgcolor="rgba(255, 255, 255, 0.8)",
            bordercolor="black",
            borderwidth=1
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
        height=effective_height
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