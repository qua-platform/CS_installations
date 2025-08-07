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
# Ramsey fitting functions
# --------------------------------------------------------------------
def oscillation_decay_exp(t, a, f, phi, offset, decay):
    """
    Ramsey oscillation model: offset + a·exp(-decay·t)·cos(2πf·t + φ)
    
    Parameters:
    - t: time in nanoseconds
    - a: amplitude
    - f: frequency in cycles per nanosecond (will be converted to Hz later)
    - phi: phase in radians
    - offset: baseline offset
    - decay: decay rate (1/T2*)
    """
    return offset + a * np.exp(-decay * t) * np.cos(2.0 * np.pi * f * t + phi)

def guess_frequency(t, data):
    """Estimate frequency using FFT"""
    try:
        # Remove DC component and trend
        detrended = signal.detrend(data)
        
        # Apply window to reduce spectral leakage
        window = np.hanning(len(data))
        windowed = detrended * window
        
        # Compute FFT
        fft = np.fft.rfft(windowed)
        freqs = np.fft.rfftfreq(len(t), t[1] - t[0])
        
        # Find peak frequency (excluding DC)
        idx_peak = np.argmax(np.abs(fft[1:])) + 1
        freq_guess = freqs[idx_peak]
        
        return max(freq_guess, 1e-6)  # Ensure positive frequency
    except:
        # Fallback: simple zero-crossing method
        zero_crossings = np.where(np.diff(np.sign(data - np.mean(data))))[0]
        if len(zero_crossings) > 1:
            period = 2 * np.mean(np.diff(zero_crossings)) * (t[1] - t[0])
            return 1.0 / period if period > 0 else 1e-5
        return 1e-5

def guess_decay(t, data):
    """Estimate decay rate from envelope"""
    try:
        # Get envelope using Hilbert transform
        analytic_signal = signal.hilbert(data - np.mean(data))
        envelope = np.abs(analytic_signal)
        
        # Fit exponential to envelope
        if envelope[0] > 0:
            log_env = np.log(envelope + 1e-10)
            coeffs = np.polyfit(t, log_env, 1)
            decay_guess = -coeffs[0]
            return max(decay_guess, 1e-6)  # Ensure positive decay
    except:
        pass
    
    # Fallback: estimate from first and last points
    if len(data) > 10:
        first_avg = np.mean(np.abs(data[:5] - np.mean(data)))
        last_avg = np.mean(np.abs(data[-5:] - np.mean(data)))
        if first_avg > last_avg and first_avg > 0:
            decay_guess = -np.log(last_avg / first_avg) / (t[-1] - t[0])
            return max(decay_guess, 1e-6)
    
    return 1e-5  # Default small decay

def fit_ramsey_oscillation(t, data, use_existing_fit=None):
    """
    Fit Ramsey oscillation to data
    
    Returns: (success, fit_params, covariance)
    """
    try:
        # Initial parameter guesses
        offset_guess = np.mean(data)
        detrended = data - offset_guess
        amp_guess = (np.max(data) - np.min(data)) / 2
        freq_guess = guess_frequency(t, detrended)
        decay_guess = guess_decay(t, detrended)
        
        # Phase guess from first point
        if amp_guess > 0:
            phi_guess = np.arccos(np.clip(detrended[0] / amp_guess, -1, 1))
        else:
            phi_guess = 0
        
        # Use existing fit as initial guess if provided
        if use_existing_fit is not None:
            try:
                amp_guess = use_existing_fit.get('a', amp_guess)
                freq_guess = use_existing_fit.get('f', freq_guess)
                phi_guess = use_existing_fit.get('phi', phi_guess)
                offset_guess = use_existing_fit.get('offset', offset_guess)
                decay_guess = use_existing_fit.get('decay', decay_guess)
            except:
                pass
        
        # Bounds for parameters
        bounds = (
            [0, 0, -np.pi, -np.inf, 0],  # Lower bounds
            [np.inf, 1.0, np.pi, np.inf, 1.0]  # Upper bounds
        )
        
        # Perform fit with increased maxfev
        popt, pcov = curve_fit(
            oscillation_decay_exp,
            t,
            data,
            p0=[amp_guess, freq_guess, phi_guess, offset_guess, decay_guess],
            bounds=bounds,
            maxfev=10000
        )
        
        # Extract fitted parameters
        a_fit, f_fit, phi_fit, offset_fit, decay_fit = popt
        
        # Calculate T2* and its error
        if decay_fit > 0:
            t2_star_ns = 1.0 / decay_fit
            t2_star_us = t2_star_ns / 1000.0
            
            # Error propagation for T2*
            decay_error = np.sqrt(pcov[4, 4]) if pcov[4, 4] > 0 else 0
            t2_error_us = (t2_star_us * decay_error / decay_fit) if decay_fit > 0 else 0
        else:
            t2_star_us = np.inf
            t2_error_us = np.inf
        
        # Calculate residuals for quality check
        fitted_data = oscillation_decay_exp(t, *popt)
        residuals = np.sum((data - fitted_data) ** 2)
        total_variance = np.sum((data - np.mean(data)) ** 2)
        r_squared = 1 - (residuals / total_variance) if total_variance > 0 else 0
        
        # Success criteria
        success = (
            t2_star_us > 0.1 and  # T2* > 0.1 μs
            t2_star_us < 1000 and  # T2* < 1 ms (reasonable range)
            r_squared > 0.3 and  # Decent fit quality
            not np.any(np.isnan(popt)) and
            not np.any(np.isinf(popt))
        )
        
        return success, {
            'a': a_fit,
            'f': f_fit,
            'phi': phi_fit,
            'offset': offset_fit,
            'decay': decay_fit,
            't2_star_us': t2_star_us,
            't2_error_us': t2_error_us,
            'r_squared': r_squared
        }, pcov
        
    except Exception as e:
        print(f"Fit failed: {e}")
        return False, None, None

# --------------------------------------------------------------------
# 1. Data Loader for T2 Ramsey measurements
# --------------------------------------------------------------------
def load_t2_ramsey_data(folder):
    """Load T2 Ramsey data from folder"""
    folder = os.path.normpath(folder)
    paths = {
        "ds_raw":  os.path.join(folder, "ds_raw.h5"),
        "ds_fit":  os.path.join(folder, "ds_fit.h5"),
        "data_js": os.path.join(folder, "data.json"),
        "node_js": os.path.join(folder, "node.json"),
    }
    
    # Check if all files exist
    if not all(os.path.exists(p) for p in paths.values()):
        print(f"[load_t2_ramsey_data] missing file in {folder}")
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
    idle_time_ns = ds_raw["idle_time"].values
    idle_time_us = idle_time_ns / 1000.0
    detuning_signs = ds_raw["detuning_signs"].values if "detuning_signs" in ds_raw else [1]
    
    # Get I and Q data
    I_data = ds_raw["I"].values
    Q_data = ds_raw["Q"].values
    
    # Check original success flags from ds_fit
    original_success = ds_fit["success"].values if "success" in ds_fit else np.full(n_q, True)
    
    # Extract existing fit parameters if available
    existing_fits = {}
    if "fit" in ds_fit:
        fit_da = ds_fit["fit"]
        for i, q in enumerate(qubits):
            existing_fits[str(q)] = {}
            for j, sign in enumerate(detuning_signs):
                try:
                    existing_fits[str(q)][f"sign_{int(sign)}"] = {
                        'a': float(fit_da.sel(qubit=q, detuning_signs=sign, fit_vals='a').values),
                        'f': float(fit_da.sel(qubit=q, detuning_signs=sign, fit_vals='f').values),
                        'phi': float(fit_da.sel(qubit=q, detuning_signs=sign, fit_vals='phi').values),
                        'offset': float(fit_da.sel(qubit=q, detuning_signs=sign, fit_vals='offset').values),
                        'decay': float(fit_da.sel(qubit=q, detuning_signs=sign, fit_vals='decay').values),
                    }
                except:
                    pass
    
    # Perform our own fitting
    fit_results_custom = {}
    success_list = []
    t2_star_list = []
    t2_error_list = []
    freq_offset_list = []
    
    for i, q in enumerate(qubits):
        fit_results_custom[str(q)] = {}
        
        # First respect the original success flag
        if not original_success[i]:
            success_list.append(False)
            t2_star_list.append(np.nan)
            t2_error_list.append(np.nan)
            freq_offset_list.append(np.nan)
            
            # Set empty fit parameters
            for sign in detuning_signs:
                fit_results_custom[str(q)][f"sign_{int(sign)}"] = None
            continue
        
        # Try to fit for each detuning sign
        fits_per_sign = []
        success_per_sign = []
        
        for j, sign in enumerate(detuning_signs):
            # Use I quadrature for fitting (can be changed to Q or amplitude)
            data_to_fit = I_data[i, :, j]
            
            # Get existing fit parameters if available
            existing_fit = None
            if str(q) in existing_fits and f"sign_{int(sign)}" in existing_fits[str(q)]:
                existing_fit = existing_fits[str(q)][f"sign_{int(sign)}"]
            
            # Perform fit
            success, fit_params, _ = fit_ramsey_oscillation(idle_time_ns, data_to_fit, existing_fit)
            
            fit_results_custom[str(q)][f"sign_{int(sign)}"] = fit_params
            fits_per_sign.append(fit_params)
            success_per_sign.append(success)
        
        # Overall success if at least one sign fits well
        overall_success = any(success_per_sign)
        success_list.append(overall_success)
        
        if overall_success:
            # Average T2* from successful fits
            t2_values = [f['t2_star_us'] for f, s in zip(fits_per_sign, success_per_sign) 
                        if s and f is not None]
            t2_errors = [f['t2_error_us'] for f, s in zip(fits_per_sign, success_per_sign) 
                        if s and f is not None]
            
            if t2_values:
                t2_star_list.append(np.mean(t2_values))
                t2_error_list.append(np.mean(t2_errors))
            else:
                t2_star_list.append(np.nan)
                t2_error_list.append(np.nan)
            
            # Calculate frequency offset (difference between positive and negative detuning)
            if len(detuning_signs) == 2 and all(f is not None for f in fits_per_sign):
                f_plus = fits_per_sign[list(detuning_signs).index(1)]['f'] if 1 in detuning_signs else 0
                f_minus = fits_per_sign[list(detuning_signs).index(-1)]['f'] if -1 in detuning_signs else 0
                # Frequency offset in Hz (convert from cycles/ns to Hz)
                freq_offset = (f_plus - f_minus) * 0.5 * 1e9
                freq_offset_list.append(freq_offset)
            else:
                # Single detuning or calculation failed
                freq_offset_list.append(np.nan)
        else:
            t2_star_list.append(np.nan)
            t2_error_list.append(np.nan)
            freq_offset_list.append(np.nan)
    
    # Calculate transmission amplitude in mV
    trans_amp = np.sqrt(I_data**2 + Q_data**2) * 1e3
    
    return dict(
        qubits=qubits,
        n=n_q,
        idle_time_ns=idle_time_ns,
        idle_time_us=idle_time_us,
        detuning_signs=detuning_signs,
        trans_amp=trans_amp,
        I=I_data,
        Q=Q_data,
        original_success=original_success,
        success=np.array(success_list),
        t2_star_us=np.array(t2_star_list),
        t2_error_us=np.array(t2_error_list),
        freq_offset_hz=np.array(freq_offset_list),
        fit_params=fit_results_custom,
        data_json=data_json,
        node_json=node_json
    )

# --------------------------------------------------------------------
# 2. Plot Generation for T2 Ramsey measurements
# --------------------------------------------------------------------
def create_t2_ramsey_plots(
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
    """Create T2 Ramsey plots with fits for multiple qubits"""
    
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
    
    # Color map for detuning signs
    color_map = {1: "blue", -1: "red"}
    
    # Add traces for each qubit
    for idx, q in enumerate(data["qubits"]):
        r, c = divmod(idx, n_cols)
        r += 1
        c += 1
        
        x_ns = data["idle_time_ns"]
        
        # Plot for each detuning sign
        for j, sign in enumerate(data["detuning_signs"]):
            color = color_map.get(int(sign), "gray")
            sign_label = "+" if sign == 1 else "-"
            
            # Get y data based on plot variable
            if plot_variable == "amp":
                y_data = data["trans_amp"][idx, :, j]
                ylabel = "|IQ| [mV]"
            elif plot_variable == "I":
                y_data = data["I"][idx, :, j] * 1e3
                ylabel = "I [mV]"
            elif plot_variable == "Q":
                y_data = data["Q"][idx, :, j] * 1e3
                ylabel = "Q [mV]"
            else:
                y_data = data["trans_amp"][idx, :, j]
                ylabel = "Signal"
            
            # Add raw data points
            fig.add_trace(
                go.Scatter(
                    x=x_ns,
                    y=y_data,
                    mode="lines+markers",
                    marker=dict(size=3, color=color),
                    line=dict(color=color, width=1),
                    name=f"Δ={sign_label}",
                    legendgroup=f"raw_{sign_label}",
                    showlegend=(idx == 0),  # Show legend only for first subplot
                ),
                row=r, col=c
            )
            
            # Add fit if successful
            if data["success"][idx] and str(q) in data["fit_params"]:
                sign_key = f"sign_{int(sign)}"
                if sign_key in data["fit_params"][str(q)] and data["fit_params"][str(q)][sign_key] is not None:
                    fit_p = data["fit_params"][str(q)][sign_key]
                    
                    # Generate smooth fit curve
                    x_fit_ns = np.linspace(x_ns.min(), x_ns.max(), 500)
                    
                    # Calculate fitted values based on the variable being plotted
                    if plot_variable == "I":
                        # Fit was done on I quadrature
                        y_fit = oscillation_decay_exp(
                            x_fit_ns,
                            fit_p['a'],
                            fit_p['f'],
                            fit_p['phi'],
                            fit_p['offset'],
                            fit_p['decay']
                        ) * 1e3
                    else:
                        # For other variables, scale appropriately
                        y_fit = oscillation_decay_exp(
                            x_fit_ns,
                            fit_p['a'],
                            fit_p['f'],
                            fit_p['phi'],
                            fit_p['offset'],
                            fit_p['decay']
                        )
                        if plot_variable in ("Q", "amp"):
                            y_fit *= 1e3
                    
                    # Darker color for fit
                    fit_color = "darkblue" if sign == 1 else "darkred"
                    
                    fig.add_trace(
                        go.Scatter(
                            x=x_fit_ns,
                            y=y_fit,
                            mode="lines",
                            line=dict(color=fit_color, width=2, dash="solid"),
                            name=f"Fit Δ={sign_label}",
                            legendgroup=f"fit_{sign_label}",
                            showlegend=(idx == 0),  # Show legend only for first subplot
                        ),
                        row=r, col=c
                    )
        
        # Add T2* value and success indicator as annotation
        if data["success"][idx]:
            t2_val = data["t2_star_us"][idx]
            t2_err = data["t2_error_us"][idx]
            freq_off = data["freq_offset_hz"][idx]
            
            if not np.isnan(t2_val):
                # Format frequency offset
                if not np.isnan(freq_off):
                    if abs(freq_off) > 1e6:
                        freq_str = f"Δf = {freq_off/1e6:.2f} MHz"
                    elif abs(freq_off) > 1e3:
                        freq_str = f"Δf = {freq_off/1e3:.1f} kHz"
                    else:
                        freq_str = f"Δf = {freq_off:.0f} Hz"
                else:
                    freq_str = ""
                
                # Format T2* with error
                if not np.isnan(t2_err) and t2_err > 0:
                    t2_str = f"T2* = {t2_val:.1f} ± {t2_err:.1f} μs"
                else:
                    t2_str = f"T2* = {t2_val:.1f} μs"
                
                annotation_text = f"{t2_str}\n{freq_str}\nFit: ✓"
            else:
                annotation_text = "Fit parameters invalid\nFit: ✗"
            
            bg_color = "rgba(144, 238, 144, 0.3)"  # Light green
            border_color = "green"
        else:
            annotation_text = "Fit Failed\nFit: ✗"
            bg_color = "rgba(255, 200, 200, 0.3)"  # Light red
            border_color = "red"
        
        # Determine y position for annotation
        if plot_variable == "amp":
            y_data_all = data["trans_amp"][idx, :, :]
        elif plot_variable == "I":
            y_data_all = data["I"][idx, :, :] * 1e3
        elif plot_variable == "Q":
            y_data_all = data["Q"][idx, :, :] * 1e3
        else:
            y_data_all = data["trans_amp"][idx, :, :]
        
        y_max = np.nanmax(y_data_all)
        y_min = np.nanmin(y_data_all)
        
        fig.add_annotation(
            text=annotation_text,
            xref=f"x{idx+1 if idx > 0 else ''}",
            yref=f"y{idx+1 if idx > 0 else ''}",
            x=x_ns.max() - (x_ns.max() - x_ns.min()) * 0.02,
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
            title_text="Idle time [ns]" if r == n_rows else None,
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
    }
    
    layout_args = dict(
        title=f"T2* Ramsey – {var_title_map.get(plot_variable, 'Signal')}",
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
# 3. Summary Table for T2 Ramsey measurements
# --------------------------------------------------------------------
def create_t2_ramsey_summary_table(data):
    """Create summary table showing T2*, frequency offset, and fit success"""
    rows = []
    
    for i, q in enumerate(data["qubits"]):
        # Check both original and our fitting success
        original_ok = bool(data["original_success"][i])
        our_ok = bool(data["success"][i])
        
        t2_val = data["t2_star_us"][i]
        t2_err = data["t2_error_us"][i]
        freq_off = data["freq_offset_hz"][i]
        
        # Format T2* value
        if our_ok and not np.isnan(t2_val):
            if not np.isnan(t2_err) and t2_err > 0:
                t2_str = f"{t2_val:.1f} ± {t2_err:.1f}"
            else:
                t2_str = f"{t2_val:.1f}"
        else:
            t2_str = "—"
        
        # Format frequency offset
        if our_ok and not np.isnan(freq_off):
            if abs(freq_off) > 1e6:
                freq_str = f"{freq_off/1e6:.2f} MHz"
            elif abs(freq_off) > 1e3:
                freq_str = f"{freq_off/1e3:.1f} kHz"
            else:
                freq_str = f"{freq_off:.0f} Hz"
        else:
            freq_str = "—"
        
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
                html.Td(freq_str),
                html.Td(status),
            ], className=row_class)
        )
    
    header = html.Thead(html.Tr([
        html.Th("Qubit"),
        html.Th("T2* [μs]"),
        html.Th("Freq. Offset"),
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
# 4. Layout + Callbacks for T2 Ramsey measurements
# --------------------------------------------------------------------
def create_t2_ramsey_layout(folder):
    """Create the complete layout for T2 Ramsey visualization"""
    uid = folder.replace("\\", "_").replace("/", "_").replace(":", "")
    data = load_t2_ramsey_data(folder)
    
    if not data:
        return html.Div([
            dbc.Alert("Failed to load T2 Ramsey data", color="danger"),
            html.Pre(folder)
        ])
    
    default_height = 400 * ceil(data["n"] / 2)  # 2 columns by default
    init_fig = create_t2_ramsey_plots(data, n_cols=2, fig_height=default_height, plot_variable="I")
    
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
                                id={"type": "t2-var", "index": uid},
                                options=[
                                    {"label": "I-quadrature", "value": "I"},
                                    {"label": "Q-quadrature", "value": "Q"},
                                    {"label": "Amplitude |IQ|", "value": "amp"},
                                ],
                                value="I",
                                clearable=False
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Columns per Row"),
                            dcc.Dropdown(
                                id={"type": "t2-cols", "index": uid},
                                options=[{"label": i, "value": i} for i in range(1, 5)],
                                value=2,
                                clearable=False
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Figure Width (px)"),
                            dcc.Slider(
                                id={"type": "t2-width", "index": uid},
                                min=600, max=2000, step=100, value=1200,
                                marks={i: str(i) for i in range(600, 2001, 400)},
                                tooltip={"placement": "bottom", "always_visible": True}
                            )
                        ]), width=3),
                        dbc.Col(html.Div([
                            html.Label("Figure Height (px)"),
                            dcc.Slider(
                                id={"type": "t2-height", "index": uid},
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
        id={"type": "copy-t2-plot", "index": uid},
        color="secondary",
        size="sm",
        className="mb-2"
    )
    
    # Store for base64 encoded image
    image_store = dcc.Store(id={"type": "t2-plot-image-store", "index": uid})
    
    # Summary section
    summary_content = html.Div([
        html.Div([
            html.H6("T2* Ramsey Summary", style={"display": "inline-block", "marginRight": "10px"}),
            dcc.Clipboard(
                id={"type": "copy-t2-summary", "index": uid},
                target_id={"type": "t2-summary-table-content", "index": uid},
                title="Copy summary to clipboard",
                style={"display": "inline-block", "verticalAlign": "middle"}
            )
        ], style={"marginBottom": "10px"}),
        html.Div(
            create_t2_ramsey_summary_table(data),
            id={"type": "t2-summary-table-content", "index": uid}
        )
    ])
    
    # Side panel
    side_panel = html.Div(
        id={"type": "t2-side-panel", "index": uid},
        children=[
            html.Div(
                dbc.Button(
                    "◀ Info",
                    id={"type": "toggle-t2-side-panel", "index": uid},
                    color="primary",
                    size="sm",
                    style={
                        "writingMode": "vertical-rl",
                        "textOrientation": "mixed",
                        "height": "100px",
                        "padding": "10px 5px"
                    }
                ),
                id={"type": "t2-side-toggle-container", "index": uid},
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
                id={"type": "t2-side-panel-content", "index": uid},
                children=[
                    summary_content,
                    html.Hr(),
                    html.H6("Measurement Info"),
                    html.Pre(f"Folder: {folder}\nQubits: {data['n']}\nDetuning signs: {data['detuning_signs'].tolist()}"),
                    html.Hr(),
                    html.H6("T2* Ramsey Description"),
                    html.P([
                        "The T2* (Ramsey) measurement consists of playing a Ramsey sequence ",
                        "(x90 - idle_time - x90/y90 - measurement) for different idle times. ",
                        "Virtual Z rotations are used to mimic detuning by rotating the frame ",
                        "of the second pulse. The oscillation frequency gives the detuning, ",
                        "and the decay envelope gives T2*. This measurement captures both ",
                        "intrinsic decoherence (T2) and inhomogeneous broadening effects."
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
        dcc.Store(id={"type": "t2-data", "index": uid}, data={"folder": folder}),
        dcc.Store(id={"type": "t2-side-panel-state", "index": uid}, data={"is_open": False}),
        image_store,
        dbc.Row(dbc.Col(html.H3(f"T2* Ramsey Measurement – {Path(folder).name}")), className="mb-3"),
        controls_accordion,
        dbc.Row([
            dbc.Col([
                copy_plot_btn,
                dcc.Loading(
                    dcc.Graph(
                        id={"type": "t2-plot", "index": uid},
                        figure=init_fig,
                        config={"displayModeBar": True}
                    )
                )
            ], width=12)
        ]),
        side_panel
    ])

def register_t2_ramsey_callbacks(app):
    """Register callbacks for T2 Ramsey visualization"""
    
    @app.callback(
        [Output({"type": "t2-plot", "index": MATCH}, "figure"),
         Output({"type": "t2-summary-table-content", "index": MATCH}, "children")],
        Input({"type": "t2-var", "index": MATCH}, "value"),
        Input({"type": "t2-cols", "index": MATCH}, "value"),
        Input({"type": "t2-width", "index": MATCH}, "value"),
        Input({"type": "t2-height", "index": MATCH}, "value"),
        State({"type": "t2-data", "index": MATCH}, "data"),
    )
    def update_t2_plot(plot_var, n_cols, fig_w, fig_h, store):
        """Update T2 Ramsey plot based on user inputs"""
        data = load_t2_ramsey_data(store["folder"])
        fig = create_t2_ramsey_plots(
            data,
            n_cols=n_cols,
            fig_width=fig_w,
            fig_height=fig_h,
            plot_variable=plot_var
        )
        summary_table = create_t2_ramsey_summary_table(data)
        return fig, summary_table
    
    # Toggle side panel callback
    @app.callback(
        [Output({"type": "t2-side-panel-content", "index": MATCH}, "style"),
         Output({"type": "t2-side-toggle-container", "index": MATCH}, "style"),
         Output({"type": "toggle-t2-side-panel", "index": MATCH}, "children"),
         Output({"type": "t2-side-panel-state", "index": MATCH}, "data")],
        Input({"type": "toggle-t2-side-panel", "index": MATCH}, "n_clicks"),
        State({"type": "t2-side-panel-state", "index": MATCH}, "data"),
        prevent_initial_call=True
    )
    def toggle_t2_side_panel(n_clicks, state_data):
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
        Output({"type": "t2-plot-image-store", "index": MATCH}, "data"),
        Input({"type": "copy-t2-plot", "index": MATCH}, "n_clicks"),
        State({"type": "t2-plot", "index": MATCH}, "figure"),
        prevent_initial_call=True
    )
    def update_t2_image_store(n_clicks, current_figure):
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
                                        const btn = document.querySelector('[id*="copy-t2-plot"]');
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
        Output({"type": "copy-t2-plot", "index": MATCH}, "children"),
        Input({"type": "t2-plot-image-store", "index": MATCH}, "data"),
        State({"type": "copy-t2-plot", "index": MATCH}, "n_clicks"),
    )

# --------------------------------------------------------------------
# Example usage
# --------------------------------------------------------------------
if __name__ == "__main__":
    # Example: Create a simple Dash app to test the T2 Ramsey plotting tool
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    # Example folder path - replace with your actual data folder
    test_folder = "path/to/your/t2_ramsey_data"
    
    # Create layout
    app.layout = html.Div([
        create_t2_ramsey_layout(test_folder)
    ])
    
    # Register callbacks
    register_t2_ramsey_callbacks(app)
    
    # Run the app
    app.run_server(debug=True)