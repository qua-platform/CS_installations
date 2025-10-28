# %%
"""
     XYZ
"""

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_lf_fem import *
from qualang_tools.results import fetching_tool
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler
import matplotlib

matplotlib.use('TkAgg')

##################
#   Parameters   #
##################

n_avg = 3  # The number of averages
rrs1 = RL_CONSTANTS["rl1"]["RESONATORS"]
rrs2 = RL_CONSTANTS["rl2"]["RESONATORS"]

save_data_dict = {
    "n_avg": n_avg,
    "config": config,
}


###################
#   QUA Program   #
###################

with program() as PROGRAM:
    n = declare(int)  # QUA variable for the averaging loop

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        for rr in rrs1:
            play("readout", rr)
        align()
        for rr in rrs2:
            play("readout", rr)
        # wait(40)


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
        res = job.get_simulated_samples()
        res.con1.plot()
        fig2 = plt.figure()
        for p in ["5-1", "5-2"]:
            samples = res.con1.analog[p]
            fft_freq = np.fft.fftfreq(len(samples))
            fft = np.abs(np.fft.fft(samples) - samples.mean())
            plt.plot(fft_freq, fft)
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