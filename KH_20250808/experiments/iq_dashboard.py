import dash
from dash import dcc, html, Input, Output, State, MATCH, ctx
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
# 1. Data Loader for IQ Blob measurements
# --------------------------------------------------------------------
def load_iq_blob_data(folder):
    """Load IQ Blob data from folder"""
    folder = os.path.normpath(folder)
    paths = {
        "ds_raw": os.path.join(folder, "ds_raw.h5"),
        "ds_fit": os.path.join(folder, "ds_fit.h5"),
        "data_js": os.path.join(folder, "data.json"),
        "node_js": os.path.join(folder, "node.json"),
    }
    
    # Check if all files exist
    if not all(os.path.exists(p) for p in paths.values()):
        print(f"[load_iq_blob_data] missing file in {folder}")
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
    
    # Get IQ data for ground and excited states (rotated)
    Ig = ds_fit["Ig"].values if "Ig" in ds_fit else ds_raw["Ig"].values  # Shape: (n_qubits, n_runs)
    Qg = ds_fit["Qg"].values if "Qg" in ds_fit else ds_raw["Qg"].values
    Ie = ds_fit["Ie"].values if "Ie" in ds_fit else ds_raw["Ie"].values
    Qe = ds_fit["Qe"].values if "Qe" in ds_fit else ds_raw["Qe"].values
    
    # Convert to mV for display
    Ig = Ig * 1e3
    Qg = Qg * 1e3
    Ie = Ie * 1e3
    Qe = Qe * 1e3
    
    # Check success flags
    success = ds_fit["success"].values if "success" in ds_fit else np.full(n_q, True)
    
    # Extract confusion matrix elements from ds_fit if available
    gg = ds_fit["gg"].values if "gg" in ds_fit else np.full(n_q, np.nan)
    ge = ds_fit["ge"].values if "ge" in ds_fit else np.full(n_q, np.nan)
    eg = ds_fit["eg"].values if "eg" in ds_fit else np.full(n_q, np.nan)
    ee = ds_fit["ee"].values if "ee" in ds_fit else np.full(n_q, np.nan)
    
    # Extract readout fidelity
    readout_fidelity = ds_fit["readout_fidelity"].values if "readout_fidelity" in ds_fit else np.full(n_q, np.nan)
    
    # Extract thresholds (in original units, then convert to mV)
    ge_threshold = ds_fit["ge_threshold"].values * 1e3 if "ge_threshold" in ds_fit else np.full(n_q, np.nan)
    rus_threshold = ds_fit["rus_threshold"].values * 1e3 if "rus_threshold" in ds_fit else np.full(n_q, np.nan)
    
    # Get fit results from JSON if available
    fit_results_json = data_json.get("fit_results", {})
    
    # Fallback to JSON data if arrays are not good
    for i, q in enumerate(qubits):
        q_str = str(q)
        if q_str in fit_results_json:
            fit_data = fit_results_json[q_str]
            if np.isnan(gg[i]) and "confusion_matrix" in fit_data:
                cm = fit_data["confusion_matrix"]
                gg[i] = cm[0][0]
                ge[i] = cm[0][1]
                eg[i] = cm[1][0]
                ee[i] = cm[1][1]
            if np.isnan(readout_fidelity[i]) and "readout_fidelity" in fit_data:
                readout_fidelity[i] = fit_data["readout_fidelity"]
            if np.isnan(ge_threshold[i]) and "ge_threshold" in fit_data:
                ge_threshold[i] = fit_data["ge_threshold"] * 1e3
            if np.isnan(rus_threshold[i]) and "rus_threshold" in fit_data:
                rus_threshold[i] = fit_data["rus_threshold"] * 1e3
            if "success" in fit_data:
                success[i] = fit_data["success"]
    
    return dict(
        qubits=qubits,
        n=n_q,
        Ig=Ig,
        Qg=Qg,
        Ie=Ie,
        Qe=Qe,
        gg=gg,
        ge=ge,
        eg=eg,
        ee=ee,
        readout_fidelity=readout_fidelity,
        ge_threshold=ge_threshold,
        rus_threshold=rus_threshold,
        success=success,
        data_json=data_json,
        node_json=node_json,
        ds_raw=ds_raw,
        ds_fit=ds_fit
    )

# --------------------------------------------------------------------
# 2. Plot Generation for IQ Blob measurements
# --------------------------------------------------------------------
def create_confusion_matrix_plot(
    data,
    n_cols: int = 2,
    fig_width: int = None,
    fig_height: int = None,
    vertical_spacing_px: int = 40
):
    """Create confusion matrix plots for multiple qubits"""
    
    if not data:
        return go.Figure()
    
    n_q = data["n"]
    n_cols = max(1, min(n_cols, n_q))
    n_rows = ceil(n_q / n_cols)
    
    # Compute ideal height
    SUBPLOT_HEIGHT_PX = 350
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
        vs_fraction = 0.05
    
    # Create subplot titles
    subplot_titles = [str(q) for q in data["qubits"]]
    
    fig = subplots.make_subplots(
        rows=n_rows, cols=n_cols,
        subplot_titles=subplot_titles,
        vertical_spacing=vs_fraction,
        horizontal_spacing=0.12
    )
    
    # Add confusion matrices for each qubit
    for idx, q in enumerate(data["qubits"]):
        r, c = divmod(idx, n_cols)
        r += 1
        c += 1
        
        # Create confusion matrix - note the order matches the reference image
        # The matrix shows P(measured | prepared)
        z = np.array([[data["gg"][idx], data["ge"][idx]],
                      [data["eg"][idx], data["ee"][idx]]])
        
        # Create text annotations with percentages
        text = np.array([[f"{data['gg'][idx]*100:.1f}%", f"{data['ge'][idx]*100:.1f}%"],
                         [f"{data['eg'][idx]*100:.1f}%", f"{data['ee'][idx]*100:.1f}%"]])
        
        # Custom colorscale matching the reference (white to red)
        colorscale = [
            [0.0, 'rgb(255, 255, 255)'],
            [0.1, 'rgb(255, 230, 230)'],
            [0.5, 'rgb(255, 150, 150)'],
            [0.9, 'rgb(220, 20, 60)'],
            [1.0, 'rgb(178, 34, 34)']
        ]
        
        fig.add_trace(
            go.Heatmap(
                z=z[::-1],  # Flip vertically to match reference
                text=text[::-1],
                texttemplate="%{text}",
                textfont={"size": 20, "color": "white"},  # White text like in reference
                colorscale=colorscale,
                zmin=0,
                zmax=1,
                showscale=False,  # No colorbar shown in reference
                hovertemplate="Prepared: %{y}<br>Measured: %{x}<br>Probability: %{z:.3f}<extra></extra>"
            ),
            row=r, col=c
        )
        
        # Update axes to match reference
        fig.update_xaxes(
            tickmode='array',
            tickvals=[0, 1],
            ticktext=['|g⟩', '|e⟩'],
            title_text="Measured" if r == n_rows else None,
            row=r, col=c,
            showgrid=False
        )
        fig.update_yaxes(
            tickmode='array',
            tickvals=[0, 1],
            ticktext=['|e⟩', '|g⟩'],  # Reversed because of flip
            title_text="Prepared" if c == 1 else None,
            row=r, col=c,
            showgrid=False
        )
    
    # Layout
    layout_args = dict(
        title="IQ Readout – Confusion Matrix",
        font=dict(size=11),
        title_font_size=14,
        autosize=True,
        margin=dict(
            t=TITLE_MARGIN_PX,
            b=BOTTOM_MARGIN_PX,
            l=80,
            r=80
        ),
        height=effective_height,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )
    if fig_width:
        layout_args["width"] = fig_width
    
    fig.update_layout(**layout_args)
    return fig

def create_histogram_plot(
    data,
    n_cols: int = 2,
    fig_width: int = None,
    fig_height: int = None,
    vertical_spacing_px: int = 40
):
    """Create histogram plots for rotated I-quadrature"""
    
    if not data:
        return go.Figure()
    
    n_q = data["n"]
    n_cols = max(1, min(n_cols, n_q))
    n_rows = ceil(n_q / n_cols)
    
    # Compute ideal height
    SUBPLOT_HEIGHT_PX = 350
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
        vs_fraction = 0.05
    
    # Create subplot titles
    subplot_titles = [str(q) for q in data["qubits"]]
    
    fig = subplots.make_subplots(
        rows=n_rows, cols=n_cols,
        subplot_titles=subplot_titles,
        vertical_spacing=vs_fraction,
        horizontal_spacing=0.08
    )
    
    # Add histograms for each qubit
    for idx, q in enumerate(data["qubits"]):
        r, c = divmod(idx, n_cols)
        r += 1
        c += 1
        
        Ig = data["Ig"][idx]
        Ie = data["Ie"][idx]
        
        # Create bins
        all_values = np.concatenate([Ig, Ie])
        bin_min = np.min(all_values)
        bin_max = np.max(all_values)
        n_bins = 50
        
        # Add histograms
        fig.add_trace(
            go.Histogram(
                x=Ig,
                nbinsx=n_bins,
                name="|g⟩",
                marker_color="skyblue",
                opacity=0.7,
                showlegend=(idx == 0),
                legendgroup="g"
            ),
            row=r, col=c
        )
        
        fig.add_trace(
            go.Histogram(
                x=Ie,
                nbinsx=n_bins,
                name="|e⟩",
                marker_color="lightsalmon",
                opacity=0.7,
                showlegend=(idx == 0),
                legendgroup="e"
            ),
            row=r, col=c
        )
        
        # Add threshold lines
        if not np.isnan(data["rus_threshold"][idx]):
            fig.add_vline(
                x=data["rus_threshold"][idx],
                line=dict(color="black", dash="dash", width=2),
                row=r, col=c
            )
        
        if not np.isnan(data["ge_threshold"][idx]):
            fig.add_vline(
                x=data["ge_threshold"][idx],
                line=dict(color="red", dash="dash", width=2),
                row=r, col=c
            )
        
        # Update axes
        fig.update_xaxes(
            title_text="I-rot [mV]" if r == n_rows else None,
            row=r, col=c,
            showgrid=True,
            gridcolor="rgba(0,0,0,0.1)"
        )
        fig.update_yaxes(
            title_text="Counts" if c == 1 else None,
            row=r, col=c,
            showgrid=True,
            gridcolor="rgba(0,0,0,0.1)"
        )
    
    # Layout
    layout_args = dict(
        title="IQ Readout – Rotated-I Histograms",
        barmode="overlay",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(255, 255, 255, 0.9)",
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
        height=effective_height,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )
    if fig_width:
        layout_args["width"] = fig_width
    
    fig.update_layout(**layout_args)
    return fig

def create_scatter_blob_plot(
    data,
    n_cols: int = 2,
    fig_width: int = None,
    fig_height: int = None,
    vertical_spacing_px: int = 40
):
    """Create scatter (blob) plots for IQ data"""
    
    if not data:
        return go.Figure()
    
    n_q = data["n"]
    n_cols = max(1, min(n_cols, n_q))
    n_rows = ceil(n_q / n_cols)
    
    # Compute ideal height
    SUBPLOT_HEIGHT_PX = 400
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
        vs_fraction = 0.05
    
    # Create subplot titles
    subplot_titles = [str(q) for q in data["qubits"]]
    
    fig = subplots.make_subplots(
        rows=n_rows, cols=n_cols,
        subplot_titles=subplot_titles,
        vertical_spacing=vs_fraction,
        horizontal_spacing=0.08
    )
    
    # Add scatter plots for each qubit
    for idx, q in enumerate(data["qubits"]):
        r, c = divmod(idx, n_cols)
        r += 1
        c += 1
        
        # Add ground state blob
        fig.add_trace(
            go.Scatter(
                x=data["Ig"][idx],
                y=data["Qg"][idx],
                mode="markers",
                marker=dict(
                    color="skyblue",
                    size=3,
                    opacity=0.5
                ),
                name="|g⟩",
                showlegend=(idx == 0),
                legendgroup="g",
                hovertemplate="I: %{x:.3f}<br>Q: %{y:.3f}<extra></extra>"
            ),
            row=r, col=c
        )
        
        # Add excited state blob
        fig.add_trace(
            go.Scatter(
                x=data["Ie"][idx],
                y=data["Qe"][idx],
                mode="markers",
                marker=dict(
                    color="lightsalmon",
                    size=3,
                    opacity=0.5
                ),
                name="|e⟩",
                showlegend=(idx == 0),
                legendgroup="e",
                hovertemplate="I: %{x:.3f}<br>Q: %{y:.3f}<extra></extra>"
            ),
            row=r, col=c
        )
        
        # Add threshold lines
        if not np.isnan(data["rus_threshold"][idx]):
            fig.add_vline(
                x=data["rus_threshold"][idx],
                line=dict(color="black", dash="dash", width=2),
                row=r, col=c
            )
        
        if not np.isnan(data["ge_threshold"][idx]):
            fig.add_vline(
                x=data["ge_threshold"][idx],
                line=dict(color="red", dash="dash", width=2),
                row=r, col=c
            )
        
        # Update axes with equal aspect ratio
        fig.update_xaxes(
            title_text="I-rot [mV]" if r == n_rows else None,
            row=r, col=c,
            showgrid=True,
            gridcolor="rgba(0,0,0,0.1)",
            scaleanchor=f"y{idx+1 if idx > 0 else ''}",
            scaleratio=1
        )
        fig.update_yaxes(
            title_text="Q-rot [mV]" if c == 1 else None,
            row=r, col=c,
            showgrid=True,
            gridcolor="rgba(0,0,0,0.1)"
        )
    
    # Layout
    layout_args = dict(
        title="IQ Readout – Rotated-IQ Blob",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(255, 255, 255, 0.9)",
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
        height=effective_height,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )
    if fig_width:
        layout_args["width"] = fig_width
    
    fig.update_layout(**layout_args)
    return fig

# --------------------------------------------------------------------
# 3. Summary Table for IQ Blob measurements
# --------------------------------------------------------------------
def create_iq_blob_summary_table(data):
    """Create summary table showing readout fidelity and fit success"""
    rows = []
    
    for i, q in enumerate(data["qubits"]):
        success = bool(data["success"][i])
        
        # Format readout fidelity
        if success and not np.isnan(data["readout_fidelity"][i]):
            fidelity_str = f"{data['readout_fidelity'][i]:.1f}%"
        else:
            fidelity_str = "—"
        
        # Format confusion matrix values
        if success and not np.isnan(data["gg"][i]):
            cm_str = f"gg:{data['gg'][i]*100:.1f}% ee:{data['ee'][i]*100:.1f}%"
        else:
            cm_str = "—"
        
        # Determine row class based on success
        if success:
            row_class = "table-success"
            status = "✓"
        else:
            row_class = "table-warning"
            status = "✗"
        
        rows.append(
            html.Tr([
                html.Td(str(q)),
                html.Td(fidelity_str),
                html.Td(cm_str, style={"fontSize": "11px"}),
                html.Td(status),
            ], className=row_class)
        )
    
    header = html.Thead(html.Tr([
        html.Th("Qubit"),
        html.Th("Readout Fidelity"),
        html.Th("Confusion Matrix"),
        html.Th("Fit")
    ]))
    
    return dbc.Table(
        [header, html.Tbody(rows)],
        bordered=True,
        striped=True,
        size="sm",
        responsive=True
    )

# --------------------------------------------------------------------
# 4. Layout + Callbacks for IQ Blob measurements
# --------------------------------------------------------------------
def create_iq_blob_layout(folder):
    """Create the complete layout for IQ Blob visualization"""
    uid = folder.replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_iq_blob_data(folder)
    
    if not data:
        return html.Div([
            dbc.Alert("Failed to load IQ Blob data", color="danger"),
            html.Pre(folder)
        ])
    
    default_height = 400 * ceil(data["n"] / 2)  # 2 columns by default
    init_fig = create_confusion_matrix_plot(data, n_cols=2, fig_height=default_height)
    
    # Plot mode options
    plot_modes = [
        {"label": "Confusion Matrix", "value": "confusion"},
        {"label": "Histogram", "value": "histogram"},
        {"label": "Scatter (Blob)", "value": "scatter"}
    ]
    
    # Controls
    controls_accordion = dbc.Accordion(
        [
            dbc.AccordionItem(
                title="Display Options",
                children=[
                    dbc.Row([
                        dbc.Col(html.Div([
                            html.Label("Plot Type"),
                            dcc.Dropdown(
                                id={"type": "iq-mode", "index": uid},
                                options=plot_modes,
                                value="confusion",
                                clearable=False
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Columns per Row"),
                            dcc.Dropdown(
                                id={"type": "iq-cols", "index": uid},
                                options=[{"label": i, "value": i} for i in range(1, 5)],
                                value=2,
                                clearable=False
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Figure Width (px)"),
                            dcc.Slider(
                                id={"type": "iq-width", "index": uid},
                                min=600, max=2000, step=100, value=1200,
                                marks={i: str(i) for i in range(600, 2001, 400)},
                                tooltip={"placement": "bottom", "always_visible": True}
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Figure Height (px)"),
                            dcc.Slider(
                                id={"type": "iq-height", "index": uid},
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
        id={"type": "copy-iq-plot", "index": uid},
        color="secondary",
        size="sm",
        className="mb-2"
    )
    
    # Store for base64 encoded image
    image_store = dcc.Store(id={"type": "iq-plot-image-store", "index": uid})
    
    # Summary section
    summary_content = html.Div([
        html.Div([
            html.H6("IQ Blob Summary", style={"display": "inline-block", "marginRight": "10px"}),
            dcc.Clipboard(
                id={"type": "copy-iq-summary", "index": uid},
                target_id={"type": "iq-summary-table-content", "index": uid},
                title="Copy summary to clipboard",
                style={"display": "inline-block", "verticalAlign": "middle"}
            )
        ], style={"marginBottom": "10px"}),
        html.Div(
            create_iq_blob_summary_table(data),
            id={"type": "iq-summary-table-content", "index": uid}
        )
    ])
    
    # Side panel
    side_panel = html.Div(
        id={"type": "iq-side-panel", "index": uid},
        children=[
            html.Div(
                dbc.Button(
                    "◀ Info",
                    id={"type": "toggle-iq-side-panel", "index": uid},
                    color="primary",
                    size="sm",
                    style={
                        "writingMode": "vertical-rl",
                        "textOrientation": "mixed",
                        "height": "100px",
                        "padding": "10px 5px"
                    }
                ),
                id={"type": "iq-side-toggle-container", "index": uid},
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
                id={"type": "iq-side-panel-content", "index": uid},
                children=[
                    summary_content,
                    html.Hr(),
                    html.H6("Measurement Info"),
                    html.Pre(f"Folder: {folder}\nQubits: {data['n']}"),
                    html.Hr(),
                    html.H6("IQ Blobs Description"),
                    html.P([
                        "The IQ Blobs measurement involves measuring the resonator state N times, ",
                        "first with the qubit in the |g⟩ state (after thermalization) and then ",
                        "in the |e⟩ state (after applying a π pulse). The resulting IQ blobs are ",
                        "analyzed to determine: (1) the rotation angle for optimal state separation ",
                        "along the I-quadrature, (2) the discrimination threshold between |g⟩ and |e⟩, ",
                        "(3) the RUS (Repeat Until Success) threshold for active reset, and ",
                        "(4) the readout confusion matrix indicating measurement fidelity."
                    ], style={"fontSize": "12px"}),
                    html.Hr(),
                    html.H6("Threshold Lines"),
                    html.Ul([
                        html.Li([html.B("Black dashed line:"), " RUS threshold (center of |g⟩ blob)"]),
                        html.Li([html.B("Red dashed line:"), " g-e discrimination threshold"]),
                    ], style={"fontSize": "11px"}),
                    html.Hr(),
                    html.H6("Confusion Matrix"),
                    html.P([
                        "Shows P(measured|prepared). Diagonal elements (gg, ee) represent ",
                        "correct state identification. Off-diagonal elements (ge, eg) show ",
                        "measurement errors. Readout fidelity = (gg + ee) / 2."
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
        dcc.Store(id={"type": "iq-data", "index": uid}, data={"folder": folder}),
        dcc.Store(id={"type": "iq-side-panel-state", "index": uid}, data={"is_open": False}),
        image_store,
        dbc.Row(dbc.Col(html.H3(f"IQ Blobs – {Path(folder).name}")), className="mb-3"),
        controls_accordion,
        dbc.Row([
            dbc.Col([
                copy_plot_btn,
                dcc.Loading(
                    dcc.Graph(
                        id={"type": "iq-plot", "index": uid},
                        figure=init_fig,
                        config={"displayModeBar": True}
                    )
                )
            ], width=12)
        ]),
        side_panel
    ])

def register_iq_blob_callbacks(app):
    """Register callbacks for IQ Blob visualization"""
    
    @app.callback(
        [Output({"type": "iq-plot", "index": MATCH}, "figure"),
         Output({"type": "iq-summary-table-content", "index": MATCH}, "children")],
        [Input({"type": "iq-mode", "index": MATCH}, "value"),
         Input({"type": "iq-cols", "index": MATCH}, "value"),
         Input({"type": "iq-width", "index": MATCH}, "value"),
         Input({"type": "iq-height", "index": MATCH}, "value")],
        State({"type": "iq-data", "index": MATCH}, "data"),
    )
    def update_iq_plot(plot_mode, n_cols, fig_w, fig_h, store):
        """Update IQ Blob plot based on user inputs"""
        data = load_iq_blob_data(store["folder"])
        
        if plot_mode == "confusion":
            fig = create_confusion_matrix_plot(data, n_cols=n_cols, fig_width=fig_w, fig_height=fig_h)
        elif plot_mode == "histogram":
            fig = create_histogram_plot(data, n_cols=n_cols, fig_width=fig_w, fig_height=fig_h)
        else:  # scatter
            fig = create_scatter_blob_plot(data, n_cols=n_cols, fig_width=fig_w, fig_height=fig_h)
        
        summary_table = create_iq_blob_summary_table(data)
        return fig, summary_table
    
    # Toggle side panel callback
    @app.callback(
        [Output({"type": "iq-side-panel-content", "index": MATCH}, "style"),
         Output({"type": "iq-side-toggle-container", "index": MATCH}, "style"),
         Output({"type": "toggle-iq-side-panel", "index": MATCH}, "children"),
         Output({"type": "iq-side-panel-state", "index": MATCH}, "data")],
        Input({"type": "toggle-iq-side-panel", "index": MATCH}, "n_clicks"),
        State({"type": "iq-side-panel-state", "index": MATCH}, "data"),
        prevent_initial_call=True
    )
    def toggle_iq_side_panel(n_clicks, state_data):
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
        Output({"type": "iq-plot-image-store", "index": MATCH}, "data"),
        Input({"type": "copy-iq-plot", "index": MATCH}, "n_clicks"),
        State({"type": "iq-plot", "index": MATCH}, "figure"),
        prevent_initial_call=True
    )
    def update_iq_image_store(n_clicks, current_figure):
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

# --------------------------------------------------------------------
# Example usage
# --------------------------------------------------------------------
if __name__ == "__main__":
    # Example: Create a simple Dash app to test the IQ Blob plotting tool
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    # Example folder path - replace with your actual data folder
    test_folder = "path/to/your/iq_blob_data"
    
    # Create layout
    app.layout = html.Div([
        create_iq_blob_layout(test_folder)
    ])
    
    # Register callbacks
    register_iq_blob_callbacks(app)
    
    # Run the app
    app.run_server(debug=True)