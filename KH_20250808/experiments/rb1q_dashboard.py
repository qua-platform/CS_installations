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
# RB fitting functions
# --------------------------------------------------------------------
def decay_exp(x: np.ndarray, a: float, offset: float, decay: float) -> np.ndarray:
    """
    RB decay model – offset + a·exp(decay·x)
    
    Parameters:
    - x: circuit depth (number of Clifford gates)
    - a: amplitude
    - offset: baseline offset (should be around 0.5 for RB)
    - decay: decay rate (related to gate fidelity)
    """
    return offset + a * np.exp(decay * x)

# --------------------------------------------------------------------
# 1. Data Loader for Randomized Benchmarking measurements
# --------------------------------------------------------------------
def load_rb_data(folder: str | Path) -> dict | None:
    """
    Load RB result files (ds_raw.h5, ds_fit.h5, data.json, node.json)
    from folder and return in dict format ready for use in plotting.
    
    Returns:
    --------
    Dictionary containing:
    - qubits: array of qubit names
    - n: number of qubits
    - depths: array of circuit depths
    - y_data: averaged data for each qubit (shape: n_qubits x n_depths)
    - success: fit success status for each qubit
    - rb_fidelity: RB fidelity in percent (100 * (1 - error_per_gate))
    - fit_a/offset/decay: fit parameters
    - error_per_clifford: error per Clifford gate
    - error_per_gate: error per single gate
    - ds_raw, ds_fit: original datasets
    - data_json, node_json: metadata
    """
    folder = Path(folder).expanduser().resolve()
    paths = {
        "ds_raw": folder / "ds_raw.h5",
        "ds_fit": folder / "ds_fit.h5",
        "data_js": folder / "data.json",
        "node_js": folder / "node.json",
    }
    
    if not all(p.exists() for p in paths.values()):
        print(f"[load_rb_data] Required files not found in {folder}")
        return None
    
    # ── File loading ─────────────────────────────────────────────────
    ds_raw = open_xr_dataset(str(paths["ds_raw"]))
    ds_fit = open_xr_dataset(str(paths["ds_fit"]))
    data_js = json.loads(paths["data_js"].read_text(encoding="utf-8"))
    node_js = json.loads(paths["node_js"].read_text(encoding="utf-8"))
    
    # Extract qubit information
    qubits = ds_fit.get("qubit", ds_raw["qubit"]).values.astype(str)
    n_q = len(qubits)
    
    # ── depth axis (circuit depths) ────────────────────────────────────
    depths = (
        ds_fit.coords["depths"]
        if "depths" in ds_fit.coords
        else ds_fit.coords.get("circuit_depth", None)
    )
    if depths is None:
        raise KeyError("'depths' coordinate not found in dataset.")
    depths = depths.values.astype(float)
    
    # ── Average state data (y-axis) ────────────────────────────────────
    if "averaged_data" in ds_fit:
        y_data = ds_fit["averaged_data"].values  # (q, d)
    elif "averaged_data" in ds_raw:
        y_data = ds_raw["averaged_data"].values  # (q, d)
    elif "state" in ds_fit:  # (q, seq, d)
        y_data = ds_fit["state"].mean(dim="nb_of_sequences").values
    else:
        raise KeyError("averaged_data/state variable not found.")
    
    # ── Fitting parameters extraction ────────────────────────────────────
    def param_from(name: str) -> np.ndarray:
        """Extract parameter from fit_data or directly from dataset"""
        if "fit_data" in ds_fit:
            try:
                return ds_fit["fit_data"].sel(fit_vals=name).values
            except:
                pass
        return ds_fit.get(name, np.full(n_q, np.nan)).values
    
    fit_a = param_from("a")
    fit_offset = param_from("offset")
    fit_decay = param_from("decay")
    
    # ── Success status from data.json ───────────────────────────────────
    success = np.zeros(n_q, dtype=bool)
    error_per_clifford = np.full(n_q, np.nan)
    error_per_gate = np.full(n_q, np.nan)
    rb_fidelity = np.full(n_q, np.nan)
    
    # Extract from fit_results in data.json
    fit_results = data_js.get("fit_results", {})
    for i, q in enumerate(qubits):
        q_str = str(q)
        if q_str in fit_results:
            res = fit_results[q_str]
            # Check success flag
            if "success" in res:
                success[i] = bool(res["success"])
            
            # Extract error metrics
            if "error_per_clifford" in res and res["error_per_clifford"] is not None:
                error_per_clifford[i] = float(res["error_per_clifford"])
            
            if "error_per_gate" in res and res["error_per_gate"] is not None:
                epg = float(res["error_per_gate"])
                error_per_gate[i] = epg
                # Calculate RB fidelity (in percent)
                if not np.isnan(epg) and success[i]:
                    rb_fidelity[i] = 100.0 * (1.0 - epg)
    
    # If success not available in JSON, derive from fit parameters
    if not any(success):
        success = ~np.isnan(fit_decay)
    
    # Extract error_per_clifford and error_per_gate from ds_fit if available
    if "error_per_clifford" in ds_fit:
        error_per_clifford_ds = ds_fit["error_per_clifford"].values
        # Use ds_fit values where JSON values are missing
        mask = np.isnan(error_per_clifford)
        error_per_clifford[mask] = error_per_clifford_ds[mask]
    
    if "error_per_gate" in ds_fit:
        error_per_gate_ds = ds_fit["error_per_gate"].values
        mask = np.isnan(error_per_gate)
        error_per_gate[mask] = error_per_gate_ds[mask]
        # Recalculate RB fidelity for updated values
        for i in range(n_q):
            if not np.isnan(error_per_gate[i]) and success[i]:
                rb_fidelity[i] = 100.0 * (1.0 - error_per_gate[i])
    
    return dict(
        qubits=qubits,
        n=n_q,
        depths=depths,
        y_data=y_data,
        success=success,
        rb_fidelity=rb_fidelity,
        error_per_clifford=error_per_clifford,
        error_per_gate=error_per_gate,
        fit_a=fit_a,
        fit_offset=fit_offset,
        fit_decay=fit_decay,
        ds_raw=ds_raw,
        ds_fit=ds_fit,
        data_json=data_js,
        node_json=node_js,
        fit_results=fit_results
    )

# --------------------------------------------------------------------
# 2. Plot Generation for Randomized Benchmarking measurements
# --------------------------------------------------------------------
def create_rb_plots(
    data,
    n_cols: int = 2,
    fig_width: int = None,
    fig_height: int = None,
    vertical_spacing_px: int = 20,
    legend_x: float = 0.98,
    legend_y: float = 1.02,
    legend_xanchor: str = "right",
    legend_yanchor: str = "bottom",
    legend_orientation: str = "h",
    show_only_successful: bool = False
):
    """
    Create RB plots with fits for multiple qubits.
    
    Parameters:
    -----------
    data: dict from load_rb_data
    n_cols: number of columns in subplot grid
    fig_width: figure width in pixels
    fig_height: figure height in pixels
    vertical_spacing_px: vertical spacing between subplots in pixels
    show_only_successful: if True, only show qubits with successful fits
    """
    
    if not data:
        return go.Figure()
    
    # Filter qubits if requested
    if show_only_successful:
        indices = [i for i in range(data["n"]) if data["success"][i]]
        if not indices:
            # No successful fits
            fig = go.Figure()
            fig.add_annotation(
                text="No successful fits found",
                xref="paper", yref="paper",
                x=0.5, y=0.5,
                showarrow=False,
                font=dict(size=20)
            )
            return fig
        qubits_to_plot = [data["qubits"][i] for i in indices]
        n_q = len(qubits_to_plot)
    else:
        indices = list(range(data["n"]))
        qubits_to_plot = data["qubits"]
        n_q = data["n"]
    
    n_cols = max(1, min(n_cols, n_q))
    n_rows = ceil(n_q / n_cols)
    
    # Compute ideal height
    SUBPLOT_HEIGHT_PX = 350
    TITLE_MARGIN_PX = 80
    BOTTOM_MARGIN_PX = 60
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
        vs_fraction = 0.03
    
    # Create subplot titles with fidelity info
    subplot_titles = []
    for idx, orig_idx in enumerate(indices):
        q = data["qubits"][orig_idx]
        if data["success"][orig_idx] and not np.isnan(data["rb_fidelity"][orig_idx]):
            fid = data["rb_fidelity"][orig_idx]
            subplot_titles.append(f"{q} (Fidelity: {fid:.2f}%)")
        else:
            subplot_titles.append(f"{q} (Fit Failed)")
    
    fig = subplots.make_subplots(
        rows=n_rows, cols=n_cols,
        subplot_titles=subplot_titles,
        vertical_spacing=vs_fraction,
        horizontal_spacing=0.08
    )
    
    # Maximum valid fidelity threshold (to filter unrealistic values)
    MAX_VALID_FIDELITY = 99.99
    
    # Add traces for each qubit
    for plot_idx, orig_idx in enumerate(indices):
        r, c = divmod(plot_idx, n_cols)
        r += 1
        c += 1
        
        q = data["qubits"][orig_idx]
        depths = data["depths"]
        y_data = data["y_data"][orig_idx, :]
        
        # Add raw data points (markers)
        fig.add_trace(
            go.Scatter(
                x=depths,
                y=y_data,
                mode="markers",
                marker=dict(size=6, color="royalblue"),
                name="Data",
                legendgroup="raw",
                showlegend=(plot_idx == 0),  # Show legend only for first subplot
            ),
            row=r, col=c
        )
        
        # Add fit curve if successful
        fid_val = data["rb_fidelity"][orig_idx]
        fit_valid = (
            bool(data["success"][orig_idx]) and 
            not np.isnan(data["fit_decay"][orig_idx]) and 
            not (fid_val >= MAX_VALID_FIDELITY)  # Filter unrealistic values
        )
        
        if fit_valid:
            # Generate smooth fit curve
            x_fit = np.linspace(depths.min(), depths.max(), 500)
            y_fit = decay_exp(
                x_fit,
                data["fit_a"][orig_idx],
                data["fit_offset"][orig_idx],
                data["fit_decay"][orig_idx]
            )
            
            fig.add_trace(
                go.Scatter(
                    x=x_fit,
                    y=y_fit,
                    mode="lines",
                    line=dict(color="firebrick", dash="dash", width=2),
                    name="Fit",
                    legendgroup="fit",
                    showlegend=(plot_idx == 0),  # Show legend only for first subplot
                ),
                row=r, col=c
            )
            
            # Add annotation with RB metrics
            error_gate = data["error_per_gate"][orig_idx]
            error_cliff = data["error_per_clifford"][orig_idx]
            
            if not np.isnan(error_gate):
                annotation_text = (
                    f"Fidelity: {fid_val:.2f}%<br>"
                    f"Error/gate: {error_gate:.2e}<br>"
                    f"Error/Clifford: {error_cliff:.2e}"
                )
                bg_color = "rgba(144, 238, 144, 0.3)"  # Light green
                border_color = "green"
            else:
                annotation_text = "Fit parameters invalid"
                bg_color = "rgba(255, 255, 200, 0.3)"  # Light yellow
                border_color = "orange"
        else:
            annotation_text = "Fit Failed"
            bg_color = "rgba(255, 200, 200, 0.3)"  # Light red
            border_color = "red"
        
        # Add annotation box
        y_max = np.nanmax(y_data)
        y_min = np.nanmin(y_data)
        
        fig.add_annotation(
            text=annotation_text,
            xref=f"x{plot_idx+1 if plot_idx > 0 else ''}",
            yref=f"y{plot_idx+1 if plot_idx > 0 else ''}",
            x=depths.max() - (depths.max() - depths.min()) * 0.02,
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
            title_text="Circuit depth" if r == n_rows else None,
            row=r, col=c,
            showgrid=True,
        )
        fig.update_yaxes(
            title_text="Qubit state" if c == 1 else None,
            row=r, col=c,
            showgrid=True,
            range=[0, 1]  # RB data typically ranges from 0 to 1
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
    layout_args = dict(
        title="Single-qubit Randomized Benchmarking",
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
# 3. Summary Table for RB measurements
# --------------------------------------------------------------------
def create_rb_summary_table(data):
    """
    Create summary table showing RB fidelity, error rates, and fit success.
    Table is colored based on success status.
    """
    rows = []
    
    for i, q in enumerate(data["qubits"]):
        success = bool(data["success"][i])
        fidelity = data["rb_fidelity"][i]
        error_gate = data["error_per_gate"][i]
        error_cliff = data["error_per_clifford"][i]
        
        # Format values
        if success and not np.isnan(fidelity):
            fid_str = f"{fidelity:.2f}%"
            # Determine quality based on fidelity
            if fidelity >= 99.9:
                row_class = "table-success"
                quality = "Excellent"
            elif fidelity >= 99.5:
                row_class = "table-info"
                quality = "Good"
            elif fidelity >= 99.0:
                row_class = "table-warning"
                quality = "Fair"
            else:
                row_class = "table-warning"
                quality = "Poor"
        else:
            fid_str = "—"
            row_class = "table-danger"
            quality = "Failed"
        
        # Format error values
        if not np.isnan(error_gate):
            error_gate_str = f"{error_gate:.2e}"
        else:
            error_gate_str = "—"
        
        if not np.isnan(error_cliff):
            error_cliff_str = f"{error_cliff:.2e}"
        else:
            error_cliff_str = "—"
        
        # Status indicator
        if success:
            status = "✓"
        else:
            status = "✗"
        
        rows.append(
            html.Tr([
                html.Td(str(q)),
                html.Td(fid_str),
                html.Td(error_gate_str),
                html.Td(error_cliff_str),
                html.Td(quality),
                html.Td(status, style={"textAlign": "center"}),
            ], className=row_class)
        )
    
    # Calculate statistics for successful fits
    successful_fidelities = [
        data["rb_fidelity"][i] 
        for i in range(data["n"]) 
        if data["success"][i] and not np.isnan(data["rb_fidelity"][i])
    ]
    
    if successful_fidelities:
        avg_fidelity = np.mean(successful_fidelities)
        std_fidelity = np.std(successful_fidelities)
        min_fidelity = np.min(successful_fidelities)
        max_fidelity = np.max(successful_fidelities)
        
        # Add statistics row
        rows.append(
            html.Tr([
                html.Td(html.B("Statistics"), colSpan=6, style={"textAlign": "center"}),
            ], className="table-secondary")
        )
        rows.append(
            html.Tr([
                html.Td("Average"),
                html.Td(f"{avg_fidelity:.2f}%"),
                html.Td("—"),
                html.Td("—"),
                html.Td(f"σ = {std_fidelity:.2f}%"),
                html.Td(f"{len(successful_fidelities)}/{data['n']}"),
            ], className="table-info")
        )
        rows.append(
            html.Tr([
                html.Td("Min/Max"),
                html.Td(f"{min_fidelity:.2f}% / {max_fidelity:.2f}%"),
                html.Td("—"),
                html.Td("—"),
                html.Td("—"),
                html.Td("—"),
            ], className="table-info")
        )
    
    header = html.Thead(html.Tr([
        html.Th("Qubit"),
        html.Th("RB Fidelity"),
        html.Th("Error/Gate"),
        html.Th("Error/Clifford"),
        html.Th("Quality"),
        html.Th("Fit", style={"textAlign": "center"})
    ]))
    
    return dbc.Table(
        [header, html.Tbody(rows)],
        bordered=True,
        striped=True,
        size="sm",
        responsive=True,
        hover=True
    )

# --------------------------------------------------------------------
# 4. Layout + Callbacks for RB measurements
# --------------------------------------------------------------------
def create_rb_layout(folder):
    """Create the complete layout for RB visualization"""
    uid = folder.replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_rb_data(folder)
    
    if not data:
        return html.Div([
            dbc.Alert("Failed to load Randomized Benchmarking data", color="danger"),
            html.Pre(folder)
        ])
    
    default_height = 400 * ceil(data["n"] / 2)  # 2 columns by default
    init_fig = create_rb_plots(data, n_cols=2, fig_height=default_height)
    
    # Controls
    controls_accordion = dbc.Accordion(
        [
            dbc.AccordionItem(
                title="Display Options",
                children=[
                    dbc.Row([
                        dbc.Col(html.Div([
                            html.Label("Filter Qubits"),
                            dcc.Dropdown(
                                id={"type": "rb-filter", "index": uid},
                                options=[
                                    {"label": "Show All Qubits", "value": "all"},
                                    {"label": "Show Only Successful Fits", "value": "success"}
                                ],
                                value="all",
                                clearable=False
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Columns per Row"),
                            dcc.Dropdown(
                                id={"type": "rb-cols", "index": uid},
                                options=[{"label": i, "value": i} for i in range(1, 5)],
                                value=2,
                                clearable=False
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Figure Width (px)"),
                            dcc.Slider(
                                id={"type": "rb-width", "index": uid},
                                min=600, max=2000, step=100, value=1200,
                                marks={i: str(i) for i in range(600, 2001, 400)},
                                tooltip={"placement": "bottom", "always_visible": True}
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Figure Height (px)"),
                            dcc.Slider(
                                id={"type": "rb-height", "index": uid},
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
        id={"type": "copy-rb-plot", "index": uid},
        color="secondary",
        size="sm",
        className="mb-2"
    )
    
    # Store for base64 encoded image
    image_store = dcc.Store(id={"type": "rb-plot-image-store", "index": uid})
    
    # Summary section
    summary_content = html.Div([
        html.Div([
            html.H6("RB Fidelity Summary", style={"display": "inline-block", "marginRight": "10px"}),
            dcc.Clipboard(
                id={"type": "copy-rb-summary", "index": uid},
                target_id={"type": "rb-summary-table-content", "index": uid},
                title="Copy summary to clipboard",
                style={"display": "inline-block", "verticalAlign": "middle"}
            )
        ], style={"marginBottom": "10px"}),
        html.Div(
            create_rb_summary_table(data),
            id={"type": "rb-summary-table-content", "index": uid}
        )
    ])
    
    # Measurement info from node.json
    measurement_info = ""
    if "data" in data.get("node_json", {}):
        if "parameters" in data["node_json"]["data"]:
            params = data["node_json"]["data"]["parameters"]
            measurement_info = f"""
Measurement Parameters:
- Max depth: {params.get('max_circuit_depth', 'N/A')}
- Number of sequences: {params.get('num_of_sequences', 'N/A')}
- Averages: {params.get('n_avg', 'N/A')}
"""
    
    # Side panel
    side_panel = html.Div(
        id={"type": "rb-side-panel", "index": uid},
        children=[
            html.Div(
                dbc.Button(
                    "◀ Info",
                    id={"type": "toggle-rb-side-panel", "index": uid},
                    color="primary",
                    size="sm",
                    style={
                        "writingMode": "vertical-rl",
                        "textOrientation": "mixed",
                        "height": "100px",
                        "padding": "10px 5px"
                    }
                ),
                id={"type": "rb-side-toggle-container", "index": uid},
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
                id={"type": "rb-side-panel-content", "index": uid},
                children=[
                    summary_content,
                    html.Hr(),
                    html.H6("Measurement Info"),
                    html.Pre(f"Folder: {Path(folder).name}\nQubits: {data['n']}\n{measurement_info}"),
                    html.Hr(),
                    html.H6("Randomized Benchmarking"),
                    html.P([
                        "Randomized Benchmarking (RB) consists of playing random sequences of Clifford gates ",
                        "and measuring the state of the qubit afterward. Each sequence ends with a recovery gate ",
                        "that brings the qubit back to its ground state. The gate fidelity is extracted by fitting ",
                        "the exponential decay of the measured state as a function of circuit depth. ",
                        "RB provides a robust measure of average gate fidelity that is insensitive to SPAM errors."
                    ], style={"fontSize": "12px"}),
                    html.Hr(),
                    html.H6("Quality Indicators"),
                    html.Ul([
                        html.Li("Excellent: Fidelity ≥ 99.9%", style={"color": "green"}),
                        html.Li("Good: Fidelity ≥ 99.5%", style={"color": "blue"}),
                        html.Li("Fair: Fidelity ≥ 99.0%", style={"color": "orange"}),
                        html.Li("Poor: Fidelity < 99.0%", style={"color": "darkorange"}),
                        html.Li("Failed: Fit unsuccessful", style={"color": "red"}),
                    ], style={"fontSize": "11px"}),
                    html.Hr(),
                    html.H6("Metrics Explained"),
                    html.Ul([
                        html.Li([
                            html.B("RB Fidelity: "),
                            "Average gate fidelity (1 - error_per_gate) × 100%"
                        ]),
                        html.Li([
                            html.B("Error/Gate: "),
                            "Average error per single-qubit gate"
                        ]),
                        html.Li([
                            html.B("Error/Clifford: "),
                            "Average error per Clifford operation"
                        ]),
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
        dcc.Store(id={"type": "rb-data", "index": uid}, data={"folder": folder}),
        dcc.Store(id={"type": "rb-side-panel-state", "index": uid}, data={"is_open": False}),
        image_store,
        dbc.Row(dbc.Col(html.H3(f"Randomized Benchmarking – {Path(folder).name}")), className="mb-3"),
        controls_accordion,
        dbc.Row([
            dbc.Col([
                copy_plot_btn,
                dcc.Loading(
                    dcc.Graph(
                        id={"type": "rb-plot", "index": uid},
                        figure=init_fig,
                        config={"displayModeBar": True}
                    )
                )
            ], width=12)
        ]),
        side_panel
    ])

def register_rb_callbacks(app):
    """Register callbacks for RB visualization"""
    
    @app.callback(
        [Output({"type": "rb-plot", "index": MATCH}, "figure"),
         Output({"type": "rb-summary-table-content", "index": MATCH}, "children")],
        Input({"type": "rb-filter", "index": MATCH}, "value"),
        Input({"type": "rb-cols", "index": MATCH}, "value"),
        Input({"type": "rb-width", "index": MATCH}, "value"),
        Input({"type": "rb-height", "index": MATCH}, "value"),
        State({"type": "rb-data", "index": MATCH}, "data"),
    )
    def update_rb_plot(filter_mode, n_cols, fig_w, fig_h, store):
        """Update RB plot based on user inputs"""
        data = load_rb_data(store["folder"])
        show_only_successful = (filter_mode == "success")
        
        fig = create_rb_plots(
            data,
            n_cols=n_cols,
            fig_width=fig_w,
            fig_height=fig_h,
            show_only_successful=show_only_successful
        )
        summary_table = create_rb_summary_table(data)
        return fig, summary_table
    
    # Toggle side panel callback
    @app.callback(
        [Output({"type": "rb-side-panel-content", "index": MATCH}, "style"),
         Output({"type": "rb-side-toggle-container", "index": MATCH}, "style"),
         Output({"type": "toggle-rb-side-panel", "index": MATCH}, "children"),
         Output({"type": "rb-side-panel-state", "index": MATCH}, "data")],
        Input({"type": "toggle-rb-side-panel", "index": MATCH}, "n_clicks"),
        State({"type": "rb-side-panel-state", "index": MATCH}, "data"),
        prevent_initial_call=True
    )
    def toggle_rb_side_panel(n_clicks, state_data):
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
        Output({"type": "rb-plot-image-store", "index": MATCH}, "data"),
        Input({"type": "copy-rb-plot", "index": MATCH}, "n_clicks"),
        State({"type": "rb-plot", "index": MATCH}, "figure"),
        prevent_initial_call=True
    )
    def update_rb_image_store(n_clicks, current_figure):
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
                                        const btn = document.querySelector('[id*="copy-rb-plot"]');
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
        Output({"type": "copy-rb-plot", "index": MATCH}, "children"),
        Input({"type": "rb-plot-image-store", "index": MATCH}, "data"),
        State({"type": "copy-rb-plot", "index": MATCH}, "n_clicks"),
    )

# --------------------------------------------------------------------
# Example usage
# --------------------------------------------------------------------
if __name__ == "__main__":
    # Example: Create a simple Dash app to test the RB plotting tool
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    # Example folder path - replace with your actual data folder
    test_folder = "path/to/your/rb_data"
    
    # Create layout
    app.layout = html.Div([
        create_rb_layout(test_folder)
    ])
    
    # Register callbacks
    register_rb_callbacks(app)
    
    # Run the app
    app.run_server(debug=True)