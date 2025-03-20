# %%
from qm.qua import *
from qualang_tools.loops.loops import from_array
from qualang_tools.units import unit
from qm import QuantumMachinesManager, SimulationConfig

from qua_config.configuraiton_cluster4_3chassis_8fems422_band1 import *


##################
#   Parameters   #
##################

rr1 = get_elements("resonator", cons="con1", fems=1, ports=1)
rr2 = get_elements("resonator", cons="con2", fems=1, ports=1)
rr3 = get_elements("resonator", cons="con3", fems=1, ports=1)
qb1 = get_elements("qubit", cons="con1", fems=1, ports=2)
qb2 = get_elements("qubit", cons="con2", fems=1, ports=2)
qb3 = get_elements("qubit", cons="con3", fems=1, ports=2)

qubits = [qb1, qb2, qb3]
resonators = [rr1, rr2, rr3]


print_elements_ports(qubits + resonators)


config["pulses"]["const_pulse"]["length"] = 100


delay_array = np.arange(4, 100, 4)
##################
#      QUA       #
##################


with program() as PROG:

    delay = declare(int)
    I = [declare(fixed) for _ in range(len(resonators))]
    Q = [declare(fixed) for _ in range(len(resonators))]


    with infinite_loop_():

        with for_(*from_array(delay, delay_array)):

            for i, (qb, rr) in enumerate(zip(qubits, resonators)):

                play("const", qb) # play('x180', rr)

                wait(delay, qb)

                play("const", rr) # play('x180', rr)
                
                align(qb, rr)

                measure(
                    "readout",
                    rr,
                    dual_demod.full("cos", "sin", I[i]),
                    dual_demod.full("minus_sin", "cos", Q[i]),
                )
            
                wait(50, rr)


        
if __name__ == "__main__":
    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(host=host_ip, cluster_name=cluster_name)
    qmm.clear_all_job_results()
    qmm.close_all_qms()


    ###########################
    # Run or Simulate Program #
    ###########################

    simulate = False

    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
        # Simulate blocks python until the simulation is done
        
        job = qmm.simulate(config, PROG, simulation_config)
        # Plot the simulated samples
        job.get_simulated_samples().con1.plot()

    else:
        # Open a quantum machine to execute the QUA program

        from pathlib import Path
        from qm import generate_qua_script
        debug_filepath = sourceFile = f"debug_{Path(__file__).stem}.py"
        sourceFile = open(debug_filepath, "w")
        print(generate_qua_script(PROG, config), file=sourceFile)
        sourceFile.close()

        qm = qmm.open_qm(config)

        # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
        job = qm.execute(PROG)

# %%
