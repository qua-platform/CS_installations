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

# ---- IQ blobs ---- #
qubit_subset_indices = [0, 1, 3]
qub_key_subset = [qubit_keys[i] for i in qubit_subset_indices]
res_key_subset = [resonator_keys[i] for i in qubit_subset_indices]

with program() as IQ_blobs:
    pd = declare(int)
    i = declare(int)
    I_g = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q_g = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    I_e = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q_e = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_e_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_e_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(i, 0, i < n_avg, i + 1):
        for j in range(len(qub_key_subset)): # a real Python for loop so it unravels and executes in parallel, not sequentially
            measure(
                "readout",
                res_key_subset[j],
                None, # Warning vs Error depending on version, I'm keeping it
                dual_demod.full("cos", "sin", I_g[j]),
                dual_demod.full("minus_sin", "cos", Q_g[j])
            )
            save(I_g[j], I_g_st[j])
            save(Q_g[j], Q_g_st[j])
            align(res_key_subset[j], qub_key_subset[j]) # Make sure the readout occurs after the pulse to qubit
            wait(qub_relaxation, qub_key_subset[j]) 
            wait(res_relaxation, res_key_subset[j])
            align(res_key_subset[j], qub_key_subset[j]) # Make sure the readout occurs after the pulse to qubit
            play(
                "x180", 
                qub_key_subset[j],
            )
            align(qub_key_subset[j], res_key_subset[j]) # Make sure the readout occurs after the pulse to qubit
            measure(
                "readout",
                res_key_subset[j],
                None, # Warning vs Error depending on version, I'm keeping it
                dual_demod.full("cos", "sin", I_e[j]),
                dual_demod.full("minus_sin", "cos", Q_e[j])
            )
            save(I_e[j], I_e_st[j])
            save(Q_e[j], Q_e_st[j])
            if multiplexed:
                wait(res_relaxation, res_key_subset[j])
                wait(qub_relaxation, qub_key_subset[j]) 
            else:
                align(res_key_subset[j], res_key_subset[(j+1)%len(res_key_subset)]) # When python unravels, this makes sure the readouts are sequential
                if j == len(res_key_subset)-1:
                    wait(res_relaxation, *res_key_subset) # after last resonator, we wait for relaxation
                    wait(qub_relaxation, *qub_key_subset)
    with stream_processing():
        for j in range(len(qub_key_subset)):
            I_g_st[j].save_all("I_g"+str(j))
            Q_g_st[j].save_all("Q_g"+str(j))
            I_e_st[j].save_all("I_e"+str(j))
            Q_e_st[j].save_all("Q_e"+str(j))