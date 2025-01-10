from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig, LoopbackInterface
from config1 import *
import matplotlib.pyplot as plt
from qualang_tools.units import unit
from scipy import signal
from qualang_tools.loops import from_array
import plotly.io as pio
pio.renderers.default='browser'

vpp_0 = -0.11
vpp_pi = 0.14

phase_start= 0.
phase_stop  = 1
phase_points = 21
input_amp= 0.25
alfa = 1.05

LO_input_freq = 5e9

start_cooldown_time = 100 #in nanoseconds
qd_duration = 200*2
input_duration = 200 #in nanosecs
tilt_delay = 100
readout_duration = 2000
flip_delay = 40
reset_time = 1000 
sequence_duration = 2.25e4 - 19684
sequence_duration_2 = 2.25e4  - qd_duration - 16
sequence_duration_3  = 4.5e3  - qd_duration - 68
pi_amplitude = 0.185
amplitudes = [0,1]
#if_freq = 37.86e6 #37.85e6
zero_point = 0.0495
meas_point = 0.01
n_avg = 3

input_phase = np.linspace(phase_start, phase_stop, phase_points)

config1 = create_config(readout_len=readout_duration, dc_flux_reset=0.25, readout_amp = 0.5,
                    const_len = input_duration, qd_len=200, x180_amplitude = pi_amplitude, #stimulus len
                    )

delay_1 = 2.25e4 - 19684 + 200
delay_2 = 2.25e4 - qd_duration - 16
delay_3 = 2.25e4 - qd_duration - 68

desired_delay = 2.25e4
def qua_prog(delay_1, delay_2, delay_3):
    with program() as hello_qua:
        # QUA variables declaration
        I = declare(fixed)
        Q = declare(fixed)
        I_st = declare_stream()
        Q_st = declare_stream()
        phase = declare(fixed)
        n = declare(int)
        flag = declare(bool)

        with for_(*from_array(phase, input_phase)):
            play("x180" * amp(0), "qubit")
            wait(delay_3 * u.ns)
            with for_(n, 0, n < n_avg, n+1):
                play("x180" * amp(0), "qubit")
                wait(delay_2 * u.ns)
                with for_each_(flag, [False, True]):
                    #### Qubit at |0>
                    reset_global_phase()
                    reset_frame("stimulus")
                    frame_rotation_2pi(phase, 'stimulus')
                    align("qubit","stimulus","fast_flux_line","dc_flux_line","dc_flux_line2","resonator")

                    #JDPD PREPARATION
                    play("const"*amp(vpp_0 * 4), "fast_flux_line")
                    play("const"*amp(zero_point* 4), "dc_flux_line")
                    play("const"*amp(zero_point * 4*alfa), "dc_flux_line2")

                    #Drive
                    wait(start_cooldown_time * u.ns, "qubit")
                    play("x180", "qubit", condition=flag)

                    #Stimulus
                    wait((start_cooldown_time + qd_duration)  * u.ns, "stimulus")
                    play("cw"*amp(input_amp*4), "stimulus")


                    #after play it means delay keeping the same value, than it plays for 16 ( the dur set in the config)
                    wait((start_cooldown_time + qd_duration + input_duration - 16 - flip_delay) * u.ns, "fast_flux_line")
                    wait((start_cooldown_time + qd_duration + input_duration + tilt_delay - 16) * u.ns, "dc_flux_line")
                    wait((start_cooldown_time + qd_duration + input_duration + tilt_delay - 16) * u.ns, "dc_flux_line2")

                    #play("cw"*amp(input_amp), "stimulus")
                    play("const"*amp((vpp_pi - vpp_0) * 4), "fast_flux_line")
                    play("const"*amp((meas_point - zero_point) * 4), "dc_flux_line")
                    play("const"*amp((meas_point - zero_point) * 4*alfa), "dc_flux_line2")

                    #wait((readout_duration + 50 - 16) * u.ns, "stimulus")
                    wait((readout_duration + flip_delay+ 50 - 16) * u.ns, "fast_flux_line")
                    wait((readout_duration -tilt_delay + 50 - 16) * u.ns, "dc_flux_line")
                    wait((readout_duration -tilt_delay+ 50 - 16) * u.ns, "dc_flux_line2")

                    # Measurement
                    wait((start_cooldown_time + input_duration + tilt_delay+16 + qd_duration) * u.ns, "resonator")  # Wait some time after setting the dc flux
                    # Measure using dual demodulation
                    measure(
                        "readout",
                        "resonator",
                        None,
                        dual_demod.full("cos", "out1", "sin", "out2", I),
                        dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
                    )
                    align("fast_flux_line","dc_flux_line","dc_flux_line2","resonator")
                    # End of the sequence
                    ramp_to_zero("fast_flux_line")
                    ramp_to_zero("dc_flux_line")
                    ramp_to_zero("dc_flux_line2")
                    wait((thermalization_time - delay_1) * u.ns, "resonator")
                    # Save the data
                    save(I, I_st)
                    save(Q, Q_st)
        # Transfer the data from the FPGA to the CPU and perform some operations on the way (buffering, averaging, FFT...)
        with stream_processing():
            I_st.buffer(2).buffer(n_avg).buffer(len(input_phase)).save("I")
            Q_st.buffer(2).buffer(n_avg).buffer(len(input_phase)).save("Q")

    return hello_qua

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)


simulation = True
if simulation:
    simulation_config = SimulationConfig(duration=600000//4)
    # Good values
    delay1 = desired_delay - 19684 - 40
    delay2 = desired_delay - x180_len - 16
    delay3 = desired_delay - x180_len - 68
    # Initial guess
    # delay1 = desired_delay
    # delay2 = desired_delay - x180_len
    # delay3 = desired_delay - x180_len
    for i in range(1):
        job = qmm.simulate(config1, qua_prog(int(delay1), int(delay2), int(delay3)), simulation_config)
        samples = job.get_simulated_samples()# get the waveform report object
        waveform_report = job.get_simulated_waveform_report()

        slopes = np.where(np.abs(np.diff(samples.con1.analog["5"])) > 0)
        slopes_diff = np.diff(slopes[0][::3])
        delays = np.array([np.diff(slopes[0][::3])[i] for i in [0, 1, 3]]) - thermalization_time
        print(slopes_diff)
        stim_amp = samples.con1.analog["1"][slopes[0]]
        print(stim_amp)

        delay1 += delays[0]
        delay2 -= np.cumsum(np.diff(delays))[0] - desired_delay
        delay3 -= np.cumsum(np.diff(delays))[1] - 2*desired_delay - (np.cumsum(np.diff(delays))[0] - desired_delay)
        print(f"delay_1 to add: {delays[0]} ns")
        print(f"delay_2 to add: {-(np.cumsum(np.diff(delays))[0] - desired_delay)} ns")
        print(f"delay_3: {-(np.cumsum(np.diff(delays))[1] - 2*desired_delay - (np.cumsum(np.diff(delays))[0] - desired_delay))} ns")

        print(f"Time between two successive stimulus pulses: {np.diff(np.where(np.abs(np.diff(samples.con1.analog['1'])) > 0)[0])[np.diff(np.where(np.abs(np.diff(samples.con1.analog['1'])) > 0)[0])>1]} ns")
else:

    if_freqs = np.linspace(130e6,150e6,5)
    prob_if = []
    prob_if = []
    plot = False
    for if_freq in if_freqs:
    
        qm1 = qmm.open_qm(config1, close_other_machines= False) 
        qm1.set_intermediate_frequency(element ='stimulus', freq= if_freq)
        job = qm1.execute(qua_prog(int(delay_1), int(delay_2), int(delay_3)))
        results = fetching_tool(job, data_list=["I", "Q"])#, "I_e", "Q_e"])
        res = results.fetch_all()
        qm1.close()

        res2 = np.array(res)
        I_tot_all_states,Q_tot_all_states= np.array(res2)
        #I_tot = np.transpose(I_tot)
        #Q_tot = np.transpose(Q_tot)72
        max_separation_radians = []
        colors = plt.cm.RdBu(np.linspace(0,1,len(amplitudes)))
        
        
        for i in range(len(amplitudes)):
            I_tot = I_tot_all_states[:,:,i]
            Q_tot = Q_tot_all_states[:,:, i]
            thrs_I_tot= (np.max(I_tot) + np.min(I_tot))/2
            thrs_Q_tot = (np.max(Q_tot) + np.min(Q_tot))/2
            plt.figure(1)
            prob_I = []
            prob_Q = []
            for i,start_point in enumerate(input_phase):
                x = np.ones(n_avg) * start_point
            
                I = I_tot[i]
                Q = Q_tot[i]
                plt.figure(1)
                plt.title('Q')
                plt.plot(x,Q,'o',color = 'k')
                prob_Q.append(len(np.where(Q>thrs_Q_tot)[0])/len(Q))
                prob_I.append(len(np.where(I>thrs_I_tot)[0])/len(I))
            
                
                plt.figure(2)
                plt.title('I')
                plt.plot(x,I,'o',color = 'k')
                
                phase = signal.detrend(np.unwrap(np.angle(I + 1j * Q)))
                plt.figure(3)
                plt.plot(x,phase,'o',color = 'k')
                plt.legend()
            
            plt.figure(5)
            plt.title('I')
            plt.plot(input_phase, prob_I, 'o-')
        
            plt.figure(8)
            plt.title('Q')
            plt.plot(input_phase, prob_Q, 'o-')
        
        #index_min = np.argmin(prob_Q)
        #max_separation_radians.append(input_phase[index_min])
            #plt.axvline(x = 0.0213,color = 'r')
        prob_if.append((max(prob_I) + 1 - min(prob_I))/2)
            #prob_g_if.append((max(prob_g) + 1 - min(prob_g))/2)
            
        
        #plt.figure(5)
        #plt.plot(input_phase, prob_e, 'o-')
        #plt.plot(input_phase, prob_g, 'o-')
        #plt.pause(0.1)

        #prob_e_if.append((max(prob_e) + 1 - min(prob_e))/2)
        #prob_g_if.append((max(prob_g) + 1 - min(prob_g))/2)
        
        #plt.axvline(x = 0.0213,color = 'r')
        #for i,phase_point in enumerate(input_phase):