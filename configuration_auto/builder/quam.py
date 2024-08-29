from pathlib import Path
from typing import Union

from configuration_auto.builder.pulses import add_default_transmon_pulses, add_default_transmon_pair_pulses
from configuration_auto.builder.transmons.add_transmon_drive_component import add_transmon_drive_component
from configuration_auto.builder.transmons.add_transmon_flux_component import add_transmon_flux_component
from configuration_auto.builder.transmons.add_transmon_resonator_component import add_transmon_resonator_component
from configuration_auto.builder.wiring.create_wiring import create_wiring
from qualang_tools.wirer import Connectivity
from qualang_tools.wirer.connectivity.wiring_spec import WiringLineType
from quam_libs.components import OPXPlusQuAM, FEMQuAM, QuAM, Transmon, TransmonPair


def build_quam(connectivity: Connectivity, host_ip: str, cluster_name: str,
               quam_state_path: Union[Path, str]) -> QuAM:

    machine = create_base_machine(connectivity)
    add_name_and_ip(machine, cluster_name, host_ip)
    machine.wiring = create_wiring(connectivity)
    add_ports(machine)
    add_transmons(machine)
    add_pulses(machine)
    add_octaves(machine, connectivity)

    save_machine(machine, quam_state_path)

    return machine

def create_base_machine(connectivity: Connectivity):
    """
    Detects whether the `connectivity` is using OPX+ or OPX1000 and returns
    the corresponding base object. Otherwise, raises a TypeError.
    """
    for element in connectivity.elements.values():
        for channels in element.channels.values():
            for channel in channels:
                if channel.instrument_id in ["lf-fem", "mw-fem"]:
                    return FEMQuAM()
                elif channel.instrument_id in ["opx+"]:
                    return OPXPlusQuAM()

    raise TypeError("Couldn't identify connectivity as OPX+ or LF-FEM. "
                    "Are channels were allocated for the connectivity?")


def add_name_and_ip(machine: QuAM, host_ip: str, cluster_name: str):
    """ Stores the minimal information to connect to a QuantumMachinesManager. """
    machine.network = {
        "host": host_ip,
        "cluster_name": cluster_name
    }


def add_ports(machine: QuAM):
    """
    Creates and stores all input/output ports according to what has been
    allocated to each element in the machine's wiring.
    """
    for wiring_by_element in machine.wiring.values():
        for wiring_by_line_type in wiring_by_element.values():
            for ports in wiring_by_line_type.values():
                for port in ports:
                    machine.ports.reference_to_port(
                        ports.get_unreferenced_value(port),
                        create=True
                    )

def add_transmons(machine: QuAM):
    for element_type, wiring_by_element in machine.wiring.items():
        if element_type == 'qubits':
            for qubit_id, wiring_by_line_type in wiring_by_element.items():
                transmon = Transmon(id=qubit_id)
                for line_type, ports in wiring_by_line_type.items():
                    wiring_path = f"#/wiring/{element_type}/{qubit_id}/{line_type}"
                    if line_type == WiringLineType.RESONATOR.value:
                        add_transmon_resonator_component(transmon, wiring_path, ports)
                    elif line_type == WiringLineType.DRIVE.value:
                        add_transmon_drive_component(transmon, wiring_path, ports)
                    elif line_type == WiringLineType.FLUX.value:
                        add_transmon_flux_component(transmon, wiring_path, ports)
                    else:
                        raise ValueError(f'Unknown line type: {line_type}')
                machine.qubits[qubit_id] = transmon
                machine.active_qubit_names.append(transmon.name)

        elif element_type == 'qubit_pairs':
            for qubit_pair_id, wiring_by_line_type in wiring_by_element.items():
                transmon_pair = TransmonPair(id=qubit_pair_id)
                for line_type, ports in wiring_by_line_type.items():
                    wiring_path = f"#/wiring/{element_type}/{qubit_id}/{line_type}"
                    if line_type == WiringLineType.COUPLER.value:
                        add_transmon_pair_component(transmon_pair, wiring_path, ports)
                    else:
                        raise ValueError(f'Unknown line type: {line_type}')
                machine.qubits[qubit_id] = transmon
                machine.active_qubit_names.append(transmon.name)

    pass
    # # Add qubit pairs along with couplers
    # for i, qubit_pair_wiring in enumerate(machine.wiring.qubit_pairs):
    #     qubit_control_name = qubit_pair_wiring.qubit_control.name
    #     qubit_target_name = qubit_pair_wiring.qubit_target.name
    #     qubit_pair_name = f"{qubit_control_name}_{qubit_target_name}"
    #     coupler_name = f"coupler_{qubit_pair_name}"
    #
    #     machine.ports.reference_to_port(qubit_pair_wiring.coupler.get_unreferenced_value("opx_output"), create=True)
    #
    #     coupler = TunableCoupler(
    #         id=coupler_name, opx_output=qubit_pair_wiring.coupler.get_unreferenced_value("opx_output")
    #     )
    #
    #     # Note: The Q channel is set to the I channel plus one.
    #     qubit_pair = TransmonPair(
    #         id=qubit_pair_name,
    #         qubit_control=qubit_pair_wiring.get_unreferenced_value("qubit_control"),
    #         qubit_target=qubit_pair_wiring.get_unreferenced_value("qubit_target"),
    #         coupler=coupler,
    #     )
    #     machine.qubit_pairs.append(qubit_pair)
    #     machine.active_qubit_pair_names.append(qubit_pair_name)

    # # Add additional input ports for calibrating the mixers
    # print(qubit_wiring.xy.frequency_converter_up.get_reference())
    #
    # # if using_opx_1000:
    # #     machine.ports.get_analog_input("con1", 2, 1, create=True)
    # #     machine.ports.get_analog_input("con1", 2, 2, create=True)
    # # else:


def add_pulses(machine: QuAM):
    if hasattr(machine, 'qubits'):
        for transmon in machine.qubits.values():
            add_default_transmon_pulses(transmon)

    if hasattr(machine, 'qubit_pairs'):
        for qubit_pair in machine.qubit_pairs:
            add_default_transmon_pair_pulses(qubit_pair)

def add_octaves(machine: QuAM, connectivity: Connectivity):
    # for i in range(len(octave_ips)):
    #     octave = Octave(
    #         name=f"octave{i + 1}",
    #         ip=machine.network["octave_ips"][i],
    #         port=machine.network["octave_ports"][i],
    #         calibration_db_path=os.path.dirname(__file__),
    #     )
    #     machine.octaves[f"octave{i + 1}"] = octave
    #     octave.initialize_frequency_converters()
    #     print("Please update the octave settings in: quam.octave")

    return machine


def save_machine(machine: QuAM, quam_state_path: Union[Path, str]):
    machine.save(
        path=quam_state_path,
        content_mapping={
            "wiring.json": ["network", "wiring"]
        }
    )


