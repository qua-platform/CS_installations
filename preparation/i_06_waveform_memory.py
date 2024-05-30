from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *

from scipy.signal.windows import gaussian


###################
# The QUA program #
###################
wf = np.array( list(0.1+0.4*(gaussian(100,60)-gaussian(100,60)[0])) + list(np.arange(0.1, 0.4, 0.01)) + [0.5]*2 + list(np.arange(0.4, 0.1, -0.01)) + [0.0]*100)
# wf -= wf[0]
# wf = 0.1 * np.random.random_sample(size=65000)
config["waveforms"]["arbitrary_wf"] = {"type": "arbitrary", "samples": wf.tolist()}
config["pulses"]["arbitrary_pulse"]["length"] = len(wf)

t_min = len(wf)  # In clock cycles (4ns) - Must be larger than 4 clock cycles = 16ns
t_max = min(2**24, 10*len(wf))  # In clock cycles (4ns) - Must be lower than 2**24 clock cycles = 67ms
step = len(wf)  # In clock cycles (4ns)
with program() as cw:
    t = declare(int)
    with infinite_loop_():
        play("const", "lf_element_2")
        with for_(t, t_min, t < t_max, t + step):
            play("arbitrary", "lf_element_1", duration=t)

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
    job = qmm.simulate(config, cw, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(cw)
