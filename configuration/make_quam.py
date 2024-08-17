import os.path
from typing import Dict, List, Type, TypeVar
from pathlib import Path
import json
from quam.core import QuamRoot
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
from make_wiring import default_port_allocation, custom_port_allocation, create_wiring, create_ports_from_wiring, create_network_connectivity, create_octaves
from quam.components.hardware import FrequencyConverter, LocalOscillator, Mixer

# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)

# Define the QuAM type
QuamTypes = TypeVar("QuamTypes", OPXPlusQuAM, FEMQuAM)

def port_wiring(default_port_wiring=True):
    if default_port_wiring:
        port_allocation = default_port_allocation(
            num_qubits=2,
            using_opx_1000=using_opx_1000,
            starting_fem=3
        )
    else:
        custom_port_wiring = {
            "qubits": {
                "q0": {
                    "res": (1, 1, 1, 1),  # (module, i_ch, octave, octave_ch)
                    "xy": (1, 5),  # (module, i_ch)
                    "flux": (5, 1),  # (module, i_ch)
                },
                "q1": {
                    "res": (1, 1, 1, 1),
                    "xy": (1, 7),
                    "flux": (5, 2),
                },
                "q2": {
                    "res": (1, 1, 1, 1),
                    "xy": (2, 1),
                    "flux": (5, 3),
                },
                "q3": {
                    "res": (1, 1, 1, 1),
                    "xy": (2, 3),
                    "flux": (5, 4),
                },
                "q4": {
                    "res": (1, 1, 1, 1),
                    "xy": (2, 5),
                    "flux": (5, 5),
                },
                "q5": {
                    "res": (1, 1, 1, 1),
                    "xy": (2, 7),
                    "flux": (5, 6),
                },
                "q6": {
                    "res": (1, 3, 1, 2),
                    "xy": (3, 1),
                    "flux": (5, 7),
                },
                "q7": {
                    "res": (1, 3, 1, 2),
                    "xy": (3, 3),
                    "flux": (5, 8),
                },
                "q8": {
                    "res": (1, 3, 1, 2),
                    "xy": (3, 5),
                    "flux": (6, 1),
                },
                "q9": {
                    "res": (1, 3, 1, 2),
                    "xy": (3, 7),
                    "flux": (6, 2),
                },
                "q10": {
                    "res": (1, 3, 1, 2),
                    "xy": (4, 1),
                    "flux": (6, 3),
                },
                "q11": {
                    "res": (1, 3, 1, 2),
                    "xy": (4, 3),
                    "flux": (6, 4),
                },
            },
        }
        port_allocation = custom_port_allocation(custom_port_wiring)
    return port_allocation

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
    # Create network connectivity
    machine.network = create_network_connectivity(machine,
                                                  host_ip="172.16.33.107",
                                                  Cluster_name="Beta_8",
                                                  octave_ips=["172.16.33.109"],
                                                  octave_ports=[80] * 1)
    # Create Octaves
    create_octaves(machine, octaves=octaves)
    # Create port wiring
    create_ports_from_wiring(machine, wiring)


    for qubit_name, qubit_wiring in machine.wiring.qubits.items():

        # Create qubit components
        transmon = Transmon(id=qubit_name)
        machine.qubits[transmon.name] = transmon
        machine.active_qubit_names.append(transmon.name)

        transmon.xy = IQChannel(
            opx_output_I=qubit_wiring.xy.get_reference("opx_output_I"),
            opx_output_Q=qubit_wiring.xy.get_reference("opx_output_Q"),
            frequency_converter_up=FrequencyConverter(
                local_oscillator=LocalOscillator(frequency=4e9), mixer=Mixer(
                    correction_gain=0,
                    correction_phase=0,
                )
            ),
            intermediate_frequency=-200 * u.MHz,
            digital_outputs={
                "octave_switch": DigitalOutputChannel(
                    opx_output=qubit_wiring.xy.get_reference("digital_port"),
                    delay=87,  # 57ns for QOP222 and above
                    buffer=15,  # 18ns for QOP222 and above
                )
            },
        )

        if "z" in qubit_wiring:
            transmon.z = FluxLine(opx_output=qubit_wiring.z.get_reference("opx_output"))

        transmon.resonator = ReadoutResonator(
            opx_output_I=qubit_wiring.resonator.get_reference("opx_output_I"),
            opx_output_Q=qubit_wiring.resonator.get_reference("opx_output_Q"),
            opx_input_I=qubit_wiring.resonator.get_reference("opx_input_I"),
            opx_input_Q=qubit_wiring.resonator.get_reference("opx_input_Q"),
            digital_outputs={
                "octave_switch": DigitalOutputChannel(
                    opx_output=qubit_wiring.resonator.get_reference("digital_port"),
                    delay=87,  # 57ns for QOP222 and above
                    buffer=15,  # 18ns for QOP222 and above
                )
            },
            opx_input_offset_I=0.0,
            opx_input_offset_Q=0.0,
            frequency_converter_up=qubit_wiring.resonator.get_reference(
                "frequency_converter_up"
            ),
            frequency_converter_down=qubit_wiring.resonator.get_reference(
                "frequency_converter_down"
            ),
            intermediate_frequency=-250 * u.MHz,
            depletion_time=1 * u.us,
        )

        # Create pulses
        add_default_transmon_pulses(transmon)

        # Configure Octaves
        if qubit_name in ["q0", "q6"]:
            # First readout line
            RF_output_resonator = transmon.resonator.frequency_converter_up
            RF_output_resonator.channel = transmon.resonator.get_reference()
            RF_output_resonator.output_mode = "always_on"
            RF_output_resonator.LO_frequency = 6 * u.GHz
            print("-" * 50)
            print(f"Please set the LO frequency and output mode of {RF_output_resonator.get_reference()}")

            RF_input_resonator = transmon.resonator.frequency_converter_down
            RF_input_resonator.channel = transmon.resonator.get_reference()
            RF_input_resonator.LO_frequency = RF_output_resonator.LO_frequency  # same LO frequency as Up converter

            if RF_input_resonator.LO_source == 'external':
                print('Dont forget to connect the external LO to Dmd2LO in the Octave back panel')

    # machine.ports.get_analog_input("con1", 2, 1, create=True)
    # machine.ports.get_analog_input("con1", 2, 2, create=True)

    return machine


if __name__ == "__main__":
    folder = Path(__file__).parent
    quam_folder = folder / "quam_state"

    quam_class = FEMQuAM

    using_opx_1000 = quam_class is FEMQuAM

    port_allocation = port_wiring(default_port_wiring=False)
    wiring = create_wiring(port_allocation, using_opx_1000=using_opx_1000)
    machine = create_quam_superconducting(quam_class, wiring)

    machine.save(quam_folder, content_mapping={"wiring.json": {"wiring", "network"}})

    qua_file = folder / "qua_config.json"
    qua_config = machine.generate_config()
    json.dump(qua_config, qua_file.open("w"), indent=4)

    quam_loaded = QuAM.load(quam_folder)
    qua_config_loaded = quam_loaded.generate_config()
    json.dump(qua_config_loaded, qua_file.open("w"), indent=4)
