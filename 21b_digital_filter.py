# %%
"""
        MW ON
The program plays WM in order to verify the signal on an osccilloscope.
"""

from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from configuration import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy import optimize
from qualang_tools.digital_filters import exponential_decay, single_exponential_correction

#############
# WAVEFORMS #
#############

A = -0.5
exp_tau = 100
exp_len = 1000
exp_amp = 0.2
exp_ts = np.arange(exp_len)
exp_wf = exp_amp * (1 + A * np.exp(-exp_ts / exp_tau))


# fig = plt.figure()
# plt.plot(ts, xs)
# plt.show()


# Fit your data with the exponential_decay function
[A_lpf, tau_lpf_ns], _ = optimize.curve_fit(
    exponential_decay,
    exp_ts,
    exp_wf/exp_wf.max(),
)
# Derive the corresponding taps
feedforward_taps, feedback_tap = single_exponential_correction(A_lpf, tau_lpf_ns)

# config["controllers"]["con1"]["analog_outputs"][1] = {
#     "offset": 0.0, 
#     "filter": {"feedforward": feedforward_taps, "feedback": feedback_tap}}



###################
# The QUA program #
###################

with program() as pulse_on:
    n = declare(int)

    with for_(n, 0, n < 10, n + 1):
        play("exp", "mw")
        wait(200 * u.ns)


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=None, cluster_name=cluster_name, octave=octave_config)

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, pulse_on, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
else:
    # Open Quantum Machine
    qm = qmm.open_qm(config)
    # Execute program
    job = qm.execute(pulse_on)

# %%