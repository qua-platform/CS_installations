# %%
from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_7qb import *

###################
# The QUA program #
###################

resonators = [key for key in RR_CONSTANTS.keys() if 'twin' not in key]

with program() as hello_qua:
    
    with infinite_loop_():

        for rr_key in ['q1_rr', 'q3_rr']:
            play("cw", rr_key)

        for qubit_key in QUBIT_CONSTANTS.keys():
            play("cw", qubit_key)

        for flux_key in FLUX_CONSTANTS.keys():
            play("unipolar", flux_key)

        wait(100)
        
# %%
        
if __name__ == "__main__":
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
        
        job = qmm.simulate(config, hello_qua, simulation_config)
        # Plot the simulated samples
        job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
    else:
        # Open a quantum machine to execute the QUA program
        qm = qmm.open_qm(config)

        # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
        job = qm.execute(hello_qua)

# %%
