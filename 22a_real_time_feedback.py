# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_mwfem_lffem import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
import matplotlib

matplotlib.use("TkAgg")


###################
# The QUA program #
###################
n_shots = 1


with program() as hello_qua:
    n = declare(int)
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_shots, n + 1):
        measure(
            "readout",
            "tank_circuit",
            None,
            demod.full("cos", I, "out1"),
            demod.full("sin", Q, "out1"),
        )

        with if_(I > 0.00323):
            play("step", "P1")
        with elif_(I > 0.00323):
            play("step", "P2")
        with else_():
            play("step", "B1")
        play("step", "P1", condition=I > 0.01869855)
        play("ramp", "P1", condition=I < 0.01869855)
        wait(250)

        save(I, I_st)
        save(Q, Q_st)
        save(n, n_st)

    with stream_processing():
        I_st.save_all("I")
        Q_st.save_all("Q")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################

# from qm import generate_qua_script
# sourceFile = open('debug.py', 'w')
# print(generate_qua_script(hello_qua, config), file=sourceFile)
# sourceFile.close()

qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
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

    results = fetching_tool(job, data_list=["I", "Q", "iteration"])
    I, Q, iteration = results.fetch_all()
    print(f"I = {I}, {I > 0.01869855}")


# %%
