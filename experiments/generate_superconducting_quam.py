from pathlib import Path
import json
from typing import List
from quam.components import *
from quam.components.channels import IQChannel
from quam.components.pulses import ConstantReadoutPulse
from components import Transmon, ReadoutResonator, QuAM, FluxLine
from qm.octave import QmOctaveConfig
from quam.core import QuamRoot

from qualang_tools.units import unit


network = {"host": "qum.phys.sinica.edu.tw", "cluster_name": "QPX_1", "port": 9800}
octave1_network = dict(ip=network["host"], port=11250)
octave2_network = dict(ip=network["host"], port=11251)


def create_quam_superconducting_referenced(num_qubits: int) -> (QuamRoot, QmOctaveConfig):
    """Create a QuAM with a number of qubits.

    Args:
        num_qubits (int): Number of qubits to create.

    Returns:
        QuamRoot: A QuAM with the specified number of qubits.
    """
    # Class containing tools to help handling units and conversions.
    u = unit(coerce_to_integer=True)
    # Initiate the QuAM class
    quam = QuAM()

    # Add the Octave to the quam
    octave1 = Octave(name="octave1", **octave1_network)
    octave1.initialize_frequency_converters()
    quam.octaves["octave1"] = octave1

    octave2 = Octave(name="octave2", **octave2_network)
    octave2.initialize_frequency_converters()
    quam.octaves["octave2"] = octave2

    octave_config = octave1.get_octave_config()
    octave_config.add_device_info(octave2.name, octave2.host, octave2.port)
    octave_config.add_opx_octave_port_mapping(portmap=octave2.get_portmap())

    # Define the connectivity
    quam.wiring = {
        "qubits": {
            "q1": {
                "xy": {"opx_output_I": ("con2", 1), "opx_output_Q": ("con2", 2)},
                "z": {"opx_output": ("con2", 5)},
            },
            "q2": {
                "xy": {"opx_output_I": ("con1", 7), "opx_output_Q": ("con1", 8)},
                "z": {"opx_output": ("con2", 6)},
            },
            "q3": {
                "xy": {"opx_output_I": ("con1", 5), "opx_output_Q": ("con1", 6)},
                "z": {"opx_output": ("con2", 7)},
            },
            "q4": {
                "xy": {"opx_output_I": ("con1", 9), "opx_output_Q": ("con1", 10)},
                "z": {"opx_output": ("con2", 8)},
            },
            "q00": {
                "xy": {"opx_output_I": ("con1", 9), "opx_output_Q": ("con1", 10)},
                "z": {"opx_output": ("con2", 9)},
            },
            "q5": {
                "xy": {"opx_output_I": ("con1", 3), "opx_output_Q": ("con1", 4)},
                "z": {"opx_output": ("con2", 3)},
            },
        }
    }
    for qubit_wiring in quam.wiring["qubits"].values():
        qubit_wiring["resonator"] = {
            "opx_output_I": ("con1", 1),
            "opx_output_Q": ("con1", 2),
            "opx_input_I": ("con1", 1),
            "opx_input_Q": ("con1", 2),
        }

    quam.network = network
    # Add the transmon components (xy, z and resonator) to the quam
    for qubit_name in quam.wiring.qubits:
        # Determine Octave settings
        qubit_wiring = quam.wiring.qubits[qubit_name]
        opx_output_I = qubit_wiring.xy.opx_output_I
        if opx_output_I[0] == "con1":
            octave = octave1
        elif opx_output_I[0] == "con2":
            octave = octave2
        else:
            raise ValueError(f"Unknown Octave connection {opx_output_I}")

        RF_output_idx = int((qubit_wiring.xy.opx_output_I[1] + 1) / 2)
        RF_output = octave.RF_outputs[RF_output_idx]

        # Create qubit components
        transmon = Transmon(
            id=qubit_name,
            xy=IQChannel(
                opx_output_I=f"#/wiring/qubits/{qubit_name}/xy/opx_output_I",
                opx_output_Q=f"#/wiring/qubits/{qubit_name}/xy/opx_output_Q",
                frequency_converter_up=RF_output.get_reference(),
                intermediate_frequency=100 * u.MHz,
            ),
            z=FluxLine(opx_output=f"#/wiring/qubits/{qubit_name}/z/opx_output"),
            resonator=ReadoutResonator(
                opx_output_I=f"#/wiring/qubits/{qubit_name}/resonator/opx_output_I",
                opx_output_Q=f"#/wiring/qubits/{qubit_name}/resonator/opx_output_Q",
                opx_input_I=f"#/wiring/qubits/{qubit_name}/resonator/opx_input_I",
                opx_input_Q=f"#/wiring/qubits/{qubit_name}/resonator/opx_input_Q",
                opx_input_offset_I=0.0,
                opx_input_offset_Q=0.0,
                frequency_converter_up=octave1.RF_outputs[1].get_reference(),
                frequency_converter_down=octave1.RF_inputs[1].get_reference(),
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
        # Set the Octave frequency and channels TODO: be careful to set the right upconverters!!
        RF_output.channel = transmon.xy.get_reference()
        RF_output.LO_frequency = 7 * u.GHz  # Remember to set the LO frequency

        octave1.RF_outputs[1].channel = transmon.resonator.get_reference()
        octave1.RF_inputs[1].channel = transmon.resonator.get_reference()
        octave1.RF_outputs[1].LO_frequency = 4 * u.GHz
        octave1.RF_inputs[1].LO_frequency = 4 * u.GHz
    return quam, octave_config


def rewire_for_active_qubits(quam: QuAM, active_qubit_names: List[str]):
    quam.active_qubit_names = []
    for idx, name in enumerate(active_qubit_names):
        q = quam.qubits[name]
        quam.active_qubit_names.append(name)
        q.xy.frequency_converter_up = None
        q.xy.frequency_converter_up = quam.octave.RF_outputs[2 * (idx + 1)].get_reference()
        q.xy.opx_output_I = f"#/wiring/qubits/{idx}/port_I"
        q.xy.opx_output_Q = f"#/wiring/qubits/{idx}/port_Q"
        q.z.opx_output = f"#/wiring/qubits/{idx}/port_Z"
        quam.octave.RF_outputs[2 * (idx + 1)].channel = q.xy.get_reference()
        quam.octave.RF_outputs[2 * (idx + 1)].LO_frequency = q.f_01 - q.xy.intermediate_frequency


if __name__ == "__main__":
    folder = Path("")
    folder.mkdir(exist_ok=True)

    machine, _ = create_quam_superconducting_referenced(num_qubits=5)
    machine.save(folder / "quam_state", content_mapping={"wiring.json": {"wiring", "network"}})

    qua_file = folder / "qua_config.json"
    qua_config = machine.generate_config()
    json.dump(qua_config, qua_file.open("w"), indent=4)

    quam_loaded = QuAM.load(folder / "quam_state")
    qua_file_loaded = folder / "qua_config2.json"
    qua_config_loaded = quam_loaded.generate_config()
    json.dump(qua_config_loaded, qua_file.open("w"), indent=4)
