# %%

import numpy as np
import matplotlib.pyplot as plt

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_octave import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
from qdac2_driver import QDACII, load_voltage_list
from macros import RF_reflectometry_macro, DC_current_sensing_macro
from qualang_tools.results.data_handler import DataHandler

##################
#   Parameters   #
##################

# Points in the charge stability map [V1, V2]
level_empty = [-0.2, 0.0]
duration_empty = 5000

seq = VoltageGateSequence(config, ["P1_sticky", "P2_sticky"])
seq.add_points("empty", level_empty, duration_empty)
seq.add_points("initialization", level_init, duration_init)
seq.add_points("readout", level_readout, duration_readout)

###################
# The QUA program #
###################
with program() as PSB_search_prog:
    seq.add_step(voltage_point_name="empty")
    seq.add_step(voltage_point_name="initialization")
    seq.add_step(voltage_point_name="readout")
    seq.add_compensation_pulse(duration=duration_compensation_pulse)

    wait((duration_init + duration_empty) * u.ns, "tank_circuit")
    measure(
        "readout",
        "tank_circuit",
        None,
        # demod.full("cos", I, "out2"),
        # demod.full("sin", Q, "out2"),
    )
    wait(1_000 * u.ns, "tank_circuit")

    # Ramp the voltage down to zero at the end of the triangle (needed with sticky elements)
    seq.ramp_to_zero()


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, cluster_name=cluster_name, octave_calibration_db_path=os.getcwd()
)

###########################
# Run or Simulate Program #
###########################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=4_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PSB_search_prog, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # span for duration_empty, duration_init,duration_readout
    t0_list = [
        np.nonzero(samples.con1.analog[k])[0] for k in samples.con1.analog.keys()
    ]
    t0_list = [t0[0] for t0 in t0_list if len(t0) > 0]
    t0 = min(t0_list)
    durations = [
        duration_empty,
        duration_init,
        duration_readout,
        duration_compensation_pulse,
    ]
    texts = [
        "Empty",
        "Initialization",
        "Readout",
        "Compensation",
    ]
    colors = ["blue", "green", "orange", "red"]
    for duration, color, text in zip(durations, colors, texts):
        t1 = t0 + duration
        plt.axvspan(t0, t1, color=color, alpha=0.3)
        plt.text(
            (t0 + t1) / 2,
            -0.1,
            text,
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=12,
            color=color,
            rotation="vertical",
        )
        t0 = t1

    # # Get the waveform report object
    # waveform_report = job.get_simulated_waveform_report()
    # # Cast the waveform report to a python dictionary
    # waveform_dict = waveform_report.to_dict()
    # # Visualize and save the waveform report
    # waveform_report.create_plot(
    #     samples, plot=True, save_path=str(Path(__file__).resolve())
    # )
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PSB_search_prog)
    # Get results from QUA program and initialize live plotting
    results = fetching_tool(
        job, data_list=["I", "Q", "dc_signal", "iteration"], mode="live"
    )
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I, Q, DC_signal, iteration = results.fetch_all()
        # Convert results into Volts
        min_idx = min(I.shape[0], Q.shape[0])
        S = u.demod2volts(
            I[:min_idx, :] + 1j * Q[:min_idx, :],
            reflectometry_readout_length,
            single_demod=True,
        )
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        DC_signal = u.demod2volts(DC_signal, readout_len, single_demod=True)
        # Progress bar
        progress_counter(iteration, n_points_slow)
        # Plot data
        plt.subplot(121)
        plt.cla()
        plt.title(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.pcolor(voltage_values_fast, voltage_values_slow[:min_idx], R)
        plt.xlabel("Fast voltage axis [V]")
        plt.ylabel("Slow voltage axis [V]")
        plt.subplot(122)
        plt.cla()
        plt.title("Phase [rad]")
        plt.pcolor(voltage_values_fast, voltage_values_slow[:min_idx], phase)
        plt.xlabel("Fast voltage axis [V]")
        plt.ylabel("Slow voltage axis [V]")
        plt.tight_layout()
        plt.pause(0.1)
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"I_data": I})
    save_data_dict.update({"Q_data": Q})
    save_data_dict.update({"DC_signal_data": DC_signal})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {
        script_name: script_name,
        **default_additional_files,
    }
    data_handler.save_data(
        data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0]
    )
