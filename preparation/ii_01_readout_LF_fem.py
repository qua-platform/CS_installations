from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000_2GHz import *
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from macros import interrupt_on_close
from scipy import signal
import matplotlib.pyplot as plt


###################
# The QUA program #
###################
n_avg = 100
frequencies = np.arange(-900e6, 900e6, 0.1e6)
with program() as rf_reflectometry:
    I = declare(fixed)
    Q = declare(fixed)
    n = declare(int)
    f = declare(int)
    n_st = declare_stream()
    I_st = declare_stream()
    Q_st = declare_stream()

    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
        play("const", "lf_element_2")
        play("const"*amp(1), "lf_element_1")
        with for_(*from_array(f, frequencies)):
            update_frequency("lf_readout_element", f)
            measure("readout"*amp(1), "lf_readout_element", None, demod.full("cos", I, "out1"), demod.full("sin", Q, "out1"))
            save(I, I_st)
            save(Q, Q_st)
            wait(250)
        save(n, n_st)

    with stream_processing():
        I_st.buffer(len(frequencies)).average().save("I")
        Q_st.buffer(len(frequencies)).average().save("Q")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, rf_reflectometry, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(rf_reflectometry)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, readout_len, single_demod=True)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.subplot(211)
        plt.cla()
        plt.plot(frequencies / u.MHz, R, ".")
        plt.xlabel("Intermediate frequency [MHz]")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(212)
        plt.cla()
        plt.plot(frequencies / u.MHz, signal.detrend(np.unwrap(phase)), ".")
        plt.xlabel("Intermediate frequency [MHz]")
        plt.ylabel("Phase [rad]")
        plt.pause(0.1)
        plt.tight_layout()

# config["controllers"]["con1"]["fems"][3]["analog_outputs"][3] = {"offset": 0.0, "sampling_rate": 2e9, "output_mode": "amplified", "delay": 0}
# with program() as rf_reflectometry:
#     I = declare(fixed)
#     Q = declare(fixed)
#     n = declare(int)
#     f = declare(int)
#     n_st = declare_stream()
#     I_st = declare_stream()
#     Q_st = declare_stream()
#
#     with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
#         play("const", "lf_element_2")
#         with for_(*from_array(f, frequencies)):
#             update_frequency("lf_readout_element", f)
#             measure("readout"*amp(1/5), "lf_readout_element", None, demod.full("cos", I, "out1"), demod.full("sin", Q, "out1"))
#             save(I, I_st)
#             save(Q, Q_st)
#             wait(250)
#         save(n, n_st)
#
#     with stream_processing():
#         I_st.buffer(len(frequencies)).average().save("I")
#         Q_st.buffer(len(frequencies)).average().save("Q")
#         n_st.save("iteration")
#
# # Open a quantum machine to execute the QUA program
# qm = qmm.open_qm(config)
# # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
# job = qm.execute(rf_reflectometry)
# # Get results from QUA program
# results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
# # Live plotting
# fig = plt.figure()
# interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
# while results.is_processing():
#     # Fetch results
#     I, Q, iteration = results.fetch_all()
#     # Convert results into Volts
#     S = u.demod2volts(I + 1j * Q, readout_len, single_demod=True)
#     R2 = np.abs(S)  # Amplitude
#     phase2 = np.angle(S)  # Phase
#     # Progress bar
#     progress_counter(iteration, n_avg, start_time=results.get_start_time())
#     # Plot results
#     plt.subplot(211)
#     plt.cla()
#     plt.plot(frequencies / u.MHz, R2, ".")
#     plt.xlabel("Intermediate frequency [MHz]")
#     plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
#     plt.subplot(212)
#     plt.cla()
#     plt.plot(frequencies / u.MHz, signal.detrend(np.unwrap(phase2)), ".")
#     plt.xlabel("Intermediate frequency [MHz]")
#     plt.ylabel("Phase [rad]")
#     plt.pause(0.1)
#     plt.tight_layout()
#
# plt.close()
# plt.figure()
# plt.plot(frequencies / u.MHz, 20*np.log10(R) + 14.5)
# plt.plot(frequencies / u.MHz, 20*np.log10(R2) + 14.5)
# # plt.axhline(-6, color="k")
# plt.grid(True)
# plt.legend(("direct", "amplified"))
# plt.xlabel("frequency [MHz]")
# plt.ylabel("Demodulated power [dB]")