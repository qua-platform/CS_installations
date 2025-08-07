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
from scipy import signal
from scipy.signal import find_peaks

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
# 1. Data Loader
# --------------------------------------------------------------------
def load_res_data(folder):
    folder = os.path.normpath(folder)
    paths = {
        "ds_raw":  os.path.join(folder, "ds_raw.h5"),
        "ds_fit":  os.path.join(folder, "ds_fit.h5"),
        "data_js": os.path.join(folder, "data.json"),
        "node_js": os.path.join(folder, "node.json"),
    }
    if not all(os.path.exists(p) for p in paths.values()):
        print(f"[load_res_data] missing file in {folder}")
        return None
    
    ds_raw = open_xr_dataset(paths["ds_raw"])
    ds_fit = open_xr_dataset(paths["ds_fit"])
    
    with open(paths["data_js"], "r", encoding="utf-8") as f:
        data_json = json.load(f)
    with open(paths["node_js"], "r", encoding="utf-8") as f:
        node_json = json.load(f)
    
    qubits        = ds_raw["qubit"].values
    full_freq_hz  = ds_raw["full_freq"].values       # shape (n_qubits, n_pts), Hz
    full_freq_ghz = full_freq_hz / 1e9                 # GHz
    IQ_abs        = ds_raw["IQ_abs"].values * 1e3     # mV
    phase         = ds_raw["phase"].values
    success       = ds_fit["success"].values
    base_line     = ds_fit["base_line"].values
    pos           = ds_fit["position"].values
    width_fit     = ds_fit["width"].values
    amp           = ds_fit["amplitude"].values
    res_freq      = ds_fit["res_freq"].values        # Hz
    fwhm          = ds_fit["fwhm"].values            # Hz
    
    return dict(
        qubits=qubits, n=len(qubits),
        full_freq_hz=full_freq_hz, full_freq_ghz=full_freq_ghz,
        IQ_abs=IQ_abs, phase=phase,
        success=success, base_line=base_line,
        pos=pos, width_fit=width_fit, amp=amp,
        res_freq=res_freq, fwhm=fwhm,
    )

# --------------------------------------------------------------------
# 2. Lorentzian helper
# --------------------------------------------------------------------
def lorentzian(x, x0, gamma, A, offset):
    return offset - A * (gamma/2)**2 / ((x - x0)**2 + (gamma/2)**2)

# --------------------------------------------------------------------
# 3. Peak Detection Function
# --------------------------------------------------------------------
def find_amplitude_peak(x_fit_hz, y_fit):
    """Find the peak (minimum) in the amplitude fit curve"""
    try:
        # For amplitude, we're looking for the minimum (inverted peak)
        inverted = -y_fit
        peaks, properties = find_peaks(inverted, prominence=0.001)
        
        if len(peaks) > 0:
            # Get the most prominent peak
            prominences = properties['prominences']
            main_peak_idx = peaks[np.argmax(prominences)]
            return x_fit_hz[main_peak_idx] / 1e9, y_fit[main_peak_idx]
        return None, None
    except Exception as e:
        print(f"Error finding amplitude peak: {e}")
        return None, None

def find_phase_diff_peak(x_ghz, phase_data_diff):
    """Find the peak in the differential phase data"""
    try:
        # For phase differential, look for the maximum absolute value
        abs_diff = np.abs(phase_data_diff)
        peaks, properties = find_peaks(abs_diff, prominence=0.001)
        
        if len(peaks) > 0:
            # Get the most prominent peak
            prominences = properties['prominences']
            main_peak_idx = peaks[np.argmax(prominences)]
            return x_ghz[main_peak_idx], phase_data_diff[main_peak_idx]
        return None, None
    except Exception as e:
        print(f"Error finding phase diff peak: {e}")
        return None, None

# --------------------------------------------------------------------
# 4. Plot Generation with Peak Detection
# --------------------------------------------------------------------
def create_res_plots(
    data,
    view="amplitude",
    n_cols: int = 4,
    fig_width: int = None,
    fig_height: int = None,
    vertical_spacing_px: int = 20,
    unwrap: bool = False,
    smooth: bool = False,
    differentiate: bool = False,
    smooth_window: int = 11,
    diff_smooth_window: int = 11,
    legend_x: float = 1.00,
    legend_y: float = 1.00,
    legend_xanchor: str = "right",
    legend_yanchor: str = "bottom",
    legend_orientation: str = "h",
    show_peaks: bool = True  # New parameter for peak display
):
    if not data:
        return go.Figure(), {}
    
    n_q    = data["n"]
    n_cols = max(1, min(n_cols, n_q))
    n_rows = ceil(n_q / n_cols)
    
    specs = [[{"secondary_y": True} for _ in range(n_cols)]
             for _ in range(n_rows)]
    
    # Store peak information
    peaks_info = {
        'qubits': [],
        'amp_peak_freq': [],
        'amp_peak_val': [],
        'phase_diff_peak_freq': [],
        'phase_diff_peak_val': []
    }
    
    # ─── Compute ideal height ───
    SUBPLOT_HEIGHT_PX = 200
    TITLE_MARGIN_PX   = 80
    BOTTOM_MARGIN_PX  = 50
    total_spacing_px  = vertical_spacing_px * (n_rows - 1) if n_rows > 1 else 0
    ideal_height = (
        SUBPLOT_HEIGHT_PX * n_rows +
        total_spacing_px +
        TITLE_MARGIN_PX +
        BOTTOM_MARGIN_PX
    )
    effective_height = fig_height if fig_height else ideal_height
    
    # ─── Compute Plotly fraction for vertical spacing ───
    if n_rows > 1 and effective_height > 0:
        content_height = effective_height - TITLE_MARGIN_PX - BOTTOM_MARGIN_PX
        vs_fraction = vertical_spacing_px / content_height
        max_allowed = 1.0 / (n_rows - 1)
        if vs_fraction > max_allowed:
            vs_fraction = max_allowed * 0.9
            actual_px = vs_fraction * content_height
            print(f"Note: Spacing reduced from {vertical_spacing_px}px to ~{actual_px:.1f}px")
        vs_fraction = max(0.001, vs_fraction)
    else:
        vs_fraction = 0.02
    
    fig = subplots.make_subplots(
        rows=n_rows, cols=n_cols,
        specs=specs,
        subplot_titles=[str(q) for q in data["qubits"]],
        vertical_spacing=vs_fraction,
        horizontal_spacing=0.04,
        row_heights=None
    )
    
    # ─── Add traces ───
    for idx, q in enumerate(data["qubits"]):
        r, c = divmod(idx, n_cols)
        r += 1; c += 1
        x_ghz = data["full_freq_ghz"][idx]
        
        # Initialize peak info for this qubit
        peaks_info['qubits'].append(q)
        amp_peak_freq = None
        amp_peak_val = None
        phase_diff_peak_freq = None
        phase_diff_peak_val = None
        
        # Phase processing (always process for peak detection even if not displaying)
        phase_data = data["phase"][idx].copy()
        if unwrap:
            phase_data = np.unwrap(phase_data)
        if smooth:
            kernel = np.ones(smooth_window) / smooth_window
            phase_data = np.convolve(phase_data, kernel, mode='same')
        
        # Always calculate differential for peak detection
        kernel_ = np.ones(smooth_window) / smooth_window
        phase_data_ = np.convolve(phase_data.copy(), kernel_, mode='same')
        phase_data_diff = np.diff(phase_data_, prepend=phase_data[0])
        if smooth:
            kernel2 = np.ones(diff_smooth_window) / diff_smooth_window
            phase_data_diff = np.convolve(phase_data_diff, kernel2, mode='same')
        
        # Find phase differential peak
        if show_peaks:
            phase_diff_peak_freq, phase_diff_peak_val = find_phase_diff_peak(x_ghz, phase_data_diff)
        
        # Prepare phase data for display
        if differentiate:
            phase_display = phase_data_diff
        else:
            phase_display = phase_data
        
        # Amplitude traces and peak detection
        if view in ("amplitude", "both"):
            fig.add_trace(
                go.Scatter(
                    x=x_ghz, y=data["IQ_abs"][idx],
                    mode="lines", line=dict(color="blue", width=1),
                    name="Amplitude", legendgroup="amplitude",
                    showlegend=(idx == 0),
                ),
                row=r, col=c, secondary_y=False
            )
            
            if data["success"][idx] and not np.isnan(data["res_freq"][idx]):
                x_fit_hz = np.linspace(
                    data["full_freq_hz"][idx].min(),
                    data["full_freq_hz"][idx].max(), 500
                )
                baseline = np.interp(
                    x_fit_hz,
                    data["full_freq_hz"][idx],
                    data["base_line"][idx]
                )
                y_fit = lorentzian(
                    x_fit_hz,
                    data["res_freq"][idx],
                    data["width_fit"][idx],
                    data["amp"][idx],
                    baseline,
                ) * 1e3
                
                fig.add_trace(
                    go.Scatter(
                        x=x_fit_hz/1e9, y=y_fit,
                        mode="lines", line=dict(color="red", width=2),
                        name="Fit", legendgroup="fit",
                        showlegend=(idx == 0),
                    ),
                    row=r, col=c, secondary_y=False
                )
                
                # Find amplitude peak
                if show_peaks:
                    amp_peak_freq, amp_peak_val = find_amplitude_peak(x_fit_hz, y_fit)
                    if amp_peak_freq is not None:
                        fig.add_trace(
                            go.Scatter(
                                x=[amp_peak_freq], y=[amp_peak_val],
                                mode="markers",
                                marker=dict(color="red", size=10, symbol="star"),
                                name="Amp Peak", legendgroup="amp_peak",
                                showlegend=(idx == 0),
                                text=f"({amp_peak_freq:.6f}, {amp_peak_val:.3f})",
                                hovertemplate="%{text}<extra></extra>"
                            ),
                            row=r, col=c, secondary_y=False
                        )
            
            fig.update_yaxes(
                title_text="|IQ| [mV]" if c==1 else None,
                row=r, col=c, secondary_y=False,
                showgrid=True,
            )
        elif view == "phase":
            # Invisible primary trace for spacing
            fig.add_trace(
                go.Scatter(
                    x=[x_ghz[0], x_ghz[-1]],
                    y=[0, 0],
                    mode="lines",
                    line=dict(color="rgba(0,0,0,0)", width=0),
                    showlegend=False,
                    hoverinfo='skip',
                ),
                row=r, col=c, secondary_y=False
            )
            fig.update_yaxes(visible=False, row=r, col=c, secondary_y=False)
        
        # Phase traces on secondary
        if view in ("phase", "both"):
            fig.add_trace(
                go.Scatter(
                    x=x_ghz, y=-phase_display,
                    mode="lines", line=dict(color="green", width=1.5),
                    name="Phase" if not differentiate else "Phase Diff", 
                    legendgroup="phase",
                    showlegend=(idx == 0),
                ),
                row=r, col=c, secondary_y=True
            )
            
            # Add phase differential peak marker
            if show_peaks and phase_diff_peak_freq is not None:
                fig.add_trace(
                    go.Scatter(
                        x=[phase_diff_peak_freq], y=[-phase_diff_peak_val],
                        mode="markers",
                        marker=dict(color="green", size=10, symbol="diamond"),
                        name="Phase Diff Peak", legendgroup="phase_peak",
                        showlegend=(idx == 0),
                        text=f"({phase_diff_peak_freq:.6f}, {phase_diff_peak_val:.3f})",
                        hovertemplate="%{text}<extra></extra>"
                    ),
                    row=r, col=c, secondary_y=True
                )
            
            if view == "phase":
                fig.update_yaxes(
                    title_text="Phase [a.u]" if c==1 else None,
                    row=r, col=c, secondary_y=True,
                    showgrid=True,
                    side="left"
                )
            else:
                fig.update_yaxes(
                    title_text="Phase [a.u]" if c==n_cols else None,
                    row=r, col=c, secondary_y=True,
                    showgrid=False,
                    side="right"
                )
        
        # Store peak information
        peaks_info['amp_peak_freq'].append(amp_peak_freq)
        peaks_info['amp_peak_val'].append(amp_peak_val)
        peaks_info['phase_diff_peak_freq'].append(phase_diff_peak_freq)
        peaks_info['phase_diff_peak_val'].append(phase_diff_peak_val)
        
        fig.update_xaxes(
            title_text="Freq. [GHz]",
            row=r, col=c,
            showgrid=True,
        )
    
    # ─── Global styling ───
    fig.update_xaxes(
        gridcolor="rgba(0,0,0,0.2)", griddash="dash",
        zerolinecolor="rgba(0,0,0,0.2)", zerolinewidth=0.5,
        ticks="inside", ticklen=6,
        showline=True, linecolor="black", mirror=False,
    )
    fig.update_yaxes(
        gridcolor="rgba(0,0,0,0.2)", griddash="dash",
        zerolinecolor="rgba(0,0,0,0.2)", zerolinewidth=0.5,
        ticks="inside", ticklen=6,
        showline=True, linecolor="black", mirror=False,
    )
    
    # ─── Layout with controlled height + responsive width ───
    layout_args = dict(
        title=(
            "Resonator Spectroscopy – "
            + ("Amplitude" if view=="amplitude"
               else "Phase" if view=="phase"
               else "Amplitude & Phase")
        ),
        legend=dict(
            orientation=legend_orientation,
            yanchor=legend_yanchor,
            y=legend_y,
            xanchor=legend_xanchor,
            x=legend_x
        ),
        font=dict(size=11),
        title_font_size=14,
        autosize=True,
        margin=dict(t=TITLE_MARGIN_PX,
                    b=BOTTOM_MARGIN_PX,
                    l=60, r=60),
        height=effective_height
    )
    if fig_width:
        layout_args["width"] = fig_width
    
    fig.update_layout(**layout_args)
    return fig, peaks_info

# --------------------------------------------------------------------
# 5. Summary Tables (including peaks)
# --------------------------------------------------------------------
def create_summary_table(data):
    rows = []
    for i, q in enumerate(data["qubits"]):
        ok = bool(data["success"][i])
        rows.append(
            html.Tr([
                html.Td(q),
                html.Td(f"{data['res_freq'][i]/1e9:.6f}" if ok else "—"),
                html.Td(f"{data['fwhm'][i]/1e3:.1f}"   if ok else "—"),
                html.Td("✓" if ok else "✗"),
            ], className="table-success" if ok else "table-warning")
        )
    
    header = html.Thead(html.Tr([
        html.Th("Qubit"), html.Th("Res Freq [GHz]"),
        html.Th("FWHM [kHz]"), html.Th("Fit OK")
    ]))
    
    return dbc.Table([header, html.Tbody(rows)],
                     bordered=True, striped=True,
                     size="sm", responsive=True)

def create_peaks_table(peaks_info):
    """Create a table showing peak detection results"""
    if not peaks_info or 'qubits' not in peaks_info:
        return html.Div("No peak information available")
    
    rows = []
    for i, q in enumerate(peaks_info['qubits']):
        amp_freq = peaks_info['amp_peak_freq'][i]
        amp_val = peaks_info['amp_peak_val'][i]
        phase_freq = peaks_info['phase_diff_peak_freq'][i]
        phase_val = peaks_info['phase_diff_peak_val'][i]
        
        rows.append(
            html.Tr([
                html.Td(q),
                html.Td(f"{amp_freq:.6f}" if amp_freq is not None else "fail"),
                html.Td(f"{amp_val:.3f}" if amp_val is not None else "—"),
                html.Td(f"{phase_freq:.6f}" if phase_freq is not None else "fail"),
                html.Td(f"{phase_val:.3f}" if phase_val is not None else "—"),
            ])
        )
    
    header = html.Thead(html.Tr([
        html.Th("Qubit"), 
        html.Th("Amp Peak Freq [GHz]"),
        html.Th("Amp Peak Val [mV]"),
        html.Th("Phase Diff Peak Freq [GHz]"),
        html.Th("Phase Diff Peak Val [a.u]")
    ]))
    
    return dbc.Table([header, html.Tbody(rows)],
                     bordered=True, striped=True,
                     size="sm", responsive=True)

# --------------------------------------------------------------------
# 6. Layout + Callbacks with Collapsible Side Tables
# --------------------------------------------------------------------
def create_res_layout(folder):
    uid  = folder.replace("\\","_").replace("/","_").replace(":","")
    data = load_res_data(folder)
    if not data:
        return html.Div([dbc.Alert("Failed to load data", color="danger"), html.Pre(folder)])
    default_height = data["n"] * 400
    init_fig, init_peaks = create_res_plots(data, view="amplitude", fig_height=default_height, vertical_spacing_px=20, show_peaks=True)
    
    # Accordion grouping of controls
    controls_accordion = dbc.Accordion(
        [
            dbc.AccordionItem(
                title="Display Options",
                children=[
                    # Row 1: View mode and Columns
                    dbc.Row([
                        dbc.Col(
                            dcc.RadioItems(
                                id={"type":"res-view","index":uid},
                                options=[
                                    {"label":"Amplitude","value":"amplitude"},
                                    {"label":"Phase","value":"phase"},
                                    {"label":"Both","value":"both"},
                                ],
                                value="amplitude",
                                inline=True,
                                labelStyle={"display": "inline-block", "margin-right": "1rem"},
                                inputStyle={"margin-right": "0.3rem"},
                                className="dark-radio",
                                style={"padding": "0.5rem"}
                            ),
                            width=6
                        ),
                        dbc.Col(html.Div([
                            html.Label("Columns per Row"),
                            dcc.Dropdown(
                                id={"type":"res-cols","index":uid},
                                options=[{"label":i,"value":i} for i in range(1,9)],
                                value=1, clearable=False
                            )
                        ]), width=6),
                    ], align="center", className="mb-3"),
                    
                    # Row 2: Figure dimensions
                    dbc.Row([
                        dbc.Col(html.Div([
                            html.Label("Figure Width (px)"),
                            dcc.Slider(
                                id={"type":"res-width","index":uid},
                                min=400, max=2000, step=100, value=1000,
                                marks={i:str(i) for i in range(400,2001,400)},
                                tooltip={"placement":"bottom","always_visible":True}
                            )
                        ]), width=4),
                        dbc.Col(html.Div([
                            html.Label("Figure Height (px)"),
                            dcc.Slider(
                                id={"type":"res-height","index":uid},
                                min=100, max=10101, step=100, value=default_height,
                                marks={i:str(i) for i in range(1000,10101,3000)},
                                tooltip={"placement":"bottom","always_visible":True}
                            )
                        ]), width=4),
                        dbc.Col(html.Div([
                            html.Label("Vertical Spacing (px)"),
                            dcc.Slider(
                                id={"type":"res-vspacing","index":uid},
                                min=0, max=150, step=5, value=100,
                                marks={i:str(i) for i in range(0,151,30)},
                                tooltip={"placement":"bottom","always_visible":True}
                            ),
                            html.Small("Note: Spacing may be reduced for many rows to fit layout constraints", 
                                     className="text-muted")
                        ]), width=4),
                    ], align="center", className="mb-3"),
                    
                    # Row 3: Phase processing options
                    dbc.Row([
                        dbc.Col(html.Div([
                            html.Label("Phase Processing"),
                            dcc.Checklist(
                                id={"type":"res-phase-proc","index":uid},
                                options=[
                                    {"label":"Unwrap","value":"unwrap"},
                                    {"label":"Smooth","value":"smooth"},
                                    {"label":"Differentiate","value":"diff"},
                                ],
                                value=[], inline=True, className="dark-radio"
                            )
                        ]), width=4),
                        dbc.Col(html.Div([
                            html.Label("Smooth Window"),
                            dcc.Slider(
                                id={"type":"res-smooth-window","index":uid},
                                min=1, max=61, step=5, value=6,
                                marks={i:str(i) for i in range(1,62,20)},
                                tooltip={"placement":"bottom","always_visible":False}
                            )
                        ]), width=4),
                        dbc.Col(html.Div([
                            html.Label("Derivative Smooth Window"),
                            dcc.Slider(
                                id={"type":"res-diff-smooth-window","index":uid},
                                min=1, max=61, step=5, value=6,
                                marks={i:str(i) for i in range(1,62,20)},
                                tooltip={"placement":"bottom","always_visible":False}
                            )
                        ]), width=4),
                    ], align="center", className="mb-3"),
                    
                    # Row 4: Peak detection options
                    dbc.Row([
                        dbc.Col(html.Div([
                            dcc.Checklist(
                                id={"type":"res-show-peaks","index":uid},
                                options=[
                                    {"label":"Show Peak Detection","value":"show_peaks"},
                                ],
                                value=["show_peaks"], inline=True, className="dark-radio"
                            )
                        ]), width=12),
                    ], align="center", className="mb-3"),
                ]
            ),
        ],
        start_collapsed=True,
        flush=True,
        className="mb-4"
    )
    
    # Copy-plot button
    copy_plot_btn = dbc.Button(
        "Copy Plot to Clipboard",
        id={"type":"copy-plot","index":uid},
        color="secondary",
        size="sm",
        className="mb-2"
    )
    
    # Store for base64 encoded image
    image_store = dcc.Store(id={"type":"plot-image-store","index":uid})
    
    # Summary Table with Collapsible Side Panel
    summary_content = html.Div([
        html.Div([
            html.H6("Summary Table", style={"display": "inline-block", "marginRight": "10px"}),
            dcc.Clipboard(
                id={"type":"copy-summary","index":uid},
                target_id={"type":"summary-table-content","index":uid},
                title="Copy summary to clipboard",
                style={"display": "inline-block", "verticalAlign": "middle"}
            )
        ], style={"marginBottom": "10px"}),
        html.Div(
            create_summary_table(data),
            id={"type":"summary-table-content","index":uid}
        )
    ])

    # Peak Detection Results with Collapsible Side Panel
    peaks_content = html.Div([
        html.Div([
            html.H6("Peak Detection Results", style={"display": "inline-block", "marginRight": "10px"}),
            dcc.Clipboard(
                id={"type":"copy-peaks","index":uid},
                target_id={"type":"peaks-table-content","index":uid},
                title="Copy peaks to clipboard",
                style={"display": "inline-block", "verticalAlign": "middle"}
            )
        ], style={"marginBottom": "10px"}),
        html.Div(
            create_peaks_table(init_peaks),
            id={"type":"peaks-table-content","index":uid}
        )
    ])

    # Collapsible Side Panel Container
    side_panel = html.Div(
        id={"type":"side-panel","index":uid},
        children=[
            # Toggle button that appears on the side
            html.Div(
                dbc.Button(
                    "◀ Tables",
                    id={"type":"toggle-side-panel","index":uid},
                    color="primary",
                    size="sm",
                    style={
                        "writingMode": "vertical-rl",
                        "textOrientation": "mixed",
                        "height": "100px",
                        "padding": "10px 5px"
                    }
                ),
                id={"type":"side-toggle-container","index":uid},
                style={
                    "position": "fixed",
                    "right": "0",
                    "top": "50%",
                    "transform": "translateY(-50%)",
                    "zIndex": "1000",
                    "transition": "right 0.3s ease-in-out"
                }
            ),
            # Panel content
            html.Div(
                id={"type":"side-panel-content","index":uid},
                children=[
                    summary_content,
                    html.Hr(),
                    peaks_content,
                    html.Hr(),
                    html.H6("Load Folder"),
                    html.Pre(f"Folder: {folder}\nQubits: {data['n']}")
                ],
                style={
                    "position": "fixed",
                    "right": "-400px",  # Initially hidden
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
        dcc.Store(id={"type":"res-data","index":uid}, data={"folder":folder}),
        dcc.Store(id={"type":"side-panel-state","index":uid}, data={"is_open": False}),
        image_store,
        dbc.Row(dbc.Col(html.H3(f"Resonator Spectroscopy – {Path(folder).name}")), className="mb-3"),
        controls_accordion,
        dbc.Row([
            dbc.Col([
                copy_plot_btn,
                dcc.Loading(
                    dcc.Graph(
                        id={"type":"res-plot","index":uid},
                        figure=init_fig,
                        config={"displayModeBar": True}
                    )
                )
            ], width=12)  # Full width for plot
        ]),
        side_panel  # Add the collapsible side panel
    ])

def register_res_callbacks(app):
    @app.callback(
        [Output({"type":"res-plot","index":MATCH},"figure"),
         Output({"type":"peaks-table-content","index":MATCH},"children")],
        Input({"type":"res-view",  "index":MATCH},"value"),
        Input({"type":"res-cols",  "index":MATCH},"value"),
        Input({"type":"res-width","index":MATCH},"value"),
        Input({"type":"res-height","index":MATCH},"value"),
        Input({"type":"res-vspacing","index":MATCH},"value"),
        Input({"type":"res-phase-proc","index":MATCH},"value"),
        Input({"type":"res-smooth-window","index":MATCH},"value"),
        Input({"type":"res-diff-smooth-window","index":MATCH},"value"),
        Input({"type":"res-show-peaks","index":MATCH},"value"),
        State({"type":"res-data",  "index":MATCH},"data"),
    )
    def update_plot(view_mode, n_cols, fig_w, fig_h, v_spacing, proc_modes, 
                   smooth_w, diff_smooth_w, show_peaks_list, store):
        data = load_res_data(store["folder"])
        unwrap_flag = 'unwrap' in proc_modes if proc_modes else False
        smooth_flag = 'smooth' in proc_modes if proc_modes else False
        diff_flag   = 'diff'   in proc_modes if proc_modes else False
        show_peaks  = 'show_peaks' in show_peaks_list if show_peaks_list else False
        
        fig, peaks_info = create_res_plots(
            data,
            view=view_mode,
            n_cols=n_cols,
            fig_width=fig_w,
            fig_height=fig_h,
            vertical_spacing_px=v_spacing,
            unwrap=unwrap_flag,
            smooth=smooth_flag,
            differentiate=diff_flag,
            smooth_window=smooth_w,
            diff_smooth_window=diff_smooth_w,
            show_peaks=show_peaks
        )
        
        # Create peaks table content only
        peaks_table_content = create_peaks_table(peaks_info)
        
        return fig, peaks_table_content
    
    # New callback for toggling the side panel
    @app.callback(
        [Output({"type":"side-panel-content","index":MATCH}, "style"),
         Output({"type":"side-toggle-container","index":MATCH}, "style"),
         Output({"type":"toggle-side-panel","index":MATCH}, "children"),
         Output({"type":"side-panel-state","index":MATCH}, "data")],
        Input({"type":"toggle-side-panel","index":MATCH}, "n_clicks"),
        State({"type":"side-panel-state","index":MATCH}, "data"),
        prevent_initial_call=True
    )
    def toggle_side_panel(n_clicks, state_data):
        is_open = state_data.get("is_open", False) if state_data else False
        
        if n_clicks:
            is_open = not is_open
        
        if is_open:
            # Panel is open
            panel_style = {
                "position": "fixed",
                "right": "0",  # Slide in from right
                "top": "0",
                "width": "550px",
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
                "right": "550px",  # Move button with panel
                "top": "50%",
                "transform": "translateY(-50%)",
                "zIndex": "1000",
                "transition": "right 0.3s ease-in-out"
            }
            button_text = "▶ Tables"
        else:
            # Panel is closed
            panel_style = {
                "position": "fixed",
                "right": "-400px",  # Hide to the right
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
                "right": "0",  # Button at edge
                "top": "50%",
                "transform": "translateY(-50%)",
                "zIndex": "1000",
                "transition": "right 0.3s ease-in-out"
            }
            button_text = "◀ Tables"
        
        return panel_style, toggle_style, button_text, {"is_open": is_open}
    
    # Callback to update image store when copy button is clicked
    @app.callback(
        Output({"type":"plot-image-store","index":MATCH},"data"),
        Input({"type":"copy-plot","index":MATCH}, "n_clicks"),
        State({"type":"res-plot","index":MATCH},"figure"),
        prevent_initial_call=True
    )
    def update_image_store(n_clicks, current_figure):
        if n_clicks and current_figure:
            try:
                # Convert the current figure to base64 encoded PNG image
                fig = go.Figure(current_figure)
                
                # Extract the width and height from the current figure layout
                width = current_figure.get('layout', {}).get('width', 800)
                height = current_figure.get('layout', {}).get('height', 600)
                
                # If width is None (autosize), use a default or calculate from viewport
                if width is None:
                    width = 800  # Default width
                if height is None:
                    height = 600  # Default height
                
                try:
                    # Pass width and height explicitly to to_image
                    image_bytes_io = fig.to_image(
                        format="png", 
                        engine="kaleido",
                        width=width,
                        height=height
                    )
                except:
                    # Fallback to default engine if kaleido is not installed
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
    
    # ────────────────────────────────────────────────────────
    # CLIENTSIDE callback: copy the Plotly graph to clipboard
    # ────────────────────────────────────────────────────────
    app.clientside_callback(
        """
        function(stored_image_data, n_clicks) {
            if (n_clicks && stored_image_data) {
                // Create an image element from the base64 data
                const img = new Image();
                img.src = 'data:image/png;base64,' + stored_image_data;
                
                img.onload = function() {
                    // Create a canvas element
                    const canvas = document.createElement('canvas');
                    canvas.width = this.naturalWidth;
                    canvas.height = this.naturalHeight;
                    
                    // Draw the image on the canvas
                    const ctx = canvas.getContext('2d');
                    ctx.drawImage(this, 0, 0);
                    
                    // Convert canvas to blob and copy to clipboard
                    canvas.toBlob(function(blob) {
                        if (blob) {
                            const item = new ClipboardItem({'image/png': blob});
                            navigator.clipboard.write([item]).then(
                                function() {
                                    console.log('Image copied to clipboard successfully');
                                    // Change button text temporarily
                                    setTimeout(function() {
                                        const btn = document.querySelector('[id*="copy-plot"]');
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
                
                // Return a success message
                return "Copied!";
            }
            return "Copy Plot to Clipboard";
        }
        """,
        Output({"type":"copy-plot","index":MATCH}, "children"),
        Input({"type":"plot-image-store","index":MATCH}, "data"),
        State({"type":"copy-plot","index":MATCH}, "n_clicks"),
    )

# # --------------------------------------------------------------------
# # Example usage (for testing)
# # --------------------------------------------------------------------
# if __name__ == "__main__":
#     # Initialize the Dash app
#     app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    
#     # Example folder path - replace with your actual folder
#     folder_path = "/path/to/your/data/folder"
    
#     # Create the layout
#     app.layout = html.Div([
#         create_res_layout(folder_path)
#     ])
    
#     # Register callbacks
#     register_res_callbacks(app)
    
#     # Run the app
#     app.run_server(debug=True)
