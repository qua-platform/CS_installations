import os.path
from typing import Dict, List, Type, TypeVar
from pathlib import Path
import json

from qualang_tools.units import unit
from quam.components import Octave, IQChannel, DigitalOutputChannel
from quam_libs.components import (
    Transmon,
    ReadoutResonator,
    FluxLine,
    QuAM,
    FEMQuAM,
    OPXPlusQuAM,
)

from make_pulses import add_default_transmon_pulses, add_default_transmon_pair_pulses
from make_wiring import default_port_allocation, custom_port_allocation, create_wiring
from quam.components.hardware import FrequencyConverter, LocalOscillator, Mixer

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

    host_ip = "172.16.33.107"
    Cluster_name = "Beta_8"

    # octave_ips = [host_ip] * 1
    # or "192.168.88.X" if configured internally
    octave_ips = ["172.16.33.109"]

    # octave_ports = [11109]  # 11XXX where XXX are the last digits of the Octave IP
    # or 80 if configured internally
    octave_ports = [80] * 1

    machine.network = {
        "host": host_ip,
        "cluster_name": Cluster_name,
        "octave_ips": octave_ips,
        "octave_ports": octave_ports,
        "data_folder": r"C:\Git\QM-CS-Michal\Customers\Lincoln_Labs\data",
    }
    print("Please update the default network settings in: quam.network")

    if octaves is not None:
        machine.octaves = octaves
        print("If you haven't configured the octaves, please run: octave.initialize_frequency_converters()")

    else:
        # Add the Octave to the quam
        for i in range(len(octave_ips)):
            octave = Octave(
                name=f"octave{i+1}",
                ip=machine.network["octave_ips"][i],
                port=machine.network["octave_ports"][i],
                calibration_db_path=os.path.dirname(__file__),
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
        machine.ports.reference_to_port(qubit_wiring.z.get_unreferenced_value("opx_output"), create=True)
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
                frequency_converter_up=FrequencyConverter(
                    local_oscillator=LocalOscillator(frequency=4e9), mixer=Mixer(
                        correction_gain=0,
                        correction_phase=0,
                    )
                ),
                intermediate_frequency=-200 * u.MHz,
                digital_outputs={
                    "switch": DigitalOutputChannel(
                        opx_output=qubit_wiring.xy.get_unreferenced_value("digital_port"),
                        delay=136,
                        buffer=0,
                    )
                },
            ),
            z=FluxLine(opx_output=qubit_wiring.z.get_unreferenced_value("opx_output")),
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

        add_default_transmon_pulses(transmon)

        # RF_output = transmon.xy.frequency_converter_up
        # RF_output.channel = transmon.xy.get_reference()
        # RF_output.output_mode = "always_on"
        # RF_output.LO_frequency = 4 * u.GHz
        # print(f"Please set the LO frequency of {RF_output.get_reference()}")
        # print(f"Please set the output mode of {RF_output.get_reference()} to always_on or triggered")
        if qubit_name=="q0":
            # First readout line
            RF_output_resonator = transmon.resonator.frequency_converter_up
            RF_output_resonator.channel = transmon.resonator.get_reference()
            RF_output_resonator.output_mode = "always_on"
            RF_output_resonator.LO_frequency = 6 * u.GHz
            print(f"Please set the LO frequency of {RF_output_resonator.get_reference()}")
            print(f"Please set the output mode of {RF_output_resonator.get_reference()} to always_on or triggered")

            RF_input_resonator = transmon.resonator.frequency_converter_down
            RF_input_resonator.channel = transmon.resonator.get_reference()
            RF_input_resonator.LO_frequency = RF_output_resonator.LO_frequency  # same LO frequency as Up converter
            if "RF_inputs/2" in RF_input_resonator.get_reference():
                RF_input_resonator.LO_source = 'external'
                print('Dont forget to connect the external LO to Dmd2LO in the Octave back panel')
            else:
                RF_input_resonator.LO_source = 'internal'


            print(f"Please set the LO frequency of {RF_input_resonator.get_reference()}")
        if qubit_name=="q6":
            RF_output_resonator = transmon.resonator.frequency_converter_up
            RF_output_resonator.channel = transmon.resonator.get_reference()
            RF_output_resonator.output_mode = "always_on"
            RF_output_resonator.LO_frequency = 6 * u.GHz
            print(f"Please set the LO frequency of {RF_output_resonator.get_reference()}")
            print(f"Please set the output mode of {RF_output_resonator.get_reference()} to always_on or triggered")

            RF_input_resonator = transmon.resonator.frequency_converter_down
            RF_input_resonator.channel = transmon.resonator.get_reference()
            RF_input_resonator.LO_frequency = RF_output_resonator.LO_frequency  # same LO frequency as Up converter
            if "RF_inputs/2" in RF_input_resonator.get_reference():
                RF_input_resonator.LO_source = 'external'
                print('Dont forget to connect the external LO to Dmd2LO in the Octave back panel')
            else:
                RF_input_resonator.LO_source = 'internal'
            print(f"Please set the LO frequency of {RF_input_resonator.get_reference()}")
    # machine.ports.get_analog_input("con1", 2, 1, create=True)
    # machine.ports.get_analog_input("con1", 2, 2, create=True)

    return machine


if __name__ == "__main__":
    folder = Path(__file__).parent
    quam_folder = folder / "quam_state"

    quam_class = FEMQuAM

    using_opx_1000 = quam_class is FEMQuAM
    # module refers to the FEM number (OPX1000) or OPX+ connection index (OPX+)
    custom_port_wiring = {
        "qubits": {
            "q1": {
                "res": (3, 1, 1, 1),  # (module, i_ch, octave, octave_ch)
                "xy": (3, 5),  # (module, i_ch)
                "flux": (4, 1),  # (module, i_ch)
            },
            "q2": {
                "res": (3, 1, 1, 1),
                "xy": (3, 7),
                "flux": (4, 2),
            },
            # "q3": {
            #     "res": (1, 1, 1, 1),
            #     "xy": (2, 1),
            #     "flux": (5, 3),
            # },
            # "q4": {
            #     "res": (1, 1, 1, 1),
            #     "xy": (2, 3),
            #     "flux": (5, 4),
            # },
            # "q5": {
            #     "res": (1, 1, 1, 1),
            #     "xy": (2, 5),
            #     "flux": (5, 5),
            # },
            # "q6": {
            #     "res": (1, 1, 1, 1),
            #     "xy": (2, 7),
            #     "flux": (5, 6),
            # },
            # "q7": {
            #     "res": (1, 3, 1, 2),
            #     "xy": (3, 1),
            #     "flux": (5, 7),
            # },
            # "q8": {
            #     "res": (1, 3, 1, 2),
            #     "xy": (3, 3),
            #     "flux": (5, 8),
            # },
            # "q9": {
            #     "res": (1, 3, 1, 2),
            #     "xy": (3, 5),
            #     "flux": (6, 1),
            # },
            # "q10": {
            #     "res": (1, 3, 1, 2),
            #     "xy": (3, 7),
            #     "flux": (6, 2),
            # },
            # "q11": {
            #     "res": (1, 3, 1, 2),
            #     "xy": (4, 1),
            #     "flux": (6, 3),
            # },
            # "q12": {
            #     "res": (1, 3, 1, 2),
            #     "xy": (4, 3),
            #     "flux": (6, 4),
            # },
        },
    }

    # port_allocation = default_port_allocation(
    #     num_qubits=2,
    #     using_opx_1000=using_opx_1000,
    #     starting_fem=3
    # )
    port_allocation = custom_port_allocation(custom_port_wiring)
    wiring = create_wiring(port_allocation, using_opx_1000=using_opx_1000)
    machine = create_quam_superconducting(quam_class, wiring)

    machine.save(quam_folder, content_mapping={"wiring.json": {"wiring", "network"}})

    qua_file = folder / "qua_config.json"
    qua_config = machine.generate_config()
    json.dump(qua_config, qua_file.open("w"), indent=4)

    # quam_loaded = QuAM.load(quam_folder)
    # qua_config_loaded = quam_loaded.generate_config()
    # json.dump(qua_config_loaded, qua_file.open("w"), indent=4)
