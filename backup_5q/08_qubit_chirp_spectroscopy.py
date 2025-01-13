# %%
"""
        CHIRP spectroscopy
"""

import matplotlib
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.results.data_handler import DataHandler
from macros_voltage_gate_sequence import VoltageGateSequence
from scipy import signal

from configuration_with_lffem import *
from macros_initialization_and_readout_2q import *

matplotlib.use('TkAgg')


###################
# The QUA program #
###################

n_avg = 200  # Number of averages
set_init_as_dc_offset = True

qubit = "qubit1"
sweep_gates = ["P0_sticky", "P1_sticky"]
tank_circuit = "tank_circuit1"
threshold = TANK_CIRCUIT_CONSTANTS[tank_circuit]["threshold"]
num_output_streams = 2

freqs = np.arange(-120e6, 120e6, 0.5e6)
level_init_arr = np.array(LEVEL_INIT)
level_readout_arr = np.array(LEVEL_READOUT)

duration_init = 10_000 # DO NOT USE * u.ns
duration_ramp_init = 200 # DO NOT USE * u.ns
duration_readout = 1_000 + REFLECTOMETRY_READOUT_LEN # DO NOT USE * u.ns
duration_ramp_readout = 52 # DO NOT USE * u.ns

if set_init_as_dc_offset:
    level_readout_offset_arr = level_readout_arr - level_init_arr
    level_init_offset_arr = np.array([0.0, 0.0]) # level_init_arr - level_init_arr

level_init_list = level_init_arr.tolist()
level_readout_list = level_readout_arr.tolist()
level_readout_offset_list = level_readout_offset_arr.tolist()
level_init_offset_list = level_init_offset_arr.tolist()


seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization", level_init_offset_list, duration_init)
seq.add_points("readout", level_readout_offset_list, duration_readout)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "tank_circuit": tank_circuit,
    "n_avg": n_avg,
    "config": config,
}


with program() as QUBIT_CHIRP:
    f = declare(int)
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)
    P = declare(bool)
    I_st = [declare_stream() for _ in range(num_output_streams)]
    Q_st = [declare_stream() for _ in range(num_output_streams)]
    P_st = [declare_stream() for _ in range(num_output_streams)]
    
    current_level = declare(fixed, value=[0.0 for _ in sweep_gates])
    seq.current_level = current_level

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I, Q, P)

    if set_init_as_dc_offset:
        for sg, lvl_init in zip(sweep_gates, level_init_list):
            set_dc_offset(sg, "single", lvl_init)

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(f, freqs)):
            update_frequency("qubit1", f)

            P = measure_parity(I, Q, P, I_st[0], Q_st[0], P_st[0], tank_circuit, threshold)
            
            # Play the triangle
            align()
            seq.add_step(voltage_point_name="initialization", ramp_duration=duration_ramp_init) # NEVER u.ns

            wait(duration_ramp_init // 4, "rf_switch", qubit)
            play("trigger", "rf_switch", duration=(RF_SWITCH_DELAY + CONST_LEN) // 4)
            wait(RF_SWITCH_DELAY // 4, qubit)
            play("const", qubit, chirp=(19841,"Hz/nsec"))

            align()
            P = measure_parity(I, Q, P, I_st[1], Q_st[1], P_st[1], tank_circuit, threshold)

            # DO NOT REMOVE: bring the voltage back to dc_offset level.
            # Without this, it can accumulate a precision error that leads to unwanted large voltage (max of the range).
            align()
            seq.ramp_to_zero()

            # Save the LO iteration to get the progress bar
            save(n, n_st)
            wait(250)

        # Save the LO iteration to get the progress bar
        save(n, n_st)

    # Stream processing section used to process the data before saving it
    with stream_processing():
        n_st.save("iteration")
        for idx in range(num_output_streams):
            I_st[idx].buffer(len(freqs)).average().save(f"I{idx}_{tank_circuit}")
            Q_st[idx].buffer(len(freqs)).average().save(f"Q{idx}_{tank_circuit}")
            P_st[idx].boolean_to_int().buffer(len(freqs)).average().save(f"P{idx}_{tank_circuit}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, QUBIT_CHIRP, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(QUBIT_CHIRP)

    # Get results from QUA program
    fetch_names = ["iteration"]
    for idx in range(num_output_streams):
        fetch_names.extend([f"I{idx}_{tank_circuit}", f"Q{idx}_{tank_circuit}", f"P{idx}_{tank_circuit}"])
    results = fetching_tool(job, data_list=fetch_names, mode="live")

    fig = plt.figure()
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    
    while results.is_processing():
        # Fetch results
        iteration, I0, Q0, P0, I1, Q1, P1 = results.fetch_all()

        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())

        S = I + 1j * Q
        R = np.abs(S)
        phase = np.unwrap(np.angle(S))

        plt.suptitle("Qubit Chirp Spectroscopy")
        plt.clf()
        # Plot I
        ax = plt.subplot(3, 1, 1)
        ax.plot(freqs, R)
        plt.xlabel("Freq")
        plt.ylabel("R [V]")

        ax = plt.subplot(3, 1, 2)
        ax.plot(freqs, phase)
        plt.xlabel("Freq")
        plt.ylabel("Phase [rad]")

        ax = plt.subplot(3, 1, 2)
        ax.plot(freqs, P)
        plt.xlabel("Freq")
        plt.ylabel("Average Parity")

        plt.tight_layout()
        plt.pause(1)

    # Fetch results
    iteration, I, Q, P = results.fetch_all()
    save_data_dict["I"] = I
    save_data_dict["Q"] = Q
    save_data_dict["P"] = P

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {
        script_name: script_name,
        **default_additional_files,
    }
    data_handler.save_data(data=save_data_dict, name=script_name.replace(".py",""))

    qm.close()

# %%
