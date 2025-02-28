# %%
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import build_quam

path = "/workspaces/HI_20250303_NobuKaneko/configuration/quam_state"

machine = QuAM.load(path)

# octave_settings = {"octave1": {"port": 11109}}  # externally configured: (11XXX where XXX are last three digits of oct ip)
# octave_settings = {"octave1": {"port": 11109}, "octave2": {"port": 11109}}  # externally configured: (11XXX where XXX are last three digits of oct ip)
octave_settings = {"octave1": {"ip": "172.16.33.109"} }  # "internally" configured: use the local ip address of the Octave
# octave_settings = {}

# Make the QuAM object and save it
quam = build_quam(machine, quam_state_path=path, octaves_settings=octave_settings)

# %%
