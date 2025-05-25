# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_mw_fem import *

##################
#   Parameters   #
##################

###################
#   QUA Program   #
###################

with program() as PROGRAM:
    play("const", 'q1_rr')
    play("const", 'q2_rr')
    play("const", 'q3_rr')
    play("const", 'q4_rr')
    play("const", 'q5_rr')
    play("const", 'q6_rr')
    play("const", 'q7_rr')
    
    # align()

    # play("const", 'q1_rr_twin')
    # play("const", 'q2_rr_twin')
    # play("const", 'q3_rr_twin')
    # play("const", 'q4_rr_twin')
    # play("const", 'q5_rr_twin')
    # play("const", 'q6_rr_twin')
    # play("const", 'q7_rr_twin')    

    # align()

    # play("const", 'q1_xy')
    # play("const", 'q2_xy')
    # play("const", 'q3_xy')
    # play("const", 'q4_xy')
    # play("const", 'q5_xy')
    # play("const", 'q6_xy')
    # play("const", 'q7_xy')
    
    # align()

    # play("const", 'cr_drive_c1t2')
    # play("const", 'cr_drive_c2t1')
    # play("const", 'cr_drive_c2t3')
    # play("const", 'cr_drive_c3t2')
    # play("const", 'cr_drive_c3t4')
    # play("const", 'cr_drive_c4t3')
    # align()
    # play("const", 'cr_drive_c4t5')
    # play("const", 'cr_drive_c5t4')
    # play("const", 'cr_drive_c5t6')
    # play("const", 'cr_drive_c6t5')
    # play("const", 'cr_drive_c6t7')
    # play("const", 'cr_drive_c7t6')
    
    # align()

    # play("const", 'cr_cancel_c1t2')
    # play("const", 'cr_cancel_c2t1')
    # play("const", 'cr_cancel_c2t3')
    # play("const", 'cr_cancel_c3t2')
    # play("const", 'cr_cancel_c3t4')
    # play("const", 'cr_cancel_c4t3')
    # align()
    # play("const", 'cr_cancel_c4t5')
    # play("const", 'cr_cancel_c5t4')
    # play("const", 'cr_cancel_c5t6')
    # play("const", 'cr_cancel_c6t5')
    # play("const", 'cr_cancel_c6t7')
    # play("const", 'cr_cancel_c7t6')
    
    # align()

    # play("const", 'cr_drive_c1t2_twin')
    # play("const", 'cr_drive_c2t1_twin')
    # play("const", 'cr_drive_c2t3_twin')
    # play("const", 'cr_drive_c3t2_twin')
    # play("const", 'cr_drive_c3t4_twin')
    # play("const", 'cr_drive_c4t3_twin')
    # align()
    # play("const", 'cr_drive_c4t5_twin')
    # play("const", 'cr_drive_c5t4_twin')
    # play("const", 'cr_drive_c5t6_twin')
    # play("const", 'cr_drive_c6t5_twin')
    # play("const", 'cr_drive_c6t7_twin')
    # play("const", 'cr_drive_c7t6_twin')
    
    # align()

    # play("const", 'cr_cancel_c1t2_twin')
    # play("const", 'cr_cancel_c2t1_twin')
    # play("const", 'cr_cancel_c2t3_twin')
    # play("const", 'cr_cancel_c3t2_twin')
    # play("const", 'cr_cancel_c3t4_twin')
    # play("const", 'cr_cancel_c4t3_twin')
    # align()
    # play("const", 'cr_cancel_c4t5_twin')
    # play("const", 'cr_cancel_c5t4_twin')
    # play("const", 'cr_cancel_c5t6_twin')
    # play("const", 'cr_cancel_c6t5_twin')
    # play("const", 'cr_cancel_c6t7_twin')
    # play("const", 'cr_cancel_c7t6_twin')
    
        
if __name__ == "__main__":
    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

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
        from qm import generate_qua_script
        sourceFile = open('debug.py', 'w')
        print(generate_qua_script(PROGRAM, config), file=sourceFile) 
        sourceFile.close()

        # Open a quantum machine to execute the QUA program
        qm = qmm.open_qm(config)

        # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
        job = qm.execute(PROGRAM)

# %%
