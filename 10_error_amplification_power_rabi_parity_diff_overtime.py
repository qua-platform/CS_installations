# %%
"""
        spectroscopy
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

n_avg = 10  # Number of averages

qubit = "qubit1"
sweep_gates = ["P0_sticky", "P1_sticky"]
tank_circuit = "tank_circuit1"
threshold = TANK_CIRCUIT_CONSTANTS[tank_circuit]["threshold"]
num_output_streams = 2

# Pulse duration sweep in ns - must be larger than 4 clock cycles
a_min = 0.8
a_max = 1.2
a_step = 0.001
amp_scalilngs = np.arange(a_min, a_max, a_step)
# Number of applied Rabi pulses sweep
max_n_pulses = 400  # Maximum number of qubit pulses
pi_len = QUBIT_CONSTANTS[qubit]["square_pi_len"]
pi_amp = QUBIT_CONSTANTS[qubit]["square_pi_amp"]
max_tau_pulse = max_n_pulses * pi_len
repeated_pulses = 20
# n_pulses = np.arange(2, max_n_pulses, 2)  # Always play an odd/even number of pulses to end up in the same state


save_data_dict = {
    "sweep_gates": sweep_gates,
    "tank_circuit": tank_circuit,
    # "n_pulses": n_pulses,
    "amp_scalilngs": amp_scalilngs,
    "n_avg": n_avg,
    "config": config,
}


with program() as ERROR_AMP_RABI:
    a = declare(fixed)  # QUA variable for the qubit pulse duration
    m = declare(int)  # QUA variable for the qubit drive amplitude
    n_rabi = declare(int)
    d_ops = declare(int)
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)
    P1 = declare(bool)
    P2 = declare(bool)
    P_diff_st = declare_stream()
    r = declare(int)
    current_level = declare(fixed, value=[0.0 for _ in sweep_gates])
    seq.current_level = current_level

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element(tank_circuit, I, Q, P1, P2)

    if set_init_as_dc_offset:
        for sg, lvl_init in zip(sweep_gates, level_init_list):
            set_dc_offset(sg, "single", lvl_init)

    with for_(r, 0, r < 16_000 * 10, r+1): # approx 10h

        with for_(n, 0, n < n_avg, n + 1):

            # save(n, n_st)

            # with for_(*from_array(n_rabi, n_pulses)):  # Loop over the qubit pulse amplitude
            assign(d_ops, (RF_SWITCH_DELAY + (repeated_pulses * int(pi_len)) + RF_SWITCH_DELAY) >> 2)
            # play("x180_square" * amp(0), qubit, duration=d_ops)

            with for_(*from_array(a, amp_scalilngs)):  # Loop over the qubit pulse duration

                P1 = measure_parity(I, Q, None, None, None, None, tank_circuit, threshold)
                
                # Play the triangle
                align()
                seq.add_step(voltage_point_name="initialization_1q", ramp_duration=duration_ramp_init) # NEVER u.ns

                wait(duration_ramp_init // 4, "rf_switch", qubit)
                play("trigger", "rf_switch", duration=d_ops)
                wait(RF_SWITCH_DELAY // 4, qubit)
                with strict_timing_():
                    with for_(m, 0, m < repeated_pulses, m + 1):
                        play("x180_square" * amp(a), qubit)

                align()
                P2 = measure_parity(I, Q, None, None, None, None, tank_circuit, threshold)

                # DO NOT REMOVE: bring the voltage back to dc_offset level.
                # Without this, it can accumulate a precision error that leads to unwanted large voltage (max of the range).
                align()
                seq.ramp_to_zero()

                with if_(P1 == P2):
                    save(0, P_diff_st)
                with else_():
                    save(1, P_diff_st)
                    
                # Save the LO iteration to get the progress bar
                wait(250)

            wait(250_000)

        # Save the LO iteration to get the progress bar
        save(r, n_st)

    # Stream processing section used to process the data before saving it
    with stream_processing():
        n_st.save("iteration")
        P_diff_st.buffer(len(amp_scalilngs)).buffer(n_avg).map(FUNCTIONS.average()).save(f"P_diff_avg_{tank_circuit}")


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
    job = qmm.simulate(config, ERROR_AMP_RABI, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ERROR_AMP_RABI)

    # Get results from QUA program
    # fetch_names = ["iteration", f"P_diff_{tank_circuit}", f"P_diff_avg_{tank_circuit}"]
    fetch_names = ["iteration", f"P_diff_avg_{tank_circuit}"]

    results = fetching_tool(job, data_list=fetch_names, mode="live")

    fig = plt.figure()
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    collected_data = []

    while results.is_processing():
        # Fetch results
        iteration, P_diff_avg = results.fetch_all()

        collected_data.append(P_diff_avg)

        # Progress bar
        progress_counter(iteration, 16_000, start_time=results.get_start_time())

        plt.suptitle(f"Error Amplification Power Rabi: {qubit}")
        # Plot results
        plt.clf()
        plt.title(f"Average Parity Diff: {qubit}")
        plt.pcolor(amp_scalilngs * pi_amp, np.arange(len(collected_data))*5/60, collected_data)
        plt.xlabel("Qubit pulse amplitude [V]")
        plt.ylabel("time (mins)")

        plt.colorbar()
        plt.tight_layout()
        plt.pause(5)

    # Fetch results
    iteration, P_diff_avg = results.fetch_all()
    save_data_dict["P_diff_avg"] = P_diff_avg

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
