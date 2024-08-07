from octave_sdk.grpc.quantummachines.octave.api.v1 import OctaveModule, MonitorResponseOctaveError

from octave_sdk._octave_client import ExploreResult, MonitorResult, MonitorData
from octave_sdk.connectivity.connectivity import ModulesSlotsFromIdentity
from octave_sdk.connectivity.connectivity_util import octave_module_to_module_name_mapping, slot_index_to_panel_mapping
from octave_sdk.health_client import HealthClient
import logging

logger = logging.getLogger("qm")


class HealthMonitor:
    # Health Monitor responsible to monitor the Octave HW and update the system connectivity accordingly
    # Use case:
    # create the HealthMonitor, monitor thread will start automatically
    # Use run_once get monitor result and reset the connectivity in the called thread
    # call stop() to request the monitor thread to exit
    #
    # On EVERY change in modules status, the complete print of the monitor result will be showed including errors
    # In case of health return without errors, Health check passed will be printed
    # In case of monitor connection to Octave drop unexpectedly, new connection will be made and error will be printed
    def __init__(
        self, client, name: str, reset_connectivity, slots_list: ModulesSlotsFromIdentity, interval_seconds: int = 5
    ):
        """

        @param client: The Octave client for HW communication
        @param name: The name of the device
        @param reset_connectivity: The function to call in case of reset scenario detected
        @param slots_list: list of slots indexes allowed to be used in this octave
        @param interval_seconds: Health check polling interval, set to 0 for manual check using run_once()
        """
        self._interval_seconds = interval_seconds
        self._client = client
        self._octave_name = name
        self._reset_callback = reset_connectivity
        self._slot_list: ModulesSlotsFromIdentity = slots_list

        self._health_monitor = HealthClient(5, self._client, self._health_update)
        self._health_monitor.run_once()
        self._health_monitor.start()

    def _health_update(self, explore_result: ExploreResult, monitor_result: MonitorResult):
        # int the system with the current modules
        self._reset_callback(explore_result)

        errors_found = False
        max_temp = -300
        for module_name, module_list in monitor_result.modules.items():
            for module_index, monitor_data in enumerate(module_list):
                if monitor_data is not None:
                    if monitor_data.temp > max_temp:
                        max_temp = monitor_data.temp
                    if monitor_data.errors and self._is_module_in_identity(module_name, module_index + 1):
                        errors_found = True
                        self._translate_error_to_string(module_name, module_index + 1, monitor_data)

        if not errors_found:
            logger.info(f'Octave "{self._octave_name}" Health check passed, current temperature {int(max_temp)}')

    def _translate_error_to_string(self, module_name: OctaveModule, module_index: int, monitor_data: MonitorData):
        list_of_errors = "".join(' "' + MonitorResponseOctaveError(err.type).name + '"' for err in monitor_data.errors)

        print_string = (
            f'Octave "{self._octave_name}" {octave_module_to_module_name_mapping[module_name]} index {slot_index_to_panel_mapping(module_index, module_name)} error:'
            + list_of_errors
            + f". temp={monitor_data.temp}"
        )
        logger.warning(print_string)

    # Slot should start from 1
    def _is_module_in_identity(self, name: OctaveModule, slot_index: int):
        slot_list = []

        if name == OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER:
            slot_list = self._slot_list.rf_out_list
        elif name == OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER:
            slot_list = self._slot_list.rf_in_list
        elif name == OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER:
            slot_list = self._slot_list.if_list
        elif name == OctaveModule.OCTAVE_MODULE_SYNTHESIZER:
            slot_list = self._slot_list.synth_list
        elif name == OctaveModule.OCTAVE_MODULE_MOTHERBOARD or name == OctaveModule.OCTAVE_MODULE_SOM:
            slot_list = [1]

        return slot_index in slot_list

    def run_once(self):
        self._health_monitor.run_once()
