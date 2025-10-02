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

# ---- Time Rabi Chevron Multiplexed ---- #
qubit_freqs = qubit_absfreq # np.array([4.7, 4.9, 5.1, 5.2]) * u.GHz
qubit_subset_indices = [0, 1]
qub_key_subset = [qubit_keys[i] for i in qubit_subset_indices]
qub_freq_subset = qubit_freqs[qubit_subset_indices]
res_key_subset = [resonator_keys[i] for i in qubit_subset_indices]

qub_IFs = qub_freq_subset - qubit_LO
qub_spec_span = 20 * u.MHz
qub_spec_df = 2 * u.MHz
qub_spec_sweep_dfs = np.arange(-qub_spec_span, qub_spec_span + qub_spec_df, qub_spec_df)
qub_spec_frequencies = np.array([qub_spec_sweep_dfs + guess for guess in qub_freq_subset])

pulse_duration_min = 20 # ns 
pulse_duration_max = 800 # ns 
pulse_duration_dns = 40 # ns 
pulse_durations_ns = np.arange(pulse_duration_min, pulse_duration_max + pulse_duration_dns, pulse_duration_dns) 
pulse_durations_cycles = pulse_durations_ns // 4 # Converted to clock cycles 

with program() as time_rabi_chevron_multiplexed:
    i = declare(int)
    pd = declare(int)
    df = declare(int)
    I = [declare(fixed) for _ in range(resonator_guesses.shape[0])]
    Q = [declare(fixed) for _ in range(resonator_guesses.shape[0])]
    I_st = [declare_stream() for _ in range(resonator_guesses.shape[0])]
    Q_st = [declare_stream() for _ in range(resonator_guesses.shape[0])]

    with for_(i, 0, i < n_avg, i + 1):
        with for_(*from_array(pd, pulse_durations_cycles)):
            with for_(*from_array(df, qub_spec_sweep_dfs)):
                for j in range(len(qub_key_subset)): # a real Python for loop so it unravels and executes in parallel, not sequentially
                    update_frequency(qub_key_subset[j], df + qub_IFs[j])
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
            I_st[j].buffer(len(qub_spec_sweep_dfs)).buffer(len(pulse_durations_cycles)).average().save("I_"+str(j))
            Q_st[j].buffer(len(qub_spec_sweep_dfs)).buffer(len(pulse_durations_cycles)).average().save("Q_"+str(j))