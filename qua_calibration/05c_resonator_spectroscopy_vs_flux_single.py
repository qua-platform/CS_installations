"""
        RESONATOR SPECTROSCOPY VERSUS CURRENT (GS200)
This sequence measures the resonator by sending a readout pulse and demodulating the signals to extract the
'I' and 'Q' quadratures. It is performed across readout intermediate dfs for multiple current biases supplied
by a Yokogawa GS200 in current mode. The resonator frequency vs current is then extracted and fitted.

Prereqs:
    - Time of flight, offsets, gains calibrated.
    - Readout IQ mixer calibrated.
    - Readout pulse amplitude and duration configured.
    - Depletion time specified in the configuration.
"""

from pathlib import Path
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.optimize import curve_fit

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_mw_fem import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.results.data_handler import DataHandler

# Yokogawa GS200 (QCoDeS)
from qcodes.instrument_drivers.yokogawa import YokogawaGS200

##################
#   Parameters   #
##################
# Averaging
n_avg = 6000


# Current sweep (A) provided by GS200 in CURR mode
i_min = -0.010
i_max = +0.010
i_step = 0.0005
currents = np.arange(i_min, i_max + i_step / 2, i_step)

resonator = "rr1"

# Parameters Definition
n_avg = 200  # The number of averages
frequencies = {
    "rr1": np.arange(10e6, +450e6, 20e3),
    "rr2": np.arange(80e6, +130e6, 100e3),
}

# GS200 settings
gs_address = "USB::0xB21::0x39::YOUR_SERIAL::INSTR"  # <-- set your VISA address
voltage_limit = 1.0          # compliance voltage (V) in CURR mode
auto_range = True            # if False, set current_range below
current_range = 0.01         # A, used only when auto_range == False
settle_time_s = 0.02         # wait after setting current

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "frequencies": frequencies,
    "currents": currents,
    "config": config,
}

###################
# The QUA program #
###################
# Single-current program: sweep dfs and average; no DC sweep inside QUA
with program() as resonator_spec_1D:
    n = declare(int)
    f = declare(int)
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()
    n_st = declare_stream()

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(f, frequencies[resonator])):
            update_frequency(resonator, f)
            measure(
                "readout",
                resonator,
                None,
                dual_demod.full("cos", "sin", I),
                dual_demod.full("minus_sin", "cos", Q),
            )
            wait(depletion_time * u.ns, resonator)
            save(I, I_st)
            save(Q, Q_st)
        save(n, n_st)

    with stream_processing():
        I_st.buffer(len(frequencies[resonator])).average().save("I")
        Q_st.buffer(len(frequencies[resonator])).average().save("Q")
        n_st.save("iteration")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, resonator_spec_1D, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)

    # Open GS200 (current mode)
    gs = YokogawaGS200("gs200", address=gs_address, terminator="\n")
    gs.source_mode("CURR")
    gs.voltage_limit(voltage_limit)
    gs.auto_range(auto_range)
    # if not auto_range:
    #     gs.current_range(current_range)
    # gs.current(0.0)
    # gs.output("on")

    # Allocate result maps
    F = len(frequencies[resonator])
    M = len(currents)
    R = np.zeros((F, M))
    PH = np.zeros((F, M))

    # Live plotting
    fig = plt.figure()
    # plot will be updated after each current point

    try:
        for j, i_set in enumerate(currents):
            # Set current and wait for settling
            gs.ramp_current(i_set, 0.00001, 1)  
            # gs.current(float(i_set))
            # time.sleep(settle_time_s)

            # Run QUA for this current point
            job = qm.execute(resonator_spec_1D)
            results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
            interrupt_on_close(fig, job)

            while results.is_processing():
                I, Q, iteration = results.fetch_all()
                progress_counter(iteration, n_avg, start_time=results.get_start_time())

            # Convert to volts and store
            S = u.demod2volts(I + 1j * Q, readout_len)
            R[:, j] = np.abs(S)
            PH[:, j] = signal.detrend(np.unwrap(np.angle(S)))

            # Update live plot
            plt.clf()
            plt.suptitle(f"Resonator spectroscopy - LO = {resonator_LO / u.GHz} GHz")
            plt.subplot(211)
            plt.title(r"$R=\sqrt{I^2 + Q^2}$")
            plt.pcolor(currents, (frequencies[resonator] + resonator_LO) / u.GHz, R)
            plt.ylabel("Frequency [GHz]")

            plt.subplot(212)
            plt.title("Phase")
            plt.pcolor(currents, (frequencies[resonator] + resonator_LO) / u.GHz, PH)
            plt.xlabel("Current [A]")
            plt.ylabel("Frequency [GHz]")
            plt.tight_layout()
            plt.pause(0.1)

        # Close QM and return GS200 to safe state before fitting
        qm.close()
        # gs.current(0.0)
        # gs.output("off")
        # gs.close()

        plt.figure()
        plt.suptitle(f"Resonator spectroscopy - LO = {resonator_LO / u.GHz} GHz")
        plt.pcolor(currents, (frequencies[resonator]) / u.MHz, R)
        plt.xlabel("Current [A]")
        plt.ylabel("Readout IF [MHz]")
        plt.legend()

        # Save results
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        save_data_dict.update({"I_data": R})   # amplitude map
        save_data_dict.update({"Q_data": PH})  # phase map (unwrapped & detrended)
        save_data_dict.update({"fig_live": fig})
        data_handler.additional_files = {script_name: script_name, **default_additional_files}
        data_handler.save_data(
            data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0] + "_gs200_curr"
        )

    except Exception as e:
        print(f"An exception occurred: {e}")
        try:
            qm.close()
        except Exception:
            pass
