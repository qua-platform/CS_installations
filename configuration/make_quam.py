# %%
import math
import os.path
from typing import Dict, List, Type, TypeVar
from pathlib import Path
import json

from qualang_tools.units import unit
from quam.components import Octave, IQChannel, DigitalOutputChannel
from quam_libs.components import (
    Transmon,
    ReadoutResonator,
    CrossResonanceDrive,
    TransmonPair,
    QuAM,
    FEMQuAM,
    OPXPlusQuAM,
)

from make_pulses import add_default_transmon_pulses, add_default_transmon_pair_pulses
from make_wiring import allocate_ports, custom_port_allocation, create_wiring

# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)

QuamTypes = TypeVar("QuamTypes", OPXPlusQuAM, FEMQuAM)


def create_quam_superconducting(
    quam_class: Type[QuamTypes],
    wiring: dict = None,
    octaves: Dict[str, Octave] = None,
) -> QuamTypes:
    """Create a QuAM with a number of qubits.

    Args:
        wiring (dict): Wiring of the qubits.

    Returns:
        QuamRoot: A QuAM with the specified number of qubits.
    """
    # Initiate the QuAM class
    machine = quam_class()

    # Define the connectivity
    if wiring is not None:
        machine.wiring = wiring
    else:
        raise ValueError("Wiring must be provided.")

    host_ip = "120.0.0.1"
    machine.network = {
        "host": host_ip,
        "cluster_name": "QPX_20q",
        "data_folder": "/CS_installations/data",
    }
    print("Please update the default network settings in: quam.network")

    num_qubits = len(wiring["qubits"])

    octaves = None

    # Add the transmon components (xy, z and resonator) to the quam
    for qubit_name, qubit_wiring in machine.wiring.qubits.items():
        # Create all necessary ports
        machine.ports.reference_to_port(qubit_wiring.xy.get_unreferenced_value("digital_port"), create=True)
        machine.ports.reference_to_port(qubit_wiring.xy.get_unreferenced_value("opx_output"), create=True)
        machine.ports.reference_to_port(qubit_wiring.resonator.get_unreferenced_value("opx_output"), create=True)
        machine.ports.reference_to_port(qubit_wiring.resonator.get_unreferenced_value("opx_input"), create=True)
        machine.ports.reference_to_port(qubit_wiring.resonator.get_unreferenced_value("digital_port"), create=True)

        # Create qubit components
        transmon = Transmon(
            id=qubit_name,
            xy=IQChannel(
                opx_output=qubit_wiring.xy.get_unreferenced_value("opx_output"),
                frequency_converter_up=qubit_wiring.xy.frequency_converter_up.get_reference(),
                intermediate_frequency=-200 * u.MHz,
                digital_outputs={
                    "octave_switch": DigitalOutputChannel(
                        opx_output=qubit_wiring.xy.get_unreferenced_value("digital_port"),
                        delay=87,  # 57ns for QOP222 and above
                        buffer=15,  # 18ns for QOP222 and above
                    )
                },
            ),
            resonator=ReadoutResonator(
                opx_output=qubit_wiring.resonator.get_unreferenced_value("opx_output"),
                opx_input=qubit_wiring.resonator.get_unreferenced_value("opx_input"),
                digital_outputs={
                    "octave_switch": DigitalOutputChannel(
                        opx_output=qubit_wiring.resonator.get_unreferenced_value("digital_port"),
                        delay=87,  # 57ns for QOP222 and above
                        buffer=15,  # 18ns for QOP222 and above
                    )
                },
                opx_input_offset=0.0,
                frequency_converter_up=qubit_wiring.resonator.frequency_converter_up.get_reference(),
                frequency_converter_down=qubit_wiring.resonator.frequency_converter_down.get_reference(),
                intermediate_frequency=-250 * u.MHz,
                depletion_time=1 * u.us,
            ),
        )
        machine.qubits[transmon.name] = transmon
        machine.active_qubit_names.append(transmon.name)

        add_default_transmon_pulses(transmon)

        RF_output = transmon.xy.frequency_converter_up
        RF_output.channel = transmon.xy.get_reference()
        RF_output.output_mode = "always_on" # "triggered"
        RF_output.LO_frequency = 4.7 * u.GHz
        print(f"Please set the LO frequency of {RF_output.get_reference()}")
        print(f"Please set the output mode of {RF_output.get_reference()} to always_on or triggered")

    # Only set resonator RF outputs once
    RF_output_resonator = transmon.resonator.frequency_converter_up
    RF_output_resonator.channel = transmon.resonator.get_reference()
    RF_output_resonator.output_mode = "always_on"
    # RF_output_resonator.output_mode = "triggered"
    RF_output_resonator.LO_frequency = 6.2 * u.GHz
    print(f"Please set the LO frequency of {RF_output_resonator.get_reference()}")
    print(f"Please set the output mode of {RF_output_resonator.get_reference()} to always_on or triggered")

    RF_input_resonator = transmon.resonator.frequency_converter_down
    RF_input_resonator.channel = transmon.resonator.get_reference()
    RF_input_resonator.LO_frequency = 6.2 * u.GHz
    print(f"Please set the LO frequency of {RF_input_resonator.get_reference()}")

    # Add qubit pairs along with couplers
    for i, qubit_pair_wiring in enumerate(machine.wiring.qubit_pairs):
        qubit_control_name = qubit_pair_wiring.qubit_control.name
        qubit_target_name = qubit_pair_wiring.qubit_target.name
        qubit_pair_name = f"{qubit_control_name}_{qubit_target_name}"

        machine.ports.reference_to_port(qubit_pair_wiring.qubit_control.xy.get_unreferenced_value("opx_output"), create=True)
        machine.ports.reference_to_port(qubit_pair_wiring.qubit_target.xy.get_unreferenced_value("opx_output"), create=True)
        
        # Note: The Q channel is set to the I channel plus one.
        qubit_pair = TransmonPair(
            id=qubit_pair_name,
            qubit_control=qubit_pair_wiring.get_unreferenced_value("qubit_control"),
            qubit_target=qubit_pair_wiring.get_unreferenced_value("qubit_target"),
            cr_drive_control=CrossResonanceDrive(
                opx_output=qubit_pair_wiring.qubit_control.xy.get_unreferenced_value("opx_output"),
                frequency_converter_up=qubit_pair_wiring.qubit_target.xy.get_reference("frequency_converter_up"), # referencing target LO
                intermediate_frequency=qubit_pair_wiring.qubit_target.xy.get_reference("intermediate_frequency"), # referencing target IF
                digital_outputs=qubit_pair_wiring.qubit_control.xy.get_reference("digital_outputs")
            ),
            cr_drive_target=CrossResonanceDrive(
                opx_output=qubit_pair_wiring.qubit_target.xy.get_unreferenced_value("opx_output"),
                frequency_converter_up=qubit_pair_wiring.qubit_target.xy.get_reference("frequency_converter_up"),
                intermediate_frequency=qubit_pair_wiring.qubit_target.xy.get_reference("intermediate_frequency"),
                digital_outputs=qubit_pair_wiring.qubit_target.xy.get_reference("digital_outputs")
            ),
        )
        machine.qubit_pairs.append(qubit_pair)
        machine.active_qubit_pair_names.append(qubit_pair_name)
        add_default_transmon_pair_pulses(qubit_pair)

    # Add additiional analog input ports
    machine.ports.get_analog_input("con1", 2, 1, create=True)

    machine.active_qubits.pop(0)

    return machine


if __name__ == "__main__":
    folder = Path(__file__).parent
    quam_folder = folder / "quam_state"
    quam_class = FEMQuAM
    qubits = [1, 2, 3, 4]
    qubit_pairs = [
        (1, 2), (2, 1),
        (2, 3), (3, 2),
        (3, 4), (4, 3),
    ]
    qubit_xy_port_map = {
        1: (1, 1, 1, None),
        2: (1, 1, 2, None),
        3: (1, 1, 3, None),
        4: (1, 1, 4, None),
    }
    resonator_port_map = {
        1: (1, 1, 8, 1),
        2: (1, 1, 8, 1),
        3: (1, 1, 8, 1),
        4: (1, 1, 8, 1),
    } 

    port_allocation = allocate_ports(
        num_qubits=2,
    )
    # port_allocation = custom_port_allocation(custom_port_wiring)
    print(f"{port_allocation=}")
    wiring = create_wiring(port_allocation)
    print(f"{wiring=}")
    machine = create_quam_superconducting(quam_class, wiring)

    machine.save(quam_folder, content_mapping={"wiring.json": {"wiring", "network"}})

    qua_file = folder / "qua_config.json"
    qua_config = machine.generate_config()
    json.dump(qua_config, qua_file.open("w"), indent=4)

    quam_loaded = QuAM.load(quam_folder)
    qua_config_loaded = quam_loaded.generate_config()
    json.dump(qua_config_loaded, qua_file.open("w"), indent=4)

# %%
