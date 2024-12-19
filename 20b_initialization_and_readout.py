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
import matplotlib

from configuration_with_lffem import *

# from configuration import *
from macros import RF_reflectometry_macro

matplotlib.use("TkAgg")


###################
# The QUA program #
###################
n_shots = 100  # Number of averages
num_tank_circuits = len(TANK_CIRCUIT_CONSTANTS)

# Points in the charge stability map [V1, V2]
level_inits = {
    "P1-P2": [-0.2, -0.3],
    "P4-P5": [-0.2, -0.3],
}
level_readout = [0.05, 0.15]
duration_init = 200
duration_manip = 300
duration_readout = 500
delay_before_readout = 16
Ps_sticky = ["P1_sticky", "P2_sticky"]

seq = VoltageGateSequence(config, Ps_sticky)
seq.add_points("initialization_P1-P2", level_init["P1-P2"], duration_init)
seq.add_points("initialization_P4-P5", level_init["P4-P5"], duration_init)
seq.add_points("initialization_P3", level_init["P3"], duration_init)
seq.add_points("readout_12", level_readout, duration_readout)
seq.add_points("readout_45", level_readout, duration_readout)


def initialization(I, Q, P, I_st, Q_st, P_st):
    read_init12(I[0], Q[0], P[0], I_st[0], Q_st[0], P_st[0])  # save_count = 1

    # 1st
    read_init3(I[0], Q[0], P[0], I_st[0], Q_st[0], P_st[0])  # save_count = 2
    read_init12(I[0], Q[0], P[0], I_st[0], Q_st[0], P_st[0])  # save_count = 3
    # 2nd
    read_init3(I[0], Q[0], P[0], I_st[0], Q_st[0], P_st[0])  # save_count = 4
    read_init12(I[0], Q[0], P[0], I_st[0], Q_st[0], P_st[0])  # save_count = 5

    read_init45(I[1], Q[1], P[1], I_st[1], Q_st[1], P_st[1])  # save_count = 1


def readout(I, Q, P, I_st, Q_st, P_st):
    read_init12(I[0], Q[0], P[0], I_st[0], Q_st[0], P_st[0])  # save_count = 6
    read_init3(I[0], Q[0], P[0], I_st[0], Q_st[0], P_st[0])  # save_count = 7
    read_init45(I[1], Q[1], P[1], I_st[1], Q_st[1], P_st[1])  # save_count = 2


def read_init12(I, Q, P, I_st, Q_st, P_st):
    measure_parity(
        I, Q, P, I_st, Q_st, P_st, qp="P1-P2", elem="tank_circuit1", threshold=0.0
    )


def read_init45(I, Q, P, I_st, Q_st, P_st):
    measure_parity(
        I, Q, P, I_st, Q_st, P_st, qp="P4-P5", elem="tank_circuit2", threshold=0.0
    )


def read_init3(I, Q, P, I_st, Q_st, P_st):
    play_CNOT23()
    P = measure_parity(
        I, Q, P, I_st, Q_st, P_st, qp="P1-P2", elem="tank_circuit1", threshold=0.0
    )
    play("x180", "P3", condition=P)


def play_CNOT23():
    play("step" * amp(0.1), "B2", duration=100 * u.ns)
    wait(4, "P3")
    play("cnot", "P3", duration=100 * u.ns)


def measure_parity(
    I, Q, P, I_st, Q_st, P_st, qp="P1-P2", elem="tank_circuit1", threshold=0.0
):
    # Play the triangle
    seq.add_step(voltage_point_name=f"initialization_{qp}")
    seq.add_step(voltage_point_name=f"readout_{qp}")
    seq.add_compensation_pulse(duration=duration_compensation_pulse)
    # Measure the dot right after the qubit manipulation
    wait((duration_init) * u.ns, "tank_circuit")
    # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
    # frequency and the integrated quadratures are stored in "I" and "Q"
    measure(
        "readout",
        elem,
        None,
        demod.full("cos", I, "out1"),
        demod.full("sin", Q, "out1"),
    )
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
    I_st = [declare_stream() for _ in range(num_tank_circuits)]
    Q_st = [declare_stream() for _ in range(num_tank_circuits)]
    P_st = [declare_stream() for _ in range(num_tank_circuits)]

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I[0], Q[0], P[0])
    assign_variables_to_element("tank_circuit2", I[1], Q[1], P[1])

    with for_(n, 0, n < n_shots, n + 1):  # The averaging loop
        # initizaliz
        initialization(I, Q, P, I_st, Q_st, P_st)

        # manipulation
        # TODO

        # readout
        readout(I, Q, P, I_st, Q_st, P_st)

        seq.ramp_to_zero()
        wait(1000 * u.ns)

        # Save the LO iteration to get the progress bar
        save(n, n_st)

    # Stream processing section used to process the data before saving it.
    with stream_processing():
        n_st.save("iteration")
        I_st[0].buffer(7).save_all("I1")
        Q_st[0].buffer(7).save_all("Q1")
        P_st[0].boolean_to_int.buffer(7).save_all("P1")
        I_st[1].buffer(2).save_all("I2")
        Q_st[1].buffer(2).save_all("Q2")
        P_st[1].boolean_to_int.buffer(2).save_all("P2")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

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
        job, data_list=["I1", "Q1", "P1", "I2", "Q2", "P2", "iteration"], mode="live"
    )
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch the data from the last OPX run corresponding to the current slow axis iteration
        I1, Q1, P1, I2, Q2, P2, iteration = results.fetch_all()
        # Convert results into Volts
        min_idx = min(I.shape[0], Q.shape[0])
        S = u.demod2volts(
            I[:min_idx, :] + 1j * Q[:min_idx, :], reflectometry_readout_length
        )
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
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
