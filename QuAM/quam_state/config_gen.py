
import json
from qualang_tools.units import unit
from quam_config import Quam
from quam_builder.builder.superconducting.pulses import add_DragCosine_pulses
from quam.components.pulses import GaussianPulse, SquarePulse  # (+SquarePulse)
import numpy as np
import json
from pprint import pprint
import matplotlib.pyplot as plt
from qualang_tools.wirer.wirer.channel_specs import *
from pathlib import Path

########################################################################################################################
# %%                                 QUAM loading and auxiliary functions
########################################################################################################################
# Loads the QUAM
machine = Quam.load(Path("C:/Users/BenjaminSafvati/Customers/Mo_Chen/QuAM/quam_state"))

cfg = machine.generate_config()

pprint(machine.generate_config())
with open("config.json", "w+") as f:
    json.dump(machine.generate_config(), f, indent=4)