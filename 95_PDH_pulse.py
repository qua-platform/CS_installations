# %%
"""
Drives CW for test
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_MWFEM import *
import matplotlib.pyplot as plt

###################
# The QUA program #
###################


def play_pdh_pulse(a=1.0):
    play("pdh_carrier" * amp(a), "resonator")
    play("pdh_modulation" * amp(a), "resonator_sb_high")
    play("pdh_modulation" * amp(a), "resonator_sb_low")


with program() as hello_qua:
    with infinite_loop_():
        play_pdh_pulse(1)

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)


###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=200)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, hello_qua, simulation_config)
    # Plot the simulated samples
    samples = job.get_simulated_samples()
    samples.con1.plot()
    plt.show()

    # Plot the spectrogram
    x = samples.con1.analog[f"1-{resonator_port}-1"].real
    NFFT = 2**10
    Fs = 1e9
    ax1 = plt.subplot(111)
    Pxx, freqs, bins, im = ax1.specgram(
        x, NFFT=NFFT, Fs=Fs, noverlap=100, cmap=plt.cm.gist_heat
    )
    xticks = ax1.get_xticks()
    ax1.set_xticks(xticks)
    ax1.set_xticklabels([f"{int(tick * 1e9)}" for tick in xticks])
    ytick_vals = ax1.get_yticks()
    ax1.set_yticks(ytick_vals)
    ax1.set_yticklabels((ytick_vals / 1e6).astype(int))
    plt.xlabel("t [ns]")
    plt.ylabel("IF [MHz]")
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)

# %%
