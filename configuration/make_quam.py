from pathlib import Path

from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import build_quam

# make the QuAM object
path = Path(".") / "quam_state"

machine = QuAM.load(path)

octave_settings = {"oct1": {"port": 11234} }

quam = build_quam(machine, quam_state_path=path, octaves_settings=octave_settings)

# todo: add non-default time-of-flight once it is added to MWInOutChannel
