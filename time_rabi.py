import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.loops import from_array
from OPX1000config_transmons import config, qubit_keys, qubit_absfreq, qubit_LO, qubit_IFs, resonator_keys, resonator_absfreq, resonator_LO, resonator_IFs
from qm_saas import QmSaas, QOPVersion
from qm import SimulationConfig
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import savgol_filter
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)

# ---- Multiplexed program parameters ----
n_avg = 8
multiplexed = True
qub_relaxation = 1600//4 # From ns to clock cycles
res_relaxation = 1600//4 # From ns to clock cycles

# ---- Time Rabi Multiplexed ---- #
qubit_subset_indices = [0, 1, 3]
qub_key_subset = [qubit_keys[i] for i in qubit_subset_indices]
res_key_subset = [resonator_keys[i] for i in qubit_subset_indices]

pulse_duration_min = 20 # ns 
pulse_duration_max = 800 # ns 
pulse_duration_dns = 40 # ns 
pulse_durations_ns = np.arange(pulse_duration_min, pulse_duration_max + pulse_duration_dns, pulse_duration_dns) 
pulse_durations_cycles = pulse_durations_ns // 4 # Converted to clock cycles 

pulse_amp_min = 0.1 # ratio of max amplitude 
pulse_amp_max = 1.0 # ratio of max amplitude 
pulse_amp_damp = 0.1 # step in ratio of max amplitude 
pulse_amps = np.arange(pulse_amp_min, pulse_amp_max + pulse_amp_damp, pulse_amp_damp) 

with program() as time_rabi_multiplexed:
    pd = declare(int)
    i = declare(int)
    I = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(i, 0, i < n_avg, i + 1):
        with for_(*from_array(pd, pulse_durations_cycles)):
            for j in range(len(qub_key_subset)): # a real Python for loop so it unravels and executes in parallel, not sequentially
                play(
                    "x180", 
                    qub_key_subset[j], 
                    duration=pd
                )
                align(qub_key_subset[j], res_key_subset[j]) # Make sure the readout occurs after the pulse to qubit
                measure(
                    "readout",
                    res_key_subset[j],
                    None, # Warning vs Error depending on version, I'm keeping it
                    dual_demod.full("cos", "sin", I[j]),
                    dual_demod.full("minus_sin", "cos", Q[j])
                )
                save(I[j], I_st[j])
                save(Q[j], Q_st[j])
                if multiplexed:
                    wait(res_relaxation, res_key_subset[j])
                    wait(qub_relaxation, qub_key_subset[j]) 
                else:
                    align() # When python unravels, this makes sure the readouts are sequential
                    if j == len(res_key_subset)-1:
                        wait(res_relaxation, *res_key_subset) # after last resonator, we wait for relaxation
                        wait(qub_relaxation, *qub_key_subset)
    with stream_processing():
        for j in range(len(qub_key_subset)):
            I_st[j].buffer(len(pulse_durations_cycles)).average().save("I_"+str(j))
            Q_st[j].buffer(len(pulse_durations_cycles)).average().save("Q_"+str(j))