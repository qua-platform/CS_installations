# %%
"""
        IQ BLOBS
This sequence involves measuring the state of the resonator 'N' times, first after thermalization (with the qubit
in the |g> state) and then after applying a pi pulse to the qubit (bringing the qubit to the |e> state) successively.
The resulting IQ blobs are displayed, and the data is processed to determine:
    - The rotation angle required for the integration weights, ensuring that the separation between |g> and |e> states
      aligns with the 'I' quadrature.
    - The threshold along the 'I' quadrature for effective qubit state discrimination.
    - The readout fidelity matrix, which is also influenced by the pi pulse fidelity.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.

Next steps before going to the next node:
    - Update the rotation angle (rotation_angle) in the configuration.
    - Update the g -> e threshold (ge_threshold) in the configuration.
"""

from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
# from configuration_opxplus_with_octave import *
from configuration_opxplus_without_octave import *
import matplotlib.pyplot as plt
from qualang_tools.results import fetching_tool
from macros import qua_declaration, multiplexed_readout, gef_state_discriminator_blob_mean

###################
# The QUA program #
###################

qubits = ["q2_xy", "q3_xy"]
resonators = ["q2_rr", "q3_rr"]
qubits_all = list(QUBIT_CONSTANTS.keys())
resonators_all = [key for key in RR_CONSTANTS.keys()]
remaining_resonators = list(set(resonators_all) - set(resonators))
weights = "" # ["", "rotated_", "opt_"] 
reset_method = "active" # can also be "active"
readout_operation = "readout" # "readout" or "midcircuit_readout"

n_runs = 20  # Number of runs

assert len(qubits_all) == len(resonators_all), "qubits and resonators don't have the same length"
assert len(qubits) == len(resonators), "qubits and resonators under study don't have the same length"
assert all([qb.replace("_xy", "") == rr.replace("_rr", "") for qb, rr in zip(qubits, resonators)]), "qubits and resonators don't correspond"
assert weights in ["", "rotated_", "opt_"], 'weight_type must be one of ["", "rotated_", "opt_"]'
assert reset_method in ["wait", "active"], "Invalid reset_method, use either wait or active"
assert readout_operation in ["readout", "midcircuit_readout"], "Invalid readout_operation, use either readout or midcircuit_readout"
assert n_runs < 20_000, "check the number of shots"

save_data_dict = {
    "qubits_all": qubits_all,
    "resonators_all": resonators_all,
    "qubits": qubits,
    "resonators": resonators,
    "shots": n_runs,
    "config": config,
    "readout_operation": readout_operation,
}

blob_mean = {
    "q1": {
        "g": [1e-4, 0.0],
        "e": [0.0, 0.0],
        "f": [-1e-4, 0.0],
    },
    "q2": {
        "g": [0.0, 1e-4],
        "e": [0.0, 0.0],
        "f": [0.0, -1e-4],
    },
}


with program() as iq_blobs:
    I, I_st, Q, Q_st, n, _ = qua_declaration(resonators)
    state = [declare(bool, size=3) for _ in range(len(resonators))]
    state_st = [declare_stream() for _ in range(len(resonators))]
    
    with for_(n, 0, n < n_runs, n + 1):
        # ground iq blobs for both qubits
        wait(qb_reset_time >> 2)
        multiplexed_readout(I, I_st, Q, Q_st, None, None, resonators, weights="")
        for i, q in enumerate([1, 2]):
            gef_state_discriminator_blob_mean(I[i], Q[i], state[i], state_st[i], blob_mean[f"q{q}"])

    with stream_processing():
        # Save all streamed points for plotting the IQ blobs
        for i in range(2):
            I_st[i].average().save(f"I_q{i + 1}")
            Q_st[i].average().save(f"Q_q{i + 1}")
            state_st[i].boolean_to_int().buffer(3).average().save(f"state_q{i + 1}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip,
    port=qop_port,
    cluster_name=cluster_name,
    octave=octave_config,
)

###########################
# Run or Simulate Program #
###########################

simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, iq_blobs, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(iq_blobs)
    # fetch data
    results = fetching_tool(job, [
        "I_q1", "Q_q1", "state_q1", "I_q2", "Q_q2", "state_q2",
        ]
    )
    I_q1, Q_q1, state_q1, I_q2, Q_q2, state_q2 = results.fetch_all()

    print("state_q1 (g, e, f) :", state_q1)
    print("state_q2 (g, e, f) :", state_q2)

# for x, y, x2, y2, d, b, s in zip(xs_q1, ys_q1, xs2_q1, ys2_q2, dist_q1, state_bool_q1, state_q1):
#     print(x)
#     print(y)
#     print(x2)
#     print(y2)
#     print(d)
#     print(b)
#     print(s)
#     print()


# %%