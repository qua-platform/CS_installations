import matplotlib.pyplot as plt
from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.config import parameters
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from scipy import signal

###################
# The QUA program #
###################
n_avg = 100  # The number of averages
# The duration sweep parameters
t_min = 4 * u.ns
t_max = 10 * u.us
dt = 100 * u.ns
durations = np.arange(t_min, t_max + 0.1, dt)  # The duration sweep


with program() as memory_T1:
    n = declare(int)  # QUA variable for the averaging loop
    t = declare(int)  # QUA variable for the waiting time
    I1 = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q1 = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I2 = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q2 = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I_st1 = declare_stream()  # Stream for the 'I' quadrature
    Q_st1 = declare_stream()  # Stream for the 'Q' quadrature
    I_st2 = declare_stream()  # Stream for the 'I' quadrature
    Q_st2 = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_(*from_array(t, durations)):  # QUA for_ loop for sweeping the waiting time
            play("cw", "memory1")
            play("cw", "memory2")
            align()
            wait(t, "ATS1", "ATS2")
            measure(
                "readout",
                "ATS1",
                None,
                demod.full("cos", I1),
                demod.full("sin", Q1),
            )
            measure(
                "readout",
                "ATS2",
                None,
                demod.full("cos", I2),
                demod.full("sin", Q2),
            )
            # Wait for the resonator to deplete
            wait(1000 * u.ns)
            # Save the 'I' & 'Q' quadratures to their respective streams
            save(I1, I_st1)
            save(Q1, Q_st1)
            save(I2, I_st2)
            save(Q2, Q_st2)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_st1.buffer(len(durations)).average().save("I1")
        Q_st1.buffer(len(durations)).average().save("Q1")
        I_st2.buffer(len(durations)).average().save("I2")
        Q_st2.buffer(len(durations)).average().save("Q2")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, memory_T1, simulation_config)
    # Plot the simulated samples
    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.figure()
    job.get_simulated_samples().con2.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(memory_T1)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I1", "Q1", "I2", "Q2", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I1, Q1, I2, Q2, iteration = results.fetch_all()
        # Convert results into Volts
        S1 = u.demod2volts(I1 + 1j * Q1, readout_len)
        S2 = u.demod2volts(I2 + 1j * Q2, readout_len)
        R1 = np.abs(S1)  # Amplitude
        R2 = np.abs(S2)  # Amplitude
        phase1 = np.angle(S1)  # Phase
        phase2 = np.angle(S2)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        ax1 = plt.subplot(221)
        plt.cla()
        plt.plot(durations / u.us, R1, ".")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(222, sharex=ax1)
        plt.cla()
        plt.plot(durations / u.us, signal.detrend(np.unwrap(phase1)), ".")
        plt.ylabel("Phase [rad]")
        ax2 = plt.subplot(223)
        plt.cla()
        plt.plot(durations / u.us, R2, ".")
        plt.xlabel("Waiting time [us]")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(224, sharex=ax1)
        plt.cla()
        plt.plot(durations / u.us, signal.detrend(np.unwrap(phase2)), ".")
        plt.xlabel("Waiting time [us]")
        plt.ylabel("Phase [rad]")
        plt.pause(0.1)

    fig.tight_layout()
    plt.show()

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()
