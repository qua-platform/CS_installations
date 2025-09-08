from __future__ import annotations
from typing import TYPE_CHECKING, List


from typing import List

import matplotlib.pyplot as plt
import xarray as xr
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from qualang_tools.units import unit
from qualibration_libs.plotting import QubitGrid, grid_iter
from quam_builder.architecture.superconducting.qubit import AnyTransmon
from qualibration_libs.analysis import lorentzian_peak
import numpy as np
u = unit(coerce_to_integer=True)


def plot_raw_data_with_fit(ds: xr.Dataset, qubits: List[AnyTransmon], fits: xr.Dataset):
    """
    Plots the resonator spectroscopy amplitude IQ_abs with fitted curves for the given qubits.

    Parameters
    ----------
    ds : xr.Dataset
        The dataset containing the quadrature data.
    qubits : list of AnyTransmon
        A list of qubits to plot.
    fits : xr.Dataset
        The dataset containing the fit parameters.

    Returns
    -------
    Figure
        The matplotlib figure object containing the plots.

    Notes
    -----
    - The function creates a grid of subplots, one for each qubit.
    - Each subplot contains the raw data and the fitted curve.
    """
    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        plot_individual_data_with_fit(ax, ds, qubit, fits.sel(qubit=qubit["qubit"]))

    grid.fig.suptitle("Flux duration vs flux amplitude")
    grid.fig.set_size_inches(15, 9)
    grid.fig.tight_layout()
    return grid.fig


def plot_parabolas_with_fit(ds: xr.Dataset, qubits: List[AnyTransmon], fits: xr.Dataset):
    """
    Plots the resonator spectroscopy amplitude IQ_abs with fitted curves for the given qubits.

    Parameters
    ----------
    ds : xr.Dataset
        The dataset containing the quadrature data.
    qubits : list of AnyTransmon
        A list of qubits to plot.
    fits : xr.Dataset
        The dataset containing the fit parameters.

    Returns
    -------
    Figure
        The matplotlib figure object containing the plots.

    Notes
    -----
    - The function creates a grid of subplots, one for each qubit.
    - Each subplot contains the raw data and the fitted curve.
    """
    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        plot_individual_parabolas_with_fit(ax, ds, qubit, fits.sel(qubit=qubit["qubit"]))

    grid.fig.suptitle("flux duration vs flux amplitude frequency ")
    grid.fig.set_size_inches(15, 9)
    grid.fig.tight_layout()
    return grid.fig


def plot_individual_data_with_fit(ax: Axes, ds: xr.Dataset, qubit: dict[str, str], fit: xr.Dataset = None):
    """
    Plots individual qubit data on a given axis with optional fit.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axis on which to plot the data.
    ds : xr.Dataset
        The dataset containing the quadrature data.
    qubit : dict[str, str]
        mapping to the qubit to plot.
    fit : xr.Dataset, optional
        The dataset containing the fit parameters (default is None).

    Notes
    -----
    - If the fit dataset is provided, the fitted curve is plotted along with the raw data.
    """
    qname = qubit["qubit"]

    da = ds.sel(qubit=qname).state
    da.plot(ax=ax, x="flux_bias", y="z_duration")
    ax.set_title(qubit["qubit"])
    ax.set_ylabel("Flux_time (uS)")
    ax.set_xlabel(" Flux (V)")

    # axis labels from attrs 
    ylab = f"{da.z_duration.attrs.get('long_name', 'z_duration')} ({da.z_duration.attrs.get('units','')})"
    xlab = f"{da.flux_bias.attrs.get('long_name', 'flux_bias')} ({da.flux_bias.attrs.get('units','')})"
    ax.set_title(qname)
    ax.set_xlabel(xlab.strip())
    ax.set_ylabel(ylab.strip())

    # overlay TLS flux-biases
    if fit is not None and "tls_flux_bias" in fit and "tls_qubit" in fit:
        tls_mask = (fit.tls_qubit == qname)
        if tls_mask.any():
            for fb in fit.tls_flux_bias.where(tls_mask, drop=True).values:
                ax.axhline(float(fb), linestyle="--", alpha=0.5)

def plot_tls_decay_envelopes(ds: xr.Dataset, qubits: List[AnyTransmon], fits: xr.Dataset):
    grid = QubitGrid(ds, [q.grid_location for q in qubits])

    for ax, qubit in grid_iter(grid):
        qname = qubit["qubit"]
        ax.set_title(f"{qname} – TLS envelopes")
        ax.set_ylabel("Flux duration (arb. units)")
        ax.set_xlabel("State")

        # draw the colormap in the background
        ds.sel(qubit=qname).state.plot(ax=ax, x="flux_bias", y="z_duration")
        
        # pick TLS rows belonging to this qubit
        tls_mask = (fits.tls_qubit == qname)
        if tls_mask.any():
            for fb, tau_us in zip(fits.tls_flux_bias.where(tls_mask, drop=True).values,
                                  fits.tls_tau_us.where(tls_mask, drop=True).values):
                # fetch fitted params at that flux
                a     = fits.fit_results.sel(qubit=qname, fit_vals="a").sel(flux_bias=fb, method="nearest").values
                off   = fits.fit_results.sel(qubit=qname, fit_vals="offset").sel(flux_bias=fb, method="nearest").values
                decay = fits.fit_results.sel(qubit=qname, fit_vals="decay").sel(flux_bias=fb, method="nearest").values

                t = ds.state.sel(qubit=qname, flux_bias=fb, method="nearest").z_duration.values
                # envelope = offset +- |a| * exp(-decay * t)
                env = np.abs(a) * np.exp(-decay * t)
                ax.plot(t, off + env, linewidth=2)
                ax.plot(t, off - env, linewidth=2)
                ax.axhline(fb, linestyle="--", alpha=0.3) 

    grid.fig.suptitle("TLS resonance decay envelopes")
    grid.fig.set_size_inches(15, 9)
    grid.fig.tight_layout()
    return grid.fig


def plot_individual_parabolas_with_fit(ax: Axes, ds: xr.Dataset, qubit: dict[str, str], fit: xr.Dataset = None):
    """
    Plots individual qubit data on a given axis with optional fit.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axis on which to plot the data.
    ds : xr.Dataset
        The dataset containing the quadrature data.
    qubit : dict[str, str]
        mapping to the qubit to plot.
    fit : xr.Dataset, optional
        The dataset containing the fit parameters (default is None).

    Notes
    -----
    - If the fit dataset is provided, the fitted curve is plotted along with the raw data.
    """
    detuning = fit.artifitial_detuning

    (fit.sel(fit_vals="f").fit_results * 1e3 - detuning).plot(ax=ax, linestyle="--", marker=".")
    ax.set_title(qubit["qubit"])
    ax.set_xlabel("Flux offset (V)")
    ax.set_ylabel("Qubit SweetSpot detuning (MHz)")

    flux_offset = fit.flux_offset

    ax.axvline(flux_offset, color="red", linestyle="--", label="Flux offset")

    freq_offset = fit.freq_offset.values * 1e-3 - detuning

    ax.axhline(freq_offset, color="green", linestyle="--", label="Detuning from SweetSpot")

    ax.legend()


