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


f_start = 1e6
f_end = 4e8
n_segs = 40
dt = pulse_duration / n_segs

a = (f_end - f_start) / (pulse_duration) ** 2

time_vec = dt * np.array(range(n_segs + 1))
freq_vec = a * time_vec**2 + f_start
rates = (np.diff(freq_vec) / (pulse_duration / n_segs)).astype(int).tolist()
units = "Hz/nsec"
with program() as prog:
    for i in range(n_tweezers):
        col_sel = f"col_selector_{i + 1:02d}"
        update_frequency(col_sel, f_start + i * 10e6)
        play("const", col_sel, chirp=(rates, units))

job = qmm.simulate(config, prog, SimulationConfig(int(pulse_duration // 4)))  # in clock cycles, 4 ns

samples = job.get_simulated_samples()

x = samples.con1.analog["1"]
NFFT = 2**10
Fs = 1e9
plt.figure()
ax1 = plt.subplot(111)
Pxx, freqs, bins, im = plt.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=1000, cmap=plt.cm.gist_heat)
ax1.set_xticklabels((ax1.get_xticks() * 1e6).astype(int))
ax1.set_yticklabels((ax1.get_yticks() / 1e6).astype(int))
plt.title("Quadratic Chirp")
plt.xlabel("t [us]")
plt.ylabel("f [MHz]")
plt.show()

# %%
