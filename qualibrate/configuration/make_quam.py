# %%
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import build_quam

path = "./quam_state"

machine = QuAM.load(path)

octave_settings = {}

# Make the QuAM object and save it
quam = build_quam(machine, quam_state_path=path, octaves_settings=octave_settings)

# %%
