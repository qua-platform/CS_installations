# %%
"""
        Readout & Init
"""

import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.voltage_gates import VoltageGateSequence

from configuration_with_lffem import *

import matplotlib
matplotlib.use('TkAgg')


###################
# The QUA program #
###################
n_shots = 3  # Number of averages
num_tank_circuits = len(TANK_CIRCUIT_CONSTANTS)

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

delay_init_qubit = 16
delay_qubit_read = 16
duration_init = delay_init_qubit + PI_LEN + delay_qubit_read
assert delay_init_qubit == 0 or delay_init_qubit >= 16
assert delay_qubit_read == 0 or delay_qubit_read >= 16
delay_read_reflec_start = 16
delay_read_reflec_end = 16
duration_readout = REFLECTOMETRY_READOUT_LEN + delay_read_reflec_start + delay_read_reflec_end
duration_compensation_pulse = 1000

sweap_gates = ["P1_sticky", "P2_sticky", "P3_sticky", "P4_sticky", "P5_sticky"] # TODO: 
# sweap_gates = ["P1_sticky", "P2_sticky", "P3_sticky", "P4_sticky", "P5_sticky"]

seq = VoltageGateSequence(config, sweap_gates)
seq.add_points("initialization_P1-P2", level_inits["P1-P2"], duration_init)
seq.add_points("initialization_P4-P5", level_inits["P4-P5"], duration_init)
seq.add_points("initialization_P3", level_inits["P3"], duration_init)
seq.add_points("readout_P1-P2", level_readouts["P1-P2"], duration_readout)
seq.add_points("readout_P3", level_readouts["P3"], duration_readout)
seq.add_points("readout_P4-P5", level_readouts["P4-P5"], duration_readout)


def zero_average_power(seq):
    for i, gate in enumerate(sweap_gates):
        seq.average_power[i] = 0
    return seq


def initialization(I, Q, P, I_st, Q_st, P_st):
    qua_vars0 = I[0], Q[0], P[0], I_st, Q_st, P_st
    qua_vars1 = I[1], Q[1], P[1], I_st, Q_st, P_st

    res1_1 = read_init12(*qua_vars0)  # save_count = 2 -> 2

    # 1st
    res1_2 = read_init3(*qua_vars0)  # save_count = 1 -> 3
    res1_3 = read_init12(*qua_vars0)  # save_count = 2 -> 5
    # 2nd
    res1_4 = read_init3(*qua_vars0)  # save_count = 1 -> 6
    res1_5 = read_init12(*qua_vars0)  # save_count = 2 -> 8

    res2_1 = read_init45(*qua_vars1)  # save_count = 2 -> 10


def readout(I, Q, P, I_st, Q_st, P_st):
    qua_vars0 = I[0], Q[0], P[0], I_st, Q_st, P_st
    qua_vars1 = I[1], Q[1], P[1], I_st, Q_st, P_st

    res1_6 = read_init12(*qua_vars0)  # save_count = 2 -> 12
    res1_7 = read_init3(*qua_vars0)  # save_count = 1 -> 13
    res2_2 = read_init45(*qua_vars1)  # save_count = 2 -> 15


def read_init12(I, Q, P, I_st, Q_st, P_st):
    qua_vars = I, Q, P, I_st, Q_st, P_st
    qp = "P1-P2"
    tc = "tank_circuit1"
    threshold = TANK_CIRCUIT_CONSTANTS[tc]["threshold"]

    P = measure_parity(*qua_vars, qp=qp, tank_circuit=tc, threshold=threshold)
    wait(duration_readout * u.ns, "qubit1")
    play_feedback(qp=qp, qubit="qubit1", parity=P)
    wait(duration_init * u.ns, *sweap_gates)
    P = measure_parity(*qua_vars, qp=qp, tank_circuit=tc, threshold=threshold)

    return P


def read_init45(I, Q, P, I_st, Q_st, P_st):
    qua_vars = I, Q, P, I_st, Q_st, P_st
    qp = "P4-P5"
    tc = "tank_circuit2"
    threshold = TANK_CIRCUIT_CONSTANTS[tc]["threshold"]

    P = measure_parity(*qua_vars, qp=qp, tank_circuit=tc, threshold=threshold)
    wait((duration_init + duration_readout) * u.ns, "qubit1")
    play_feedback(qp=qp, qubit="qubit5", parity=P)

    P = measure_parity(*qua_vars, qp=qp, tank_circuit=tc, threshold=threshold)

    return P


def read_init3(I, Q, P, I_st, Q_st, P_st):
    qua_vars = I, Q, P, I_st, Q_st, P_st
    qp = "P1-P2"
    tc = "tank_circuit1"
    threshold = TANK_CIRCUIT_CONSTANTS[tc]["threshold"]

    play_CNOT23()
    P = measure_parity(*qua_vars, qp=qp, tank_circuit=tc, threshold=threshold)
    play_feedback(qp=qp, qubit="qubit3", parity=P)

    return P


def play_CNOT23():
    play("step" * amp(0.1), "B2", duration=116 * u.ns)
    wait(4, "qp_control_c3t2")
    play("x180", "qp_control_c3t2", duration=100 * u.ns)


def play_feedback(qp, qubit, parity):
    seq.add_step(voltage_point_name=f"initialization_{qp}")
    seq.add_compensation_pulse(duration=duration_compensation_pulse)
    wait(delay_init_qubit * u.ns, qubit)
    play("x180", qubit, condition=parity)


def measure_parity(I, Q, P, I_st, Q_st, P_st, qp, tank_circuit, threshold):
    # Play the triangle
    # seq.add_step(voltage_point_name=f"initialization_{qp}")
    seq.add_step(voltage_point_name=f"readout_{qp}")
    # Measure the dot right after the qubit manipulation
    wait(delay_read_reflec_start * u.ns, tank_circuit)
    # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
    # frequency and the integrated quadratures are stored in "I" and "Q"
    measure(
        "readout",
        tank_circuit,
        None,
        demod.full("cos", I, "out1"),
        demod.full("sin", Q, "out1"),
    )
    
    # seq.ramp_to_zero()

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

    with for_(n, 0, n < n_shots, n + 1):  # The averaging loop
        # # initizaliz
        # initialization(I, Q, P, I_st, Q_st, P_st)

        # # manipulation
        # # TODO

        # # readout
        # readout(I, Q, P, I_st, Q_st, P_st)

        res1_1 = read_init12(*qua_vars0)

        # qp = "P1-P2"
        # tc = "tank_circuit1"
        # threshold = TANK_CIRCUIT_CONSTANTS[tc]["threshold"]

        # P = measure_parity(*qua_vars0, qp=qp, tank_circuit=tc, threshold=threshold)

        seq.add_compensation_pulse(duration=duration_compensation_pulse)
        seq.ramp_to_zero()

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
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
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
