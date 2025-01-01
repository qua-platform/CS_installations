# %%
"""
        Readout & Init
"""

import matplotlib
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.voltage_gates import VoltageGateSequence

from configuration_with_lffem import *
from macros import get_other_elements

matplotlib.use('TkAgg')


###################
# The QUA program #
###################
n_shots = 2  # Number of averages

qubits = ["qubit1", "qubit2", "qubit3", "qubit4", "qubit5"]
sweep_gates = ["P1_sticky", "P2_sticky", "P3_sticky", "P4_sticky", "P5_sticky"]
barrier_gates = ["B2"]
qp_controls = ["qp_control_c3t2"]
tank_circuits = ['tank_circuit1', 'tank_circuit2']
num_tank_circuits = len(TANK_CIRCUIT_CONSTANTS)
all_elements = qubits + sweep_gates + barrier_gates + qp_controls + tank_circuits


# Points in the charge stability map [V1, V2]
level_inits = {
    "P1-P2": [-0.05, 0.05, 0.0, 0.0, 0.0],
    "P3": [0.0, 0.0, -0.05, 0.0, 0.0],
    "P4-P5": [0.0, 0.0, 0.0, -0.06, 0.04],
}
level_readouts = {
    "P1-P2": [-0.01, 0.01, 0.0, 0.0, 0.0],
    "P3": [-0.01, 0.01, 0.0, 0.0, 0.0],
    "P4-P5": [0.0, 0.0, 0.0, -0.01, 0.01],
}
level_waits = {
    "P1-P2": [-0.01, 0.01, 0.0, 0.0, 0.0],
    "P3": [-0.01, 0.01, 0.0, 0.0, 0.0],
    "P4-P5": [0.0, 0.0, 0.0, -0.01, 0.01],
}


delay_init_qubit_start = 16
delay_init_qubit_end = 16
duration_init_1q = delay_init_qubit_start + PI_LEN + delay_init_qubit_end
duration_init_2q = delay_init_qubit_start + CROT_RF_LEN + delay_init_qubit_end
assert delay_init_qubit_start == 0 or delay_init_qubit_start >= 16
assert delay_init_qubit_end == 0 or delay_init_qubit_end >= 16

delay_read_reflec_start = 16
delay_read_reflec_end = 16
duration_readout = delay_read_reflec_start + REFLECTOMETRY_READOUT_LEN + delay_read_reflec_end
assert delay_read_reflec_start == 0 or delay_read_reflec_start >= 16
assert delay_read_reflec_end == 0 or delay_read_reflec_end >= 16

duration_compensation_pulse = 1000
duration_wait = 200


seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization_1q_P1-P2", level_inits["P1-P2"], duration_init_1q)
seq.add_points("initialization_1q_P4-P5", level_inits["P4-P5"], duration_init_1q)
seq.add_points("initialization_1q_P3", level_inits["P3"], duration_init_1q)
seq.add_points("initialization_2q_P1-P2", level_inits["P1-P2"], duration_init_2q)
seq.add_points("initialization_2q_P4-P5", level_inits["P4-P5"], duration_init_2q)
seq.add_points("initialization_2q_P3", level_inits["P3"], duration_init_2q)
seq.add_points("readout_P1-P2", level_readouts["P1-P2"], duration_readout)
seq.add_points("readout_P3", level_readouts["P3"], duration_readout)
seq.add_points("readout_P4-P5", level_readouts["P4-P5"], duration_readout)
seq.add_points("wait_P1-P2", level_waits["P1-P2"], duration_wait)
seq.add_points("wait_P3", level_waits["P3"], duration_wait)
seq.add_points("wait_P4-P5", level_waits["P4-P5"], duration_wait)



def initialization(I, Q, P, I_st, Q_st, P_st):
    qua_vars0 = I[0], Q[0], P[0], I_st, Q_st, P_st
    qua_vars1 = I[1], Q[1], P[1], I_st, Q_st, P_st
    other_elements = get_other_elements(sweep_gates)

    res1_1 = read_init12(*qua_vars0)  # save_count = 2 -> 2
    # wait_after_read_init(qp="P1-P2")

    # 1st
    res1_2 = read_init3(*qua_vars0)  # save_count = 1 -> 3
    # wait_after_read_init(qp="P3")

    res1_3 = read_init12(*qua_vars0)  # save_count = 2 -> 5
    # wait_after_read_init(qp="P1-P2")

    # 2nd
    res1_4 = read_init3(*qua_vars0)  # save_count = 1 -> 6
    # wait_after_read_init(qp="P3")

    res1_5 = read_init12(*qua_vars0)  # save_count = 2 -> 8
    # wait_after_read_init(qp="P1-P2")

    res2_1 = read_init45(*qua_vars1)  # save_count = 2 -> 10
    # wait_after_read_init(qp="P4-P5")


def readout(I, Q, P, I_st, Q_st, P_st):
    qua_vars0 = I[0], Q[0], P[0], I_st, Q_st, P_st
    qua_vars1 = I[1], Q[1], P[1], I_st, Q_st, P_st
    other_elements = get_other_elements(sweep_gates)

    res1_6 = read_init12(*qua_vars0)  # save_count = 2 -> 12
    # wait_after_read_init(qp="P1-P2")

    res1_7 = read_init3(*qua_vars0)  # save_count = 1 -> 13
    # wait_after_read_init(qp="P1-P2")

    res2_2 = read_init45(*qua_vars1)  # save_count = 2 -> 15
    # wait_after_read_init(qp="P4-P5")


def read_init12(I, Q, P, I_st, Q_st, P_st):
    qua_vars = I, Q, P, I_st, Q_st, P_st
    qp = "P1-P2"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit1"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["qubit1", "tank_circuit1"] + sweep_gates)

    P = measure_parity(*qua_vars, qp=qp, tank_circuit="tank_circuit1", threshold=threshold)
    wait(duration_readout * u.ns, "qubit1")

    play_feedback(qp=qp, qubit="qubit1", parity=P)    
    wait(duration_init_1q * u.ns, "tank_circuit1")

    P = measure_parity(*qua_vars, qp=qp, tank_circuit="tank_circuit1", threshold=threshold)
    wait(duration_readout * u.ns, "qubit1")

    wait((duration_init_1q + 2 * duration_readout) * u.ns, *other_elements)

    return P


def read_init45(I, Q, P, I_st, Q_st, P_st):
    qua_vars = I, Q, P, I_st, Q_st, P_st
    qp = "P4-P5"
    tank_circuit = "tank_circuit2"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit2"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["qubit5", "tank_circuit2"] + sweep_gates)

    P = measure_parity(*qua_vars, qp=qp, tank_circuit=tank_circuit, threshold=threshold)
    wait(duration_readout * u.ns, "qubit5")

    play_feedback(qp=qp, qubit="qubit5", parity=P)
    wait(duration_init_1q * u.ns, "tank_circuit2")

    P = measure_parity(*qua_vars, qp=qp, tank_circuit=tank_circuit, threshold=threshold)
    wait(duration_readout * u.ns, "qubit5")

    wait((duration_init_1q + 2 * duration_readout) * u.ns, *other_elements)

    return P


def read_init3(I, Q, P, I_st, Q_st, P_st):
    qua_vars = I, Q, P, I_st, Q_st, P_st
    qp = "P3"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit1"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["B2", "qp_control_c3t2", "qubit3", "tank_circuit1"] + sweep_gates)

    play_CNOT_c3t2(qp=qp)
    wait(duration_init_2q * u.ns, "tank_circuit1", "qubit3")

    P = measure_parity(*qua_vars, qp=qp, tank_circuit="tank_circuit1", threshold=threshold)
    wait(duration_readout * u.ns, "B2", "qp_control_c3t2", "qubit3")

    play_feedback(qp=qp, qubit="qubit3", parity=P)
    wait(duration_init_1q * u.ns, "B2", "qp_control_c3t2", "tank_circuit1")

    wait((duration_init_2q + duration_readout + duration_init_1q) * u.ns, *other_elements)

    return P


def play_feedback(qp, qubit, parity):
    seq.add_step(voltage_point_name=f"initialization_1q_{qp}")

    wait(delay_init_qubit_start * u.ns, qubit) if delay_init_qubit_start >= 16 else None
    # play("x180", qubit, condition=parity)
    play("x180", qubit)
    wait(delay_init_qubit_end * u.ns, qubit) if delay_init_qubit_end >= 16 else None


def play_CNOT_c3t2(qp):
    seq.add_step(voltage_point_name=f"initialization_2q_{qp}")

    wait(delay_init_qubit_start * u.ns, "B2", "qp_control_c3t2") if delay_init_qubit_start >= 16 else None
    play("step" * amp(0.1), "B2", duration=CROT_DC_LEN * u.ns)
    play("x180", "qp_control_c3t2")
    wait(delay_init_qubit_end * u.ns, "B2", "qp_control_c3t2") if delay_init_qubit_end >= 16 else None


def wait_after_read_init(qp):
    other_elements = get_other_elements(elements_in_use=sweep_gates)

    seq.add_step(voltage_point_name=f"wait_{qp}")
    wait(duration_wait * u.ns, *other_elements)


def measure_parity(I, Q, P, I_st, Q_st, P_st, qp, tank_circuit, threshold):
    # Play the triangle
    # seq.add_step(voltage_point_name=f"initialization_1q_{qp}")
    seq.add_step(voltage_point_name=f"readout_{qp}")
    # Measure the dot right after the qubit manipulation
    wait(delay_read_reflec_start * u.ns, tank_circuit) if delay_read_reflec_start >= 16 else None
    measure(
        "readout",
        tank_circuit,
        None,
        demod.full("cos", I, "out1"),
        demod.full("sin", Q, "out1"),
    )
    wait(delay_read_reflec_end * u.ns, tank_circuit) if delay_read_reflec_end >= 16 else None

    assign(P, I > threshold)  # TODO: I > threashold is even?
    save(I, I_st)
    save(Q, Q_st)
    save(P, P_st)
    return P


with program() as READ_INIT:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    P = [declare(bool) for _ in range(num_tank_circuits)]  # true if even parity
    I_st = declare_stream()
    Q_st = declare_stream()
    P_st = declare_stream()

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I[0], Q[0], P[0])
    assign_variables_to_element("tank_circuit2", I[1], Q[1], P[1])

    qua_vars0 = I[0], Q[0], P[0], I_st, Q_st, P_st
    qua_vars1 = I[1], Q[1], P[1], I_st, Q_st, P_st
    other_elements = get_other_elements(sweep_gates)

    with for_(n, 0, n < n_shots, n + 1):  # The averaging loop
        # # initizaliz
        initialization(I, Q, P, I_st, Q_st, P_st)

        # # manipulation
        # # TODO

        # # readout
        # readout(I, Q, P, I_st, Q_st, P_st)

        # res1_1 = read_init12(*qua_vars0)
        # wait(200 * u.ns, *all_elements)
        # res1_2 = read_init45(*qua_vars1)
        # wait(200 * u.ns, *all_elements)
        # res1_3 = read_init3(*qua_vars0)

        seq.add_compensation_pulse(duration=duration_compensation_pulse)
        wait(duration_compensation_pulse * u.ns, *other_elements)
        seq.ramp_to_zero()
        wait(400 * u.ns)

        save(n, n_st)

    # Stream processing section used to process the data before saving it.
    with stream_processing():
        n_st.save("iteration")
        I_st.buffer(15).save_all("I12")
        Q_st.buffer(15).save_all("Q12")
        P_st.boolean_to_int().buffer(15).save_all("P12")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)
qmm.clear_all_job_results()
qmm.close_all_qms()

###########################
# Run or Simulate Program #
###########################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=5_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, READ_INIT, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(READ_INIT)
    # Get results from QUA program and initialize live plotting
    results = fetching_tool(
        job, data_list=["I12", "Q12", "P12", "iteration"], mode="live"
    )
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I12, Q12, P12, iteration = results.fetch_all()
        # Convert results into Volts
        min_idx = min(I12.shape[0], Q12.shape[0], P12.shape[0])
        # Progress bar
        progress_counter(iteration, n_shots)
        # # Plot dat
        # plt.subplot(121)
        # plt.cla()
        # plt.title(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        # plt.pcolor(voltage_values_fast, voltage_values_slow[:min_idx], R)
        # plt.xlabel("Fast voltage axis [V]")
        # plt.ylabel("Slow voltage axis [V]")
        # plt.subplot(122)
        # plt.cla()
        # plt.title("Phase [rad]")
        # plt.pcolor(voltage_values_fast, voltage_values_slow[:min_idx], phase)
        # plt.xlabel("Fast voltage axis [V]")
        # plt.ylabel("Slow voltage axis [V]")
        # plt.tight_layout()
        # plt.pause(0.1)

# %%
