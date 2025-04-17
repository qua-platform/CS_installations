"""
CPMG Example, with

pulse:  pi/2_x--[tau --- Pi_y ---]*N_pulses
time:   0--------1/4t----------3/4t------t----5/4t---------7/4t------2t----
"""

from qm import SimulationConfig
from qm.qua import *
from qm import LoopbackInterface
from qm import QuantumMachinesManager
from configuration import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from macros import get_c2c_time
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
from qualang_tools.macros import long_wait

###################
# The QUA program #
###################

duration = 100 * u.ns

pulses = 6
tau = 1000 * u.ns
reset_time = 10_000 * u.ns

n_avg = 10

phases = [np.deg2rad(_) for _ in [0, 180]]



with program() as CPMG:
    n = declare(int)
    n_pulses = declare(int)
    phase = declare(fixed, )
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()
    n_st = declare_stream()
    adc_st = declare_stream(adc_trace = True)

    with for_(n, 0, n < n_avg, n+1):

        save(n,n_st) #For progress bar

        with for_each_(phase, phases):

            reset_if_phase("readout_element")
            reset_frame("readout_element")
            reset_if_phase("qubit")
            reset_frame("qubit")
            frame_rotation_2pi(phase, "qubit")

            play("pi_half", "qubit")

            with for_(n_pulses, 0, n_pulses < pulses, n_pulses + 1):
                wait(tau, "qubit")
                play("pi", "qubit")
                wait(tau, "qubit")


            frame_rotation_2pi(phase, "readout_element")

            align("qubit","readout_element")
            
            measure(
                    "readout",
                    "readout_element",
                    dual_demod.full("cos", "out1", "sin", "out2", I),
                    dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
                    adc_stream = adc_st
                )
            save(I, I_st)
            save(Q, Q_st)

            wait(reset_time)

    with stream_processing():
        I_st.buffer(len(phases)).average().save("I")
        Q_st.buffer(len(phases)).average().save("Q")
        adc_st.input1().buffer(len(phases)).average().save("adc_1_average")
        adc_st.input1().buffer(len(phases)).buffer(n_avg).save("adc_1_raw")
        adc_st.input2().buffer(len(phases)).average().save("adc_2_average")
        adc_st.input2().buffer(len(phases)).buffer(n_avg).save("adc_2_raw")
    

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=20_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, CPMG, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
else:
    qm = qmm.open_qm(config)
    job = qm.execute(CPMG)

    res = job.result_handles

    res.wait_for_all_values()

    I = res.get("I").fetch_all()
    print(I)
    adc1 = res.get("adc_1_average").fetch_all()
    print(adc1.shape)
    plt.figure()
    plt.plot(adc1.T)
    

plt.show()