import numpy as np
from scipy import signal
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from qualang_tools.plot.fitting import Fit
import qualang_tools.units as u

def plot_resonator_spectroscopy_plotly(npz_path, resonator_LO):
    """
    Load a .npz containing 'IF_frequencies', 'I_data', 'Q_data',
    plot amplitude & phase in Plotly with extra spacing, then fit.
    """

    # --- 1) Load & compute ---
    data = np.load(npz_path)
    freqs_Hz = data['IF_frequencies']
    freqs_MHz = freqs_Hz / 1e6
    I, Q = data['I_data'], data['Q_data']
    S = I + 1j * Q
    R = np.abs(S)
    phase = np.unwrap(np.angle(S))
    phase = signal.detrend(phase)

    # --- 2) Create Plotly subplots with more vertical_spacing ---
    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.15,  # increase space between panels
        subplot_titles=[r"$R=\sqrt{I^2+Q^2}$", "Phase"]
    )

    fig.add_trace(
        go.Scatter(x=freqs_MHz, y=R, mode='markers', marker=dict(size=6)),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=freqs_MHz, y=phase, mode='markers', marker=dict(size=6)),
        row=2, col=1
    )

    fig.update_xaxes(
        title_text="Intermediate frequency [MHz]",
        row=2, col=1,
        showgrid=True, gridcolor='lightgrey',
        ticks='inside', mirror=True
    )
    fig.update_yaxes(
        title_text=r"$R$ [V]",
        row=1, col=1,
        showgrid=True, gridcolor='lightgrey',
        ticks='inside', mirror=True
    )
    fig.update_yaxes(
        title_text="Phase [rad]",
        row=2, col=1,
        showgrid=True, gridcolor='lightgrey',
        ticks='inside', mirror=True
    )

    fig.update_layout(
        title=f"Resonator spectroscopy — LO = {resonator_LO/u.GHz:.3f} GHz",
        title_x=0.5,
        template='plotly_white',
        height=600, width=800,
        margin=dict(t=80, b=50, l=60, r=20)
    )

    fig.show()

    # --- 3) fit the resonance (amplitude) using Matplotlib ---
    fit = Fit()
    res_spec_fit = fit.reflection_resonator_spectroscopy(
        freqs_Hz / u.MHz,
        R,
        plot=True
    )
    import matplotlib.pyplot as plt
    plt.title(f"Resonator spectroscopy — LO = {resonator_LO/u.GHz:.3f} GHz")
    plt.xlabel("Intermediate frequency [MHz]")
    plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ [V]")
    print(
        f"Resonator resonance frequency to update in the config: "
        f"resonator_IF = {res_spec_fit['f'][0]:.6f} MHz"
    )
    plt.show()

