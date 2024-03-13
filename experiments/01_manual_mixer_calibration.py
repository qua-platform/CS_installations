# %%
"""
        MIXER CALIBRATION
The program is designed to play a continuous single tone to calibrate an IQ mixer. To do this, connect the mixer's
output to a spectrum analyzer. Adjustments for the DC offsets, gain, and phase must be made manually.

If you have access to the API for retrieving data from the spectrum analyzer, you can utilize the commented lines below
to semi-automate the process.

Before proceeding to the next node, take the following steps:
    - Update the DC offsets in the configuration at: config/controllers/"con1"/analog_outputs.
    - Modify the DC gain and phase for the IQ signals in the configuration, under either:
      mixer_qubit_g & mixer_qubit_g or mixer_resonator_g & mixer_resonator_g.
"""
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from configuration import *


with program() as cw_output:
    with infinite_loop_():
        play("cw", "qubit")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

qm = qmm.open_qm(config)
job = qm.execute(cw_output)

# %%
