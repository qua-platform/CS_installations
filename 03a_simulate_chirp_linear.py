# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import numpy as np
import matplotlib.pyplot as plt
from configuration import *

qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)


pulse_duration = 4e5
config["pulses"]["const_pulse"]["length"] = pulse_duration

rate = int(3e8 / pulse_duration)
units = "Hz/nsec"
with program() as prog:
    for i in range(n_tweezers):
        col_sel = f"col_selector_{i + 1:02d}"
        if_start = config["elements"][col_sel]["intermediate_frequency"]
        update_frequency(col_sel, if_start + i * 10e6)
        play("const", col_sel, chirp=(rate, units))

job = qmm.simulate(config, prog, SimulationConfig(int(pulse_duration // 4)))  # in clock cycles, 4 ns

samples = job.get_simulated_samples()
x = samples.con1.analog["1"]
NFFT = 2**10
Fs = 1e9
ax1 = plt.subplot(111)
Pxx, freqs, bins, im = plt.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=100, cmap=plt.cm.gist_heat)
plt.show()
ax1.set_xticklabels((ax1.get_xticks() * 1e6).astype(int))
ax1.set_yticklabels((ax1.get_yticks() / 1e6).astype(int))
plt.xlabel("t [us]")
plt.ylabel("f [MHz]")

# %%
