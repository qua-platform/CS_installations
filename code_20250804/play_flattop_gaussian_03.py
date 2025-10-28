# %%
"""
     XYZ
"""

from copy import deepcopy
from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_mw_fem import *
from qualang_tools.results import fetching_tool
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler
import matplotlib

matplotlib.use('TkAgg')

##################
#   Parameters   #
##################

qb1 = "q1_xy"
qb2 = f"{qb1}_twin"
n_avg = 3  # The number of averages

flattop_durations = np.arange(16, 80, 16)
relative_phases = 2 * np.pi * np.arange(0.0, 1.1, 0.15)
cos_py = np.cos(relative_phases).tolist()
sin_py = np.sin(relative_phases).tolist()

print("Number of flattop_durations is", len(flattop_durations))

save_data_dict = {
    "qubit": qb1,
    "flattop_durations": flattop_durations,
    "n_avg": n_avg,
    "config": config,
}


###################
#   QUA Program   #
###################

use_twin = True
a_py = 0.5

with program() as PROGRAM:
    n = declare(int)  # QUA variable for the averaging loop
    i = declare(int)
    t = declare(int)  # QUA variable for the readout frequency --> Hz int 32 up to 2^32
    cos = declare(fixed)
    sin = declare(fixed)

    update_frequency(qb1, 0)
    update_frequency(qb2, 0)
    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_(*from_array(t, flattop_durations)):  # QUA for_ loop for sweeping the frequency
            with for_each_((cos, sin), (cos_py, sin_py)):
                play("rise" * amp(cos, -sin, sin, cos), qb1)
                wait(4, qb2)

                play("flattop" * amp(cos, -sin, sin, cos), qb2, duration=t)
                wait(t - 2, qb1) # -2 to avoid gap

                play("fall" * amp(cos, -sin, sin, cos), qb1)

                wait(20)
            play("const", "q2_xy")
            wait(40)

if __name__ == "__main__":

    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)
    qmm.close_all_qms()

    ###########################
    # Run or Simulate Program #
    ###########################

    simulate = True

    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=1200)  # In clock cycles = 4ns
        # Simulate blocks python until the simulation is done
        
        job = qmm.simulate(config, PROGRAM, simulation_config)
        # Plot the simulated samples
        job.get_simulated_samples().con1.plot()
        plt.show()

    else:
        from qm import generate_qua_script
        sourceFile = open('debug.py', 'w')
        print(generate_qua_script(PROGRAM, config), file=sourceFile) 
        sourceFile.close()

        # Open a quantum machine to execute the QUA program
        qm = qmm.open_qm(config)

        # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
        job = qm.execute(PROGRAM)

# %%