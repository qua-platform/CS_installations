#Imports for new virtual environment
import numpy as np
from qm import QuantumMachinesManager
from qm import SimulationConfig
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.units import unit
from qm.qua import *
from qm.qua import time_tagging

from quam.components import *
from quam.components.channels import TimeTaggingAddon


u = unit()
qop_ip = "172.16.33.101"
cluster_name = "Cluster_81"
qop_port = None

machine = BasicQuAM()

# Add Octaves
machine.octaves["octave1"]= Octave(name = "oct1", ip  = "172.16.33.101", port = 80)

machine.octaves["octave1"].initialize_frequency_converters()

EOM_output = machine.octaves["octave1"].RF_outputs[1]
EOM_A_output = machine.octaves["octave1"].RF_outputs[1]
EOM_B_output = machine.octaves["octave1"].RF_outputs[1]
mwe_output = machine.octaves["octave1"].RF_outputs[2]
mwg_output = machine.octaves["octave1"].RF_outputs[3]

# Convert Elements to channels
# For IQ Analog outputs
# Note, want to make EOM A and B
machine.channels["EOM"] = EOM = IQChannel(
    opx_output_I = ("con1", 1),
    opx_output_Q = ("con1", 2),
    frequency_converter_up= EOM_output.get_reference(),
    digital_outputs={"trigger": DigitalOutputChannel (opx_output=("con1",4), delay = 0, buffer = 0)},
    intermediate_frequency = 30e6,
)   
EOM_output.channel = EOM.get_reference()
EOM_output.LO_frequency = 6e9

machine.channels["EOM_A"] = EOM_A = IQChannel(
    opx_output_I = ("con1", 1),
    opx_output_Q = ("con1", 2),
    frequency_converter_up= EOM_A_output.get_reference(),
    digital_outputs={"trigger": DigitalOutputChannel (opx_output=("con1",4), delay = 0, buffer = 0)},
    intermediate_frequency = 30e6,
)   
EOM_A_output.channel = EOM.get_reference()
EOM_A_output.LO_frequency = 6e9

machine.channels["EOM_B"] = EOM_B = IQChannel(
    opx_output_I = ("con1", 1),
    opx_output_Q = ("con1", 2),
    frequency_converter_up= EOM_B_output.get_reference(),
    digital_outputs={"trigger": DigitalOutputChannel (opx_output=("con1",4), delay = 0, buffer = 0)},
    intermediate_frequency = 30e6,
)   
EOM_B_output.channel = EOM.get_reference()
EOM_B_output.LO_frequency = 6e9


machine.channels["mwe"] = mwe = IQChannel(
    opx_output_I = ("con1", 3),
    opx_output_Q = ("con1", 4),
    frequency_converter_up= mwe_output.get_reference(),
    intermediate_frequency = 30e6,
    
)   
mwe_output.channel = mwe.get_reference()
mwe_output.LO_frequency = 2.5e9

machine.channels["mwg"] = mwg = IQChannel(
    opx_output_I = ("con1", 5),
    opx_output_Q = ("con1", 6),
    frequency_converter_up= mwg_output.get_reference(),
    intermediate_frequency = 30e6,
)   
mwg_output.channel = mwg.get_reference()
mwg_output.LO_frequency= 2.5e9

# For single analog outputs, may convert to single AOM qith mu
machine.channels['AOM1'] = AOM1 = SingleChannel(
    opx_output = ("con1", 7),
)
machine.channels['AOM2'] = AOM2 = SingleChannel(
    opx_output = ("con1", 8),
)

# machine.channels['AOM']= AOM = SingleChannel(
#     opx_output_I = ("con1", 7),
#     opx_output_Q = ("con1", 8),
# )

# #Single Analog Input, testing time_tagging from Serwan
machine.channels["SNSPD"] = SNSPD = InSingleChannel(
    id = "SNSPD",
    opx_input = ("con1", 1),
    digital_outputs={"trigger":DigitalOutputChannel(opx_output=("con1", 2),delay = 0,buffer = 0)},
    time_tagging = TimeTaggingAddon(
        signal_threshold=0.1, 
        signal_polarity = "above", 
        derivative_threshold= -0.2,
        derivative_polarity= "above",
        ),
    time_of_flight = 36,
)

machine.channels["SNSPD_RAW"] = SNSPD_RAW = InSingleChannel(
    id = "SNSPD_RAW",
    opx_input = ("con1", 1),
    digital_outputs={"trigger":DigitalOutputChannel(opx_output=("con1", 2),delay = 0,buffer = 0)},
    # time_tagging = TimeTaggingAddon(
    #     signal_threshold=0.1, 
    #     signal_polarity = "above", 
    #     derivative_threshold= -0.2,
    #     derivative_polarity= "above",
    #     ),
    time_of_flight = 36,
)
                

# Elements/Channels with digital outputs only
machine.channels["OpticalTrigger"] = OpticalTrigger = Channel(
    digital_outputs={"trigger":DigitalOutputChannel(opx_output=("con1", 1),delay = 0,buffer = 0)}
)
machine.channels["RF_switch"] = RF_switch = Channel(
    digital_outputs={"trigger":DigitalOutputChannel(opx_output=("con1", 3),delay = 0,buffer = 0)}
)

# Converting Pulses, and adding digital outputs to elements/channels, start with waveforms and work 
# towards mapping operations to elements/channels.
# Need "waveforms", "digital_waveforms", "integration_weights", "pulses", and then element["operations"]

EOM.operations["const_pulse"] = pulses.SquarePulse(
    id = "const_pulse",
    length = 512,
    amplitude = 0.01,
    axis_angle= 0,
)
EOM.operations["pi"] = pulses.SquarePulse(
    length = 512,
    amplitude = 0.02,
    axis_angle= 0,
)
EOM.operations["pi_half"] = pulses.SquarePulse(
    length = 256,
    amplitude = 0.03,
    axis_angle= 0,
)

EOM_A.operations["const_pulse"] = pulses.SquarePulse(
    id = "const_pulse",
    length = 512,
    amplitude = 0.01,
    axis_angle= 0,
)
EOM_A.operations["pi"] = pulses.SquarePulse(
    length = 512,
    amplitude = 0.02,
    axis_angle= 0,
)
EOM_A.operations["pi_half"] = pulses.SquarePulse(
    length = 256,
    amplitude = 0.03,
    axis_angle= 0,
)

EOM_B.operations["const_pulse"] = pulses.SquarePulse(
    id = "const_pulse",
    length = 512,
    amplitude = 0.01,
    axis_angle= 0,
)
EOM_B.operations["pi"] = pulses.SquarePulse(
    length = 512,
    amplitude = 0.02,
    axis_angle= 0,
)
EOM_B.operations["pi_half"] = pulses.SquarePulse(
    length = 256,
    amplitude = 0.03,
    axis_angle= 0,
)

mwe.operations["const_pulse"] = pulses.SquarePulse(
    length = 512,
    amplitude = 0.04,
    axis_angle= 0,
)
mwe.operations["pi"] = pulses.SquarePulse(
    length = 512,
    amplitude = 0.05,
    axis_angle= 0,
)
mwe.operations["pi_half"] = pulses.SquarePulse(
    length = 256,
    amplitude = 0.04,
    axis_angle= 0,
)

mwg.operations["const_pulse"] = pulses.SquarePulse(
    length = 512,
    amplitude = 0.03,
    axis_angle= 0,
)
mwg.operations["pi"] = pulses.SquarePulse(
    length = 512,
    amplitude = 0.02,
    axis_angle= 0,
)
mwg.operations["pi_half"] = pulses.SquarePulse(
    length = 256,
    amplitude = 0.01,
    axis_angle= 0,
    )

AOM1.operations["AOM1_ON"] = pulses.SquarePulse(
    length = 512,
    amplitude = 0.02,
)
AOM2.operations["AOM2_ON"] = pulses.SquarePulse(
    length = 512,
    amplitude = 0.03,
)

SNSPD.operations["readout"] = pulses.Pulse(
    length = 1024,
    digital_marker=[(1,0)]
)

SNSPD_RAW.operations["readout"] = pulses.Pulse(
    length = 1024,
    digital_marker=[(1,0)]
)

OpticalTrigger.operations["Laser_ON"] = pulses.Pulse(
    length = 512,
    digital_marker=[(1,0)]
)
RF_switch.operations["RF_ON"] = pulses.Pulse(
    length = 512,
    digital_marker=[(1,0)]
)

from pprint import pprint
# Generate the QUA configuration from QuAM
pprint(machine.generate_config())
machine.save('C:/Users/BradCole/OneDrive - QM Machines LTD/Documents/Brewery/GitHubPull_testing_Dir/Princeton_QuAM/state.json')

