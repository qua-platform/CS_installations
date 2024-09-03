# %%
import sys
import os
from pathlib import Path
from typing import Dict, List, Type, TypeVar
from pathlib import Path
import json

from qualang_tools.units import unit
from quam.components import Octave, IQChannel, DigitalOutputChannel

# Add the parent directory of `quam_libs` to the system path
current_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(current_dir))
from quam_libs.components import (
    Transmon,
    ReadoutResonator,
    TunableCoupler,
    CrossResonance,
    TransmonPair,
    QuAM,
    FEMQuAM,
    OPXPlusQuAM,
)

from make_pulses import add_default_transmon_pulses, add_default_transmon_pair_pulses
from make_wiring import default_port_allocation, create_wiring
from json2python import json_to_python_file


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

    host_ip = "127.0.0.1"
    octave_ips = [
        "127.0.0.1",
        "127.0.0.1",
        "127.0.0.1",
    ] # or "192.168.88.X" if configured internally
    octave_ports = [
        11243,
        11240,
        11241,
    ]  # 11XXX where XXX are the last digits of the Octave IP or 80 if configured internally

    machine.network = {
        "host": host_ip,
        "cluster_name": "QPX_20q",
        "octave_ips": octave_ips,
        "octave_ports": octave_ports,
        "data_folder": r"/Users/adamachuck/Documents/GitHub/ASQUM/qua-libs/Quantum-Control-Applications-QuAM/Superconducting/data",
    }
    print("Please update the default network settings in: quam.network")

    num_qubits = len(wiring["qubits"])

    if octaves is not None:
        machine.octaves = octaves
        print("If you haven't configured the octaves, please run: octave.initialize_frequency_converters()")
    else:
        # Add the Octave to the quam
        for i in range(len(octave_ips)):
            # Assumes 1 Octave for every 4 qubits
            octave = Octave(
                name=f"octave{i+1}",
                ip=machine.network["octave_ips"][i],
                port=machine.network["octave_ports"][i],
                calibration_db_path=os.path.dirname(__file__)
            )
            machine.octaves[f"octave{i+1}"] = octave
            octave.initialize_frequency_converters()
            print("Please update the octave settings in: quam.octave")

    # Add the transmon components (xy, z and resonator) to the quam
    for qubit_name, qubit_wiring in machine.wiring.qubits.items():
        # Create all necessary ports
        machine.ports.reference_to_port(qubit_wiring.xy.get_unreferenced_value("digital_port"), create=True)
        machine.ports.reference_to_port(qubit_wiring.xy.get_unreferenced_value("opx_output_I"), create=True)
        machine.ports.reference_to_port(qubit_wiring.xy.get_unreferenced_value("opx_output_Q"), create=True)
        machine.ports.reference_to_port(qubit_wiring.resonator.get_unreferenced_value("opx_output_I"), create=True)
        machine.ports.reference_to_port(qubit_wiring.resonator.get_unreferenced_value("opx_output_Q"), create=True)
        machine.ports.reference_to_port(qubit_wiring.resonator.get_unreferenced_value("opx_input_I"), create=True)
        machine.ports.reference_to_port(qubit_wiring.resonator.get_unreferenced_value("opx_input_Q"), create=True)
        machine.ports.reference_to_port(qubit_wiring.resonator.get_unreferenced_value("digital_port"), create=True)

        # Create qubit components
        transmon = Transmon(
            id=qubit_name,
            xy=IQChannel(
                opx_output_I=qubit_wiring.xy.get_unreferenced_value("opx_output_I"),
                opx_output_Q=qubit_wiring.xy.get_unreferenced_value("opx_output_Q"),
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
                opx_output_I=qubit_wiring.resonator.get_unreferenced_value("opx_output_I"),
                opx_output_Q=qubit_wiring.resonator.get_unreferenced_value("opx_output_Q"),
                opx_input_I=qubit_wiring.resonator.get_unreferenced_value("opx_input_I"),
                opx_input_Q=qubit_wiring.resonator.get_unreferenced_value("opx_input_Q"),
                digital_outputs={
                    "octave_switch": DigitalOutputChannel(
                        opx_output=qubit_wiring.resonator.get_unreferenced_value("digital_port"),
                        delay=87,  # 57ns for QOP222 and above
                        buffer=15,  # 18ns for QOP222 and above
                    )
                },
                opx_input_offset_I=0.0,
                opx_input_offset_Q=0.0,
                frequency_converter_up=qubit_wiring.resonator.frequency_converter_up.get_reference(),
                frequency_converter_down=qubit_wiring.resonator.frequency_converter_down.get_reference(),
                intermediate_frequency=-250 * u.MHz,
                depletion_time=1 * u.us,
            ),
        )
        machine.qubits[transmon.name] = transmon
        machine.active_qubit_names.append(transmon.name)

        # Add default pulses
        add_default_transmon_pulses(transmon)

        RF_output_qubit_xy = transmon.xy.frequency_converter_up
        RF_output_qubit_xy.channel = transmon.xy.get_reference()
        RF_output_qubit_xy.output_mode = "always_on"
        # RF_output_qubit_xy.output_mode = "triggered"
        RF_output_qubit_xy.LO_frequency = 4.7 * u.GHz
        print(f"Please set the LO frequency of {RF_output_qubit_xy.get_reference()}")
        print(f"Please set the output mode of {RF_output_qubit_xy.get_reference()} to always_on or triggered")

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
        cr_control_name = f"cr_control_C{qubit_control_name}_T{qubit_target_name}"
        cr_target_name = f"cr_target_C{qubit_target_name}_T{qubit_control_name}"

        cr_control = CrossResonance(
            id=cr_control_name,
            opx_output_I=qubit_pair_wiring.cr_control.get_unreferenced_value("opx_output_I"),
            opx_output_Q=qubit_pair_wiring.cr_control.get_unreferenced_value("opx_output_Q"),
            frequency_converter_up=qubit_pair_wiring.cr_control.get_unreferenced_value("frequency_converter_up"),
            # intermediate_frequency=qubit_pair_wiring.qubit_target.xy.get_unreferenced_value("intermediate_frequency"),
            intermediate_frequency=f"#/qubits/{qubit_target_name}/xy/intermediate_frequency",
        )
        cr_target = CrossResonance(
            id=cr_target_name,
            opx_output_I=qubit_pair_wiring.cr_target.get_unreferenced_value("opx_output_I"),
            opx_output_Q=qubit_pair_wiring.cr_target.get_unreferenced_value("opx_output_Q"),
            frequency_converter_up=qubit_pair_wiring.cr_target.get_unreferenced_value("frequency_converter_up"),
            # intermediate_frequency=qubit_pair_wiring.qubit_control.xy.get_unreferenced_value("intermediate_frequency"),
            intermediate_frequency=f"#/qubits/{qubit_control_name}/xy/intermediate_frequency",
        )

        # Note: The Q channel is set to the I channel plus one.
        qubit_pair = TransmonPair(
            id=qubit_pair_name,
            qubit_control=qubit_pair_wiring.get_unreferenced_value("qubit_control"),
            qubit_target=qubit_pair_wiring.get_unreferenced_value("qubit_target"),
            cr_control=cr_control,
            cr_target=cr_target,
        )
        machine.qubit_pairs.append(qubit_pair)
        machine.active_qubit_pair_names.append(qubit_pair_name)
        add_default_transmon_pair_pulses(qubit_pair)

    return machine


if __name__ == "__main__":
    folder = Path(__file__).parent
    quam_folder = folder / "quam_state"

    quam_class = FEMQuAM
    # using_opx_1000 = quam_class is FEMQuAM
    # port_allocation = default_port_allocation(
    #     num_qubits=2,
    #     using_opx_1000=using_opx_1000,
    #     starting_fem=3
    # )
    port_allocation = default_port_allocation()
    print(f"{port_allocation=}")
    wiring = create_wiring(port_allocation)
    print(f"{wiring=}")
    machine = create_quam_superconducting(quam_class, wiring)

    machine.save(quam_folder, content_mapping={"wiring.json": {"wiring", "network"}})

    # save the configs to json files
    qua_file = folder / "qua_config.json"
    qua_config = machine.generate_config()
    json.dump(qua_config, qua_file.open("w"), indent=4)

    quam_loaded = QuAM.load(quam_folder)
    qua_config_loaded = quam_loaded.generate_config()
    json.dump(qua_config_loaded, qua_file.open("w"), indent=4)

    # convert json file to python dict with ordered keys
    json_file_path = folder / "qua_config.json"
    python_file_path = folder / "qua_config.py"
    json_to_python_file(json_file_path, python_file_path)

# %%
