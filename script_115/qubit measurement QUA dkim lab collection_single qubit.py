from qm import SimulationConfig
from qm.qua import *
from qm.octave import *
from qm import LoopbackInterface
from qm import QuantumMachinesManager
from qm.octave.octave_manager import ClockMode
from configuration_room115 import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os
from datetime import datetime
from scipy.optimize import curve_fit
import time
from qualang_tools.loops import from_array
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.units import unit
from rb_lib import *

# from set_octave import *
from random import randint
import csv
import copy


get_ipython().run_line_magic("matplotlib", "qt")

##################BASIC INFORMATION################################
date = time.strftime("%Y%m%d_%H_%M", time.localtime(time.time()))
# date = time.strftime('%Y%m%d_%H_%M_%S', time.localtime(time.time()))
Nas_path = f"Z:/실험/Dilution fridge setup/OPX 관련"
local_path = r"C:\Users\measure\Desktop\OPX 관련\115 quantum measurements"
room115_path = f"Z:/share/실험/Dilution fridge setup/OPX 관련/qua/28Si quantum measurements"

my_path = local_path

###### CONDITIONAL PARAMETERS FOR THE TYPE OF MEASUREMENTS TO BE PERFORMED#############
plot_chevron = 1
run_analysis = 1  # Plot the final results when 1 (e.g. plotting chevron pattern, etc.)
adaptive_initialization = 1  # 0 : NO, 1: YES
reverse_singleshot = 0
save_data = 1
save_trace = 0
save_fig = 0
color_YlGnBu = 0
zero_one_data = 0
Ramsey = 0
Echo = 0
#######################################################################################

####### PROGRAM TYPE ####### ##########################################################
simulation = 0
looping_pi_pulse = 0
plot_1d_fre_sweep = 0
plot_amplitude_varied_2d_plot = 0
plot_fre_vs_fre_2d_plot = 0
amp_Rabi = 0
phase_Ramsey = 0
shuttling_exchange = 0
swap_freq_calibration = 0
######################################################################################

###### CURVE FITTING PARAMETERS########################################################
do_fit = 1  # Conduct curve fitting when 1
initial_A = 0.5
initial_rabi_guess = 1e6  # Hz
initial_decay_guess = 5e-6  # s
# initial_alpha = 1
initial_phase = 0  # degree
initial_offset = 0.4
initial_fr = 15.694  # GHz
initial_sigma = 0.002  # MHz
######################################################################################

######DEVICE PATAMETERS###############################################################
qubit_to_play = "Q2"
lockin_to_read = "lockin"

qubit = "qe1"
title = f""

Nrep = 1
add_prob = False
date_update = False
# -----PARAMS FOR THE WAVEFORM--------------------------------------------------------#
N = 10
tmax = 4 * 1000  # ns
t_unit2_fixed = 50.0  # time unit for operation sequence in nanoseconds
t_unit2 = int(t_unit2_fixed / 4)  # Conversion to clock cycle
t_delay_fixed = 7.0 * 1000
t_phase_varying = int(43 * 1000 / 4)  # Conversion to clock cycle
t_phase_varying2 = int(t_phase_varying / 2)  # Conversion to clock cycle

if Nrep == 1:
    add_prob = False
    date_update = False
else:
    add_prob = True
    date_update = True
    tmax = 0
trange = np.arange(0, tmax + t_unit2_fixed / 2, t_unit2_fixed)
if Echo == 1:
    trange = 2 * trange
n_rep2 = len(trange)
######################################################################################

###### MW FREQUENCY SETTING - for readout qubit ################################### ######################
resonance_freq = 15.65e9  # 15.71575e9
# lo_freq = config['elements'][qubit]['mixInputs']['lo_frequency']
lo_freq = config["octaves"][octave]["RF_outputs"][int(qubit[-1])]["LO_frequency"]
fnpoints = 51
if_start = 15.580e9 - lo_freq  # 15.7055
if_stop = 15.690e9 - lo_freq  # 15.7105
if fnpoints == 1:
    if_start = resonance_freq - lo_freq
ifreqs = np.linspace(if_start, if_stop, fnpoints)
freqs = np.linspace(lo_freq + if_start, lo_freq + if_stop, fnpoints) / 1e9
######################################################################################

###### MW FREQUENCY SETTING - for inner qubit ################################### ######################
resonance_freq2 = 17.4922e9
resonance_if2 = resonance_freq2 - lo_freq
fnpoints2 = 101
if_start2 = 14.365e9 - lo_freq
if_stop2 = 14.475e9 - lo_freq
if fnpoints2 == 1:
    if_start2 = resonance_freq2 - lo_freq
ifreqs2 = np.linspace(if_start2, if_stop2, fnpoints2)
freqs2 = np.linspace(lo_freq + if_start2, lo_freq + if_stop2, fnpoints2) / 1e9
######################################################################################

###### RF FREQUENCY SETTING - for swap gate ################################### ######################
resonance_freq_swap = 452e6
fswapnpoints = 51
if_start_swap = 380e6
if_stop_swap = 430e6
if fswapnpoints == 1:
    if_start_swap = resonance_freq_swap
ifreqs_swap = np.linspace(if_start_swap, if_stop_swap, fswapnpoints)
freqs_swap = np.linspace(if_start_swap, if_stop_swap, fswapnpoints) / 1e6
######################################################################################


###### DETUNING PULSE SETTING ################################### ######################
amp_points = 41  # number of amplitude points #
amp_start = 0  # in V
amp_max = -0.010  # in V
step_amp = (amp_max - amp_start) / (amp_points - 1)
amp_list = np.linspace(amp_start, amp_max, amp_points)
n_amp = len(amp_list)
######################################################################################

###### PHASE setting for phase varying Ramsey ################
phase_step = 10  # in degree #
phase_start = 0
phase_max = 720
phase_list = np.arange(phase_start, phase_max + phase_step / 2, phase_step)
n_phase = len(phase_list)
######################################################################################


######## OPX MEASURE READOUT SETTING ################################################
Iarr_weight = 2560 / slice_size
Iarr_weight2 = 2560
slice_size_inv = 1 / slice_size
# disc_thr_comp = disc_tr/Iarr_weight
# disc_thr_comp2 = disc_thr/Iarr_weight2
disc_thr = (
    12.0e-3  # discrimination threshold for single-shot determination in Volts (V)
)
disc_thr_abs = 96e-3  # V
disc_thr_real = disc_thr / Iarr_weight
disc_thr_real2 = disc_thr / Iarr_weight2  # disc_thr/Iarr_weight2

readout_array_length = int(
    readout_pulse_length / (slice_size * 4)
)  # Length of the rf trace array (Iarr)
######################################################################################

######### DETUNING PULSE SETTING ####################################################
total_width = int(360 * 1000 / 4)  # us 650
pulse_width = int(55 * 1000 / 4)  # us 105
# pulse_width2 = int(505*1000/4) # us
wait_width = int(total_width - pulse_width)
read_wait_width = int(0.5 * 1000 / 4) + pulse_width  # us
switching_delay = int(3 * 1000 / 4)
shuttling_delay = int(3 * 1000 / 4)
t_delay = int(t_delay_fixed / 4)
Trigger_period = int(100 * 1000 / 4)  # 12500  #6250# 5000+10#12500#25000 #6250 #25000
#######################################################################################

# if plot_amplitude_varied_2d_plot == 1 or amp_Rabi:
#    print(f'sweep frequency from {(lo_freq+if_start)/1e9:3f} to {(lo_freq+if_stop)/1e9:3f} GHz, # of points = {fnpoints}\nwith increasing amplitude {amp_start} ~ {amp_max}V , {n_amp} steps\n')
#    print(f'estimated time : {fnpoints*n_amp*N*(total_width*4*1e-9)/60} min')
# else:
#    print(f'sweep frequency from {(lo_freq+if_start)/1e9:3f} to {(lo_freq+if_stop)/1e9:3f} GHz, # of points = {fnpoints}\nwith increasing mw burst time 0 ~ {tmax/1000}us , {n_rep2} steps\n')
#    print(f'estimated time : {fnpoints*n_rep2*N*(total_width*4*1e-9)/60} min')


def add_data_to_csv(file_path, data):
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)


######################################################################################
###############  The QUA program -1 : infinite trigger           ###############
######################################################################################
with program() as inf_loop_pi_pulse:
    f = declare(int)
    n = declare(int, value=0)  # average (repetition)
    m = declare(int, value=0)  # adaptive initialization
    l = declare(int, value=0)  # mw burst time sweep
    k = declare(int, value=0)
    it = declare(int, value=0)  # to save readout array
    I = declare(fixed)  # 1/0 value
    I2 = declare(fixed)  # for adaptive initialization
    Iarr = declare(fixed, size=readout_array_length)  # demod trace
    I_st = declare_stream()  # 1/0 stream
    Iarr_st = declare_stream()  # trace strea,

    # update_frequency(qubit, if_start)
    with infinite_loop_():
        ################## 1.0 Let HDAWG play operation pulse #####
        ## Detuning pulse ##
        play("trigger", "Trigger5", duration=50)
        ramp_to_zero("Trigger5", 1)

        wait(Trigger_period)
        # reset_phase(qubit)

        # play('pi', qubit)
        # align('Trigger5', lockin_to_read)

        ################## 1.1 Readout  ####################################
        # measure("readout", lockin_to_read , None,
        #        integration.sliced("integ_weights_cos", Iarr,slice_size),
        #        ) # f_IF = 0 , demodulate the raw ADC data and save as an array


# %%

######################################################################################
###############  The QUA program 0 : for EDSR 1D freq sweep            ###############
######################################################################################
with program() as EDSR:
    f = declare(int)
    n = declare(int, value=0)  # average (repetition)
    m = declare(int, value=0)  # adaptive initialization
    l = declare(int, value=0)  # mw burst time sweep
    k = declare(int, value=0)
    it = declare(int, value=0)  # to save readout array
    I = declare(fixed)  # 1/0 value
    I2 = declare(fixed)  # for adaptive initialization
    Iarr = declare(fixed, size=readout_array_length)  # demod trace
    I_st = declare_stream()  # 1/0 stream
    Iarr_st = declare_stream()  # trace strea,
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(k, 0, k < 100000 / 4, k + 1):
        play("trigger", "Trigger5", duration=pulse_width)
        ramp_to_zero("Trigger5", 1)
        wait(t_delay, qubit)  # 2us
        play("pi", qubit)
        wait(wait_width)
    align()

    with while_(n < N):  # repetition
        with for_(*from_array(f, ifreqs)):
            update_frequency(qubit, f)

            ################## 1.0 Let HDAWG play operation pulse #####
            ## Detuning pulse ##
            play("trigger", "Trigger5", duration=pulse_width)
            ramp_to_zero("Trigger5", 1)

            wait(t_delay, qubit)
            reset_phase(qubit)

            play("pi", qubit)

            align("Trigger5", lockin_to_read)

            ################## 1.1 Readout  ####################################
            measure(
                "readout",
                lockin_to_read,
                None,
                integration.sliced("integ_weights_cos", Iarr, slice_size),
            )  # f_IF = 0 , demodulate the raw ADC data and save as an array

            with if_((Math.max(Iarr) - Math.min(Iarr)) > disc_thr_real):
                assign(I, 1)

            with else_():
                assign(I, 0)

            save(I, I_st)

            if save_trace == 1:
                with for_(it, 0, it < readout_array_length, it + 1):
                    save(Iarr[it], Iarr_st)

            ######################### 1.2 check initialization #################
            if adaptive_initialization == 1:
                measure(
                    "readout2",
                    lockin_to_read,
                    None,
                    integration.full("integ_weights_cos2", I2),
                )
                if reverse_singleshot == 1:
                    with while_(
                        (I2 - Math.max(Iarr) * slice_size_inv > disc_thr_real2)
                        & (m < 5000)
                    ):
                        measure(
                            "readout2",
                            lockin_to_read,
                            None,
                            integration.full("integ_weights_cos2", I2),
                        )
                        assign(m, m + 1)  # avoid infinite loop
                else:
                    with while_(
                        (I2 - Math.min(Iarr) * slice_size_inv > disc_thr_real2)
                        & (m < 2500)
                    ):
                        # with while_( (I2 > disc_thr_real2) & (m<2500) ):
                        measure(
                            "readout2",
                            lockin_to_read,
                            None,
                            integration.full("integ_weights_cos2", I2),
                        )
                        assign(m, m + 1)  # avoid infinite loop
                assign(m, 0)

        save(n, n_st)
        assign(n, n + 1)

    with stream_processing():
        # I_st.buffer(N, fnpoints).save('I')
        I_st.buffer(fnpoints).average().save("I")
        if save_trace == 1:
            Iarr_st.save_all("Iarr")
        n_st.save("iteration")

######################################################################################
###############  The QUA program 1 : for Rabi, Ramsey, Echo, fre vs time   ###############
######################################################################################
with program() as Single_Spin:
    f = declare(int)
    n = declare(int, value=0)  # average (repetition)
    m = declare(int, value=0)  # adaptive initialization
    l = declare(int, value=0)  # mw burst time sweep
    k = declare(int, value=0)
    it = declare(int, value=0)  # to save readout array
    I = declare(fixed)  # 1/0 value
    I2 = declare(fixed)  # for adaptive initialization
    Iarr = declare(fixed, size=readout_array_length)  # demod trace
    I_st = declare_stream()  # 1/0 stream
    Iarr_st = declare_stream()  # trace strea,
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(k, 0, k < 100000 / 4, k + 1):
        play(amp(0.0) * "trigger", "Trigger5", duration=pulse_width)
        ramp_to_zero("Trigger5", 1)
        wait(t_delay, qubit)  # 2us
        play(amp(0.0) * "pi", qubit)
        wait(wait_width)
    align()

    with while_(n < N):  # repetition
        with for_(*from_array(f, ifreqs)):
            update_frequency(qubit, f)

            with for_(l, 0, l < n_rep2, l + 1):  # mw burst time sweep (HDAWG Trigger)
                ################## 1.0 Let HDAWG play operation pulse #####
                ## Detuning pulse ##
                play(amp(0.0) * "trigger", "Trigger5", duration=pulse_width)
                ramp_to_zero("Trigger5", 1)

                wait(t_delay, qubit)
                # wait(shuttling_delay, qubit)

                ## MW pulse for pi/2 on Q3##
                # update_frequency(qubit, resonance_if2)
                # reset_phase(qubit)
                # play('half_pi', qubit)
                # wait(t_delay, qubit)

                ## MW pulse for pi on Q1##
                update_frequency(qubit, f)
                reset_phase(qubit)

                ## MW pulse for Ramsey##
                if Ramsey == 1:
                    with if_(l == 0):
                        play("pi", qubit)
                    with else_():
                        play("half_pi", qubit)
                        wait(t_unit2 * l, qubit)
                        play("half_pi", qubit)

                ## MW pulse for Echo##
                elif Echo == 1:
                    with if_(l == 0):
                        play("half_pi", qubit)
                        play("pi", qubit)
                        play("half_pi", qubit)

                    with else_():
                        play("half_pi", qubit)
                        wait(t_unit2 * l, qubit)
                        play("pi", qubit)
                        wait(t_unit2 * l, qubit)
                        play("half_pi", qubit)

                ## MW pulse for Rabi##
                elif n_rep2 == 1:  # tmax=0us
                    play("pi", qubit)
                    # play('pi_zero', qubit)
                else:
                    with if_(l > 0):
                        play(amp(0.0) * "CW", qubit, duration=t_unit2 * l)

                align("Trigger5", lockin_to_read)

                ################## 1.1 Readout  ####################################
                measure(
                    "readout",
                    lockin_to_read,
                    None,
                    integration.sliced("integ_weights_cos", Iarr, slice_size),
                )  # f_IF = 0 , demodulate the raw ADC data and save as an array

                with if_((Math.max(Iarr) - Math.min(Iarr)) > disc_thr_real):
                    assign(I, 1)

                with else_():
                    assign(I, 0)

                save(I, I_st)

                if save_trace == 1:
                    with for_(it, 0, it < readout_array_length, it + 1):
                        save(Iarr[it], Iarr_st)

                ######################### 1.2 check initialization #################
                if adaptive_initialization == 1:
                    measure(
                        "readout2",
                        lockin_to_read,
                        None,
                        integration.full("integ_weights_cos2", I2),
                    )
                    if reverse_singleshot == 1:
                        with while_(
                            (I2 - Math.max(Iarr) * slice_size_inv > disc_thr_real2)
                            & (m < 5000)
                        ):
                            measure(
                                "readout2",
                                lockin_to_read,
                                None,
                                integration.full("integ_weights_cos2", I2),
                            )
                            assign(m, m + 1)  # avoid infinite loop
                    else:
                        with while_(
                            (I2 - Math.min(Iarr) * slice_size_inv > disc_thr_real2)
                            & (m < 2500)
                        ):
                            # with while_( (I2 > disc_thr_real2) & (m<2500) ):
                            measure(
                                "readout2",
                                lockin_to_read,
                                None,
                                integration.full("integ_weights_cos2", I2),
                            )
                            assign(m, m + 1)  # avoid infinite loop
                    assign(m, 0)

        save(n, n_st)
        assign(n, n + 1)

    with stream_processing():
        # I_st.buffer(N, fnpoints, n_rep2).save('I')
        I_st.buffer(fnpoints, n_rep2).average().save("I")

        if save_trace == 1:
            Iarr_st.save_all("Iarr")

        n_st.save("iteration")
# %% Program 2.
######################################################################################
###############  The QUA program 2                                 ###############
######################################################################################
with program() as amplitude_Rabi:
    f = declare(int)
    n = declare(int, value=0)  # average (repetition)
    m = declare(int, value=0)  # adaptive initialization
    l = declare(int, value=0)  # mw burst time sweep
    k = declare(int, value=0)  # mw burst time sweep
    a = declare(fixed, value=0.0)
    it = declare(int, value=0)  # to save readout array
    I = declare(fixed)  # 1/0 value
    I2 = declare(fixed)  # for adaptive initialization
    Iarr = declare(fixed, size=readout_array_length)  # demod trace
    I_st = declare_stream()  # 1/0 stream
    Iarr_st = declare_stream()  # trace strea,
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(k, 0, k < 5000, k + 1):
        play("trigger", "Trigger5", duration=pulse_width)
        ramp_to_zero("Trigger5", 1)
        wait(wait_width)
    align()

    with while_(n < N):  # repetition
        update_frequency(qubit, if_start)
        with for_(*from_array(a, amp_list)):
            ################## 1.0 Let HDAWG play operation pulse #####
            ## ver.1 step pulse ##

            ## Detuning pulse ##
            play("trigger", "Trigger5", duration=pi_len_cycle1 + pulse_width)
            ramp_to_zero("Trigger5", 1)

            wait(t_delay, qubit)
            reset_phase(qubit)

            play(amp(a) * "pi", qubit)

            align("Trigger5", lockin_to_read)

            ################## 1.1 Readout  ####################################
            measure(
                "readout",
                lockin_to_read,
                None,
                integration.sliced("integ_weights_cos", Iarr, slice_size),
            )  # f_IF = 0 , demodulate the raw ADC data and save as an array

            with if_((Math.max(Iarr) - Math.min(Iarr)) > disc_thr_real):
                assign(I, 1)

            with else_():
                assign(I, 0)

            save(I, I_st)

            if save_trace == 1:
                with for_(it, 0, it < readout_array_length, it + 1):
                    save(Iarr[it], Iarr_st)

            ######################### 1.2 check initialization #################
            if adaptive_initialization == 1:
                measure(
                    "readout2",
                    lockin_to_read,
                    None,
                    integration.full("integ_weights_cos2", I2),
                )
                if reverse_singleshot == 1:
                    with while_(
                        (I2 - Math.max(Iarr) * slice_size_inv > disc_thr_real2)
                        & (m < 5000)
                    ):
                        measure(
                            "readout2",
                            lockin_to_read,
                            None,
                            integration.full("integ_weights_cos2", I2),
                        )
                        assign(m, m + 1)  # avoid infinite loop
                else:
                    with while_(
                        (I2 - Math.min(Iarr) * slice_size_inv > disc_thr_real2)
                        & (m < 5000)
                    ):
                        # with while_( (I2 > disc_thr_real2) & (m<2500) ):
                        measure(
                            "readout2",
                            lockin_to_read,
                            None,
                            integration.full("integ_weights_cos2", I2),
                        )
                        assign(m, m + 1)  # avoid infinite loop
                assign(m, 0)

        save(n, n_st)
        assign(n, n + 1)

    with stream_processing():
        # I_st.buffer(N, n_amp).save('I')
        I_st.buffer(n_amp).average().save("I")
        if save_trace == 1:
            Iarr_st.save_all("Iarr")
        n_st.save("iteration")

# %% Program 3.
######################################################################################
###############  The QUA program 3 : Exchange spec etc, fre vs. amplitude     ########
######################################################################################
with program() as amplitude_sweep:
    f = declare(int)
    n = declare(int, value=0)  # average (repetition)
    m = declare(int, value=0)  # adaptive initialization
    l = declare(int, value=0)  # detuning amplitude sweep
    k = declare(int, value=0)  # mw burst time sweep
    a = declare(fixed, value=0.0)
    it = declare(int, value=0)  # to save readout array
    I = declare(fixed)  # 1/0 value
    I2 = declare(fixed)  # for adaptive initialization
    Iarr = declare(fixed, size=readout_array_length)  # demod trace
    I_st = declare_stream()  # 1/0 stream
    Iarr_st = declare_stream()  # trace strea,
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with while_(n < N):  # repetition
        with for_(l, 0, l < n_amp, l + 1):
            with for_(*from_array(f, ifreqs)):  # amplitude sweep index
                ################## 1.0 Let HDAWG play operation pulse #####
                ## Detuning pulse ##
                play("trigger", "Trigger5", duration=pulse_width)
                ramp_to_zero("Trigger5", 1)
                wait(1750, qubit)  # 펄스 1750

                # wait(t_delay, qubit)
                ## MW pulse for pi on Q2##
                # update_frequency(qubit, 277e6)
                # reset_phase(qubit)
                # play('pi2', qubit)
                # wait(500, qubit)

                ## MW pulse for pi on Q1##
                update_frequency(qubit, f)
                reset_phase(qubit)
                play("pi", qubit)
                align("Trigger5", lockin_to_read)

                ################## 1.1 Readout  ####################################
                measure(
                    "readout",
                    lockin_to_read,
                    None,
                    integration.sliced("integ_weights_cos", Iarr, slice_size),
                )  # f_IF = 0 , demodulate the raw ADC data and save as an array

                with if_((Math.max(Iarr) - Math.min(Iarr)) > disc_thr_real):
                    assign(I, 1)

                with else_():
                    assign(I, 0)

                save(I, I_st)

                if save_trace == 1:
                    with for_(it, 0, it < readout_array_length, it + 1):
                        save(Iarr[it], Iarr_st)
                #######################################################################

                # play('trigger', "Trigger5", duration=100000)
                # ramp_to_zero('Trigger5', 1)
                # align('Trigger5', lockin_to_read)

                ######################### 1.2 check initialization #################
                if adaptive_initialization == 1:
                    measure(
                        "readout2",
                        lockin_to_read,
                        None,
                        integration.full("integ_weights_cos2", I2),
                    )
                    if reverse_singleshot == 1:
                        with while_(
                            (I2 - Math.max(Iarr) * slice_size_inv > disc_thr_real2)
                            & (m < 5000)
                        ):
                            measure(
                                "readout2",
                                lockin_to_read,
                                None,
                                integration.full("integ_weights_cos2", I2),
                            )
                            assign(m, m + 1)  # avoid infinite loop
                    else:
                        with while_(
                            (I2 - Math.min(Iarr) * slice_size_inv > disc_thr_real2)
                            & (m < 5000)
                        ):
                            # with while_( (I2 > disc_thr_real2) & (m<2500) ):
                            measure(
                                "readout2",
                                lockin_to_read,
                                None,
                                integration.full("integ_weights_cos2", I2),
                            )
                            assign(m, m + 1)  # avoid infinite loop
                    assign(m, 0)

                ##wait(250*1000*50)

        save(n, n_st)
        assign(n, n + 1)

    with stream_processing():
        # I_st.buffer(N, n_amp, fnpoints).save('I')
        I_st.buffer(n_amp, fnpoints).average().save("I")
        if save_trace == 1:
            Iarr_st.save_all("Iarr")
        n_st.save("iteration")

# %% Program 4.
######################################################################################
###############  The QUA program 4 : Exchange spec, dB cal, fre 1 vs. fre 2 at fixed exchange amplitude     ########
######################################################################################
with program() as exchange_dB_cal_fixed_amp:
    f = declare(int)
    f2 = declare(int)
    n = declare(int, value=0)  # average (repetition)
    m = declare(int, value=0)  # adaptive initialization
    l = declare(int, value=0)  # detuning amplitude sweep
    k = declare(int, value=0)  # mw burst time sweep
    a = declare(fixed, value=0.0)
    it = declare(int, value=0)  # to save readout array
    I = declare(fixed)  # 1/0 value
    I2 = declare(fixed)  # for adaptive initialization
    Iarr = declare(fixed, size=readout_array_length)  # demod trace
    I_st = declare_stream()  # 1/0 stream
    Iarr_st = declare_stream()  # trace strea,
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with while_(n < N):  # repetition
        with for_(*from_array(f2, ifreqs2)):
            with for_(*from_array(f, ifreqs)):
                ################## 1.0 Let HDAWG play operation pulse #####
                ## Detuning pulse ##
                play("trigger", "Trigger5", duration=pulse_width)
                ramp_to_zero("Trigger5", 1)
                wait(40, qubit)

                # wait(t_delay, qubit)
                ## MW pulse for pi on Q2##
                update_frequency(qubit, f2)
                reset_phase(qubit)
                # play('pi2', qubit)
                play("half_pi", qubit)
                wait(t_unit2 * 100, qubit)
                play("half_pi", qubit)

                wait(500, qubit)

                ## MW pulse for pi on Q1##
                update_frequency(qubit, f)
                reset_phase(qubit)
                play("pi", qubit)
                align("Trigger5", lockin_to_read)

                ################## 1.1 Readout  ####################################
                measure(
                    "readout",
                    lockin_to_read,
                    None,
                    integration.sliced("integ_weights_cos", Iarr, slice_size),
                )  # f_IF = 0 , demodulate the raw ADC data and save as an array

                with if_((Math.max(Iarr) - Math.min(Iarr)) > disc_thr_real):
                    assign(I, 1)

                with else_():
                    assign(I, 0)

                save(I, I_st)

                if save_trace == 1:
                    with for_(it, 0, it < readout_array_length, it + 1):
                        save(Iarr[it], Iarr_st)
                #######################################################################

                # play('trigger', "Trigger5", duration=100000)
                # ramp_to_zero('Trigger5', 1)
                # align('Trigger5', lockin_to_read)

                ######################### 1.2 check initialization #################
                if adaptive_initialization == 1:
                    measure(
                        "readout2",
                        lockin_to_read,
                        None,
                        integration.full("integ_weights_cos2", I2),
                    )
                    if reverse_singleshot == 1:
                        with while_(
                            (I2 - Math.max(Iarr) * slice_size_inv > disc_thr_real2)
                            & (m < 5000)
                        ):
                            measure(
                                "readout2",
                                lockin_to_read,
                                None,
                                integration.full("integ_weights_cos2", I2),
                            )
                            assign(m, m + 1)  # avoid infinite loop
                    else:
                        with while_(
                            (I2 - Math.min(Iarr) * slice_size_inv > disc_thr_real2)
                            & (m < 5000)
                        ):
                            # with while_( (I2 > disc_thr_real2) & (m<2500) ):
                            measure(
                                "readout2",
                                lockin_to_read,
                                None,
                                integration.full("integ_weights_cos2", I2),
                            )
                            assign(m, m + 1)  # avoid infinite loop
                    assign(m, 0)
        save(n, n_st)
        assign(n, n + 1)

    with stream_processing():
        # I_st.buffer(N, fnpoints2, fnpoints).save('I')
        I_st.buffer(fnpoints2, fnpoints).average().save("I")
        if save_trace == 1:
            Iarr_st.save_all("Iarr")
        n_st.save("iteration")
# %% Program 4-1.
######################################################################################
###############  The QUA program 4-1: swap fre cal prob vs. fre               ########
######################################################################################
with program() as swap_freq_1d_sweep:
    f = declare(int)
    f2 = declare(int)
    n = declare(int, value=0)  # average (repetition)
    m = declare(int, value=0)  # adaptive initialization
    l = declare(int, value=0)  # detuning amplitude sweep
    k = declare(int, value=0)  # mw burst time sweep
    a = declare(fixed, value=0.0)
    it = declare(int, value=0)  # to save readout array
    I = declare(fixed)  # 1/0 value
    I2 = declare(fixed)  # for adaptive initialization
    Iarr = declare(fixed, size=readout_array_length)  # demod trace
    I_st = declare_stream()  # 1/0 stream
    Iarr_st = declare_stream()  # trace strea,
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with while_(n < N):  # repetition
        with for_(*from_array(f2, ifreqs_swap)):
            ################## 1.0 Let HDAWG play operation pulse #####
            ## Detuning pulse ##
            play("trigger", "Trigger5", duration=pulse_width)
            ramp_to_zero("Trigger5", 1)
            wait(75, qubit)

            # wait(t_delay, qubit)
            ## MW pulse for pi on Q1##
            update_frequency(qubit, if_start)
            reset_phase(qubit)
            play("pi", qubit)

            align("Trigger5", lockin_to_read)

            ################## 1.1 Readout  ####################################
            measure(
                "readout",
                lockin_to_read,
                None,
                integration.sliced("integ_weights_cos", Iarr, slice_size),
            )  # f_IF = 0 , demodulate the raw ADC data and save as an array

            with if_((Math.max(Iarr) - Math.min(Iarr)) > disc_thr_real):
                assign(I, 1)

            with else_():
                assign(I, 0)

            save(I, I_st)

            if save_trace == 1:
                with for_(it, 0, it < readout_array_length, it + 1):
                    save(Iarr[it], Iarr_st)
            #######################################################################

            ######################### 1.2 check initialization #################
            if adaptive_initialization == 1:
                measure(
                    "readout2",
                    lockin_to_read,
                    None,
                    integration.full("integ_weights_cos2", I2),
                )
                if reverse_singleshot == 1:
                    with while_(
                        (I2 - Math.max(Iarr) * slice_size_inv > disc_thr_real2)
                        & (m < 5000)
                    ):
                        measure(
                            "readout2",
                            lockin_to_read,
                            None,
                            integration.full("integ_weights_cos2", I2),
                        )
                        assign(m, m + 1)  # avoid infinite loop
                else:
                    with while_(
                        (I2 - Math.min(Iarr) * slice_size_inv > disc_thr_real2)
                        & (m < 5000)
                    ):
                        # with while_( (I2 > disc_thr_real2) & (m<2500) ):
                        measure(
                            "readout2",
                            lockin_to_read,
                            None,
                            integration.full("integ_weights_cos2", I2),
                        )
                        assign(m, m + 1)  # avoid infinite loop
                assign(m, 0)

            ## Detuning pulse ##
            play("trigger", "Trigger5", duration=pulse_width)
            ramp_to_zero("Trigger5", 1)
            wait(75, qubit)

            # align('Trigger5', lockin_to_read)

            ################## 1.1 Readout  ####################################
            measure(
                "readout",
                lockin_to_read,
                None,
                integration.sliced("integ_weights_cos", Iarr, slice_size),
            )  # f_IF = 0 , demodulate the raw ADC data and save as an array

            with if_((Math.max(Iarr) - Math.min(Iarr)) > disc_thr_real):
                assign(I, 1)

            with else_():
                assign(I, 0)

            # save(I, I_st)

            if save_trace == 1:
                with for_(it, 0, it < readout_array_length, it + 1):
                    save(Iarr[it], Iarr_st)
            #######################################################################

            ######################### 1.2 check initialization #################
            if adaptive_initialization == 1:
                measure(
                    "readout2",
                    lockin_to_read,
                    None,
                    integration.full("integ_weights_cos2", I2),
                )
                if reverse_singleshot == 1:
                    with while_(
                        (I2 - Math.max(Iarr) * slice_size_inv > disc_thr_real2)
                        & (m < 5000)
                    ):
                        measure(
                            "readout2",
                            lockin_to_read,
                            None,
                            integration.full("integ_weights_cos2", I2),
                        )
                        assign(m, m + 1)  # avoid infinite loop
                else:
                    with while_(
                        (I2 - Math.min(Iarr) * slice_size_inv > disc_thr_real2)
                        & (m < 5000)
                    ):
                        # with while_( (I2 > disc_thr_real2) & (m<2500) ):
                        measure(
                            "readout2",
                            lockin_to_read,
                            None,
                            integration.full("integ_weights_cos2", I2),
                        )
                        assign(m, m + 1)  # avoid infinite loop
                assign(m, 0)

        save(n, n_st)
        assign(n, n + 1)

    with stream_processing():
        # I_st.buffer(N, fswapnpoints).save('I')
        I_st.buffer(fswapnpoints).average().save("I")
        if save_trace == 1:
            Iarr_st.save_all("Iarr")
        n_st.save("iteration")


# %% Program 5.
######################################################################################
###############    The QUA program 5 : program for phase varing ramsey ###############
######################################################################################
with program() as phase_varying_Ramsey:
    f = declare(int)
    n = declare(int, value=0)  # average (repetition)
    m = declare(int, value=0)  # adaptive initialization
    l = declare(int, value=0)  # mw burst time sweep
    k = declare(int, value=0)  # mw burst time sweep
    a = declare(fixed, value=0.0)
    it = declare(int, value=0)  # to save readout array
    I = declare(fixed)  # 1/0 value
    I2 = declare(fixed)  # for adaptive initialization
    Iarr = declare(fixed, size=readout_array_length)  # demod trace
    I_st = declare_stream()  # 1/0 stream
    Iarr_st = declare_stream()  # trace strea,
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(k, 0, k < 100000 / 4, k + 1):
        play("trigger", "Trigger5", duration=pulse_width)
        ramp_to_zero("Trigger5", 1)
        wait(t_delay, qubit)
        play("pi", qubit)
        wait(wait_width)
    align()

    with while_(n < N):  # repetition
        update_frequency(qubit, if_start)
        with for_(*from_array(l, phase_list)):
            ################## 1.0 Let HDAWG play operation pulse #####
            ## Detuning pulse ##
            play("trigger", "Trigger5", duration=pulse_width)
            ramp_to_zero("Trigger5", 1)

            wait(t_delay, qubit)

            reset_phase(qubit)

            ## MW pulse for Ramsey##
            if Ramsey == 1:
                play("half_pi", qubit)
                wait(t_phase_varying, qubit)
                frame_rotation_2pi(l / 360, qubit)
                play("half_pi", qubit)
            elif Echo == 1:
                play("half_pi", qubit)
                wait(t_phase_varying2, qubit)
                play("pi", qubit)
                wait(t_phase_varying2, qubit)
                frame_rotation_2pi(l / 360, qubit)
                play("half_pi", qubit)

            align("Trigger5", lockin_to_read)

            ################## 1.1 Readout  ####################################
            measure(
                "readout",
                lockin_to_read,
                None,
                integration.sliced("integ_weights_cos", Iarr, slice_size),
            )  # f_IF = 0 , demodulate the raw ADC data and save as an array

            with if_((Math.max(Iarr) - Math.min(Iarr)) > disc_thr_real):
                assign(I, 1)

            with else_():
                assign(I, 0)

            save(I, I_st)

            if save_trace == 1:
                with for_(it, 0, it < readout_array_length, it + 1):
                    save(Iarr[it], Iarr_st)

            ######################### 1.2 check initialization #################
            if adaptive_initialization == 1:
                measure(
                    "readout2",
                    lockin_to_read,
                    None,
                    integration.full("integ_weights_cos2", I2),
                )
                if reverse_singleshot == 1:
                    with while_(
                        (I2 - Math.max(Iarr) * slice_size_inv > disc_thr_real2)
                        & (m < 5000)
                    ):
                        measure(
                            "readout2",
                            lockin_to_read,
                            None,
                            integration.full("integ_weights_cos2", I2),
                        )
                        assign(m, m + 1)  # avoid infinite loop
                else:
                    with while_(
                        (I2 - Math.min(Iarr) * slice_size_inv > disc_thr_real2)
                        & (m < 5000)
                    ):
                        # with while_( (I2 > disc_thr_real2) & (m<2500) ):
                        measure(
                            "readout2",
                            lockin_to_read,
                            None,
                            integration.full("integ_weights_cos2", I2),
                        )
                        assign(m, m + 1)  # avoid infinite loop
                assign(m, 0)
        save(n, n_st)
        assign(n, n + 1)

    with stream_processing():
        # I_st.buffer(N, fnpoints, n_phase).save('I')
        I_st.buffer(n_phase).average().save("I")
        if save_trace == 1:
            Iarr_st.save_all("Iarr")
        n_st.save("iteration")


# %%
######################################
# Open Communication with the Server #
######################################

#### OCTAVE SETUP ################################################
octave_config = QmOctaveConfig()
octave_config.set_calibration_db(os.getcwd())
octave_config.add_device_info("octave1", octave_ip, octave_port)
# octave_config.set_opx_octave_mapping([("con1", "octave1")])


# %%
def fit_function(
    x_values, y_values, function, init_params, min_param=None, max_param=None
):
    if (min_param is not None) and (max_param is not None):
        fitparams, conv = curve_fit(
            function, x_values, y_values, init_params, bounds=(min_param, max_param)
        )
    else:
        fitparams, conv = curve_fit(
            function, x_values, y_values, init_params, method="lm"
        )
    y_fit = function(x_values, *fitparams)

    return fitparams, y_fit


def RB_fit_function(x, A1, alpha, B1):
    return A1 * alpha**x + B1


# prog = Single_Spin

# %%

if shuttling_exchange == 1:
    print("amplitude_sweep_shuttling")
    prog = amplitude_shuttle
elif looping_pi_pulse == 1:
    print("infinite repetition of pi pulse")
    prog = inf_loop_pi_pulse
elif plot_1d_fre_sweep == 1:
    print("1D frequency sweep Program")
    prog = EDSR
elif plot_amplitude_varied_2d_plot == 1:
    print("amplitude sweep Program")
    prog = amplitude_sweep
elif plot_fre_vs_fre_2d_plot == 1:
    print("fre vs fre sweep Program")
    prog = exchange_dB_cal_fixed_amp
elif swap_freq_calibration == 1:
    print("swap_freq_1d_sweep")
    prog = swap_freq_1d_sweep

elif amp_Rabi == 1:
    print("amplitude sweep Rabi")
    prog = amplitude_Rabi
elif phase_Ramsey == 1:
    print("phase Ramsey")
    prog = phase_varying_Ramsey
else:
    print("Single Spin Program")
    prog = Single_Spin

for b in range(Nrep):
    ###################
    # Octave settings #
    ###################

    qmm = QuantumMachinesManager(host=opx_ip, port=opx_port, octave=octave_config)
    qmm.clear_all_job_results()
    qm = qmm.open_qm(config)

    qm.octave.set_clock(octave, clock_mode=ClockMode.Internal)
    qm.octave.set_lo_source(
        "qe1", OctaveLOSource.Internal
    )  # Use the internal synthetizer to generate the LO.
    qm.octave.set_lo_source(
        "qe2", OctaveLOSource.Internal
    )  # Use the internal synthetizer to generate the LO.
    qm.octave.set_lo_frequency("qe1", LO)  # assign the LO inside the octave to element
    qm.octave.set_lo_frequency("qe2", LO2)  # assign the LO inside the octave to element
    qm.octave.set_rf_output_gain(
        "qe1", octave_gain
    )  # can set the gain from -10dB to 20dB
    qm.octave.set_rf_output_gain(
        "qe2", octave_gain2
    )  # can set the gain from -10dB to 20dB
    qm.octave.set_rf_output_mode("qe1", RFOutputMode.trig_normal)
    qm.octave.set_rf_output_mode("qe2", RFOutputMode.trig_normal)

    # job = qm.execute(prog, flags=['not-strict-timing'])
    job = qm.execute(prog)

    res_handles = job.result_handles
    # res_handles.wait_for_all_values()
    # I_hand=res_handles.get('I')
    # I_hand.wait_for_values(1)

    fetching_mode = "live"
    results = fetching_tool(job, data_list=["I", "iteration"], mode=fetching_mode)

    fig, ax = plt.subplots(figsize=(8, 5))

    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        I_ave, iteration = results.fetch_all()
        progress_counter(iteration, N, start_time=results.get_start_time())
        # Plot results

        if plot_amplitude_varied_2d_plot == 1:
            plt.cla()
            pc = ax.pcolormesh(freqs, amp_list * 1e3, I_ave, cmap="viridis")
            # ax.pcolor(I_ave)
            # fig.colorbar(pc)
            current_values = ax.get_xticks()[1:-1]
            ax.set_xticks(current_values)
            ax.set_xticklabels([f"{v:.3f}" for v in current_values])
            ax.set_xlabel("Frequency(GHz)")
            ax.set_ylabel("Detuning(mV)")
        elif plot_fre_vs_fre_2d_plot == 1:
            plt.cla()
            pc = ax.pcolormesh(freqs, freqs2, I_ave, cmap="viridis")
            # ax.pcolor(I_ave)
            # fig.colorbar(pc)
            current_values = ax.get_xticks()[1:-1]
            ax.set_xticks(current_values)
            ax.set_xticklabels([f"{v:.3f}" for v in current_values])
            ax.set_xlabel("Frequency(GHz)")
            ax.set_ylabel("Frequency(GHz)")
        elif amp_Rabi == 1:
            I_ave = np.squeeze(I_ave)
            plt.cla()
            plt.plot(amp_list * step_amp, I_ave, "o-")
            ax.set_xlabel("mw amplitude")
            ax.set_ylabel("Probability")
            ax.annotate(
                f"{resonance_freq/1e9}GHz", xy=(0.8, 0.95), xycoords="axes fraction"
            )

        elif plot_1d_fre_sweep == 1:
            plt.cla()
            plt.plot(freqs, I_ave, "o-")
            plt.ylim([0, 1])
            ax.set_xlabel("frequency (GHz)")
            ax.set_ylabel("Probability")

        elif swap_freq_calibration == 1:
            plt.cla()
            plt.plot(freqs_swap, I_ave, "o-")
            plt.ylim([0, 1])
            ax.set_xlabel("frequency (MHz)")
            ax.set_ylabel("Probability")

        elif phase_Ramsey == 1:
            plt.cla()
            plt.plot(phase_list, I_ave, "o-")
            plt.ylim([0, 1])
            ax.set_xlabel("phase")
            ax.set_ylabel("Probability")
            ax.annotate(
                f"{resonance_freq/1e9}GHz\n{t_phase_varying/250}us",
                xy=(0.8, 0.95),
                xycoords="axes fraction",
            )

        elif plot_chevron == 1:
            x_tick = trange
            detune_list = freqs
            if n_rep2 == 1:
                # I_tmp = np.squeeze(I).copy()
                # I_ave = np.zeros(N//100)
                # for i in range(0, N, 100):
                #     I_ave[i//100] = sum(I_tmp[i:i+200])/200
                # print(I_ave.shape)
                # plt.plot(I_ave, 'o')

                # plt.plot(detune_list, I_ave)
                # plt.ylim([0,1])
                # current_values = ax.get_xticks()[1:-1]
                # ax.set_xticks(current_values)
                # ax.set_xticklabels([f'{v:.4f}' for v in current_values])
                # ax.set_xlabel('frequency(GHz)')
                # ax.set_ylabel('Probability')

                print(f"{b} iteration : {I_ave[0]}")
                # ax.annotate(f'thr = {disc_thr*1000}mV', xy=(0.75, 0.9), xycoords='axes fraction')

            elif fnpoints == 1:
                I_ave = np.squeeze(I_ave)
                plt.cla()
                plt.plot(x_tick, I_ave, "o-")
                ax.set_xlabel("MW burst time(ns)")
                ax.set_ylabel("Probability")
                plt.ylim([0, 1])
                ax.annotate(
                    f"{resonance_freq/1e9}GHz", xy=(0.1, 0.95), xycoords="axes fraction"
                )

            else:
                x, y = np.meshgrid(x_tick, detune_list)
                try:
                    cbar.remove()
                except:
                    pass
                plt.cla()
                if color_YlGnBu == 1:
                    pc = ax.pcolor(x, y, I_ave, cmap="YlGnBu_r")
                else:
                    pc = ax.pcolor(x, y, I_ave, cmap="viridis")
                cbar = plt.colorbar(mappable=pc, ax=ax)
                current_values = ax.get_yticks()[1:-1]
                ax.set_yticks(current_values)
                ax.ticklabel_format(useOffset=False)
                # ax.set_yticklabels([f'{v:.4f}' for v in current_values])
                ax.set_xlabel("time(ns)")
                ax.set_ylabel("frequency(GHz)")

        if not add_prob:
            ax.set_title(f"{date}_{qubit_to_play}_thr_{disc_thr*1000}mV")
            plt.show()

        plt.pause(2)

    # res_handles.wait_for_all_values()
    # I = res_handles.get("I").fetch_all()
    # job.halt()

    get_ipython().run_line_magic("matplotlib", "inline")

    ################## below is for saving data##################################

    if save_trace == 1:
        Iarr_st = res_handles.get("Iarr").fetch_all()
        N_num = 70
        if fnpoints == 1:
            freq = 0
            file_name = "_fres"
        else:
            freq = int(fnpoints / 2)
            file_name = "_2D"

        Iarr_ = Iarr_st.astype(
            np.float64
        )  # Convert the type to use the max / min function
        Iarr = (
            np.reshape(Iarr_, (N, fnpoints, n_rep2 * readout_array_length))
            * Iarr_weight
        )

        ## Define X-axis ##
        x_ = np.array(
            [
                t_unit2_fixed * (i / readout_array_length)
                for i in range(n_rep2 * readout_array_length)
            ]
        )

        ## 0/1 disc ##
        I_ = I.copy()
        y_ = np.zeros(len(x_))
        for i in range(n_rep2 * readout_array_length):
            y_[i] = disc_thr * I_[N_num][freq][i // readout_array_length]
        for i in range(n_rep2):
            y_[readout_array_length * i : readout_array_length * (i + 1)] = y_[
                readout_array_length * i : readout_array_length * (i + 1)
            ] + min(
                Iarr[N_num][freq][
                    readout_array_length * i : readout_array_length * (i + 1)
                ]
            )

        ## Text box Properties ##
        str_textBox = "Disc. Threshold : " + str(float(disc_thr))

        ## graph ##
        plt.plot(x_, Iarr[N_num][freq], x_, y_)

        plt.title(f"{date}")
        plt.xlabel("burst time (ns)")
        plt.ylabel("rf.demod (V)")
        plt.gcf().text(0.65, 0.9, str_textBox)

        ##### Parameters to save #############
        param = np.array(
            [
                ("integration time(s)", f"{slice_size*4e-9:e}"),
                ("readout time(s)", f"{readout_pulse_length*1e-9:e}"),
                ("threshold(V)", disc_thr),
                ("mw frequency(GHz)", f"{resonance_freq/1e9}"),
                ("mw burst time step(ns)", t_unit2_fixed),
                ("max burst time(us)", tmax / 1000),
            ]
        )

        path = Nas_path + f"/Data/{date[:4]}/{date[4:6]}/DATA_{date[4:6]}{date[6:8]}"
        os.makedirs(path, exist_ok=True)
        np.savez_compressed(
            f"{path}/{date}_measurement_trace" + file_name,
            parameter=param,
            Iarr=Iarr,
            I=I_,
        )

    ################## Below for plotting final averaged data ################

    if run_analysis == 1:
        header = ""
        # title=''
        # x_tick = np.array([(i+1)*t_unit2*4 + 16+ac_offset*4 for i in range(n_rep2)])
        ################

        ############below is for when one saves all the shot results without averaging #########
        if fetching_mode == "live":
            pass
        elif len(I.shape) == 1:
            I_ave = I
        elif plot_amplitude_varied_2d_plot == 1:
            I_ave = np.zeros((n_amp, fnpoints))
            for k in range(N):
                for i in range(n_amp):
                    for j in range(fnpoints):
                        I_ave[i, j] += I[k, i, j] / N
        elif plot_fre_vs_fre_2d_plot == 1:
            I_ave = np.zeros((fnpoints2, fnpoints))
            for k in range(N):
                for i in range(fnpoints2):
                    for j in range(fnpoints):
                        I_ave[i, j] += I[k, i, j] / N
        elif amp_Rabi == 1:
            I_ave = np.average(I, 0)
        elif phase_Ramsey == 1:
            I_ave = np.average(I, 0)
        elif plot_1d_fre_sweep == 1:
            I_ave = np.average(I, 0)
        elif swap_freq_calibration == 1:
            I_ave = np.average(I, 0)
        elif plot_chevron == 1:
            I_ave = np.zeros((fnpoints, n_rep2))
            for k in range(N):
                for i in range(fnpoints):
                    for j in range(n_rep2):
                        I_ave[i, j] += I[k, i, j] / N

        ############Now plotting the final result#####################

        if plot_amplitude_varied_2d_plot == 1:
            fig, ax = plt.subplots(figsize=(5, 7))
            pc = ax.pcolormesh(freqs, amp_list * 1e3, I_ave, cmap="viridis")
            # ax.pcolor(I_ave)
            fig.colorbar(pc)
            current_values = ax.get_xticks()[1:-1]
            ax.set_xticks(current_values)
            ax.set_xticklabels([f"{v:.3f}" for v in current_values])
            ax.set_xlabel("Frequency(GHz)")
            ax.set_ylabel("Detuning(mV)")
        elif plot_fre_vs_fre_2d_plot == 1:
            fig, ax = plt.subplots(figsize=(5, 7))
            pc = ax.pcolormesh(freqs, freqs2, I_ave, cmap="viridis")
            # ax.pcolor(I_ave)
            fig.colorbar(pc)
            current_values = ax.get_xticks()[1:-1]
            ax.set_xticks(current_values)
            ax.set_xticklabels([f"{v:.3f}" for v in current_values])
            ax.set_xlabel("Frequency(GHz)")
            ax.set_ylabel("Frequency(GHz)")
        elif amp_Rabi == 1:
            fig, ax = plt.subplots(figsize=(7, 5))
            I_ave = np.squeeze(I_ave)
            plt.plot(amp_list * step_amp, I_ave, "o-")
            ax.set_xlabel("mw amplitude")
            ax.set_ylabel("Probability")
            ax.annotate(
                f"{resonance_freq/1e9}GHz", xy=(0.8, 0.95), xycoords="axes fraction"
            )
            header = f"(x)=(amplitude)\n f=({freqs[0]}) GHz\n time=({pi_len1}) ns\n amp=({amp_start}, {amp_step}, {amp_max})"

        elif plot_1d_fre_sweep == 1:
            fig, ax = plt.subplots(figsize=(7, 5))
            I_ave = np.squeeze(I_ave)
            if do_fit == 1:
                try:
                    fit_params, y_fit = fit_function(
                        freqs,
                        I_ave,
                        lambda x, A, fr, sigma, B: (
                            A * np.exp(-(((x - fr) / sigma) ** 2)) + B
                        ),
                        [initial_A, initial_fr, initial_sigma, initial_offset],
                    )
                    print(f"fr = {fit_params[1]:.5f} GHz")
                    plt.plot(freqs, I_ave, "o", markersize=3)
                    plt.plot(freqs, y_fit, "b", linewidth=3, alpha=0.4)
                    plt.legend(["exp.", "fit function"], loc="lower left")
                    plt.ylim([0, 1])
                except RuntimeError:
                    print("Curve Fit RuntimeError")
                    plt.plot(freq, I_ave, "o-")
                    plt.ylim([0, 1])
            else:
                plt.plot(freqs, I_ave, "o-")
                plt.ylim([0, 1])
            ax.set_xlabel("frequency (GHz)")
            ax.set_ylabel("Probability")

        elif swap_freq_calibration == 1:
            fig, ax = plt.subplots(figsize=(7, 5))
            I_ave = np.squeeze(I_ave)
            plt.plot(freqs_swap, I_ave, "o-")
            plt.ylim([0, 1])
            ax.set_xlabel("frequency (MHz)")
            ax.set_ylabel("Probability")

        elif phase_Ramsey == 1:
            fig, ax = plt.subplots(figsize=(7, 5))
            I_ave = np.squeeze(I_ave)
            visib = round(np.max(I_ave) - np.min(I_ave), 3)
            if do_fit == 1:
                try:
                    fit_params, y_fit = fit_function(
                        phase_list,
                        I_ave,
                        lambda x, A, phi, B: (
                            A * np.sin(2 * np.pi * x / 360 + phi) + B
                        ),
                        [initial_A, initial_phase, initial_offset],
                    )
                    print(
                        f"visability = {2*abs(fit_params[0])}, phi = {fit_params[1]} rad, offset={fit_params[2]}"
                    )
                    header = f"visability = {2*abs(fit_params[0])}, phi = {fit_params[1]} rad, offset={fit_params[2]}"
                    plt.plot(phase_list, I_ave, "o", markersize=3)
                    plt.plot(phase_list, y_fit, "b", linewidth=3, alpha=0.4)
                    plt.legend(["exp.", "fit function"], loc="lower left")
                    plt.ylim([0, 1])
                except RuntimeError:
                    print("Curve Fit RuntimeError")
                    plt.plot(phase_list, I_ave, "o-")
                    plt.ylim([0, 1])
            else:
                plt.plot(phase_list, I_ave, "o-")
                plt.ylim([0, 1])
            ax.set_xlabel("phase")
            ax.set_ylabel("Probability")
            ax.annotate(
                f"{resonance_freq/1e9}GHz \nTau={t_phase_varying/250}us \nvisibility={2*abs(fit_params[0])}",
                xy=(0.7, 0.85),
                xycoords="axes fraction",
            )
            header = (
                header
                + f"(x)=(time)\n f=({freqs[0]}) GHz\n time=(0, {t_unit2_fixed}, {tmax}) ns"
            )
            # title = f'5t_Rabi'
        elif plot_chevron == 1:
            if not add_prob:
                fig, ax = plt.subplots(figsize=(7, 5))
            x_tick = trange
            detune_list = freqs
            if n_rep2 == 1:
                # I_tmp = np.squeeze(I).copy()
                # I_ave = np.zeros(N//100)
                # for i in range(0, N, 100):
                #     I_ave[i//100] = sum(I_tmp[i:i+200])/200
                # print(I_ave.shape)
                # plt.plot(I_ave, 'o')

                # plt.plot(detune_list, I_ave)
                # plt.ylim([0,1])
                # current_values = ax.get_xticks()[1:-1]
                # ax.set_xticks(current_values)
                # ax.set_xticklabels([f'{v:.4f}' for v in current_values])
                # ax.set_xlabel('frequency(GHz)')
                # ax.set_ylabel('Probability')

                print(f"{b} iteration : {I_ave[0]}")
                # ax.annotate(f'thr = {disc_thr*1000}mV', xy=(0.75, 0.9), xycoords='axes fraction')
                if fnpoints == 1:
                    header = f'f=({freqs[0]}) GHz\n pi time=({config["pulses"]["pi_pulse"+qubit[-1]]["length"]}) ns'
            elif fnpoints == 1:
                I_ave = np.squeeze(I_ave)
                if do_fit == 1:
                    try:
                        fit_params, y_fit = fit_function(
                            x_tick[1:] * 1e-9,
                            I_ave[1:],
                            # lambda x, A, T2, f_rabi, phi, B: (A*np.exp(-(x/T2)**2)*np.sin(2*np.pi*f_rabi*x + phi/180*np.pi) + B),
                            lambda x, A, T2, f_rabi, phi, B: (
                                A
                                * np.exp(-((x / T2) ** 1))
                                * np.sin(2 * np.pi * f_rabi * x + phi / 180 * np.pi)
                                + B
                            ),
                            [
                                initial_A,
                                initial_decay_guess,
                                initial_rabi_guess,
                                initial_phase,
                                initial_offset,
                            ],
                        )
                        print(
                            f"visibility = {abs(2*fit_params[0])}, T2 = {fit_params[1]:.3e} s, f_rabi={fit_params[2]:.3e} Hz"
                        )
                        header = f"visibility = {abs(2*fit_params[0])}, T2 = {fit_params[1]:.3e} s, f_rabi={fit_params[2]:.3e} Hz"
                        plt.plot(x_tick, I_ave, "o", markersize=3)
                        plt.plot(x_tick[1:], y_fit, "b", linewidth=3, alpha=0.4)
                        plt.legend(["exp.", "fit function"])
                    except RuntimeError:
                        print("Curve Fit RuntimeError")
                        plt.plot(x_tick, I_ave, "o-")
                else:
                    plt.plot(x_tick, I_ave)
                ax.set_xlabel("MW burst time(ns)")
                ax.set_ylabel("Probability")
                plt.ylim([0, 1])
                ax.annotate(
                    f"{resonance_freq/1e9}GHz", xy=(0.1, 0.95), xycoords="axes fraction"
                )
                header = (
                    header
                    + f"(x)=(time)\n f=({freqs[0]}) GHz\n time=(0, {t_unit2_fixed}, {tmax}) ns"
                )
                # title = f'5t_Rabi'
            else:
                x, y = np.meshgrid(x_tick, detune_list)
                if color_YlGnBu == 1:
                    pc = ax.pcolor(x, y, I_ave, cmap="YlGnBu_r")
                else:
                    pc = ax.pcolor(x, y, I_ave, cmap="viridis")
                fig.colorbar(pc)
                current_values = ax.get_yticks()[1:-1]
                ax.set_yticks(current_values)
                ax.ticklabel_format(useOffset=False)
                # ax.set_yticklabels([f'{v:.4f}' for v in current_values])
                ax.set_xlabel("time(ns)")
                ax.set_ylabel("frequency(GHz)")
                header = f"(xy)=(time freq)\n f=({freqs[0]}~{freqs[-1]}) GHz\n time=(0~{tmax}) ns"

        if not add_prob:
            ax.set_title(f"{date}_{qubit_to_play}_thr_{disc_thr*1000}mV")
            plt.show()

        if save_data == 1:
            if not add_prob:
                np.savetxt(
                    f"{my_path}/data/{date}_{qubit_to_play}_thr_{disc_thr*1000}mV{title}.csv",
                    I_ave,
                    delimiter=",",
                    header=header,
                )

            if zero_one_data == 1:
                if len(np.squeeze(I).shape) > 2:
                    np.save(
                        f"{my_path}/data/{date}_{qubit_to_play}_thr_{disc_thr*1000}mV_zero_one_data{title}.npy",
                        I,
                    )
                else:
                    np.savetxt(
                        f"{my_path}/data/{date}_{qubit_to_play}_thr_{disc_thr*1000}mV_zero_one_data{title}.csv",
                        np.squeeze(I),
                        delimiter=",",
                        header=header,
                    )
        if save_fig == 1:
            # fig.canvas.draw()
            # image = np.array(fig.canvas.renderer._renderer)
            # plt.imsave(fname=f'{Nas_path}/Figure/{date}.pdf', arr=I_ave, cmap='YlGnBu_r', format='pdf' )
            plt.savefig(f"{Nas_path}/Figure/{date}.pdf", dpi=300, transparent=True)

    if add_prob:
        if date_update:
            date2 = copy.deepcopy(date)
            date_update = False
        add_path = f"{my_path}/data/{date2}_{qubit_to_play}_thr_{disc_thr*1000}mV{title}_probs.csv"
        add_data_to_csv(add_path, I_ave[0])

    time.sleep(5)

############################################################################################################
# %%
load_plot = False


def import_data_from_csv(x, y, file_path):
    data = np.loadtxt(file_path, delimiter=",")
    print(data.shape)

    fig, ax = plt.subplots(figsize=(7, 5))
    pc = ax.pcolormesh(x, y, data)
    fig.colorbar(pc)
    current_values = ax.get_yticks()[1:-1]
    ax.set_yticks(current_values)
    ax.set_yticklabels([f"{v:.4f}" for v in current_values])
    ax.set_xlabel("time(s)")
    ax.set_ylabel("frequency(GHz)")
    ax.set_title(f"M8195A_{qubit_to_play}_thr_{disc_thr*1000}mV_{m8195a_plot_num}")
    fig.show()
    return data


if load_plot:
    import_data_from_csv(
        np.arange(0, 1.5e-6 + 60e-9 / 2, 60e-9), np.linspace(22.25, 22.26, 21), add_path
    )
