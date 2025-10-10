import logging
from dataclasses import dataclass
from typing import Dict, Tuple, List

import numpy as np
import xarray as xr
from qualibrate import QualibrationNode
from qualibration_libs.data import add_amplitude_and_phase, convert_IQ_to_V
from quam_config.instrument_limits import instrument_limits
from qualibration_libs.analysis import fit_oscillation_decay_exp, oscillation_decay_exp, peaks_dips


@dataclass
class FitParameters:
    """Stores the relevant qubit TLS SWAP experiment fit parameters for a single qubit"""

    success: bool
    tls_flux_biases: List[float]
    tls_frequencies_mhz: List[float]
    tls_tau_us: List[float]
    tls_fwhm_mhz: List[float]   

def log_fitted_results(fit_results: Dict, log_callable=None):
    """
    Logs the node-specific fitted results for all qubits from the fit results

    Parameters:
    -----------
    fit_results : dict
        Dictionary containing the fitted results for all qubits.
    logger : logging.Logger, optional
        Logger for logging the fitted results. If None, a default logger is used.

    """
    if log_callable is None:
        log_callable = logging.getLogger(__name__).info
    pass


def process_raw_dataset(ds: xr.Dataset, node) -> xr.Dataset:
    """
    If state discrimination was used (i.e., 'state' exists), return as-is.
    Otherwise, create 'state' = |IQ| = sqrt(I^2 + Q^2).
    Adds a single-element 'qubit' dim if missing and there is exactly one qubit.
    """
    ds = ds.copy()

    # If discriminated state already present, we're done.
    if "state" in ds.data_vars:
        # ensure a qubit dim if single-qubit
        if "qubit" not in ds["state"].dims and len(node.namespace["qubits"]) == 1:
            qname = node.namespace["qubits"][0]["qubit"]
            ds["state"] = ds["state"].expand_dims({"qubit": [qname]})
        return ds

    # Otherwise, construct amplitude from I/Q
    if ("I" not in ds.data_vars) or ("Q" not in ds.data_vars):
        raise ValueError("Expected 'state' or both 'I' and 'Q' in dataset.")

    amp = np.hypot(ds["I"], ds["Q"])  # IQ = sqrt(I^2 + Q^2)
    amp.name = "state"
    amp.attrs.update({"long_name": "|IQ|", "units": "V"})

    if "qubit" not in amp.dims and len(node.namespace["qubits"]) == 1:
        qname = node.namespace["qubits"][0]["qubit"]
        amp = amp.expand_dims({"qubit": [qname]})

    ds["state"] = amp
    return ds

def _extract_relevant_fit_parameters(fit: xr.Dataset, node: QualibrationNode):
    """Add metadata to the dataset and fit results."""
    pass

def fit_raw_data(ds: xr.Dataset, node: QualibrationNode) -> Tuple[xr.Dataset, dict[str, FitParameters]]:
    """
    Identify TLS resonances (by local maxima of fitted oscillation frequency vs flux) and
    return per-point fits + a compact TLS table (flux bias, freq, tau, ~FWHM).
    """
    y = ds["state"]

    if "z_duration" not in y.dims:
        raise KeyError(f"Expected 'z_duration' in state.dims, got {y.dims!r}")

    min_points = 3
    if "flux_bias" in y.dims:
        count = y.count(dim="z_duration")
        std   = y.std(dim="z_duration", ddof=0) 
        valid = (count >= min_points) & np.isfinite(std) & (std > 0)

        y = y.where(valid, drop=True)

        if y.sizes.get("flux_bias", 0) == 0:
            raise ValueError("No valid traces to fit (all columns empty or constant).")
    else:
        if int(y.count(dim="z_duration")) < min_points or float(y.std(dim="z_duration", ddof=0)) <= 0:
            raise ValueError("Single trace is too short or constant for fitting.")

    
    fit_data = fit_oscillation_decay_exp(y, "z_duration")
    fit_data.attrs = {"long_name": "flux duration", "units": "ns"}
    fitted = oscillation_decay_exp(
        ds.state.z_duration,
        fit_data.sel(fit_vals="a"),
        fit_data.sel(fit_vals="f"),
        fit_data.sel(fit_vals="phi"),
        fit_data.sel(fit_vals="offset"),
        fit_data.sel(fit_vals="decay"),
    )

    frequency = fit_data.sel(fit_vals="f").where(lambda x: x > 0)
    frequency.name = "frequency"
    frequency.attrs = {"long_name": "oscillation frequency", "units": "MHz"}


    decay = fit_data.sel(fit_vals="decay")
    decay.attrs = {"long_name": "decay", "units": "nSec"}

    tau = 1 / fit_data.sel(fit_vals="decay")
    tau.attrs = {"long_name": "decay rate (envelope)", "units": "GHz"}

    # approximate spectral FWHM for an exponential envelope:
    tls_like_fwhm = (1.0 / (np.pi * tau)).rename("fwhm_mhz")
    tls_like_fwhm.attrs = {"long_name": "Lorentzian FWHM (approx.)", "units": "nSec"}

    min_amp = getattr(node.parameters, "min_tls_amp", 0.02)


    frequency = frequency.where(frequency > 0, drop=True)

    tls_qubit_list = []
    tls_flux_list = []
    tls_freq_list = []
    tls_tau_list = []
    tls_fwhm_list = []

    for q in ds.qubit.values:
        f_q = frequency.sel(qubit=q)
        a_q = fit_data.sel(fit_vals="a", qubit=q)

        mask = (a_q >= min_amp)

        f_s = f_q.where(mask).rolling(flux_bias=3, center=True).mean()
        
        peak_mask = peaks_dips(f_s, dim="flux_bias")
        cand = f_s.where(peak_mask).dropna("flux_bias")


        # sort by amplitude
        if "amplitude" in cand:
            cand = cand.sortby("amplitude", ascending=False)

        for fb in cand.flux_bias.values:
            tls_qubit_list.append(q)
            tls_flux_list.append(float(fb))
            tls_freq_list.append(float(f_q.sel(flux_bias=fb)))
            tau_here = float(tau.sel(qubit=q, flux_bias=fb))
            tls_tau_list.append(tau_here)
            # compute FWHM at the same location
            fwhm_here = float(tls_like_fwhm.sel(qubit=q, flux_bias=fb))
            tls_fwhm_list.append(fwhm_here)
   
    tls = xr.Dataset(
        data_vars=dict(
            tls_flux_bias=("tls", tls_flux_list),
            tls_frequency_mhz=("tls", tls_freq_list),
            tls_tau_us=("tls", tls_tau_list),
            tls_fwhm_mhz=("tls", tls_fwhm_list),
            tls_qubit=("tls", tls_qubit_list),
        )
    )

    ds_fit = ds.copy()
    ds_fit["fit_results"] = fit_data
    ds_fit["fitted"] = fitted
    ds_fit["frequency"] = frequency
    ds_fit["decay"] = decay
    ds_fit["tau"] = tau
    ds_fit["fwhm_mhz"] = tls_like_fwhm
    ds_fit = xr.merge([ds_fit, tls]) 

    fit_results: Dict[str, FitParameters] = {}

    for q in ds.qubit.values:
        mask = (tls["tls_qubit"].values == q)
        fit_results[str(q)] = FitParameters(
            success=True,
            tls_flux_biases=np.asarray(tls["tls_flux_bias"].values)[mask].tolist(),
            tls_frequencies_mhz=np.asarray(tls["tls_frequency_mhz"].values)[mask].tolist(),
            tls_tau_us=np.asarray(tls["tls_tau_us"].values)[mask].tolist(),
            tls_fwhm_mhz=np.asarray(tls["tls_fwhm_mhz"].values)[mask].tolist(),
        )

    return ds_fit, fit_results