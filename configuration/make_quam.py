from pathlib import Path

from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import build_quam

path = Path(".") / "quam_state"

machine = QuAM.load(path)

# Configure the octave
# If "externally" configured, ip is default (host) port is 11XXX where XXX are the last three digits of octave IP
# octave_settings = {"oct1": {"port": 11234} }
# If "internally" configured, port is default (80) ip is given by the local ip address of the Octave
# octave_settings = {"oct1": {"ip": "192.168.88.250"} }
octave_settings = {}

# Make the QuAM object and save it
quam = build_quam(machine, quam_state_path=path, octaves_settings=octave_settings)
