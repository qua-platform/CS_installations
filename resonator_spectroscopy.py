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

# ---- Resonator Spectroscopy ---- #
resonator_guesses = resonator_absfreq # np.array([4.7, 4.9, 5.1, 5.2]) * u.GHz
resonator_subset_indices = [0, 1, 3]

# Get the subset of resonator keys and corresponding guesses
res_key_subset = [resonator_keys[i] for i in resonator_subset_indices]
res_guesses_subset = resonator_guesses[resonator_subset_indices]

res_IF_guesses = res_guesses_subset - resonator_LO
res_spec_span = 80 * u.MHz
res_spec_df = 5 * u.MHz
res_spec_sweep_dfs = np.arange(-res_spec_span, res_spec_span + res_spec_df, res_spec_df)
res_spec_frequencies = np.array([res_spec_sweep_dfs + guess for guess in res_guesses_subset])


with program() as res_spec_multiplexed:
    i = declare(int)
    df = declare(int)
    I = [declare(fixed) for _ in range(len(res_key_subset))]
    Q = [declare(fixed) for _ in range(len(res_key_subset))]
    I_st = [declare_stream() for _ in range(len(res_key_subset))]
    Q_st = [declare_stream() for _ in range(len(res_key_subset))]

    with for_(i, 0, i < n_avg, i + 1):
        with for_(*from_array(df, res_spec_sweep_dfs)):
            for j in range(len(res_key_subset)): # A Python for loop so it unravels and executes in parallel, not sequentially
                update_frequency(res_key_subset[j], df + res_IF_guesses[j])
                measure(
                    "readout",
                    res_key_subset[j],
                    None,
                    dual_demod.full("cos", "sin", I[j]),
                    dual_demod.full("minus_sin", "cos", Q[j])
                )
                save(I[j], I_st[j])
                save(Q[j], Q_st[j])
                if multiplexed:
                    wait(res_relaxation, res_key_subset[j])
                else:
                    align() # When python unravels, this makes sure the readouts are sequential (switch to global)
                    if j == len(res_key_subset)-1:
                        wait(res_relaxation) # Wait for the last resonator to relax before starting the next avg
    with stream_processing():
        for j in range(len(res_key_subset)):
            I_st[j].buffer(len(res_spec_sweep_dfs)).average().save("I_"+str(j))
            Q_st[j].buffer(len(res_spec_sweep_dfs)).average().save("Q_"+str(j))