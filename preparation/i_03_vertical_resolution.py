"""
The DACs have 16 bits which gives a resolution of 15µV for the direct mode and 76 µV for the amplified mode.
Voltage ramps can also be programmed by specifying the ramp rate and pulse duration.
Comments:
    - Can maintain the voltage for arbitrary sequences with ramps using sticky pulses

"""
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
with program() as scan_amp:
    a = declare(fixed)
    with infinite_loop_():
        play("const", "scope_trigger")
        with for_(a, 0, a < 100*2**-16, a + 2**-16):
            play("const" * amp(a), "lf_element_1")  # 1Vpp
            play("const" * amp(a), "lf_element_2")  # 5Vpp


with program() as ramp_prog:
    a = declare(fixed)
    with infinite_loop_():
        play("const", "scope_trigger")
        with for_(a, 1e-5, a < 5e-4, a + 6e-5):
            play(ramp(a), "lf_element_1", duration=1*u.us)  # 1Vpp
            play(ramp(a), "lf_element_2", duration=1*u.us)  # 5Vpp


with program() as ramp_sticky_prog:
    a = declare(fixed)
    with infinite_loop_():
        play("const", "scope_trigger")
        for i in range(1, 3):
            play(ramp(2e-4), f"lf_element_{i}_sticky", duration=1*u.us)
            wait(500 * u.ns, f"lf_element_{i}_sticky")
            play("const"*amp(-0.5), f"lf_element_{i}_sticky")
            wait((200 - const_len) * u.ns, f"lf_element_{i}_sticky")
            play("const"*amp(0.5), f"lf_element_{i}_sticky")
            wait((500 - const_len) * u.ns, f"lf_element_{i}_sticky")
            play(ramp(-2e-4), f"lf_element_{i}_sticky", duration=1*u.us)
            ramp_to_zero(f"lf_element_{i}_sticky")


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
    job = qmm.simulate(config, ramp_sticky_prog, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(scan_amp)
