# %%
"""
        Pauli Spin Blockade search
The goal of the script is to find the PSB region according to the protocol described in Nano Letters 2020 20 (2), 947-952.
To do so, the charge stability map is acquired by scanning the voltages provided by an external DC source,
to the DC part of the bias-tees connected to the plunger gates, while 2 OPX channels are stepping the voltages on the fast
lines of the bias-tees to navigate through the triangle in voltage space (empty - random initialization - measurement).

Depending on the cut-off frequency of the bias-tee, it may be necessary to adjust the barycenter (voltage offset) of each
triangle so that the fast line of the bias-tees sees zero voltage in average. Otherwise, the high-pass filtering effect
of the bias-tee will distort the fast pulses over time. A function has been written for this.

In the current implementation, the OPX is also measuring (either with DC current sensing or RF-reflectometry) during the
readout window (last segment of the triangle).
A single-point averaging is performed and the data is extracted while the program is running to display the results line-by-line.

Prerequisites:
    - Readout calibration (resonance frequency for RF reflectometry and sensor operating point for DC current sensing).
    - Setting the parameters of the external DC source using its driver.
    - Connect the two plunger gates (DC line of the bias-tee) to the external dc source.
    - Connect the OPX to the fast line of the plunger gates for playing the triangle pulse sequence.

Before proceeding to the next node:
    - Identify the PSB region and update the config.
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
from voltage_gate_sequence import VoltageGateSequence
from scipy import signal

from configuration_with_lffem_csrack import *

matplotlib.use('TkAgg')


###################
# The QUA program #
###################
n_shots = 200  # Number of averages
n_detunings = 5

sweep_gates = ["P1_sticky", "P2_sticky"]
tank_circuit = "tank_circuit1"

level_init_arr = np.array([-0.025, 0.025])
level_init = level_init_arr.tolist()

level_readout0_arr = np.array([-0.005, 0.005])
level_readout_min_arr = level_readout0_arr + np.array([-0.01, 0.01])
level_readout_max_arr = level_readout0_arr + np.array([0.01, -0.01])
level_readout0 = level_readout0_arr.tolist()
threshold = TANK_CIRCUIT_CONSTANTS[tank_circuit]["threshold"]

print(level_init)
print(level_readout0_arr)
print(level_readout_min_arr)
print(level_readout_max_arr)

duration_ramp_init = 52  
duration_init = 52 # 50 * u.us
duration_ramp_readout = 52
duration_readout = 52 # 1 * u.us + REFLECTOMETRY_READOUT_LEN

voltages_Px = np.linspace(level_readout_min_arr[0], level_readout_max_arr[0], n_detunings) - level_init_arr[0]
voltages_Py = np.linspace(level_readout_min_arr[1], level_readout_max_arr[1], n_detunings) - level_init_arr[1]


# voltages_Px = np.linspace(level_readout_min_arr[0], level_readout_max_arr[0], n_detunings)
# voltages_Py = np.linspace(level_readout_min_arr[1], level_readout_max_arr[1], n_detunings)

print(voltages_Px)
print(voltages_Py)


seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization", level_init, duration_init)
# for m, (v1, v2) in enumerate(zip(voltages_Px, voltages_Py)):
#     # print(f"readout_{m}", v1, v2)
#     seq.add_points(f"readout_{m}", [v1, v2], duration_readout)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "tank_circuit": tank_circuit,
    "n_shots": n_shots,
    "voltages_Px": voltages_Px,
    "voltages_Py": voltages_Py,
    "config": config,
}


with program() as PSB_search_prog:
    Vx = declare(fixed)
    Vy = declare(fixed)
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)
    P = declare(bool)
    I_st = declare_stream()
    Q_st = declare_stream()
    P_st = declare_stream()
    
    current_level = declare(fixed, value=[0.0 for _ in sweep_gates])
    seq.current_level = current_level

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I, Q, P)

    # set_dc_offset(sweep_gates[0], "single", level_init[0])
    # set_dc_offset(sweep_gates[1], "single", level_init[1])

    with for_(n, 0, n < n_shots, n + 1):
        with for_each_((Vx, Vy), (voltages_Px.tolist(), voltages_Py.tolist())):
            # Play the triangle
            seq.add_step(voltage_point_name="initialization") #1* u.us)
            seq.add_step(level=[Vx, Vy], duration=duration_readout, ramp_duration=duration_ramp_readout)
            # seq.add_step(level=[Vx, Vy], duration=duration_readout, ramp_duration=0)
            # seq.add_step(level=[Vx, Vy], duration=duration_readout)
            align()
            # Measure the dot right after the qubit manipulation
            measure(
                "readout",
                tank_circuit,
                None,
                demod.full("cos", I, "out1"),
                demod.full("sin", Q, "out1"),
            )
            assign(P, I > threshold)
            save(I, I_st)
            save(Q, Q_st)
            save(P, P_st)
            align()
            # seq.add_step(level=[Vx, Vy], duration=duration_readout, ramp_duration=duration_ramp_readout)

            # process them which can cause the OPX to crash.
            # wait(1_000 * u.ns)  # in ns
            # # Ramp the voltage down to zero at the end of the triangle (needed with sticky elements)
            # seq.ramp_to_zero()

        # Save the LO iteration to get the progress bar
        save(n, n_st)

    # Stream processing section used to process the data before saving it
    with stream_processing():
        n_st.save("iteration")
        I_st.buffer(n_detunings).buffer(n_shots).save(f"I_{tank_circuit}")
        Q_st.buffer(n_detunings).buffer(n_shots).save(f"Q_{tank_circuit}")
        P_st.boolean_to_int().buffer(n_detunings).buffer(n_shots).save(f"P_{tank_circuit}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, PSB_search_prog, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    from qm import generate_qua_script
    sourceFile = open('debug.py', 'w')
    print(generate_qua_script(PSB_search_prog, config), file=sourceFile) 
    sourceFile.close()


# %%
