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
from scipy import signal

from configuration_with_lffem_csrack import *
# from configuration_with_lffem import *
from macros_initialization_and_readout_2q_1b import *
from macros_voltage_gate_sequence import VoltageGateSequence

# matplotlib.use('TkAgg')


###################
# Local Macros #
###################


def perform_read_init(I, Q, P0_st, P1_st):
    P0 = measure_parity(I, Q, None, None, None, P0_st, tank_circuit=tank_circuit, threshold=threshold)

    # conditional pi pulse
    align()
    with if_(P0):
        seq.add_step(voltage_point_name="initialization_1q", duration=(RF_SWITCH_DELAY + pi_len + RF_SWITCH_DELAY), ramp_duration=duration_ramp_init)  # NEVER u.ns
        wait(duration_ramp_init // 4, "rf_switch", qubit)
        play("trigger", "rf_switch", duration=(RF_SWITCH_DELAY + pi_len + RF_SWITCH_DELAY) // 4)
        wait(RF_SWITCH_DELAY // 4, qubit)
        play("x180_square", qubit)

    align()
    P1 = measure_parity(I, Q, None, None, None, P1_st, tank_circuit=tank_circuit, threshold=threshold)

    return P0, P1


###################
# The QUA program #
###################

qubit = "qubit3"
barrier_gate = "B2_sticky"
sweep_gates = ["P3_sticky", "P2_sticky"]
tank_circuit = "tank_circuit1"
threshold = TANK_CIRCUIT_CONSTANTS[tank_circuit]["threshold"]
num_output_streams = 3
x180 = "x180_square"


###################
# Sweep Parameters
###################

n_avg = 3  # Number of averages

voltages_B = np.arange(0.0, 0.4, 0.01)
freqs = np.arange(140e6, 190e6, 2e6)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "tank_circuit": tank_circuit,
    "n_avg": n_avg,
    "config": config,
}


with program() as CROT_SPEC:
    f = declare(int)
    Vb = declare(fixed)
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)
    P1 = declare(bool)
    P2 = declare(bool)
    P_st = [declare_stream() for _ in range(num_output_streams)]
    P_diff_st = declare_stream()

    current_level = declare(fixed, value=[0.0 for _ in sweep_gates])
    seq.current_level = current_level

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I, Q, P1, P2)

    if set_init_as_dc_offset:
        for sg, lvl_init in zip(sweep_gates, level_init_list):
            set_dc_offset(sg, "single", lvl_init)

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(Vb, voltages_B)):
            with for_(*from_array(f, freqs)):
                update_frequency(qubit, f)

                P0, P1 = perform_read_init(I, Q, P_st[0], P_st[1])

                # Play the triangle
                align()
                seq.add_step(voltage_point_name="operation_before_crot", ramp_duration=duration_ramp_init)  # NEVER u.ns
                seq.add_step(level=level_readout_offset_list[:2] + [Vb], duration=duration_ops_barrier, ramp_duration=duration_ramp_barrier)  # NEVER u.ns
                seq.add_step(voltage_point_name="operation_after_crot", ramp_duration=duration_ramp_barrier)  # NEVER u.ns

                wait(duration_ramp_init // 4, "rf_switch", qubit)
                wait(duration_ops_before_switch // 4, "rf_switch", qubit)
                play("trigger", "rf_switch", duration=(RF_SWITCH_DELAY + pi_len + RF_SWITCH_DELAY) // 4)
                wait(RF_SWITCH_DELAY // 4, qubit)
                play(x180, qubit)
                wait(RF_SWITCH_DELAY // 4, qubit)

                align()
                P2 = measure_parity(I, Q, None, None, None, P_st[2], tank_circuit, threshold)

                # DO NOT REMOVE: bring the voltage back to dc_offset level.
                # Without this, it can accumulate a precision error that leads to unwanted large voltage (max of the range).
                align()
                seq.ramp_to_zero()

                with if_(P1 == P2):
                    save(0, P_diff_st)
                with else_():
                    save(1, P_diff_st)

                # Save the LO iteration to get the progress bar
                wait(25_000)

        # Save the LO iteration to get the progress bar
        save(n, n_st)

    # Stream processing section used to process the data before saving it
    with stream_processing():
        n_st.save("iteration")
        P_diff_st.buffer(len(freqs)).buffer(len(voltages_B)).average().save(f"P_diff_{tank_circuit}")
        for k in range(num_output_streams):
            P_st[k].boolean_to_int().buffer(len(freqs)).buffer(len(voltages_B)).average().save(f"P{k:d}_{tank_circuit}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)


###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, CROT_SPEC, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(CROT_SPEC)

    # Get results from QUA program
    fetch_names = ["iteration", f"P_diff_{tank_circuit}"] + [f"P{k:d}_{tank_circuit}" for k in range(num_output_streams)]
    results = fetching_tool(job, data_list=fetch_names, mode="live")

    fig = plt.figure()
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        iteration, P_diff, P0, P1, P2 = results.fetch_all()

        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())

        plt.suptitle("CROT Spectroscopy")
        plt.clf()

        plt.pcolor(freqs / u.MHz, voltages_B, P_diff)
        plt.xlabel("Freq [MHz]")
        plt.ylabel(f"{barrier_gate} Voltage [V]")

        # plt.subplot(2, 1, 1)
        # plt.pcolor(freqs / u.MHz, voltages_B, P_diff)
        # plt.xlabel("Freq [MHz]")
        # plt.ylabel(f"{barrier_gate} Voltage [V]")

        plt.colorbar()
        plt.tight_layout()
        plt.pause(1)

    # Fetch results
    iteration, P_diff, P0, P1, P2 = results.fetch_all()
    # save_data_dict["P_diff"] = P_diff
    save_data_dict["P_diff"] = P_diff
    save_data_dict["P0"] = P0
    save_data_dict["P1"] = P1
    save_data_dict["P2"] = P2

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name=script_name.replace(".py", ""))

    qm.close()


# %%
