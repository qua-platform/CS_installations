# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_lf_fem import *
from qualang_tools.voltage_gates import VoltageGateSequence
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
import matplotlib

matplotlib.use('TkAgg')


###################
# The QUA program #
###################
num_outer = 10
num_inner = 100

with program() as hello_qua:
    n = declare(int)
    m = declare(int)
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()

    with for_(n, 0, n < num_outer, n + 1):
        with for_(m, 0, m < num_inner, m + 1):
            # play("long_readout", "tank_circuit")
            measure(
                "long_readout",
                "tank_circuit",
                None,
                demod.full("cos", I, "out1"),
                demod.full("sin", Q, "out1"),
            )
            save(I, I_st)
            save(Q, Q_st)
            wait(measurement_delay * u.ns)  # in n
            
            # align("tank_circuit", "tank_circuit_twin")
            # measure(
            #     "long_readout",
            #     "tank_circuit_twin",
            #     None,
            #     demod.full("cos", I, "out1"),
            #     demod.full("sin", Q, "out1"),
            # )
        #     save(I, I_st)
        #     save(Q, Q_st)

        # save(n, n_st)

    with stream_processing():
        I_st.buffer(num_inner).save("I")
        Q_st.buffer(num_inner).save("Q")
    #     n_st.save("iteration")



#####################################
#  Open Communication with the QOP  #
#####################################

# from qm import generate_qua_script
# sourceFile = open('debug.py', 'w')
# print(generate_qua_script(hello_qua, config), file=sourceFile)
# sourceFile.close()

qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

###########################
# Run or Simulate Program #
###########################

#######################
# Simulate or execute #
#######################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, hello_qua, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)

# %%
