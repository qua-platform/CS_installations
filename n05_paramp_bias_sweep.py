"""
        PARAMP BIAS SWEEP WITH OPX+ DAC output
"""

import qm.qua as qua
import qm as qm_api
import numpy as np
from configuration import config, qop_ip, cluster_name, u, depletion_time, readout_len, resonator_LO
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.results.data_handler import DataHandler

data_handler = DataHandler(root_data_folder="./")

###################
# The QUA program #
###################
n_avg = 1000  # The number of averages
# The frequency sweep parameters
dc_min = 0 # volt
dc_max = 0.3 # volt
step_dc = 0.01 # volt
dc_values = np.arange(dc_min, dc_max, step_dc)  # The frequency vector (+ 0.1 to add f_max to frequencies)

paramp_bias_sweep_data = {
    "n_avg": n_avg,
    "dc_values": dc_values,
    "config": config
}

with qua.program() as paramp_dc_sweep:
    n = qua.declare(int)  # QUA variable for the averaging loop
    dac_value = qua.declare(qua.fixed)
    I = qua.declare(qua.fixed)  # QUA variable for the measured 'I' quadrature
    Q = qua.declare(qua.fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = qua.declare_stream()  # Stream for the 'I' quadrature
    Q_st = qua.declare_stream()  # Stream for the 'Q' quadrature
    n_st = qua.declare_stream()  # Stream for the averaging iteration 'n'

    with qua.for_(n, 0, n < n_avg, n + 1):
        qua.save(n, n_st)
        with qua.for_(*from_array(dac_value, dc_values)):

            qua.set_dc_offset("paramp", dac_value)

            qua.wait(1_000 * u.ns, "paramp")

            qua.align()

            qua.measure(
                "readout",
                "resonator",
                None,
                qua.dual_demod.full("cos", "out1", "sin", "out2", I),
                qua.dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
            )
            qua.wait(depletion_time * u.ns, "resonator")
            qua.save(I, I_st)
            qua.save(Q, Q_st)

    with qua.stream_processing():
        I_st.buffer(len(dc_values)).average().save("I")
        Q_st.buffer(len(dc_values)).average().save("Q")
        n_st.save("n")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = qm_api.QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = qm_api.SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, paramp_dc_sweep, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(paramp_dc_sweep)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, readout_len)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        elapsed_time = progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        ax1 = plt.subplot(211)
        plt.cla()
        plt.plot(dc_values, R, ".")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(212, sharex=ax1)
        plt.cla()
        plt.plot(dc_values, signal.detrend(np.unwrap(phase)), ".")
        plt.xlabel("Paramp bias [V]")
        plt.ylabel("Phase [rad]")
        plt.tight_layout()
        plt.pause(1)

    paramp_bias_sweep_data['I'] = I
    paramp_bias_sweep_data['Q'] = Q
    paramp_bias_sweep_data['R'] = R
    paramp_bias_sweep_data['phase'] = phase
    paramp_bias_sweep_data['elapsed_time'] = elapsed_time

    data_handler.save_data(data=paramp_bias_sweep_data, name="paramp_bias_sweep")

