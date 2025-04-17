"""
UDD Example
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


###############################
# Python variable declaration # 
###############################
n_avg = 10

N_pulses = 6

total_time = 1000 #Clock cycles
relaxation_time = 10_000*u.ns

j_array = np.arange(1, N_pulses + 1)
t_pi = np.round((total_time * (np.sin(j_array * np.pi / (2 * N_pulses + 2)))**2)).astype(int)
print(t_pi)

delay_times = np.diff(np.concatenate(([0], t_pi, [total_time]))) #calulated in clock cycles
print(delay_times)



with program() as UDD:
    n = declare(int)
    n_pulse = declare(int)
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()
    n_st = declare_stream()
    delays = declare(int, value = delay_times)
    adc_st = declare_stream(adc_trace = True)

    with for_(n, 0 , n < n_avg, n+1):
        save(n, n_st)

        play("pi_half", "qubit")

        with for_(n_pulse, 0, n_pulse < N_pulses, n_pulse + 1):

            wait(delays[n_pulse], "qubit")

            play("pi", "qubit") #Need a pi_y here actually
        
        align("qubit", "readout_element")

        measure(
                "readout",
                "readout_element",
                dual_demod.full("cos", "out1", "sin", "out2", I),
                dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
                adc_stream = adc_st
            )
        save(I, I_st)
        save(Q, Q_st)

        wait(relaxation_time)


    with stream_processing():
        I_st.average().save("I")
        Q_st.average().save("Q")
        adc_st.input1().average().save("adc_1_average")
        adc_st.input1().save_all("adc_1_raw")
        adc_st.input2().average().save("adc_2_average")
        adc_st.input2().save_all("adc_2_raw")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=20_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, UDD, simulation_config)
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
    job = qm.execute(UDD)

    

plt.show()