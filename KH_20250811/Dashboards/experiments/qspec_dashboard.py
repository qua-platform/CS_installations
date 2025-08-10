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
# xarray open_dataset with multiple engine attempts
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
# 1. Data Loader for Qubit Spectroscopy
# --------------------------------------------------------------------
def load_qubit_spec_data(folder):
    """Load qubit spectroscopy data from folder containing ds_raw.h5 and ds_fit.h5"""
    folder = os.path.normpath(folder)
    paths = {
        "ds_raw":  os.path.join(folder, "ds_raw.h5"),
        "ds_fit":  os.path.join(folder, "ds_fit.h5"),
        "data_js": os.path.join(folder, "data.json"),
        "node_js": os.path.join(folder, "node.json"),
    }
    
    if not all(os.path.exists(p) for p in paths.values()):
        print(f"[load_qubit_spec_data] missing file in {folder}")
        return None
    
    ds_raw = open_xr_dataset(paths["ds_raw"])
    ds_fit = open_xr_dataset(paths["ds_fit"])
    
    with open(paths["data_js"], "r", encoding="utf-8") as f:
        data_json = json.load(f)
    with open(paths["node_js"], "r", encoding="utf-8") as f:
        node_json = json.load(f)
    
    # Extract data arrays
    qubits        = ds_raw["qubit"].values
    full_freq_hz  = ds_raw["full_freq"].values       # shape (n_qubits, n_pts), Hz
    full_freq_ghz = full_freq_hz / 1e9               # GHz
    
    # IMPORTANT: For Qubit Spectroscopy, use IQ_abs for amplitude and phase for phase
    IQ_abs_raw    = ds_raw["IQ_abs"].values * 1e3    # Convert to mV
    phase_raw     = ds_raw["phase"].values
    
    # Check if fitting was successful
    success       = ds_fit["success"].values if "success" in ds_fit else np.zeros(len(qubits), dtype=bool)
    
    # Get fit data if available
    IQ_abs_fit = None
    phase_fit = None
    
    if any(success):
        # Use IQ_abs from fit for successful fits
        IQ_abs_fit = ds_fit["IQ_abs"].values * 1e3 if "IQ_abs" in ds_fit else None
        phase_fit = ds_fit["phase"].values if "phase" in ds_fit else None
    
    # Get other fit parameters if available
    base_line = ds_fit["base_line"].values if "base_line" in ds_fit else None
    pos = ds_fit["position"].values if "position" in ds_fit else None
    width_fit = ds_fit["width"].values if "width" in ds_fit else None
    amp = ds_fit["amplitude"].values if "amplitude" in ds_fit else None
    res_freq = ds_fit["res_freq"].values if "res_freq" in ds_fit else None
    fwhm = ds_fit["fwhm"].values if "fwhm" in ds_fit else None
    
    return dict(
        qubits=qubits, 
        n=len(qubits),
        full_freq_hz=full_freq_hz, 
        full_freq_ghz=full_freq_ghz,
        IQ_abs_raw=IQ_abs_raw, 
        phase_raw=phase_raw,
        IQ_abs_fit=IQ_abs_fit,
        phase_fit=phase_fit,
        success=success,
        base_line=base_line,
        pos=pos, 
        width_fit=width_fit, 
        amp=amp,
        res_freq=res_freq, 
        fwhm=fwhm,
    )

# --------------------------------------------------------------------
# 2. Lorentzian helper (kept for potential fitting display)
# --------------------------------------------------------------------
def lorentzian(x, x0, gamma, A, offset):
    return offset - A * (gamma/2)**2 / ((x - x0)**2 + (gamma/2)**2)

# --------------------------------------------------------------------
# 3. Peak Detection Functions for Qubit Spectroscopy (Broader Peaks)
# --------------------------------------------------------------------
def find_amplitude_peaks_qubit(x_ghz, y_data, max_peaks=5, prominence_threshold=0.0005, min_distance=10):
    """Find multiple peaks (minima) in the amplitude data for qubit spectroscopy
    Note: Uses broader peak detection parameters suitable for qubit spectroscopy"""
    try:
        # For amplitude, we're looking for minima (inverted peaks)
        inverted = -y_data
        peaks, properties = find_peaks(
            inverted, 
            prominence=prominence_threshold,
            distance=min_distance  # Smaller distance for broader peaks
        )
        
        if len(peaks) > 0:
            # Sort by prominence and take top N peaks
            prominences = properties['prominences']
            sorted_indices = np.argsort(prominences)[::-1][:max_peaks]
            peak_indices = peaks[sorted_indices]
            
            # Sort by frequency for consistent display
            peak_indices = np.sort(peak_indices)
            
            # Return lists of frequencies and values
            peak_freqs = x_ghz[peak_indices]
            peak_vals = y_data[peak_indices]
            return peak_freqs.tolist(), peak_vals.tolist()
        return [], []
    except Exception as e:
        print(f"Error finding amplitude peaks: {e}")
        return [], []

def find_phase_diff_peaks_qubit(x_ghz, phase_data, max_peaks=5, prominence_threshold=0.0005, min_distance=10):
    """Find multiple peaks in the differential phase data for qubit spectroscopy
    Note: Adapted for broader features in qubit spectroscopy"""
    try:
        # Calculate differential with smoothing for broader peaks
        kernel = np.ones(3) / 3  # Light smoothing
        phase_smoothed = np.convolve(phase_data, kernel, mode='same')
        phase_diff = np.diff(phase_smoothed, prepend=phase_smoothed[0])
        
        abs_diff = np.abs(phase_diff)
        peaks, properties = find_peaks(
            abs_diff, 
            prominence=prominence_threshold,
            distance=min_distance
        )
        
        if len(peaks) > 0:
            prominences = properties['prominences']
            sorted_indices = np.argsort(prominences)[::-1][:max_peaks]
            peak_indices = peaks[sorted_indices]
            
            # Sort by frequency for consistent display
            peak_indices = np.sort(peak_indices)
            
            peak_freqs = x_ghz[peak_indices]
            peak_vals = phase_diff[peak_indices]
            return peak_freqs.tolist(), peak_vals.tolist()
        return [], []
    except Exception as e:
        print(f"Error finding phase diff peaks: {e}")
        return [], []

# --------------------------------------------------------------------
# 4. Plot Generation with Peak Detection for Qubit Spectroscopy
# --------------------------------------------------------------------
def create_qubit_spec_plots(
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
    legend_x: float = 0.98,
    legend_y: float = 1.0,
    legend_xanchor: str = "right",
    legend_yanchor: str = "bottom",
    legend_orientation: str = "h",
    show_peaks: bool = True,
    max_peaks: int = 5,
    prominence_threshold: float = 0.0005,  # Lower threshold for broader peaks
    min_peak_distance: int = 10  # Smaller distance for broader peaks
):
    if not data:
        return go.Figure(), {}
    
    n_q    = data["n"]
    n_cols = max(1, min(n_cols, n_q))
    n_rows = ceil(n_q / n_cols)
    
    specs = [[{"secondary_y": True} for _ in range(n_cols)]
             for _ in range(n_rows)]
    
    # Store lists of peak information
    peaks_info = {
        'qubits': [],
        'amp_peak_freqs': [],
        'amp_peak_vals': [],
        'phase_diff_peak_freqs': [],
        'phase_diff_peak_vals': []
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
        amp_peak_freqs = []
        amp_peak_vals = []
        phase_diff_peak_freqs = []
        phase_diff_peak_vals = []
        
        # Phase processing
        phase_data = data["phase_raw"][idx].copy()
        if unwrap:
            phase_data = np.unwrap(phase_data)
        if smooth:
            kernel = np.ones(smooth_window) / smooth_window
            phase_data = np.convolve(phase_data, kernel, mode='same')
        
        # Calculate differential for peak detection
        if smooth:
            kernel2 = np.ones(diff_smooth_window) / diff_smooth_window
            phase_data_diff = np.convolve(phase_data.copy(), kernel2, mode='same')
            phase_data_diff = np.diff(phase_data_diff, prepend=phase_data[0])
        else:
            phase_data_diff = np.diff(phase_data, prepend=phase_data[0])
        
        # Find phase differential peaks
        if show_peaks:
            phase_diff_peak_freqs, phase_diff_peak_vals = find_phase_diff_peaks_qubit(
                x_ghz, data["phase_raw"][idx],  # Use raw data for peak detection
                max_peaks=max_peaks,
                prominence_threshold=prominence_threshold,
                min_distance=min_peak_distance
            )
        
        # Prepare phase data for display
        if differentiate:
            phase_display = phase_data_diff
        else:
            phase_display = phase_data
        
        # Amplitude traces and peak detection
        if view in ("amplitude", "both"):
            # Plot raw amplitude data
            fig.add_trace(
                go.Scatter(
                    x=x_ghz, y=data["IQ_abs_raw"][idx],
                    mode="lines", line=dict(color="blue", width=1),
                    name="Amplitude (Raw)", legendgroup="amplitude",
                    showlegend=(idx == 0),
                ),
                row=r, col=c, secondary_y=False
            )
            
            # Plot fit data if available and successful
            if data["success"][idx] and data["IQ_abs_fit"] is not None:
                fig.add_trace(
                    go.Scatter(
                        x=x_ghz, y=data["IQ_abs_fit"][idx],
                        mode="lines", line=dict(color="red", width=2),
                        name="Amplitude (Fit)", legendgroup="fit",
                        showlegend=(idx == 0),
                    ),
                    row=r, col=c, secondary_y=False
                )
                
                # Find amplitude peaks in fit data
                if show_peaks:
                    amp_peak_freqs, amp_peak_vals = find_amplitude_peaks_qubit(
                        x_ghz, data["IQ_abs_fit"][idx],
                        max_peaks=max_peaks,
                        prominence_threshold=prominence_threshold,
                        min_distance=min_peak_distance
                    )
                    
                    # Add markers for each peak
                    for i, (pf, pv) in enumerate(zip(amp_peak_freqs, amp_peak_vals)):
                        mark_txt = f"Peak {i+1}: ({pf:.6f}, {pv:.3f})"
                        fig.add_trace(
                            go.Scatter(
                                x=[pf], y=[pv],
                                mode="markers",
                                marker=dict(
                                    color="red", 
                                    size=10 if i == 0 else 8,
                                    symbol="star" if i == 0 else "star-open"
                                ),
                                name=f"Amp Peak {i+1}" if idx == 0 else "",
                                legendgroup=f"amp_peak_{i}",
                                showlegend=(idx == 0 and i < 3),
                                text=mark_txt,
                                hovertemplate=mark_txt + "<extra></extra>"
                            ),
                            row=r, col=c, secondary_y=False
                        )
            else:
                # If no fit, find peaks in raw data
                if show_peaks:
                    amp_peak_freqs, amp_peak_vals = find_amplitude_peaks_qubit(
                        x_ghz, data["IQ_abs_raw"][idx],
                        max_peaks=max_peaks,
                        prominence_threshold=prominence_threshold,
                        min_distance=min_peak_distance
                    )
                    
                    # Add markers for each peak
                    for i, (pf, pv) in enumerate(zip(amp_peak_freqs, amp_peak_vals)):
                        mark_txt = f"Peak {i+1}: ({pf:.6f}, {pv:.3f})"
                        fig.add_trace(
                            go.Scatter(
                                x=[pf], y=[pv],
                                mode="markers",
                                marker=dict(
                                    color="blue", 
                                    size=10 if i == 0 else 8,
                                    symbol="star" if i == 0 else "star-open"
                                ),
                                name=f"Amp Peak {i+1} (Raw)" if idx == 0 else "",
                                legendgroup=f"amp_peak_raw_{i}",
                                showlegend=(idx == 0 and i < 3),
                                text=mark_txt,
                                hovertemplate=mark_txt + "<extra></extra>"
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
            # Plot raw phase
            phase_name = "Phase (Raw)" if not differentiate else "Phase Diff (Raw)"
            fig.add_trace(
                go.Scatter(
                    x=x_ghz, y=phase_display,
                    mode="lines", line=dict(color="green", width=1.5),
                    name=phase_name, 
                    legendgroup="phase",
                    showlegend=(idx == 0),
                ),
                row=r, col=c, secondary_y=True
            )
            
            # Plot fit phase if available and successful
            if data["success"][idx] and data["phase_fit"] is not None:
                phase_fit_data = data["phase_fit"][idx].copy()
                if unwrap:
                    phase_fit_data = np.unwrap(phase_fit_data)
                if smooth:
                    kernel = np.ones(smooth_window) / smooth_window
                    phase_fit_data = np.convolve(phase_fit_data, kernel, mode='same')
                
                if differentiate:
                    phase_fit_diff = np.diff(phase_fit_data, prepend=phase_fit_data[0])
                    if smooth:
                        kernel2 = np.ones(diff_smooth_window) / diff_smooth_window
                        phase_fit_diff = np.convolve(phase_fit_diff, kernel2, mode='same')
                    phase_fit_display = phase_fit_diff
                else:
                    phase_fit_display = phase_fit_data
                
                phase_fit_name = "Phase (Fit)" if not differentiate else "Phase Diff (Fit)"
                fig.add_trace(
                    go.Scatter(
                        x=x_ghz, y=phase_fit_display,
                        mode="lines", line=dict(color="darkgreen", width=2),
                        name=phase_fit_name,
                        legendgroup="phase_fit",
                        showlegend=(idx == 0),
                    ),
                    row=r, col=c, secondary_y=True
                )
            
            # Add phase differential peak markers
            if show_peaks and phase_diff_peak_freqs:
                for i, (pf, pv) in enumerate(zip(phase_diff_peak_freqs, phase_diff_peak_vals)):
                    phase_mark_text = f"Phase Peak {i+1}: ({pf:.6f}, {pv:.3f})"
                    fig.add_trace(
                        go.Scatter(
                            x=[pf], y=[pv] if differentiate else [0],  # Show at 0 if not displaying diff
                            mode="markers",
                            marker=dict(
                                color="green", 
                                size=10 if i == 0 else 8,
                                symbol="diamond" if i == 0 else "diamond-open"
                            ),
                            name=f"Phase Peak {i+1}" if idx == 0 else "",
                            legendgroup=f"phase_peak_{i}",
                            showlegend=(idx == 0 and i < 3),
                            text=phase_mark_text,
                            hovertemplate=phase_mark_text + "<extra></extra>"
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
        peaks_info['amp_peak_freqs'].append(amp_peak_freqs)
        peaks_info['amp_peak_vals'].append(amp_peak_vals)
        peaks_info['phase_diff_peak_freqs'].append(phase_diff_peak_freqs)
        peaks_info['phase_diff_peak_vals'].append(phase_diff_peak_vals)
        
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
            "Qubit Spectroscopy – "
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
# 5. Summary Tables for Qubit Spectroscopy
# --------------------------------------------------------------------
def create_qubit_summary_table(data):
    rows = []
    for i, q in enumerate(data["qubits"]):
        ok = bool(data["success"][i])
        res_freq_val = data['res_freq'][i] if data['res_freq'] is not None else None
        fwhm_val = data['fwhm'][i] if data['fwhm'] is not None else None
        
        rows.append(
            html.Tr([
                html.Td(q),
                html.Td(f"{res_freq_val/1e9:.6f}" if ok and res_freq_val is not None else "—"),
                html.Td(f"{fwhm_val/1e3:.1f}" if ok and fwhm_val is not None else "—"),
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

def create_qubit_peaks_table(peaks_info):
    """Create a compact table with highlighted paired frequencies for qubit spectroscopy"""
    if not peaks_info or 'qubits' not in peaks_info:
        return html.Div("No peak information available")
    
    def calculate_all_differences_with_pairing(amp_freqs, phase_freqs):
        """Calculate differences and return pairing information"""
        if not amp_freqs or not phase_freqs:
            return [], []
        
        # For each amp peak, find nearest phase peak
        pairings = []  # List of (amp_idx, phase_idx, diff_mhz)
        
        for amp_idx, amp_f in enumerate(amp_freqs):
            # Find the nearest phase peak
            min_dist = float('inf')
            nearest_phase_idx = 0
            for phase_idx, phase_f in enumerate(phase_freqs):
                dist = abs(amp_f - phase_f)
                if dist < min_dist:
                    min_dist = dist
                    nearest_phase_idx = phase_idx
            
            diff_mhz = (amp_f - phase_freqs[nearest_phase_idx]) * 1000
            pairings.append((amp_idx, nearest_phase_idx, diff_mhz))
        
        # Find orphan phases
        orphan_phases = []
        paired_phase_indices = [p[1] for p in pairings]
        for phase_idx, phase_f in enumerate(phase_freqs):
            if phase_idx not in paired_phase_indices:
                if amp_freqs:
                    nearest_amp = min(amp_freqs, key=lambda x: abs(x - phase_f))
                    if abs(nearest_amp - phase_f) * 1000 > 50:
                        orphan_phases.append(phase_idx)
        
        return pairings, orphan_phases
    
    # Define colors for pairing
    pair_colors = ["#EFC3C3", "#92F1EA", "#B99FED", "#96CEB4", "#FFEAA7", "#DDA0DD", "#98D8C8"]
    
    rows = []
    for i, q in enumerate(peaks_info['qubits']):
        amp_freqs = peaks_info['amp_peak_freqs'][i]
        phase_freqs = peaks_info['phase_diff_peak_freqs'][i]
        
        # Calculate pairings
        pairings, orphan_indices = calculate_all_differences_with_pairing(amp_freqs, phase_freqs)
        
        # Format amplitude frequencies with color coding
        amp_freq_elements = []
        if amp_freqs:
            for amp_idx, amp_f in enumerate(amp_freqs):
                # Find which pairing this amplitude is in
                pair_color = None
                for pair_idx, (a_idx, _, _) in enumerate(pairings):
                    if a_idx == amp_idx:
                        pair_color = pair_colors[pair_idx % len(pair_colors)]
                        break
                
                if pair_color:
                    amp_freq_elements.append(
                        html.Span(
                            f"{amp_f:.4f}",
                            style={
                                "backgroundColor": pair_color,
                                "padding": "2px 4px",
                                "borderRadius": "3px",
                                "marginRight": "4px",
                                "fontWeight": "bold"
                            }
                        )
                    )
                else:
                    amp_freq_elements.append(
                        html.Span(f"{amp_f:.4f}, ", style={"marginRight": "4px"})
                    )
        else:
            amp_freq_elements = ["—"]
        
        # Format phase frequencies with matching color coding
        phase_freq_elements = []
        if phase_freqs:
            for phase_idx, phase_f in enumerate(phase_freqs):
                # Find which pairing this phase is in
                pair_color = None
                for pair_idx, (_, p_idx, _) in enumerate(pairings):
                    if p_idx == phase_idx:
                        pair_color = pair_colors[pair_idx % len(pair_colors)]
                        break
                
                if pair_color:
                    phase_freq_elements.append(
                        html.Span(
                            f"{phase_f:.4f}",
                            style={
                                "backgroundColor": pair_color,
                                "padding": "2px 4px",
                                "borderRadius": "3px",
                                "marginRight": "4px",
                                "fontWeight": "bold"
                            }
                        )
                    )
                else:
                    # Unpaired phase peak
                    phase_freq_elements.append(
                        html.Span(
                            f"{phase_f:.4f}",
                            style={
                                "color": "#999",
                                "marginRight": "4px"
                            }
                        )
                    )
        else:
            phase_freq_elements = ["—"]
        
        # Format differences with matching colors
        diff_elements = []
        if pairings:
            for pair_idx, (_, _, diff_mhz) in enumerate(pairings):
                abs_d = abs(diff_mhz)
                # Color coding for difference magnitude (adjusted for qubit spectroscopy)
                diff_color = "green" if abs_d < 1 else "orange" if abs_d < 5 else "red"
                pair_bg = pair_colors[pair_idx % len(pair_colors)]
                
                diff_elements.append(
                    html.Span(
                        f"{diff_mhz:+.3f}",
                        style={
                            "color": diff_color,
                            "backgroundColor": pair_bg,
                            "padding": "2px 4px",
                            "borderRadius": "3px",
                            "marginRight": "4px",
                            "fontWeight": "bold"
                        }
                    )
                )
        else:
            diff_elements = ["—"]
        
        rows.append(
            html.Tr([
                html.Td(q),
                html.Td(f"{len(amp_freqs)}/{len(phase_freqs)}"),
                html.Td(html.Div(amp_freq_elements), style={"fontSize": "0.85em"}),
                html.Td(html.Div(phase_freq_elements), style={"fontSize": "0.85em"}),
                html.Td(html.Div(diff_elements)),
                html.Td(len(orphan_indices)),
            ])
        )
    
    header = html.Thead(html.Tr([
        html.Th("Qubit"),
        html.Th("A/P"),
        html.Th("Amp Freq [GHz]"),
        html.Th("Phase Freq [GHz]"),
        html.Th("Δf [MHz]", style={"color": "#0066cc"}),
        html.Th("Orphans"),
    ]))
    
    # Add legend (adjusted thresholds for qubit spectroscopy)
    legend = html.Div([
        html.Small("Matched pairs have same background color | "),
        html.Small("Difference colors: "),
        html.Span("●", style={"color": "green"}),
        html.Small(" <1MHz "),
        html.Span("●", style={"color": "orange"}),
        html.Small(" 1-5MHz "),
        html.Span("●", style={"color": "red"}),
        html.Small(" >5MHz"),
        html.Small(" | Gray = unpaired"),
    ], style={"marginTop": "5px", "fontSize": "0.85em"})
    
    return html.Div([
        dbc.Table([header, html.Tbody(rows)],
                 bordered=True, striped=True,
                 size="sm", responsive=True),
        legend
    ])

# --------------------------------------------------------------------
# 6. Layout + Callbacks for Qubit Spectroscopy
# --------------------------------------------------------------------
def create_qspec_layout(folder):
    uid  = folder.replace("\\","_").replace("/","_").replace(":","")
    data = load_qubit_spec_data(folder)
    if not data:
        return html.Div([dbc.Alert("Failed to load data", color="danger"), html.Pre(folder)])
    
    default_height = data["n"] * 400
    init_fig, init_peaks = create_qubit_spec_plots(
        data, view="amplitude", 
        fig_height=default_height, 
        vertical_spacing_px=20, 
        show_peaks=True
    )
    
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
                                id={"type":"qubit-view","index":uid},
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
                                id={"type":"qubit-cols","index":uid},
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
                                id={"type":"qubit-width","index":uid},
                                min=400, max=2000, step=100, value=1000,
                                marks={i:str(i) for i in range(400,2001,400)},
                                tooltip={"placement":"bottom","always_visible":True}
                            )
                        ]), width=4),
                        dbc.Col(html.Div([
                            html.Label("Figure Height (px)"),
                            dcc.Slider(
                                id={"type":"qubit-height","index":uid},
                                min=100, max=10101, step=100, value=default_height,
                                marks={i:str(i) for i in range(1000,10101,3000)},
                                tooltip={"placement":"bottom","always_visible":True}
                            )
                        ]), width=4),
                        dbc.Col(html.Div([
                            html.Label("Vertical Spacing (px)"),
                            dcc.Slider(
                                id={"type":"qubit-vspacing","index":uid},
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
                                id={"type":"qubit-phase-proc","index":uid},
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
                                id={"type":"qubit-smooth-window","index":uid},
                                min=1, max=61, step=5, value=6,
                                marks={i:str(i) for i in range(1,62,20)},
                                tooltip={"placement":"bottom","always_visible":False}
                            )
                        ]), width=4),
                        dbc.Col(html.Div([
                            html.Label("Derivative Smooth Window"),
                            dcc.Slider(
                                id={"type":"qubit-diff-smooth-window","index":uid},
                                min=1, max=61, step=5, value=6,
                                marks={i:str(i) for i in range(1,62,20)},
                                tooltip={"placement":"bottom","always_visible":False}
                            )
                        ]), width=4),
                    ], align="center", className="mb-3"),
                    
                    # Row 4: Peak detection options with parameters suitable for qubit spectroscopy
                    dbc.Row([
                        dbc.Col(html.Div([
                            dcc.Checklist(
                                id={"type":"qubit-show-peaks","index":uid},
                                options=[
                                    {"label":"Show Peak Detection","value":"show_peaks"},
                                ],
                                value=["show_peaks"], inline=True, className="dark-radio"
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Max Peaks"),
                            dcc.Slider(
                                id={"type":"qubit-max-peaks","index":uid},
                                min=1, max=10, step=1, value=5,
                                marks={i:str(i) for i in range(1,11,2)},
                                tooltip={"placement":"bottom","always_visible":False}
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Prominence Threshold"),
                            dcc.Slider(
                                id={"type":"qubit-prominence","index":uid},
                                min=0.0001, max=0.01, step=0.0001, value=0.0005,  # Lower default for broader peaks
                                marks={0.0001:"0.0001", 0.0005:"0.0005", 0.001:"0.001", 0.01:"0.01"},
                                tooltip={"placement":"bottom","always_visible":False}
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Min Peak Distance"),
                            dcc.Slider(
                                id={"type":"qubit-peak-distance","index":uid},
                                min=5, max=100, step=5, value=10,  # Smaller default for broader peaks
                                marks={i:str(i) for i in range(10,101,30)},
                                tooltip={"placement":"bottom","always_visible":False}
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
    
    # Copy-plot button
    copy_plot_btn = dbc.Button(
        "Copy Plot to Clipboard",
        id={"type":"copy-plot-qubit","index":uid},
        color="secondary",
        size="sm",
        className="mb-2"
    )
    
    # Store for base64 encoded image
    image_store = dcc.Store(id={"type":"plot-image-store-qubit","index":uid})
    
    # Summary Table
    summary_content = html.Div([
        html.Div([
            html.H6("Summary Table", style={"display": "inline-block", "marginRight": "10px"}),
            dcc.Clipboard(
                id={"type":"copy-summary-qubit","index":uid},
                target_id={"type":"summary-table-content-qubit","index":uid},
                title="Copy summary to clipboard",
                style={"display": "inline-block", "verticalAlign": "middle"}
            )
        ], style={"marginBottom": "10px"}),
        html.Div(
            create_qubit_summary_table(data),
            id={"type":"summary-table-content-qubit","index":uid}
        )
    ])
    
    # Peak Detection Results
    peaks_content = html.Div([
        html.Div([
            html.H6("Peak Detection Results", style={"display": "inline-block", "marginRight": "10px"}),
            dcc.Clipboard(
                id={"type":"copy-peaks-qubit","index":uid},
                target_id={"type":"peaks-table-content-qubit","index":uid},
                title="Copy peaks to clipboard",
                style={"display": "inline-block", "verticalAlign": "middle"}
            )
        ], style={"marginBottom": "10px"}),
        html.Div(
            create_qubit_peaks_table(init_peaks),
            id={"type":"peaks-table-content-qubit","index":uid}
        )
    ])
    
    # Collapsible Side Panel Container
    side_panel = html.Div(
        id={"type":"side-panel-qubit","index":uid},
        children=[
            # Toggle button that appears on the side
            html.Div(
                dbc.Button(
                    "◀ Tables",
                    id={"type":"toggle-side-panel-qubit","index":uid},
                    color="primary",
                    size="sm",
                    style={
                        "writingMode": "vertical-rl",
                        "textOrientation": "mixed",
                        "height": "100px",
                        "padding": "10px 5px"
                    }
                ),
                id={"type":"side-toggle-container-qubit","index":uid},
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
                id={"type":"side-panel-content-qubit","index":uid},
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
        dcc.Store(id={"type":"qubit-data","index":uid}, data={"folder":folder}),
        dcc.Store(id={"type":"side-panel-state-qubit","index":uid}, data={"is_open": False}),
        image_store,
        dbc.Row(dbc.Col(html.H3(f"Qubit Spectroscopy – {Path(folder).name}")), className="mb-3"),
        controls_accordion,
        dbc.Row([
            dbc.Col([
                copy_plot_btn,
                dcc.Loading(
                    dcc.Graph(
                        id={"type":"qubit-plot","index":uid},
                        figure=init_fig,
                        config={"displayModeBar": True}
                    )
                )
            ], width=12)
        ]),
        side_panel
    ])

def register_qspec_callbacks(app):
    @app.callback(
        [Output({"type":"qubit-plot","index":MATCH},"figure"),
         Output({"type":"peaks-table-content-qubit","index":MATCH},"children")],
        Input({"type":"qubit-view",  "index":MATCH},"value"),
        Input({"type":"qubit-cols",  "index":MATCH},"value"),
        Input({"type":"qubit-width","index":MATCH},"value"),
        Input({"type":"qubit-height","index":MATCH},"value"),
        Input({"type":"qubit-vspacing","index":MATCH},"value"),
        Input({"type":"qubit-phase-proc","index":MATCH},"value"),
        Input({"type":"qubit-smooth-window","index":MATCH},"value"),
        Input({"type":"qubit-diff-smooth-window","index":MATCH},"value"),
        Input({"type":"qubit-show-peaks","index":MATCH},"value"),
        Input({"type":"qubit-max-peaks","index":MATCH},"value"),
        Input({"type":"qubit-prominence","index":MATCH},"value"),
        Input({"type":"qubit-peak-distance","index":MATCH},"value"),
        State({"type":"qubit-data",  "index":MATCH},"data"),
    )
    def update_qubit_plot(view_mode, n_cols, fig_w, fig_h, v_spacing, proc_modes, 
                          smooth_w, diff_smooth_w, show_peaks_list,
                          max_peaks, prominence, peak_distance, store):
        data = load_qubit_spec_data(store["folder"])
        unwrap_flag = 'unwrap' in proc_modes if proc_modes else False
        smooth_flag = 'smooth' in proc_modes if proc_modes else False
        diff_flag   = 'diff'   in proc_modes if proc_modes else False
        show_peaks  = 'show_peaks' in show_peaks_list if show_peaks_list else False
        
        fig, peaks_info = create_qubit_spec_plots(
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
            show_peaks=show_peaks,
            max_peaks=max_peaks,
            prominence_threshold=prominence,
            min_peak_distance=peak_distance
        )
        
        # Create peaks table content
        peaks_table_content = create_qubit_peaks_table(peaks_info)
        
        return fig, peaks_table_content
    
    # Callback for toggling the side panel
    @app.callback(
        [Output({"type":"side-panel-content-qubit","index":MATCH}, "style"),
         Output({"type":"side-toggle-container-qubit","index":MATCH}, "style"),
         Output({"type":"toggle-side-panel-qubit","index":MATCH}, "children"),
         Output({"type":"side-panel-state-qubit","index":MATCH}, "data")],
        Input({"type":"toggle-side-panel-qubit","index":MATCH}, "n_clicks"),
        State({"type":"side-panel-state-qubit","index":MATCH}, "data"),
        prevent_initial_call=True
    )
    def toggle_side_panel_qubit(n_clicks, state_data):
        is_open = state_data.get("is_open", False) if state_data else False
        
        if n_clicks:
            is_open = not is_open
        
        if is_open:
            # Panel is open
            panel_style = {
                "position": "fixed",
                "right": "0",
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
                "right": "550px",
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
            button_text = "◀ Tables"
        
        return panel_style, toggle_style, button_text, {"is_open": is_open}
    
    # Callback to update image store when copy button is clicked
    @app.callback(
        Output({"type":"plot-image-store-qubit","index":MATCH},"data"),
        Input({"type":"copy-plot-qubit","index":MATCH}, "n_clicks"),
        State({"type":"qubit-plot","index":MATCH},"figure"),
        prevent_initial_call=True
    )
    def update_image_store_qubit(n_clicks, current_figure):
        if n_clicks and current_figure:
            try:
                # Convert the current figure to base64 encoded PNG image
                fig = go.Figure(current_figure)
                
                # Extract the width and height from the current figure layout
                width = current_figure.get('layout', {}).get('width', 800)
                height = current_figure.get('layout', {}).get('height', 600)
                
                # If width is None (autosize), use a default
                if width is None:
                    width = 800
                if height is None:
                    height = 600
                
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
    
    # Clientside callback for copying plot to clipboard
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
                                        const btn = document.querySelector('[id*="copy-plot-qubit"]');
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
        Output({"type":"copy-plot-qubit","index":MATCH}, "children"),
        Input({"type":"plot-image-store-qubit","index":MATCH}, "data"),
        State({"type":"copy-plot-qubit","index":MATCH}, "n_clicks"),
    )