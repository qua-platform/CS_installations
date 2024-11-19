# %%

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from typing import List
from configuration import *
import matplotlib.pyplot as plt


def play_gauss_rise_segments(
    ts_segments: List[int],
    duration_in_ms: int = 100,
):
    scaling_ratio = (duration_in_ms * u.ms) // (gauss_rise_fall_len_ns * u.ns)
    if num_gauss_rise_fall_wf_segments % 2 == 0:
        elems = ["cooling_fm_even_segment", "cooling_fm_odd_segment"] * (num_gauss_rise_fall_wf_segments // 2)
    if num_gauss_rise_fall_wf_segments % 2 == 1:
        elems = ["cooling_fm_even_segment", "cooling_fm_odd_segment"] * (num_gauss_rise_fall_wf_segments // 2) + ["cooling_fm_even_segment"]

    for s, (elem, _ts) in enumerate(zip(elems, ts_segments)):
        # print(len(_ts), _ts[0], _ts[-1])
        play(f"gauss_rise_{s:02d}", elem, duration=(len(_ts) * scaling_ratio) * u.ns)
        align("cooling_fm_even_segment", "cooling_fm_odd_segment")
        


###################
# The QUA program #
###################
with program() as PROGRAM:
    n = declare(int)

    play_gauss_rise_segments(ts_segments=gauss_rise_ts_segments, duration_in_ms=100)
    # with for_(n, 0, n < 2, n + 1):
    #     play("gauss_rise_00", "cooling_fm_even")
    #     play("gauss_rise_01", "cooling_fm_odd")

    #     wait(4 * u.s)


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)


###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROGRAM, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(PROGRAM)

# %%
