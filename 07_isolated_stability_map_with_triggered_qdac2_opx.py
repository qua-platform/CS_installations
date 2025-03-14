"""
define for the 2 first axis: the number of points, the gates to sweep from start to end values
    e.g. dim_0_pts = 100, dim_0_sweeps = {"gate_1": {'start' = -1V, 'end' = 1V}}
         dim_1_pts = 200, dim_1_sweeps = {"gate_2": {'start' = 0V, 'end' = .1V}}

    define the loading sequences used to load different electron numbers N.
    loading_points = [val_1, val_2, val_3, ...] for N=0, 1, 2, ... (= dim_2)
    loading_sequence = [go_to_emptying_point, wait_time, go_to_loading_point(k),
                        wait_time, go_to_isolated_point]

    for k in dim_2: <- change the number of electrons loaded
        for j in dim_1: <- 'slow' axis = can be executed on PC

            apply the voltages(j) <- QDACs

            run loading_sequence(k) <- must be executed on the OPX right before the fast axis

            for i in dim_0: <- 'fast' axis = must be executed on the OPX
                apply the voltages(i) <- OPX
                measure <- must be stored on the OPX

            get the data from the OPX to PC
"""

import matplotlib.pyplot as plt
from configuration import *
from qdac2_driver import QDACII, load_voltage_list
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.loops.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.results.data_handler import DataHandler

##################
#   Parameters   #
##################
# Parameters Definition
n_avg = 100  # Number of averages
n_points_slow = 101  # Number of points for the slow axis
n_points_fast = 101  # Number of points for the fast axis

empty_position = [-0.1, -0.3]
empty_duration = 1000

isolated_position = [0.3, -0.1]
loading_duration = 1000

dc_duration = 400

buffer = 100

seq = VoltageGateSequence(configuration=config, elements=["P1_sticky", "P2_sticky"])

seq.add_points(name="empty_point", coordinates=empty_position, duration=empty_duration)
seq.add_points(name="manipulation_point", coordinates=[0.0, 0.0], duration=loading_duration)
seq.add_points(name="isolated_point", coordinates=isolated_position, duration=readout_len)

loading_points = [[0.1, -0.3], [0.2, -0.2], [0.3, -0.1]]

p1_amp = [list[0] for list in loading_points]
p2_amp = [list[1] for list in loading_points]


###################
# The QUA program #
###################
with program() as prog:
    n = declare(int)
    dc = declare(fixed)
    a1 = declare(fixed)
    a2 = declare(fixed)
    dc_st = declare_stream()

    with for_each_((a1, a2), (p1_amp, p2_amp)):
        with strict_timing_():
            seq.add_step(voltage_point_name="empty_point")
            seq.add_step(voltage_point_name="manipulation_point")
            seq.add_step(voltage_point_name="isolated_point")
            seq.add_compensation_pulse()
        wait(empty_duration * u.ns, "P1", "P2")
        play("step" * amp(a1 * 4), "P1", duration=loading_duration * u.ns)
        play("step"* amp(a2 * 4), "P2", duration=loading_duration * u.ns)
        align("P1", "P2", "TIA")
        measure("readout", "TIA", None, integration.full("constant", dc, "out2"))
        save(dc, dc_st)
        seq.ramp_to_zero(4)


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

## QDAC2 section
# Create the qdac instrument
# qdac = QDACII("Ethernet", IP_address="127.0.0.1", port=5025)  # Using Ethernet protocol
# # qdac = QDACII("USB", USB_device=4)  # Using USB protocol
# # Set up the qdac and load the voltage list
# load_voltage_list(
#     qdac,
#     channel=1,
#     dwell=2e-6,
#     slew_rate=2e7,
#     trigger_port="ext1",
#     output_range="low",
#     output_filter="med",
#     voltage_list=voltage_values_fast,
# )

###########################
# Run or Simulate Program #
###########################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, prog, simulation_config)
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
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
    # Get results from QUA program and initialize live plotting
    results = fetching_tool(job, data_list=["I", "Q", "dc_signal", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I, Q, DC_signal, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, reflectometry_readout_length, single_demod=True)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        DC_signal = u.demod2volts(DC_signal, readout_len, single_demod=True)
        # Progress bar
        progress_counter(iteration, n_points_slow, start_time=results.start_time)
        # Plot data
        plt.subplot(121)
        plt.cla()
        plt.title(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.pcolor(voltage_values_fast, voltage_values_slow, R)
        plt.xlabel("Fast voltage axis [V]")
        plt.ylabel("Slow voltage axis [V]")
        plt.subplot(122)
        plt.cla()
        plt.title("Phase [rad]")
        plt.pcolor(voltage_values_fast, voltage_values_slow, phase)
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
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])
