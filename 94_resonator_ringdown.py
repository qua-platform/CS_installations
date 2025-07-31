# %%
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_MWFEM import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.results.data_handler import DataHandler


def interleaved_arr(a, b):
    """
    Interleave two arrays a and b.
    """
    c = np.empty((a.size + b.size,), dtype=a.dtype)
    c[0::2] = a
    c[1::2] = b
    return c


##################
#   Parameters   #
##################
# Parameters Definition
n_avg = 100  # The number of averages
ringdown_time = 1 * u.ms  # The time to wait for the resonator to deplete
# ringdown_time = 100 * u.us  # The time to wait for the resonator to deplete
readout_time = readout_len * u.ns
n_reps = (ringdown_time // readout_time + 1) // 2
# Define a second resonator element for continuous readout
config["elements"]["resonator2"] = config["elements"]["resonator"]
# To find out the input amplitude, multiply the full_scale_power_dbm by the readout_amp
# print(u.dBm2volts(0) * 0.05)

###################
# The QUA program #
###################
with program() as ringdown:
    n1 = declare(int)
    n2 = declare(int)
    n_st = declare_stream()
    # Here we define one 'I', 'Q', 'I_st' & 'Q_st' for each resonator via a python list
    I = [declare(fixed) for _ in range(2)]
    Q = [declare(fixed) for _ in range(2)]
    I_st = [declare_stream() for _ in range(2)]
    Q_st = [declare_stream() for _ in range(2)]

    reset_global_phase()

    # play measurement pulse once to saturate the resonator
    measure(
        "readout",
        "resonator",
        # dual_demod.full("cos", "sin", I[0]),
        # dual_demod.full("minus_sin", "cos", Q[0]),
    )
    wait(readout_time, "resonator2")  # needed to delay second for_ loop
    measure(
        "readout",
        "resonator",
        # dual_demod.full("cos", "sin", I[1]),
        # dual_demod.full("minus_sin", "cos", Q[1]),
    )

    wait(readout_time, "resonator2")  # needed to delay second for_ loop

    with for_(n1, 0, n1 < n_reps, n1 + 1):  # QUA for_ loop for averaging
        measure(
            "readout" * amp(0),
            "resonator",
            dual_demod.full("cos", "sin", I[0]),
            dual_demod.full("minus_sin", "cos", Q[0]),
        )
        save(I[0], I_st[0])
        save(Q[0], Q_st[0])
        save(n1, n_st)
        wait(readout_time, "resonator")

    with for_(n2, 0, n2 < n_reps, n2 + 1):  # QUA for_ loop for averaging
        measure(
            "readout" * amp(0),
            "resonator2",
            dual_demod.full("cos", "sin", I[1]),
            dual_demod.full("minus_sin", "cos", Q[1]),
        )
        save(I[1], I_st[1])
        save(Q[1], Q_st[1])
        wait(readout_time, "resonator2")

    with stream_processing():
        n_st.save("iteration")
        for ind in range(2):
            I_st[ind].buffer(n_reps).save(f"I_{ind + 1}")
            Q_st[ind].buffer(n_reps).save(f"Q_{ind + 1}")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)


#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, ringdown, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(
        samples, plot=True, save_path=str(Path(__file__).resolve())
    )

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ringdown)
    # Get results from QUA program
    results = fetching_tool(
        job, data_list=["I_1", "I_2", "Q_1", "Q_2", "iteration"], mode="live"
    )
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I_1, I_2, Q_1, Q_2, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.cla()
        I = interleaved_arr(I_1, I_2)
        Q = interleaved_arr(Q_1, Q_2)
        S = u.demod2volts(I + 1j * Q, readout_len)
        R = np.abs(S)  # Amplitude
        t = np.arange(len(I)) * readout_time
        # plt.plot(t, I, label="I")
        # plt.plot(t, Q, label="Q")
        plt.plot(t, R, label="Amplitude")
        plt.xlabel("Time (ns)")
        plt.ylabel("Amplitude (V)")
        plt.legend()
