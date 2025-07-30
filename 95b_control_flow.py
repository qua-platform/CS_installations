# %%
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qm import LoopbackInterface
from configuration_MWFEM import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.results.data_handler import DataHandler

##################
#   Parameters   #
##################
amp_list = np.linspace(0, 1, 10)
cw_t = 20 * u.ns
short_cw_t = readout_len * u.ns
min_I = -1

###################
# The QUA program #
###################
with program() as flow:
    b = declare(fixed)
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()

    reset_global_phase()
    with for_each_((b), (amp_list)):
        measure(
            "readout" * amp(b),
            "resonator",
            # demod.full("cos", I[0], "out2"),
            # demod.full("sin", Q[0], "out2"),
            dual_demod.full("cos", "sin", I),
            dual_demod.full("minus_sin", "cos", Q),
        )
        save(I, I_st)
        save(Q, Q_st)

        with if_(I > min_I):
            play("cw", "storage", duration=cw_t)
        with port_condition(I > min_I):
            play("cw", "qubit", duration=cw_t)
        align()

    with stream_processing():
        I_st.save_all("I")
        Q_st.save_all("Q")


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
    simulation_config = SimulationConfig(
        duration=2_000,
        simulation_interface=LoopbackInterface(
            [
                (
                    "con1",
                    mw_fem_slot,
                    resonator_port,
                    "con1",
                    mw_fem_slot,
                    resonator_readout_port,
                )
            ]
        ),
    )
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, flow, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    plt.show()
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
    job = qm.execute(flow)

results = job.result_handles
results.wait_for_all_values()
I_data = results.I.fetch_all()["value"]
Q_data = results.Q.fetch_all()["value"]
plt.plot(I_data, "o")
plt.plot(Q_data, "o")
