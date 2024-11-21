# %%

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from typing import List, Literal
from configuration import *
import matplotlib.pyplot as plt


def play_gauss_segments(
    ts_segments: List[int],
    duration_scaling_ratio: int,
    rise_fall: Literal["rise", "fall"],
):
    for s, _ts in enumerate(ts_segments):
        duration_ns = len(_ts) * duration_scaling_ratio
        play(f"gauss_{rise_fall}_{s:02d}", "cooling_fm", duration=duration_ns * u.ns)
        wait(4)

###################
# The QUA program #
###################
with program() as PROGRAM:

    # play the long sequence
    play_gauss_segments(
        ts_segments=gauss_rise_ts_segments,
        duration_scaling_ratio=100_000,
        rise_fall="rise",
    )
    
    # wait(100 * u.ms)
    
    # play_gauss_segments(
    #     ts_segments=gauss_rise_ts_segments,
    #     duration_scaling_ratio=100_000,
    #     rise_fall="fall",
    # )


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
    # from qm import generate_qua_script
    # sourceFile = open('debug.py', 'w')
    # print(generate_qua_script(PROGRAM, config), file=sourceFile) 
    # sourceFile.close()
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(PROGRAM)

# %%
