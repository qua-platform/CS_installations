"""
Squeeze drive analysis
"""

from matplotlib.mlab import detrend
import matplotlib.pyplot as plt
from qualang_tools.results.results import fetching_tool, progress_counter
from configuration_squeeze import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from scipy.signal import detrend



###################
# The QUA program #
###################

n_avg = 100  # The number of averages
a_start = 0.0
a_stop = 1.0
a_num = 21
a_array = np.linspace(a_start, a_stop, a_num)

with program() as raw_trace_prog:
    a = declare(fixed)
    n = declare(int)  # QUA variable for the averaging loop
    I1 = declare(fixed)  # QUA variable for I_1 quadrature
    Q1 = declare(fixed)  # QUA variable for Q_1 quadrature
    I2 = declare(fixed)  # QUA variable for I_2 quadrature
    Q2 = declare(fixed)  # QUA variable for Q_2 quadrature
    I1_st = declare_stream()
    Q1_st = declare_stream()
    I2_st = declare_stream()
    Q2_st = declare_stream()
    n_st = declare_stream()
    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_(*from_array(a, ))
            play("drive", "pump")
            measure(
                "analyser_1", "read", None, dual_demod.full("cos", "sin", I1), dual_demod.full("minus_sin", "cos", Q1)
            )
            measure(
                "analyser_2", "read", None, dual_demod.full("cos", "sin", I2), dual_demod.full("minus_sin", "cos", Q2)
            )
            save(I1, I1_st)
            save(Q1, Q1_st)
            save(I2, I2_st)
            save(Q2, Q2_st)
            save(n, n_st)
    with stream_processing():
        I1_st.buffer(n_avg).average().save("I1")
        Q1_st.buffer(n_avg).average().save("Q1")
        I2_st.buffer(n_avg).average().save("I2")
        Q2_st.buffer(n_avg).average().save("Q2")
        n_st.save("iteration")


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
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, raw_trace_prog, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(raw_trace_prog)
    # Creates a result handle to fetch data from the OPX
    results = fetching_tool(job, data_list=["I1", "Q1", "I2", "Q2", "iteration"], mode="live")
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        I1, Q1, I2, Q2, iteration = results.fetch_all()
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        S1 = u.demod2volts(I1 + 1j * Q1, pump_len)
        S2 = u.demod2volts(I2 + 1j * Q2, pump_len)
        R1 = np.abs(S1)
        R2 = np.abs(S2)
        phase_1 = np.angle(S1)
        phase_2 = np.angle(S2)
        plt.suptitle(f"Squeeze")
        ax1 = plt.subplot(221)
        plt.cla()
        plt.plot(a_array, R1, ".--")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(222, sharex=ax1)
        plt.cla()
        plt.plot(a_array, R2, ".--")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(223, sharex=ax1)
        plt.cla()
        plt.plot(a_array, detrend(np.unwrap(phase_1)), ".--")
        plt.ylabel("Phase [rad]")
        plt.subplot(224, sharex=ax1)
        plt.cla()
        plt.plot(a_array, detrend(np.unwrap(phase_2)), ".--")
        plt.ylabel("Phase [rad]")