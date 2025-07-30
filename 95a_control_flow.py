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

##################
#   Parameters   #
##################
conditions = [0, 1, 0, 1, 1]
cw_t = 20 * u.ns
short_cw_t = readout_len * u.ns

###################
# The QUA program #
###################
with program() as flow:
    b = declare(int)

    with for_each_((b), (conditions)):
        # play("cw", "resonator", duration=cw_t)
        # play("cw", "qubit", duration=cw_t)
        play("cw", "resonator", duration=short_cw_t)
        with if_(b > 0):
            play("cw", "storage", duration=cw_t)
        with port_condition(b > 0):
            play("cw", "qubit", duration=cw_t)
        align()


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)


#######################
# Simulate or execute #
#######################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, flow, simulation_config)
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
    job = qm.execute(flow)
