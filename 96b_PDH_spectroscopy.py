# %%
"""
        PDH Spectroscopy vs Phase
Pound Drever Hall technique to find a resonator frequency and phase in the resonator.
    - The carrier frequency is swept:
    - The relative phase between the carrier and the modulation is swept
Ref: https://pubs.aip.org/aapt/ajp/article-abstract/69/1/79/1055569/An-introduction-to-Pound-Drever-Hall-laser

Prerequisites:
    - Calibration of the time of flight, offsets, and gains (referenced as "time_of_flight").
    - Calibration of the IQ mixer connected to the readout line (be it an external mixer or an Octave port).
    - Identification of the resonator's resonance frequency (referred to as "resonator_spectroscopy_multiplexed").
    - Configuration of the readout pulse amplitude (the pulse processor will sweep up to twice this value) and duration.
    - Specification of the expected resonator depletion time in the configuration.

Next steps before going to the next node:
    - Update the resonator_IF and resonator_phase in the configuration.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results.data_handler import DataHandler
from configuration_MWFEM import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import warnings
import time

# matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


###################
# The QUA program #
###################

n_avg = 1  # The number of averages
# Qubit detuning sweep with respect to qubit_IF
fs = np.arange(50 * u.MHz, 100 * u.MHz, 100 * u.kHz)
phases = np.arange(0, 1, 0.01)


def update_pdh_freqs(f, fm):
    update_frequency("resonator", f)
    update_frequency("resonator_sb_high", f + fm)
    update_frequency("resonator_sb_low", f - fm)
    update_frequency("pdh_demod", f + fm)


def play_pdh_pulse():
    play("pdh_carrier", "resonator")
    play("pdh_modulation", "resonator_sb_high")
    play("pdh_modulation", "resonator_sb_low")


with program() as PDH_spectroscopy:
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    f = declare(int)
    fm = declare(int, value=pdh_mod_IF)
    ph = declare(fixed)
    n = declare(int)

    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()

    # outside loop is for averaging many spectra
    with for_(n, 0, n < n_avg, n + 1):
        # loop over phases
        with for_(*from_array(ph, phases)):
            # loop over IFs
            with for_(*from_array(f, fs)):
                # update the frequency
                update_pdh_freqs(f, fm)

                # reset the phase of elements so that we always start with the same phase
                reset_global_phase()
                # set a relative phase between carrier and modulation
                frame_rotation_2pi(+ph, "resonator_sb_high")
                frame_rotation_2pi(-ph, "resonator_sb_high")

                # align all the elements so that they all start after the first play() command
                align()
                # This is the actual pdh pulse we will demodulate
                play_pdh_pulse()
                # measure the pdh signal with a separate element which oscillates at the sideband frequency
                # and save the result into the pdh variable. Save also the raw acquired data into adc_st
                measure(
                    "readout",
                    "pdh_demod",
                    None,
                    dual_demod.full("cos", "out1", "sin", "out2", I),
                    dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
                )

                # Save the 'I' & 'Q' quadratures to their respective streams
                save(I, I_st)
                save(Q, Q_st)
                wait(1 * u.us)

        save(n, n_st)
        wait(1 * u.us)

    # stream processing handling
    with stream_processing():
        n_st.save("iterations")
        I_st.buffer(len(fs)).buffer(len(phases)).average().save("I")
        Q_st.buffer(len(fs)).buffer(len(phases)).average().save("Q")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)


#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=20_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, PDH_spectroscopy, simulation_config)
    con1 = job.get_simulated_samples().con1
    con1.plot(analog_ports=["1", "2", "3", "4"])
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PDH_spectroscopy)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iterations"], mode="live")
    # Live plotting
    fig = plt.figure(figsize=(8, 4))

    # Create a colormap
    import matplotlib.colors as mcolors

    cmap = plt.get_cmap("coolwarm")  # 'coolwarm' goes from red to blue
    norm = mcolors.Normalize(vmin=0, vmax=1)  # Normalize phases from 0 to 1

    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iterations = results.fetch_all()
        S = u.demod2volts(I + 1j * Q, readout_len)
        R = np.abs(S)  # Amplitude

        # Plot results
        plt.suptitle("Pound spectroscopy")

        plt.subplot(121)
        plt.cla()
        for i, p in enumerate(phases):
            plt.plot(fs / u.MHz, R[i, :], linewidth=1, color=cmap(norm(p)), alpha=0.5)
        plt.title("PDH spectroscopy", fontsize=12)
        plt.xlabel("Frequency [MHz]", fontsize=12)
        plt.ylabel("PDH signal", fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)

        plt.subplot(122)
        plt.cla()
        plt.pcolor(fs / u.MHz, phases, R)
        plt.title("PDH spectroscopy: freq vs phase", fontsize=12)
        plt.xlabel("Frequency detuning [MHz]", fontsize=12)
        plt.ylabel("Phase [2pi]", fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)

        plt.tight_layout()
        plt.pause(0.1)

    plt.show()

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "fs": fs,
            "phases": phases,
            "I": I,
            "Q": Q,
            "R": R,
        }
        # Initialize the DataHandler
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {
            Path(__file__).name: Path(__file__).name,
            "configuration_with_octave.py": "configuration_with_octave.py",
        }
        # Save results
        data_folder = data_handler.save_data(data=data)

# %%
