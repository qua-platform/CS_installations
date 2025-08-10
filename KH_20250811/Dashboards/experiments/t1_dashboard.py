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

MIN_TAU_US = 2.0
MAX_TAU_US = 20000.0

def fit_t1_decay(time_ns, amplitude_data, min_tau_us=2.0, max_tau_us=10000.0):
    """
    Fit T1 decay to the data - handles both increasing and decreasing signals
    
    Parameters:
    -----------
    time_ns : array
        Time values in nanoseconds
    amplitude_data : array
        Amplitude values to fit
    min_tau_us : float
        Minimum allowed T1 value in microseconds (default: 2.0 μs)
        This prevents fitting unrealistically fast decays
    max_tau_us : float
        Maximum allowed T1 value in microseconds (default: 10000.0 μs)
        This prevents fitting unrealistically slow decays
    
    Returns:
    --------
    success : bool
        Whether the fit was successful
    tau_us : float
        T1 value in microseconds
    tau_error_us : float
        Error in T1 value in microseconds
    fit_params : dict
        Dictionary containing fit parameters
    """
    try:
        # Convert tau limits to ns for internal calculations
        min_tau_ns = min_tau_us * 1000.0
        max_tau_ns = max_tau_us * 1000.0
        
        # Determine signal direction
        initial_val = amplitude_data[0]
        final_val = amplitude_data[-1]
        signal_decreases = initial_val > final_val
        
        if signal_decreases:
            # Standard decay: high → low
            a_guess = initial_val - final_val  # positive amplitude
            offset_guess = final_val
            
            # Find 1/e point for tau estimation
            target_val = offset_guess + a_guess / np.e
            idx_1e = np.argmin(np.abs(amplitude_data - target_val))
            if idx_1e > 0:
                tau_guess = time_ns[idx_1e]
                # Constrain tau_guess to be within limits
                tau_guess = np.clip(tau_guess, min_tau_ns, max_tau_ns)
                decay_guess = -1.0 / tau_guess  # negative for decay
            else:
                # Use geometric mean of limits as default
                tau_guess = np.sqrt(min_tau_ns * max_tau_ns)
                decay_guess = -1.0 / tau_guess
            
            # Calculate decay bounds based on tau limits
            decay_min = -1.0 / min_tau_ns  # More negative = faster decay
            decay_max = -1.0 / max_tau_ns  # Less negative = slower decay
            
            # Bounds for decreasing signal
            bounds = (
                [0, 0, decay_min],        # a≥0, offset≥0, decay_min ≤ decay
                [np.inf, np.inf, decay_max]  # decay ≤ decay_max (closer to 0)
            )
        else:
            # Inverted decay: low → high (recovery)
            a_guess = final_val - initial_val  # positive amplitude  
            offset_guess = initial_val
            
            # Find 1/e point for tau estimation
            target_val = offset_guess + a_guess / np.e
            idx_1e = np.argmin(np.abs(amplitude_data - target_val))
            if idx_1e > 0:
                tau_guess = time_ns[idx_1e]
                # Constrain tau_guess to be within limits
                tau_guess = np.clip(tau_guess, min_tau_ns, max_tau_ns)
                decay_guess = 1.0 / tau_guess  # positive for growth
            else:
                # Use geometric mean of limits as default
                tau_guess = np.sqrt(min_tau_ns * max_tau_ns)
                decay_guess = 1.0 / tau_guess
            
            # Calculate decay bounds based on tau limits
            decay_min = 1.0 / max_tau_ns  # Smaller positive = slower growth
            decay_max = 1.0 / min_tau_ns  # Larger positive = faster growth
            
            # Bounds for increasing signal
            bounds = (
                [0, 0, decay_min],        # a≥0, offset≥0, decay_min ≤ decay
                [np.inf, np.inf, decay_max]  # decay ≤ decay_max
            )
        
        # Perform the fit with constrained bounds
        popt, pcov = curve_fit(
            decay_exp, 
            time_ns, 
            amplitude_data,
            p0=[a_guess, offset_guess, decay_guess],
            bounds=bounds,
            maxfev=5000
        )
        
        a_fit, offset_fit, decay_fit = popt
        
        # Calculate tau and its error (always positive)
        tau_ns = abs(1.0 / decay_fit)  # Take absolute value
        tau_us = tau_ns / 1000.0
        
        # Additional validation: check if tau is within reasonable bounds
        if tau_us < min_tau_us or tau_us > max_tau_us:
            print(f"Warning: Fitted T1={tau_us:.1f} μs is outside bounds [{min_tau_us}, {max_tau_us}]")
        
        # Calculate tau error from covariance matrix
        try:
            decay_error = np.sqrt(pcov[2, 2]) if pcov[2, 2] > 0 else 0
            tau_error_ns = tau_ns * (decay_error / abs(decay_fit))
            tau_error_us = tau_error_ns / 1000.0
        except:
            # If covariance calculation fails, use a default error
            tau_error_us = tau_us * 0.1  # 10% error as fallback
        
        # Success criteria (can be adjusted)
        success = (
            tau_us >= min_tau_us * 0.5 and  # Allow some tolerance below min
            tau_us <= max_tau_us * 2.0 and  # Allow some tolerance above max
            tau_error_us / tau_us < 1.0  # Relative error < 100%
        )
        
        return success, tau_us, tau_error_us, {
            'a': a_fit, 
            'offset': offset_fit, 
            'decay': decay_fit,
            'direction': 'decreasing' if signal_decreases else 'increasing'
        }
        
    except Exception as e:
        print(f"Fit failed: {e}")
        return False, np.nan, np.nan, None

def decay_exp(t, a, offset, decay):
    """
    Generalized exponential function for both decay and recovery
    - For decay (decay < 0): a * exp(decay * t) + offset
    - For recovery (decay > 0): a * (1 - exp(-decay * t)) + offset
    """
    if hasattr(decay, '__iter__'):
        # Handle array inputs
        result = np.zeros_like(t)
        for i, d in enumerate(decay):
            if d < 0:
                result = a[i] * np.exp(d * t) + offset[i]
            else:
                result = a[i] * (1 - np.exp(-d * t)) + offset[i]
        return result
    else:
        # Handle scalar inputs
        if decay < 0:
            return a * np.exp(decay * t) + offset
        else:
            return a * (1 - np.exp(-decay * t)) + offset

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
# 1. Data Loader for T1 measurements with adaptive data type support
# --------------------------------------------------------------------
def load_t1_data(folder, min_tau_us=2.0, max_tau_us=10000.0, fit_variable="amp"):
    """
    Load T1 data with adaptive support for state discrimination and I/Q modes
    
    Parameters:
    -----------
    folder : str
        Path to data folder
    min_tau_us : float
        Minimum allowed T1 value in microseconds
    max_tau_us : float
        Maximum allowed T1 value in microseconds
    fit_variable : str
        Variable to use for fitting: "state", "I", or "amp"
    """
    folder = os.path.normpath(folder)
    paths = {
        "ds_raw":  os.path.join(folder, "ds_raw.h5"),
        "ds_fit":  os.path.join(folder, "ds_fit.h5"),
        "node_js": os.path.join(folder, "node.json"),
        "data_js": os.path.join(folder, "data.json"),
    }
    
    # Check if essential files exist
    if not all(os.path.exists(p) for p in [paths["ds_raw"], paths["ds_fit"], paths["node_js"]]):
        print(f"[load_t1_data] missing essential files in {folder}")
        return None
    
    ds_raw = open_xr_dataset(paths["ds_raw"])
    ds_fit = open_xr_dataset(paths["ds_fit"])
    
    with open(paths["node_js"], "r", encoding="utf-8") as f:
        node_json = json.load(f)
    
    # Load data.json if it exists
    data_json = None
    if os.path.exists(paths["data_js"]):
        with open(paths["data_js"], "r", encoding="utf-8") as f:
            data_json = json.load(f)
    
    # Check if we have state discrimination data or I/Q data
    has_state = "state" in ds_raw
    has_iq = "I" in ds_raw and "Q" in ds_raw
    
    # Determine data type from node.json if available
    use_state_discrimination = False
    if "parameters" in node_json and "use_state_discrimination" in node_json["parameters"]:
        use_state_discrimination = node_json["parameters"]["use_state_discrimination"]
    elif has_state and not has_iq:
        use_state_discrimination = True
    
    # Validate fit_variable parameter based on available data
    if use_state_discrimination:
        if fit_variable not in ["state", "amp"]:
            print(f"[load_t1_data] State discrimination mode detected. Setting fit_variable to 'state'")
            fit_variable = "state"
    else:
        if fit_variable not in ["I", "amp"]:
            fit_variable = "amp"  # Default to amplitude for I/Q mode
    
    # Extract basic data
    qubits = ds_raw["qubit"].values
    n_q = len(qubits)
    idle_time_ns = ds_raw["idle_time"].values  # in nanoseconds
    idle_time_us = idle_time_ns / 1000.0  # convert to microseconds
    
    # Get data based on discrimination mode
    if use_state_discrimination:
        # State discrimination mode
        state_data = ds_raw["state"].values if has_state else None
        I_data = None
        Q_data = None
        
        # For state mode, trans_amp is just the state data
        if state_data is not None:
            trans_amp = state_data  # State is already a probability/amplitude measure
        else:
            trans_amp = np.zeros((n_q, len(idle_time_ns)))
    else:
        # I/Q mode
        I_data = ds_raw["I"].values if "I" in ds_raw else np.zeros((n_q, len(idle_time_ns)))
        Q_data = ds_raw["Q"].values if "Q" in ds_raw else np.zeros((n_q, len(idle_time_ns)))
        state_data = None
        
        # Calculate transmission amplitude in mV
        trans_amp = np.sqrt(I_data**2 + Q_data**2) * 1e3
    
    # Perform our own fitting for each qubit
    success_list = []
    tau_list = []
    tau_error_list = []
    fit_params_list = []
    
    for i in range(n_q):
        # Select data based on fit_variable and discrimination mode
        if use_state_discrimination:
            if fit_variable == "state":
                data_to_fit = state_data[i]
            else:  # amp in state mode
                data_to_fit = state_data[i]
        else:
            if fit_variable == "I":
                data_to_fit = I_data[i]
            elif fit_variable == "amp":
                # Calculate amplitude WITHOUT the 1e3 scaling for fitting
                data_to_fit = np.sqrt(I_data[i]**2 + Q_data[i]**2)
            else:
                data_to_fit = I_data[i]
        
        # Fit the decay with tau constraints
        success, tau_us, tau_error_us, fit_params = fit_t1_decay(
            idle_time_ns, 
            data_to_fit,
            min_tau_us=min_tau_us,
            max_tau_us=max_tau_us
        )
        
        success_list.append(success)
        tau_list.append(tau_us)
        tau_error_list.append(tau_error_us)
        fit_params_list.append(fit_params)
        
        print(f"Qubit {qubits[i]}: T1 = {tau_us:.1f} ± {tau_error_us:.1f} μs, Success = {success}")
        if fit_params:
            print(f"  Fit params: a={fit_params['a']:.3e}, offset={fit_params['offset']:.3e}, "
                  f"decay={fit_params['decay']:.3e}, direction={fit_params['direction']}")
    
    # Extract data.json T1 values if available
    data_json_t1_values = {}
    data_json_t1_errors = {}
    data_json_success_flags = {}
    
    if data_json and "fit_results" in data_json:
        for qubit_key, qubit_data in data_json["fit_results"].items():
            # Store T1 value in microseconds
            if "t1" in qubit_data:
                # Check if t1 is already in microseconds or needs conversion from ns
                t1_val = qubit_data.get("t1", np.nan)
                # Assume it's in ns if > 100 (typical T1 is > 100ns but < 100us)
                if t1_val > 100:
                    t1_val = t1_val / 1000.0  # Convert ns to μs
                data_json_t1_values[qubit_key] = t1_val
            else:
                data_json_t1_values[qubit_key] = np.nan
            
            if "t1_error" in qubit_data:
                t1_err = qubit_data.get("t1_error", np.nan)
                if t1_err > 100:
                    t1_err = t1_err / 1000.0  # Convert ns to μs
                data_json_t1_errors[qubit_key] = t1_err
            else:
                data_json_t1_errors[qubit_key] = np.nan
            
            data_json_success_flags[qubit_key] = qubit_data.get("success", False)
    
    # Print which variable was used for fitting
    if use_state_discrimination:
        print(f"[load_t1_data] State discrimination mode - Fitting performed using {fit_variable}")
    else:
        print(f"[load_t1_data] I/Q mode - Fitting performed using {fit_variable} quadrature/amplitude")
    
    return dict(
        qubits=qubits, 
        n=n_q,
        idle_time_ns=idle_time_ns,
        idle_time_us=idle_time_us,
        trans_amp=trans_amp,
        I=I_data,
        Q=Q_data,
        state=state_data,
        use_state_discrimination=use_state_discrimination,
        success=np.array(success_list),
        tau=np.array(tau_list),
        tau_error=np.array(tau_error_list),
        fit_params=fit_params_list,
        data_json_t1_values=data_json_t1_values,
        data_json_t1_errors=data_json_t1_errors,
        data_json_success_flags=data_json_success_flags,
        node_json=node_json,
        data_json=data_json,
        min_tau_us=min_tau_us,
        max_tau_us=max_tau_us,
        fit_variable=fit_variable
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
# 3. Plot Generation for T1 measurements with adaptive data support
# --------------------------------------------------------------------
def create_t1_plots(
    data,
    n_cols: int = 2,
    x_unit: str = "us",  
    fig_width: int = None,
    fig_height: int = None,
    vertical_spacing_px: int = 100,
    legend_x: float = 0.98,
    legend_y: float = 1.0,
    legend_xanchor: str = "right",
    legend_yanchor: str = "bottom",
    legend_orientation: str = "h",
    plot_variable: str = None  # Will be determined based on data
):
    """Create T1 plots with adaptive support for state discrimination and I/Q modes"""
    
    if not data:
        return go.Figure()
    
    # Validate x_unit parameter
    if x_unit not in ["ns", "us"]:
        raise ValueError("x_unit must be either 'ns' or 'us'")
    
    # Determine plot variable based on data type if not specified
    if plot_variable is None:
        if data["use_state_discrimination"]:
            plot_variable = "state"
        else:
            plot_variable = "I"
    
    # Validate plot_variable based on available data
    if data["use_state_discrimination"]:
        if plot_variable not in ["state", "amp"]:
            plot_variable = "state"
    else:
        if plot_variable not in ["I", "amp"]:
            plot_variable = "I"
    
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
    
    # Select appropriate data and label based on unit
    if x_unit == "ns":
        x_data = data["idle_time_ns"]
        x_label = "Idle time [ns]"
    else:  # x_unit == "us"
        x_data = data["idle_time_us"]
        x_label = "Idle time [μs]"
    
    # Add traces for each qubit
    for idx, q in enumerate(data["qubits"]):
        r, c = divmod(idx, n_cols)
        r += 1
        c += 1
        
        # Get y data based on plot variable and discrimination mode
        if data["use_state_discrimination"]:
            if plot_variable == "state":
                y_data = data["state"][idx]
                ylabel = "State Population"
            else:  # amp in state mode
                y_data = data["state"][idx]
                ylabel = "State Population"
        else:
            if plot_variable == "amp":
                y_data = data["trans_amp"][idx]
                ylabel = "|IQ| [mV]"
            elif plot_variable == "I":
                y_data = data["I"][idx] * 1e3
                ylabel = "I [mV]"
            else:
                y_data = data["trans_amp"][idx]
                ylabel = "Signal"
        
        # Add data points
        fig.add_trace(
            go.Scatter(
                x=x_data, 
                y=y_data,
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
            # IMPORTANT: Always use ns for fitting calculations
            x_fit_ns = np.linspace(data["idle_time_ns"].min(), data["idle_time_ns"].max(), 500)
            
            # Calculate fitted values using our fit parameters
            y_fit = decay_exp(x_fit_ns, fit_p['a'], fit_p['offset'], fit_p['decay'])
            
            # Scale the fit to match the displayed data scale
            if data["use_state_discrimination"]:
                # State discrimination: fit is already in correct units
                pass
            else:
                # I/Q mode: scale based on what we're plotting
                if plot_variable == "I":
                    # Fit was done on I, scale to mV for display
                    y_fit *= 1e3
                elif plot_variable == "amp":
                    # For amplitude, the fit should match the amplitude scale
                    # If fit was done on amplitude, it's in V, need to convert to mV
                    y_fit *= 1e3
            
            # Convert x_fit to appropriate unit for display
            if x_unit == "ns":
                x_fit_display = x_fit_ns
            else:  # x_unit == "us"
                x_fit_display = x_fit_ns / 1000  # Convert ns to us
            
            fig.add_trace(
                go.Scatter(
                    x=x_fit_display,
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
            t1_val = data['tau'][idx]  # This is always in μs
            t1_err = data['tau_error'][idx]
            
            # Format T1 with error
            if not np.isnan(t1_err) and t1_err > 0:
                t1_str = f"T1 = {t1_val:.1f} ± {t1_err:.1f} μs"
            else:
                t1_str = f"T1 = {t1_val:.1f} μs"
            
            annotation_text = f"{t1_str}\nFit: ✓"
            bg_color = "rgba(144, 238, 144, 0.3)"  # Light green
            border_color = "green"
        else:
            # Add failure indicator
            annotation_text = "Fit Failed\nFit: ✗"
            bg_color = "rgba(255, 200, 200, 0.3)"  # Light red
            border_color = "red"
        
        # Determine y position for annotation
        if data["use_state_discrimination"]:
            y_data_all = data["state"][idx]
        else:
            if plot_variable == "amp":
                y_data_all = data["trans_amp"][idx]
            elif plot_variable == "I":
                y_data_all = data["I"][idx] * 1e3
            else:
                y_data_all = data["trans_amp"][idx]
        
        y_max = np.nanmax(y_data_all)
        y_min = np.nanmin(y_data_all)
        
        fig.add_annotation(
            text=annotation_text,
            xref=f"x{idx+1 if idx > 0 else ''}",
            yref=f"y{idx+1 if idx > 0 else ''}",
            x=x_data.max() - (x_data.max() - x_data.min()) * 0.02,
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
            title_text=x_label,
            row=r, col=c,
            showgrid=True,
        )
        fig.update_yaxes(
            title_text=ylabel,
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
    
    # Layout with adaptive title based on data mode
    var_title_map = {
        "amp": "Amplitude |IQ|",
        "I": "I-quadrature",
        "state": "State Population",
    }
    
    mode_str = "State Discrimination" if data["use_state_discrimination"] else "I/Q"
    
    layout_args = dict(
        title=f"T1 Relaxation ({mode_str}) – {var_title_map.get(plot_variable, 'Signal')}",
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
# 4. Summary Table for T1 measurements with adaptive data support
# --------------------------------------------------------------------
def create_t1_summary_table(data):
    """Create summary table showing T1 values and fit success for both our fits and data.json"""
    rows = []
    
    for i, q in enumerate(data["qubits"]):
        # Our fitting results
        ok = bool(data["success"][i])
        tau_val = data["tau"][i]
        tau_err = data["tau_error"][i]
        
        # Format our T1 value
        if ok and not np.isnan(tau_val):
            if not np.isnan(tau_err) and tau_err > 0:
                our_t1_str = f"{tau_val:.1f} ± {tau_err:.1f}"
            else:
                our_t1_str = f"{tau_val:.1f}"
        else:
            our_t1_str = "—"
        
        # Get data.json values if available
        qubit_key = str(q)
        data_json_results = data.get("data_json_t1_values", {})
        
        if qubit_key in data_json_results:
            json_t1_val = data_json_results[qubit_key]
            json_t1_err = data.get("data_json_t1_errors", {}).get(qubit_key, np.nan)
            json_success = data.get("data_json_success_flags", {}).get(qubit_key, False)
        else:
            json_t1_val = np.nan
            json_t1_err = np.nan
            json_success = False
        
        # Format data.json T1 value
        if json_success and not np.isnan(json_t1_val):
            if not np.isnan(json_t1_err) and json_t1_err > 0:
                json_t1_str = f"{json_t1_val:.1f} ± {json_t1_err:.1f}"
            else:
                json_t1_str = f"{json_t1_val:.1f}"
        else:
            json_t1_str = "—"
        
        # Determine row color and status
        if ok and json_success:
            row_class = "table-success"
            status = "✓"
        elif ok:
            row_class = "table-warning"
            status = "✓ (refit only)"
        elif json_success:
            row_class = "table-warning"
            status = "✓ (original only)"
        else:
            row_class = "table-danger"
            status = "✗"
        
        rows.append(
            html.Tr([
                html.Td(str(q)),
                html.Td(our_t1_str),
                html.Td(json_t1_str),
                html.Td(status),
            ], className=row_class)
        )
    
    header = html.Thead(html.Tr([
        html.Th("Qubit"),
        html.Th("T1 [μs] (Refit)"),
        html.Th("T1 [μs] (Original)"),
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
# 5. Layout + Callbacks for T1 measurements with adaptive data support
# --------------------------------------------------------------------
def create_t1_layout(folder, x_unit="us"):
    """Create the complete layout for T1 visualization with adaptive data support"""
    uid = folder.replace("\\", "_").replace("/", "_").replace(":", "")
    
    # Load data initially to determine available options
    initial_data = load_t1_data(folder, min_tau_us=MIN_TAU_US, max_tau_us=MAX_TAU_US, fit_variable="amp")
    
    if not initial_data:
        return html.Div([
            dbc.Alert("Failed to load T1 data", color="danger"), 
            html.Pre(folder)
        ])
    
    default_height = 400 * ceil(initial_data["n"] / 2)  # 2 columns by default
    
    # Determine available plot variables based on data type
    if initial_data["use_state_discrimination"]:
        plot_options = [
            {"label": "State Population", "value": "state"},
            {"label": "Amplitude", "value": "amp"},
        ]
        default_plot_var = "state"
    else:
        plot_options = [
            {"label": "I-quadrature", "value": "I"},
            {"label": "Amplitude |IQ|", "value": "amp"},
        ]
        default_plot_var = "I"
    
    # Initialize with default settings
    init_fig = create_t1_plots(
        initial_data, 
        n_cols=2, 
        x_unit=x_unit, 
        fig_height=default_height, 
        plot_variable=default_plot_var
    )
    
    # Controls
    controls_accordion = dbc.Accordion(
        [
            dbc.AccordionItem(
                title="Display Options",
                children=[
                    dbc.Row([
                        dbc.Col(html.Div([
                            html.Label("Plot Variable"),
                            dcc.RadioItems(
                                id={"type": "t1-var", "index": uid},
                                options=plot_options,
                                value=default_plot_var,
                                inline=True,
                                labelStyle={'display': 'inline-block', 'marginRight': '20px'}
                            )
                        ]), width="auto"),
                        dbc.Col(html.Div([
                            html.Label("X-axis Unit"),
                            dcc.Dropdown(
                                id={"type": "t1-xunit", "index": uid},
                                options=[
                                    {"label": "ns", "value": "ns"},
                                    {"label": "us", "value": "us"},
                                ],
                                value=x_unit,
                                clearable=False
                            )
                        ]), width="auto"),
                        dbc.Col(html.Div([
                            html.Label("Columns per Row"),
                            dcc.Dropdown(
                                id={"type": "t1-cols", "index": uid},
                                options=[{"label": i, "value": i} for i in range(1, 5)],
                                value=2, 
                                clearable=False
                            )
                        ]), width="auto"),
                        dbc.Col(html.Div([
                            html.Label("Figure Width (px)"),
                            dcc.Slider(
                                id={"type": "t1-width", "index": uid},
                                min=600, max=2000, step=200, value=1200,
                                tooltip={"placement": "bottom", "always_visible": True}
                            )
                        ]), style={'flex': '1'}),
                        dbc.Col(html.Div([
                            html.Label("Figure Height (px)"),
                            dcc.Slider(
                                id={"type": "t1-height", "index": uid},
                                min=300, max=2000, step=200, value=default_height,
                                tooltip={"placement": "bottom", "always_visible": True}
                            )
                        ]), style={'flex': '1'}),
                    ], align="center", className="mb-3 g-2"),
                    dbc.Row([
                        dbc.Col([
                            dbc.Alert(
                                f"Data Mode: {'State Discrimination' if initial_data['use_state_discrimination'] else 'I/Q Quadratures'}",
                                color="info",
                                className="mt-2"
                            )
                        ], width=12)
                    ])
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
            html.H6("T1 Summary", style={"display": "inline-block", "marginRight": "10px"}),
            dcc.Clipboard(
                id={"type": "copy-t1-summary", "index": uid},
                target_id={"type": "t1-summary-table-content", "index": uid},
                title="Copy summary to clipboard",
                style={"display": "inline-block", "verticalAlign": "middle"}
            )
        ], style={"marginBottom": "10px"}),
        html.Div(
            create_t1_summary_table(initial_data),
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
                    html.Pre(
                        f"Folder: {folder}\n"
                        f"Qubits: {initial_data['n']}\n"
                        f"Data Mode: {'State Discrimination' if initial_data['use_state_discrimination'] else 'I/Q Quadratures'}"
                    ),
                    html.Hr(),
                    html.H6("T1 Measurement Description"),
                    html.P([
                        "The T1 relaxation time measurement consists of preparing ",
                        "the qubit in the excited state using a π-pulse and then ",
                        "measuring the qubit state after a variable idle time. ",
                        "The exponential decay of the excited state population ",
                        "gives the T1 relaxation time."
                    ], style={"fontSize": "12px"}),
                    html.Hr(),
                    html.H6("Data Modes"),
                    html.Ul([
                        html.Li("State Discrimination: Single value per measurement representing state population"),
                        html.Li("I/Q Quadratures: Complex signal with I and Q components"),
                    ], style={"fontSize": "11px"}),
                    html.Hr(),
                    html.H6("Summary Table Columns"),
                    html.Ul([
                        html.Li("T1 [μs] (Refit): T1 values from new fitting"),
                        html.Li("T1 [μs] (Original): T1 values from data.json"),
                        html.Li("✓: Successful fit, ✗: Failed fit")
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
        Input({"type": "t1-var", "index": MATCH}, "value"),
        Input({"type": "t1-xunit", "index": MATCH}, "value"),
        Input({"type": "t1-cols", "index": MATCH}, "value"),
        Input({"type": "t1-width", "index": MATCH}, "value"),
        Input({"type": "t1-height", "index": MATCH}, "value"),
        State({"type": "t1-data", "index": MATCH}, "data"),
    )
    def update_t1_plot(plot_var, x_unit, n_cols, fig_w, fig_h, store):
        # Reload data with the selected fit variable
        data = load_t1_data(store["folder"], fit_variable=plot_var)
        
        fig = create_t1_plots(
            data,
            n_cols=n_cols,
            x_unit=x_unit,
            fig_width=fig_w,
            fig_height=fig_h,
            plot_variable=plot_var
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