from enum import Enum
from octave_sdk.grpc.quantummachines.octave.api.v1 import OctaveModule
from typing import Dict


class RFInputRFSource(Enum):
    """ """

    Loopback_RF_out_1 = 1
    Loopback_RF_out_2 = 2
    Loopback_RF_out_3 = 3
    Loopback_RF_out_4 = 4
    Loopback_RF_out_5 = 5
    RF_in = 6
    Off = 7


synth_slot_index_to_panel_mapping: Dict[int, str] = {
    1: "5",
    2: "6",
    3: "1",
    4: "calibration",
    5: "3",
    6: "2",
}


def slot_index_to_panel_mapping(index: int, module_type: OctaveModule):
    if module_type == OctaveModule.OCTAVE_MODULE_SYNTHESIZER:
        return synth_slot_index_to_panel_mapping[index]

    return index


octave_module_to_module_name_mapping: Dict[OctaveModule, str] = {
    OctaveModule.OCTAVE_MODULE_SYNTHESIZER: "Synthesizer",
    OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER: "IF",
    OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER: "RF Down-converter",
    OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER: "RF Up-converter",
    OctaveModule.OCTAVE_MODULE_SOM: "System",
    OctaveModule.OCTAVE_MODULE_MOTHERBOARD: "Motherboard",
}
