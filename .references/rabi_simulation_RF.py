from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_rabi import *
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt


###################
# The QUA program #
###################

# Pulse duration sweep in ns - must be larger than 4 clock cycles
durations = np.arange(16, 400, 100)
# Delay in ns before stepping to the readout point after playing the qubit pulse - must be a multiple of 4ns and >= 16ns
delay_before_readout = 16

# Add the relevant voltage points describing the "slow" sequence (no qubit pulse)
seq = OPX_virtual_gate_sequence(config, ["P1_sticky", "P2_sticky"])
seq.add_points("initialization", level_init, duration_init)
seq.add_points("idle", level_manip, duration_manip)
seq.add_points("readout", level_readout, duration_readout)

with program() as Rabi_prog:

    t = declare(int)  # QUA variable for the qubit pulse duration

    with for_(*from_array(t, durations)):  # Loop over the qubit pulse duration

        # Navigate through the charge stability map
        seq.add_step(voltage_point_name="initialization")

        seq.add_step(voltage_point_name="idle", duration = t)

        align()

        seq.add_step(voltage_point_name="readout")

        I, Q, I_st, Q_st = RF_reflectometry_macro()

        # dc_signal, dc_signal_st = DC_current_sensing_macro()

        align()
        
        seq.add_compensation_pulse(duration=duration_compensation_pulse)

        seq.ramp_to_zero()

###########################
# Simulate Program #
###########################

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
# Simulates the QUA program for the specified duration
simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
# Simulate blocks python until the simulation is done
job = qmm.simulate(config, Rabi_prog, simulation_config)
# Plot the simulated samples
plt.figure()
job.get_simulated_samples().con1.plot()
plt.show()