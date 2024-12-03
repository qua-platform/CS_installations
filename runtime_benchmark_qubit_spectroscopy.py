# %%
"""
        QUBIT SPECTROSCOPY
This sequence involves sending a saturation pulse to the qubit, placing it in a mixed state,
and then measuring the state of the resonator across various qubit drive intermediate dfs.
In order to facilitate the qubit search, the qubit pulse duration and amplitude can be changed manually in the QUA
program directly without having to modify the configuration.

The data is post-processed to determine the qubit resonance frequency, which can then be used to adjust
the qubit intermediate frequency in the configuration under "qubit_IF".

Note that it can happen that the qubit is excited by the image sideband or LO leakage instead of the desired sideband.
This is why calibrating the qubit mixer is highly recommended.

This step can be repeated using the "x180" operation to adjust the pulse parameters (amplitude, duration, frequency)
before performing the next calibration steps.

Prerequisites:
    - Identification of the resonator's resonance frequency when coupled to the qubit in question (referred to as "resonator_spectroscopy_multiplexed").
    - Calibration of the
     IQ mixer connected to the qubit drive line (whether it's an external mixer or an Octave port).
    - Configuration of the cw pulse amplitude (const_amp) and duration (CONST_LEN) to transition the qubit into a mixed state.
    - Specification of the expected qubits T1 in the configuration.

Before proceeding to the next node:
    - Update the qubit frequency, labeled as "qubit_IF_q", in the configuration.
"""

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_opxplus_with_octave import *
# from configuration_opxplus_without_octave import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from macros import qua_declaration, multiplexed_readout
import matplotlib.pyplot as plt
import math
from qualang_tools.results.data_handler import DataHandler


##################
#   Parameters   #
##################

# Qubits and resonators 
qubits = [qb for qb in QUBIT_CONSTANTS.keys()]
resonators = [key for key in RR_CONSTANTS.keys()]

# Parameters Definition
n_avg = 1_000  # The number of averages
# Adjust the pulse duration and amplitude to drive the qubit into a mixed state
# Qubit detuning sweep with respect to qubit_IF
span = 2.0 * u.MHz
freq_step = 125 * u.kHz
dfs = np.arange(-span, +span, freq_step)
scaling_factor = 1.0

# Readout Parameters
weights = "rotated_" # ["", "rotated_", "opt_"]
reset_method = "wait" # ["wait", "active"]
readout_operation = "readout" # ["readout", "midcircuit_readout"]

# Assertion
assert len(dfs) <= 400, "check your frequencies"
for qb in qubits:
    assert scaling_factor * QUBIT_CONSTANTS[qb]["amp"] <= 0.499, f"{qb} scaling factor times amplitude exceeded 0.499"


###################
#   QUA Program   #
###################

with program() as qubit_spec:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(resonators)
    df = declare(int)  # QUA variable for the readout frequency

    with for_(n, 0, n < n_avg, n + 1):
        # Save the averaging iteration to get the progress bar
        save(n, n_st)
        with for_(*from_array(df, dfs)):
            # Update the frequency of the two qubit elements
            for qb in qubits:
                update_frequency(qb, df + QUBIT_CONSTANTS[qb]["IF"])
                play("saturation" * amp(scaling_factor), qb)
                
            align()

            # Multiplexed readout, also saves the measurement outcomes
            multiplexed_readout(I, I_st, Q, Q_st, None, None, resonators=resonators)

            # Wait 
            wait(rr_reset_time >> 2)

    with stream_processing():
        n_st.save("iteration")
        for ind, rr in enumerate(resonators):
            I_st[ind].buffer(len(dfs)).average().save(f"I_{rr}")
            Q_st[ind].buffer(len(dfs)).average().save(f"Q_{rr}")


if __name__ == "__main__":
    import time
    
    times = [time.time()]
    qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
    times.append(time.time())
    # Open the quantum machine
    qm = qmm.open_qm(config)
    times.append(time.time())
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(qubit_spec)
    times.append(time.time())
    job.result_handles.wait_for_all_values()
    times.append(time.time())
    job.result_handles.get("I_q1_rr").fetch_all()
    times.append(time.time())

    times = np.diff(times)

    print(f'Time for opening qmm - {times[0]}')
    print(f'Time for opening qm - {times[1]}')
    print(f'Time to execute - {times[2]}')
    print(f'Time of program runtime + stream processing - {times[3]}')
    print(f'Time to fetch data - {times[4]}')
# %%
