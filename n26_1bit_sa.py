# %%
"""
        onebit_sa WITH VIRTUAL Z ROTATIONS
"""

import qm.qua as qua
import qm as qm_api
import numpy as np
from configuration import config, qop_ip, cluster_name, u, thermalization_time, readout_len, ge_threshold, qubit_IF
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler
# import xrft
from scipy import signal

data_handler = DataHandler(root_data_folder="./")

###################
# The QUA program #
###################
n_avg = 100
# Detuning converted into virtual Z-rotations to observe onebit_sa oscillation and get the qubit frequency
detuning = 0.2 * u.MHz  # in Hz, needs to be frequency where qubit is at 0.5 of state 
ramsey_idle_time = 1 * u.MHz

onebit_sa_data = {
    "n_avg": n_avg,
    "ramsey_idle_time": ramsey_idle_time,
    "detuning": detuning,
    "config": config
}

with qua.program() as onebit_sa:
    n = qua.declare(int)  # QUA variable for the averaging loop
    I = qua.declare(qua.fixed)  # QUA variable for the measured 'I' quadrature
    Q = qua.declare(qua.fixed)  # QUA variable for the measured 'Q' quadrature
    state = qua.declare(bool)  # QUA variable for the qubit state
    I_st = qua.declare_stream()  # Stream for the 'I' quadrature
    Q_st = qua.declare_stream()  # Stream for the 'Q' quadrature
    state_st = qua.declare_stream()  # Stream for the qubit state
    n_st = qua.declare_stream()  # Stream for the averaging iteration 'n'

    qua.update_frequency('qubit', qubit_IF + detuning)

    with qua.for_(n, 0, n < n_avg, n + 1):

        # Save the averaging iteration to get the progress bar
        qua.save(n, n_st)

        # 1st x90 gate
        qua.play("x90", "qubit")
        # Wait a varying idle time
        qua.wait(ramsey_idle_time * u.us, "qubit")
        # 2nd x90 gate
        qua.play("x90", "qubit")

        # Align the two elements to measure after playing the qubit pulse.
        qua.align("qubit", "resonator")
        # Measure the state of the resonator
        qua.measure(
            "readout",
            "resonator",
            None,
            # qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I),
            # qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q),
            qua.dual_demod.full("opt_cos", "out1", "opt_sin", "out2", I),
            qua.dual_demod.full("opt_minus_sin", "out1", "opt_cos", "out2", Q),
        )
        # Wait for the qubit to decay to the ground state
        qua.wait(thermalization_time * u.ns, "resonator")
        # State discrimination
        qua.assign(state, I > ge_threshold)
        # Save the 'I', 'Q' and 'state' to their respective streams
        qua.save(I, I_st)
        qua.save(Q, Q_st)
        qua.save(state, state_st)

    with qua.stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_st.save_all("I")
        Q_st.save_all("Q")
        state_st.boolean_to_int().save_all("state")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = qm_api.QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = qm_api.SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, onebit_sa, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(onebit_sa)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "state", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, state, iteration = results.fetch_all()
        # Progress bar
        elapsed_time = progress_counter(iteration, n_avg, start_time=results.get_start_time())

    plt.figure()
    plt.title('onebit_sa')
    plt.hist(state, bins=3)
    plt.xlabel('state')

    plt.figure()
    f, pxx = signal.periodogram(state, fs = 1e9 / thermalization_time)
    plt.plot(pxx, f)
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(which='both')
    plt.xlabel('frequency [Hz]')
    plt.ylabel('power spectrum [arb.]')

    # Save the results
    onebit_sa_data["I"] = I
    onebit_sa_data["Q"] = Q
    onebit_sa_data["state"] = state
    onebit_sa_data['elapsed_time'] = elapsed_time
    onebit_sa_data['pxx'] = pxx
    onebit_sa_data['f'] = f
    data_handler.save_data(data=onebit_sa_data, name="onebit_sa")

# %%
  