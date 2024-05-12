"""
This file creates the template of a config for all the parameters in your
superconducting qubit chip. By running this file as a script, a config
directory can be created which stores a dictionary structure which reflects
the components and parameters in your chip.

Here you can change which components (e.g., Transmon, Z-Flux Line, Resonator)
will be defined and how many to define.

You should only run this once at the start of your installation, or if there
is a fundamental change to the template (e.g., you connect a new device with
different components).
"""
import os.path
from pathlib import Path
import json

from quam.components import *
from quam.components.channels import IQChannel
from quam.components.pulses import ConstantReadoutPulse
from components import Transmon, ReadoutResonator, QuAM, FluxLine
from qm.octave import QmOctaveConfig
from quam.core import QuamRoot

from qualang_tools.units import unit


CONFIG_DIRECTORY = "config"


def create_quam_superconducting_referenced(num_qubits: int) -> (QuamRoot, QmOctaveConfig):
    """Create a QuAM with a number of qubits.

    Args:
        num_qubits (int): Number of qubits to create.

    Returns:
        QuamRoot: A QuAM with the specified number of qubits.
    """
    # Class containing tools to help handling units and conversions.
    u = unit(coerce_to_integer=True)

    quam = QuAM()  # QuAM root container object

    octave = Octave(
        name="octave1",
        ip=ValueError(),
        port=11050,
    )
    quam.octave = octave

    octave.initialize_frequency_converters()
    # octave.print_summary()
    octave_config = octave.get_octave_config()

    # Define the connectivity
    quam.wiring = {
        # Stage #1: Single-qubit control
        "qubits": [
            {
                "port_I": ("con1", 3),
                "port_Q": ("con1", 4),
                "port_Z": ("con1", 5),
            },
            {
                "port_Z": ("con1", 6),
                # these two won't output anything on a 6-channel OPX
                "port_I": ("con1", 7),
                "port_Q": ("con1", 8),
            },
        ],
        # # Stage #2: Two-qubit control
        # "qubits": [
        #     {
        #         "port_I": ("con1", 3),
        #         "port_Q": ("con1", 4),
        #     },
        #     {
        #         "port_I": ("con1", 5),
        #         "port_Q": ("con1", 6),
        #     }
        # ],
        "resonator": {
            "opx_output_I": ("con1", 1),
            "opx_output_Q": ("con1", 2),
            "opx_input_I": ("con1", 1),
            "opx_input_Q": ("con1", 2),
        },
    }
    quam.network = {"host": ValueError(), "cluster_name": "Cluster_1"}
    # Add the transmon components (xy, z and resonator) to the quam
    for idx in range(num_qubits):
        # Create qubit components
        transmon = Transmon(
            id=idx,
            xy=IQChannel(
                opx_output_I=f"#/wiring/qubits/{idx}/port_I",
                opx_output_Q=f"#/wiring/qubits/{idx}/port_Q",
                frequency_converter_up=octave.RF_outputs[2 * (idx + 1)].get_reference(),
                intermediate_frequency=100 * u.MHz,
            ),
            z=FluxLine(opx_output=f"#/wiring/qubits/{idx}/port_Z"),
            resonator=ReadoutResonator(
                opx_output_I="#/wiring/resonator/opx_output_I",
                opx_output_Q="#/wiring/resonator/opx_output_Q",
                opx_input_I="#/wiring/resonator/opx_input_I",
                opx_input_Q="#/wiring/resonator/opx_input_Q",
                opx_input_offset_I=0.0,
                opx_input_offset_Q=0.0,
                frequency_converter_up=octave.RF_outputs[1].get_reference(),
                frequency_converter_down=octave.RF_inputs[1].get_reference(),
                intermediate_frequency=50 * u.MHz,
                depletion_time=1 * u.us,
            ),
        )
        # Add the transmon pulses to the quam
        transmon.xy.operations["x180"] = pulses.DragPulse(
            amplitude=0.1, sigma=7, alpha=0, anharmonicity=-200 * u.MHz, length=40, axis_angle=0
        )
        transmon.xy.operations["x90"] = pulses.DragPulse(
            amplitude=0.1 / 2, sigma=7, alpha=0, anharmonicity=-200 * u.MHz, length=40, axis_angle=0
        )
        transmon.xy.operations["-x90"] = pulses.DragPulse(
            amplitude=-0.1 / 2, sigma=7, alpha=0, anharmonicity=-200 * u.MHz, length=40, axis_angle=0
        )
        transmon.xy.operations["y180"] = pulses.DragPulse(
            amplitude=0.1, sigma=7, alpha=0, anharmonicity=-200 * u.MHz, length=40, axis_angle=90
        )
        transmon.xy.operations["y90"] = pulses.DragPulse(
            amplitude=0.1 / 2, sigma=7, alpha=0, anharmonicity=-200 * u.MHz, length=40, axis_angle=90
        )
        transmon.xy.operations["-y90"] = pulses.DragPulse(
            amplitude=-0.1 / 2, sigma=7, alpha=0, anharmonicity=-200 * u.MHz, length=40, axis_angle=90
        )
        transmon.xy.operations["saturation"] = pulses.SquarePulse(amplitude=0.25, length=10 * u.us, axis_angle=0)
        transmon.z.operations["const"] = pulses.SquarePulse(amplitude=0.1, length=100)
        transmon.resonator.operations["readout"] = ConstantReadoutPulse(
            length=1 * u.us, amplitude=0.00123, threshold=0.0
        )
        quam.qubits[transmon.name] = transmon
        quam.active_qubit_names.append(transmon.name)
        # Set the Octave frequency and channels
        # TODO: be careful to set the right upconverters!! This is setup for q1: 3+4, q2: 5+6, etc.
        octave.RF_outputs[2 * idx + 1].channel = transmon.xy.get_reference()
        octave.RF_outputs[2 * idx + 1].LO_frequency = 7 * u.GHz  # Remember to set the LO frequency

        octave.RF_outputs[1].channel = transmon.resonator.get_reference()
        octave.RF_inputs[1].channel = transmon.resonator.get_reference()
        octave.RF_outputs[1].LO_frequency = 4 * u.GHz
        octave.RF_inputs[1].LO_frequency = 4 * u.GHz

    return quam, octave_config


if __name__ == "__main__":
    folder = Path("")
    folder.mkdir(exist_ok=True)

    machine, _ = create_quam_superconducting_referenced(num_qubits=2)

    if os.path.exists(folder / CONFIG_DIRECTORY):
        raise FileExistsError(f"Directory '{CONFIG_DIRECTORY}' already exists. "
                              f"If you want to overwrite its contents, please delete it.")

    machine.save(folder / CONFIG_DIRECTORY, content_mapping={"wiring.json": {"wiring", "network"}})

    qua_file = folder / "qua_config.json"
    qua_config = machine.generate_config()
    json.dump(qua_config, qua_file.open("w"), indent=4)

    quam_loaded = QuAM.load(folder / CONFIG_DIRECTORY)
    qua_file_loaded = folder / "qua_config2.json"
    qua_config_loaded = quam_loaded.generate_config()
    json.dump(qua_config_loaded, qua_file.open("w"), indent=4)
