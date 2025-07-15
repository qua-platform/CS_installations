# %%
import numpy as np
import time
import os

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_octave import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
from qdac2_driver import QDACII, load_voltage_list, set_qdac_voltage
import matplotlib.pyplot as plt
from macros import RF_reflectometry_macro, DC_current_sensing_macro
from qualang_tools.results.data_handler import DataHandler


##########################################################################################
## QDAC2 section
# Create the qdac instrument
qdac = QDACII(
    "Ethernet", IP_address="172.16.33.101", port=5025
)  # Using Ethernet protocol
# qdac = QDACII("USB", USB_device=4)  # Using USB protocol

###########################
# Voltage scan triggering #
###########################
# Voltages in Volt
n_points_fast = 10
voltage_values_fast = np.linspace(-1.5, 1.5, n_points_fast)
load_voltage_list(
    qdac,
    channel=1,
    dwell=2e-6,
    slew_rate=2e7,
    trigger_port="ext1",
    output_range="low",
    output_filter="med",
    voltage_list=voltage_values_fast,
)

###############
# Set voltage #
###############
set_qdac_voltage(qdac, channel=2, voltage=1)

## QDAC2 section
##########################################################################################

###################################
# Open Communication with the QOP #
###################################
qmm = QuantumMachinesManager(
    host=qop_ip, cluster_name=cluster_name, octave_calibration_db_path=os.getcwd()
)

###############################
# OPX generates trigger pulse #
###############################
with program() as prog:
    with infinite_loop_():
        # Trigger the QDAC to start the voltage scan
        play("trigger", "qdac_trigger1")
        # Connect trigger2 to oscilloscope to monitor the trigger
        play("trigger", "qdac_trigger2")
        # Wait for the QDAC to finish the scan
        wait(10_000, "qdac_trigger1")

#######################################
# Execute or Simulate the QUA program #
#######################################
simulate = False
if simulate:
    simulation_config = SimulationConfig(duration=400)  # in clock cycles
    job_sim = qmm.simulate(config, prog, simulation_config)
    job_sim.get_simulated_samples().con1.plot()
    plt.show()
else:
    qm = qmm.open_qm(config)
    job = qm.execute(prog)
    # Execute does not block python! As this is an infinite loop, the job would run forever.
    # In this case, we've put a 10 seconds sleep and then halted the job.
    time.sleep(10)
    job.halt()
