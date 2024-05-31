from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
import plotly.io as pio
pio.renderers.default='browser'

# get the config
config = get_config(sampling_rate=1e9)

###################
# The QUA program #
###################
from qualang_tools.loops import from_array
n_avg = 100
frequencies = np.arange(-900e6, 900e6, 0.1e6)
with program() as hello_qua:
    I = declare(fixed)
    Q = declare(fixed)
    n = declare(int)
    f = declare(int)
    n_st = declare_stream()
    I_st = declare_stream()
    Q_st = declare_stream()

    with for_(n, 0, n < 10, n + 1):  # The averaging loop
        play("const", "lf_element_2")
        with for_(*from_array(f, frequencies)):
            update_frequency("lf_readout_element", f)
            play("const" * amp(1), "lf_element_1")
            align()
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

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, hello_qua, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path="./")
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)
