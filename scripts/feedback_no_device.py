from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_lf_fem import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.results.data_handler import DataHandler

##################
#   Parameters   #
##################
n_tries = 100
threshold = 0.05

# Add the relevant voltage points describing the "slow" sequence (no qubit pulse)
seq = VoltageGateSequence(config, ["P1_sticky", "P2_sticky"])
# seq.add_points("initialization", level_init, duration_init)
# seq.add_points("idle", level_manip, duration_manip)
# seq.add_points("readout", level_readout, duration_readout)
on_peak_coords = [0.1, 0]
off_peak_coords = [0, 0]
seq.add_points("on_peak", on_peak_coords, 16)
seq.add_points("off_peak", off_peak_coords, 16)
###################
# The QUA program #
###################
with program() as simple_feedback:
    f = declare(int)  # QUA variable for the frequency sweep
    n = declare(int)  # QUA variable for the averaging loop
    rng = Random(1)
    random_state = declare(int)
    state_str = declare_stream()
    on_off_st = declare_stream()

    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_tries, n + 1):

        assign(random_state, rng.rand_int(2))
        save(random_state, state_str)

        with if_(random_state == 1):  # On peak
            seq.add_step(voltage_point_name="off_peak")
            save(1, on_off_st)
        with elif_(random_state == 0):  # Off peak
            seq.add_step(voltage_point_name="on_peak")
            save(0, on_off_st)
        # save(Q, Q_st)
        # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
        # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
        # process them which can cause the OPX to crash.
        wait(1_000 * u.ns, "tank_circuit")
        save(n, n_st)

    with stream_processing():
        on_off_st.save_all("on_off")
        state_str.save_all("state")
        n_st.save_all("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
# qmm = QuantumMachinesManager(
#     host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
# )

#######################
# Simulate or execute #
#######################
simulate = True

if simulate:
    from test_tools.cloud_simulator import client

    with client.simulator(client.latest_version()) as instance:
        # Use the instance object to simulate QUA programs
        qmm = QuantumMachinesManager(
            host=instance.host,
            port=instance.port,
            connection_headers=instance.default_connection_headers,
        )

        job = qmm.simulate(
            config,
            simple_feedback,
            SimulationConfig(
                duration=int(1e4 // 4),  # duration of simulation in units of 4ns
            ),
        )
        samples = job.get_simulated_samples()

        waveform_report = job.get_simulated_waveform_report()
        waveform_report.create_plot(samples, plot=True)

    """
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, simple_feedback, simulation_config)
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
    """
else:

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(simple_feedback)
    # Get results from QUA program
    results = fetching_tool(
        job, data_list=["on_off", "state", "iteration"], mode="wait_for_all"
    )
    all_results = results.fetch_all()
    # plotting
    fig = plt.figure()
    plt.plot(all_results[0], label="on_off")
    fig.show()

    fig = plt.figure()
    plt.plot(all_results[1])
    fig.show()
