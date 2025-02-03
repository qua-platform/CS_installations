#%%
from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.units import unit
from quam_libs.components import QuAM
import matplotlib.pyplot as plt


def strip_octaves_from_config(config):
    octaves_config = config.pop("octaves")
    for key, channel in config["elements"].items():
        if "RF_outputs" in channel:  # OPX input IQ channels
            RF_outputs_entry = channel.pop("RF_outputs")
            octave, idx = RF_outputs_entry["port"]
            if idx != 1:
                raise ValueError("Only RF output 1 is supported for Octave")

            IF_outputs = octaves_config[octave]["IF_outputs"]
            channel["outputs"] = {
                "out1": IF_outputs["IF_out1"]["port"],
                "out2": IF_outputs["IF_out2"]["port"],
            }
        if "RF_inputs" in channel:  # OPX output IQ channels
            RF_inputs_entry = channel.pop("RF_inputs")
            octave, idx = RF_inputs_entry["port"]
            RF_input = octaves_config[octave]["RF_outputs"][idx]

            channel["mixInputs"] = {
                "I": RF_input["I_connection"],
                "Q": RF_input["Q_connection"],
                "mixer": f"{key}.mixer",
                "lo_frequency": RF_input["LO_frequency"],
            }
    return config



# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()
# Generate the OPX and Octave configurations
# config = machine.generate_config()
# octave_config = machine.get_octave_config()
# # Open Communication with the QOP
# qmm = machine.connect()

config = machine.generate_config()
config = strip_octaves_from_config(config)

settings = dict(
    host=machine.network["host"],
    cluster_name=machine.network["cluster_name"],
)
if "port" in machine.network:
    settings["port"] = machine.network["port"]

qmm = QuantumMachinesManager(**settings)

q1 = machine.qubits["q1"]

with program() as prog:
    q1.xy.play("x180")


qm = qmm.open_qm(config)
job = qm.execute(prog)
plt.show()


# %%
