from qm.qua import *
from configuration import *





tau1 = 5e6
tau_eff = [Spin_halfpipulse_length + tau1, tau1 + Spin_pipulse_length]
t_echo = [0 + 2*tau_eff[0], t1+2*tau_eff[1] ]

# tau2 = tau1 - Buffer_readout_pulse_length/2 # 3e3  # 11000
tau2 = np.mean(t_echo) - (Spin_halfpipulse_length + Spin_pipulse_length + tau1) - Buffer_readout_pulse_length/2
tau3 = 20e3

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
        reset_phase(spin_element)
        reset_phase(readout_element)
        reset_frame(spin_element)
        reset_frame(readout_element)
        play('Spin_pix', spin_element)
        wait(int(tau2/4), spin_element)
        
        with for_(kk1, 0, kk1 < int(Trec/5e9), kk1 + 1):
            align(spin_element, readout_element)
            wait(int(5e9/4), spin_element)
        
        align(spin_element, readout_element)
        reset_phase(spin_element)
        play('Spin_halfpix', spin_element)
        frame_rotation_2pi(1/4, spin_element)
        wait(int(tau1/4), spin_element)

        align(spin_element, readout_element)
        reset_phase(spin_element)
        play('Spin_pix', spin_element)
        wait(int(tau2/4), spin_element)

        align(spin_element, readout_element)
        measure(readout_pulse, readout_element, stream_x3)

        with for_(kk2, 0, kk2 < N_CPMG, kk2 + 1):
            wait(int((tau3)/4), spin_element)
            align(spin_element, readout_element)
            reset_phase(spin_element)
            play('Spin_pix', spin_element)  # pi_x
            wait(int(tau3/4), spin_element)

            align(spin_element, readout_element)
            measure(readout_pulse, readout_element, stream_x4)
            align(spin_element, readout_element)

        with for_(kk3, 0, kk3 < int(reset_time/5e9), kk3 + 1):
            align(spin_element, readout_element)
            wait(int(5e9/4), spin_element)

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

