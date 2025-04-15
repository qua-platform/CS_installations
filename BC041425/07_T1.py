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

t1 = 10_000

tau1 = 5e6
tau_eff = [square_pi_len//2 + tau1, tau1 + square_pi_len]
t_echo = [0 + 2*tau_eff[0], t1+2*tau_eff[1] ]

Buffer_readout_pulse_length = 1e3

# tau2 = tau1 - Buffer_readout_pulse_length/2 # 3e3  # 11000
tau2 = np.mean(t_echo) - (square_pi_len//2 + square_pi_len + tau1) - Buffer_readout_pulse_length/2
tau3 = 20e3

N_iterations = 10
N_CPMG = 5
Trec = 10e9
reset_time = 10e9


with program() as SpinEchovsB0:
    jj0 = declare(int)
    kk0 = declare(int)
    kk1 = declare(int)
    kk2 = declare(int)
    kk3 = declare(int)
    index_stream = declare_stream()
    # stream_x1 = declare_stream(adc_trace=True)
    # stream_x2 = declare_stream(adc_trace=True)
    stream_x3 = declare_stream(adc_trace=True)
    stream_x4 = declare_stream(adc_trace=True)

    with for_(jj0, 0, jj0 < N_iterations, jj0 + 1):
        save(jj0, index_stream)
        reset_phase("qubit")
        reset_phase("readout_element")
        reset_frame("qubit")
        reset_frame("readout_element")
        play('pi', "qubit")
        long_wait(int(tau2/4), "qubit")
        
        with for_(kk1, 0, kk1 < int(Trec/5e9), kk1 + 1):
            align("qubit", "readout_element")
            long_wait(int(5e9/4), "qubit")
        
        align("qubit", "readout_element")
        reset_phase("qubit")
        play('pi_half', "qubit")
        frame_rotation_2pi(1/4, "qubit")
        long_wait(int(tau1/4), "qubit")

        align("qubit", "readout_element")
        reset_phase("qubit")
        play('pi', "qubit")
        long_wait(int(tau2/4), "qubit")

        align("qubit", "readout_element")
        measure("readout", "readout_element", stream_x3)

        with for_(kk2, 0, kk2 < N_CPMG, kk2 + 1):
            long_wait(int((tau3)/4), "qubit")
            align("qubit", "readout_element")
            reset_phase("qubit")
            play('pi', "qubit")  # pi_x
            long_wait(int(tau3/4), "qubit")

            align("qubit", "readout_element")
            measure("readout", "readout_element", stream_x4)
            align("qubit", "readout_element")

        with for_(kk3, 0, kk3 < int(reset_time/5e9), kk3 + 1):
            align("qubit", "readout_element")
            long_wait(int(5e9/4), "qubit")

    with stream_processing():
        index_stream.save('interation')

        # stream_x1.input1().average().save('adc_results_x1_I')
        # stream_x1.input2().average().save('adc_results_x1_Q')
        # stream_x2.input1().average().save('adc_results_x2_I')
        # stream_x2.input2().average().save('adc_results_x2_Q')

        stream_x3.input1().average().save('adc_results_x3_I')
        stream_x3.input2().average().save('adc_results_x3_Q')
        stream_x4.input1().average().save('adc_results_x4_I')
        stream_x4.input2().average().save('adc_results_x4_Q')



################################
# Open quantum machine manager #
################################

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulate_config = SimulationConfig(
        duration=10_000,
    )
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, SpinEchovsB0, simulate_config)
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

    qm = qm = qmm.open_qm(config)
    job = qm.execute(SpinEchovsB0)

    res = job.result_handles
    res.wait_for_all_values()

    # I_ON = np.array(res.adc_results_x1_I.fetch_all()) - np.array(res.adc_results_x2_I.fetch_all())
    # Q_ON = np.array(res.adc_results_x1_Q.fetch_all()) - np.array(res.adc_results_x2_Q.fetch_all())

    # I_ON = np.array(res.adc_results_x1_I.fetch_all())
    # Q_ON = np.array(res.adc_results_x1_Q.fetch_all())
    # t=np.arange(len(I_ON))

    I_ON = np.concatenate((np.array(res.adc_results_x3_I.fetch_all()), np.array(res.adc_results_x4_I.fetch_all()) ) )
    Q_ON = np.concatenate((np.array(res.adc_results_x3_Q.fetch_all()), np.array(res.adc_results_x4_Q.fetch_all()) ) )
    t=np.arange(len(I_ON)) 
    print(I_ON)

plt.show()
