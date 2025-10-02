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

# ---- T1 ---- #
qubit_subset_indices = [0, 1, 3]
qub_key_subset = [qubit_keys[i] for i in qubit_subset_indices]
res_key_subset = [resonator_keys[i] for i in qubit_subset_indices]

tau_min = 0 # ns
tau_max = 16000 # ns
dtau = 64 # ns
taus_ns = np.arange(tau_min, tau_max + dtau, dtau)
taus_cycles = taus_ns // 4 # Converted to clock cycles
taus_effective_ns = taus_ns + 16 # accounting for the 4 cycles of align (there is probably more, but I'll test later)

with program() as measure_T1:
    i = declare(int)
    tau = declare(int)
    I = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(i, 0, i < n_avg, i + 1):
        with for_(*from_array(tau, taus_cycles)):
            for j in range(len(qub_key_subset)): # a real Python for loop so it unravels and executes in parallel, not sequentially
                with if_(tau >= 4):
                    play(
                        "x180", 
                        qub_key_subset[j], 
                    )
                    wait(tau, qub_key_subset[j])
                with else_():
                    play(
                        "x180", 
                        qub_key_subset[j], 
                    )
                align(qub_key_subset[j], res_key_subset[j]) 
                measure(
                    "readout",
                    res_key_subset[j],
                    None, # Warning vs Error depending on version, I'm keeping it
                    dual_demod.full("rotated_cos", "rotated_sin", I[j]),
                    dual_demod.full("rotated_minus_sin", "rotated_cos", Q[j])
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
            I_st[j].buffer(len(taus_cycles)).average().save("I_"+str(j))
            Q_st[j].buffer(len(taus_cycles)).average().save("Q_"+str(j))