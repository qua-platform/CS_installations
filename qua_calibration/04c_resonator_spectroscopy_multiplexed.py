"""
    RESONATOR SPECTROSCOPY — FLEXIBLE N-RESONATOR VERSION (QM/QUA)

This script generalizes your two-resonator spectroscopy to **any** number of
resonators with customizable labels and plotting markers. Edit the
`RESONATORS` list below to add/remove resonators and to set their labels,
intermediate frequencies, and readout amplitudes.

Key features
------------
- Arbitrary number of resonators: just add entries to `RESONATORS`.
- Per-resonator config: name, label (for plots), IF, readout amplitude.
- Optional simultaneous (multiplexed) or sequential measurement.
- Stream names are auto-generated: `I_<name>`, `Q_<name>`.
- Live plotting combines all resonators in two panels (|S| and phase) with a legend.
- Results saved with all traces and metadata.

Prerequisites
-------------
- Valid QM configuration in `configuration_mw_fem.py` (imports `config`, `u`,
  `readout_len`, `depletion_time`, `resonator_LO`, `save_dir`, `default_additional_files`, etc.).
- Proper time-of-flight, offsets, gains calibration.
- IQ mixer calibration on the readout line (external or Octave).
- Reasonable initial guesses for each resonator IF.

Usage
-----
- Edit the `RESONATORS` list and run.
- Toggle `measure_simultaneously` to True for fully multiplexed acquisition.
- Toggle `simulate` for simulation vs execution on hardware.

"""
from __future__ import annotations
from typing import List, Dict, Any

from pathlib import Path
import numpy as np
import math
import time
import matplotlib
import matplotlib.pyplot as plt
from scipy import signal

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_mw_fem import *  # noqa: F401, F403 (expects: config, u, readout_len, depletion_time, resonator_LO, etc.)
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.results.data_handler import DataHandler

matplotlib.use("TkAgg")

##################
#   Parameters   #
##################
# Define your resonators here. Each entry must include:
# - name: the element name in the QM config (e.g., "rr2")
# - IF:   intermediate frequency (in Hz) to sweep around (e.g., resonator_IF_q2)
# - amp:  readout amplitude variable from config (optional; kept for completeness)
# - label: pretty label used in plots/legend (optional; defaults to name)
RESONATORS: List[Dict[str, Any]] = [
    {"name": "rr1", "IF": resonator_IF_q1, "label": "Q1"},
    {"name": "rr2", "IF": resonator_IF_q2, "label": "Q2"},
    {"name": "rr3", "IF": resonator_IF_q3, "label": "Q3"},
    {"name": "rr4", "IF": resonator_IF_q3, "label": "Q4"},
    {"name": "rr5", "IF": resonator_IF_q3, "label": "Q5"},
    {"name": "rr6", "IF": resonator_IF_q3, "label": "Q6"},
]

# Averaging
n_avg = 100

# Frequency sweep (shared for all resonators; each is swept around its own IF)
span = 30.0 * u.MHz
step = 100 * u.kHz
# Sweep detunings: e.g., -30 MHz .. +30 MHz in steps of 100 kHz
dfs = np.arange(-span, span, step, dtype=int)

# Save dict scaffold
save_data_dict = {
    "n_avg": n_avg,
    "dfs": dfs,
    "config": config,
    "resonators": [{"name": r["name"], "IF": r["IF"], "label": r.get("label", r["name"]) } for r in RESONATORS],
}

# Measurement mode: set True to start all measures at the same time (full multiplexing)
# Set False to measure one-by-one in sequence
measure_simultaneously = False

###################
#   Sanity checks  #
###################
if len(RESONATORS) == 0:
    raise ValueError("RESONATORS list is empty. Add at least one resonator entry.")

# Convenience vectors
RES_NAMES = [r["name"] for r in RESONATORS]
RES_IFS   = [int(r["IF"]) for r in RESONATORS]
RES_LABS  = [r.get("label", r["name"]) for r in RESONATORS]

###################
#  QUA Program     #
###################
with program() as PROGRAM:
    n = declare(int)
    df = declare(int)

    n_st = declare_stream()

    # One I/Q and stream per resonator
    I = [declare(fixed) for _ in RESONATORS]
    Q = [declare(fixed) for _ in RESONATORS]
    I_st = [declare_stream() for _ in RESONATORS]
    Q_st = [declare_stream() for _ in RESONATORS]

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(df, dfs)):
            # Drain the resonators before the next readout
            wait(depletion_time * u.ns, *RES_NAMES)

            if measure_simultaneously:
                # Align all elements so the measure() calls start together
                align(*RES_NAMES)

            # Loop in Python over resonators to emit QUA ops
            for i, rr in enumerate(RES_NAMES):
                # Update per-resonator IF: f = df + IF
                update_frequency(rr, df + RES_IFS[i])

                # If measuring sequentially, ensure the next measure starts after the previous finishes (conservative)
                if not measure_simultaneously and i > 0:
                    align(RES_NAMES[i-1], rr)

                # Measure and demodulate I/Q
                measure(
                    "readout",
                    rr,
                    None,
                    dual_demod.full("cos", "sin", I[i]),
                    dual_demod.full("minus_sin", "cos", Q[i]),
                )
                save(I[i], I_st[i])
                save(Q[i], Q_st[i])

        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        for i, rr in enumerate(RES_NAMES):
            I_st[i].buffer(len(dfs)).average().save(f"I_{rr}")
            Q_st[i].buffer(len(dfs)).average().save(f"Q_{rr}")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    simulation_config = SimulationConfig(duration=10_000)
    job = qmm.simulate(config, PROGRAM, simulation_config)
    samples = job.get_simulated_samples()
    samples.con1.plot()
    waveform_report = job.get_simulated_waveform_report()
    waveform_dict = waveform_report.to_dict()
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
else:
    try:
        qm = qmm.open_qm(config)
        job = qm.execute(PROGRAM)

        # Build stream list for fetching tool dynamically: [I_<rr>, Q_<rr>, ... , "iteration"]
        stream_names = []
        for rr in RES_NAMES:
            stream_names.extend([f"I_{rr}", f"Q_{rr}"])
        stream_names.append("iteration")

        results = fetching_tool(job, stream_names, mode="live")

        fig = plt.figure()
        interrupt_on_close(fig, job)

        # Assign simple distinct markers/linestyles for clarity
        MARKERS = ["o", "s", "^", "D", "x", "*", "+", "v", "<", ">", "1", "2", "3", "4"]

        while results.is_processing():
            fetched = results.fetch_all()
            # fetched order: I_rr1, Q_rr1, I_rr2, Q_rr2, ..., iteration
            iteration = fetched[-1]
            progress_counter(iteration, n_avg, start_time=results.get_start_time())

            # Split I/Q
            I_list = fetched[0:2*len(RES_NAMES):2]
            Q_list = fetched[1:2*len(RES_NAMES):2]

            # Compute magnitude & phase
            RR_abs = []
            RR_phase = []
            for i in range(len(RES_NAMES)):
                S = u.demod2volts(I_list[i] + 1j * Q_list[i], readout_len)
                RR_abs.append(np.abs(S))
                RR_phase.append(np.angle(S))

            # Plot per-resonator panels (like the original: top=|S|, bottom=Phase)
            plt.figure(fig.number)
            plt.clf()
            ncols = len(RES_NAMES)
            fig_cur = plt.gcf()
            fig_cur.set_size_inches(max(3.2 * ncols, 8), 6, forward=True)
            fig_grid, axs = plt.subplots(2, ncols, num=fig.number)
            plt.subplots_adjust(wspace=0.35)
            if ncols == 1:
                import numpy as _np
                axs = _np.array(axs).reshape(2, 1)
            for i, lab in enumerate(RES_LABS):
                freqs_MHz = (RES_IFS[i] + dfs) / u.MHz
                # Magnitude
                axs[0, i].plot(freqs_MHz, RR_abs[i])
                axs[0, i].set_title(f"Resonator {RES_NAMES[i]}")
                axs[0, i].set_ylabel(r"|S| = $\sqrt{I^2+Q^2}$ [V]")
                # Phase
                ph = signal.detrend(np.unwrap(RR_phase[i]))
                axs[1, i].plot(freqs_MHz, ph)
                axs[1, i].set_xlabel("Readout IF [MHz]")
                axs[1, i].set_ylabel("Phase [rad]")
            plt.suptitle("Multiplexed resonator spectroscopy")
            plt.tight_layout()
            plt.pause(0.5)

            # Optional: Fit each resonance (if qualang_tools.plot.fitting is available)
            try:
                from qualang_tools.plot.fitting import Fit
                for i, lab in enumerate(RES_LABS):
                    freqs_MHz = (RES_IFS[i] + dfs) / u.MHz
                    # Create a NEW figure every time
                    fig_fit = plt.figure()
                    fit = Fit()
                    res_fit = fit.reflection_resonator_spectroscopy(freqs_MHz, RR_abs[i], plot=True)
                    plt.title(f"Resonator {RES_NAMES[i]} - LO: {resonator_LO / u.GHz} GHz")
                    plt.xlabel("Intermediate frequency [MHz]")
                    plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ [V]")
                    plt.tight_layout()

                    # Save every fit figure to disk with a unique name
                    data_handler = DataHandler(root_data_folder=save_dir)
                    save_data_dict.update({f"fig_fit_{lab}": fig_fit})
            except Exception:
                pass

            # Save results continuously (last values overwrite)
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            for i, rr in enumerate(RES_NAMES):
                save_data_dict[f"I_{rr}_data"] = I_list[i]
                save_data_dict[f"Q_{rr}_data"] = Q_list[i]
            save_data_dict.update({"fig_live": fig})
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])

    except Exception as e:
        print(f"An exception occurred: {e}")
    finally:
        try:
            qm.close()
        except Exception:
            pass
        print("Experiment QM is now closed")
        plt.show(block=True)
