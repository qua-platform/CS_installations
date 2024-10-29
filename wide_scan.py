"""
Wide scan with three Octave outputs
"""

import os

from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.units import unit

u = unit(coerce_to_integer=True)

########################
# Experiment Variables #
########################

df = 50 * u.MHz
f_max = 350 * u.MHz
avg = 3

frequencies = np.arange(-f_max, f_max + 0.1, df)

###################
# The QUA program #
###################
with program() as hello_qua:
    n = declare(int)
    f = declare(int)
    out1 = declare(fixed)
    out1_st = declare_stream()
    n_st = declare_stream()
    with for_(n, 0, n < avg, n + 1):
        with for_(*from_array(f, frequencies)):
            update_frequency("control_eom1", f)
            play("control", "control_eom1")
            measure("readout", "SNSPD", None, integration.full("constant", out1))
            save(out1, out1_st)
        with for_(*from_array(f, frequencies)):
            update_frequency("control_eom3", f)
            play("control", "control_eom3")
            measure("readout", "SNSPD", None, integration.full("constant", out1))
            save(out1, out1_st)
        with for_(*from_array(f, frequencies)):
            update_frequency("control_eom5", f)
            play("control", "control_eom5")
            measure("readout", "SNSPD", None, integration.full("constant", out1))
            save(out1, out1_st)
        save(n, n_st)

    with stream_processing():
        out1_st.buffer(3 * len(frequencies)).average().save("out1")
        n_st.save("iteration")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=50_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, hello_qua, simulation_config)
    # Plot the simulated samples
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
