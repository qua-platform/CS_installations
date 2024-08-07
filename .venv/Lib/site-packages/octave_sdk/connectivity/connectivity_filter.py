from typing import List

import copy

from octave_sdk.connectivity.exceptions import (
    ExploreResponseException,
)
from octave_sdk.grpc.quantummachines.octave.api.v1 import (
    RfSource,
    OctaveModule,
    ConstantSource,
    IfSource,
    ModuleReference,
    IdentifyResponse,
)

from octave_sdk._octave_client import ExploreResult
from octave_sdk.connectivity.connectivity_util_private import (
    clear_rfsource_synth_output_oneof,
    clear_rfsource_up_conv_oneof,
    clear_ifsource_down_conv_oneof,
    RfSourceType,
    get_rf_source_type,
    IfSourceType,
    get_if_source_type,
    get_rf_source_from_synth_panel_output,
    identity_object_to_module_ref_type_mapping,
)


# Must be called after self._identity_response is copied from the original identity
class FilteredWorkingModules:
    def __init__(
        self,
        identity_response_original: IdentifyResponse,
        explore_result: ExploreResult,
    ) -> None:
        self.identity_response_filtered: IdentifyResponse = copy.deepcopy(identity_response_original)
        self.missing_modules: list(ModuleReference) = []
        self._filter_by_working_modules(explore_result)

    def _filter_by_working_modules(self, explore_result: ExploreResult):
        if not isinstance(explore_result, ExploreResult):
            raise ExploreResponseException("Wrong explore response object")

        # ------Start with plain module removal-----
        self._filter_by_identity_module_and_explore_module(
            self.identity_response_filtered.rf_up_converters,
            explore_result.modules[OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER],
        )
        self._filter_by_identity_module_and_explore_module(
            self.identity_response_filtered.rf_down_converters,
            explore_result.modules[OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER],
        )
        self._filter_by_identity_module_and_explore_module(
            self.identity_response_filtered.if_down_converters,
            explore_result.modules[OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER],
        )
        self._filter_by_identity_module_and_explore_module(
            self.identity_response_filtered.synthesizers, explore_result.modules[OctaveModule.OCTAVE_MODULE_SYNTHESIZER]
        )

        # -----Work on input wiring, go from back to front-----
        synths = [uc.index for uc in self.identity_response_filtered.synthesizers]

        # panel outputs - remove all synths
        self._remove_synths_from_panel_output(synths)

        # RF up - remove all synths
        self._remove_synths_from_rf_up(synths)

        # RF down - remove all synths and Upconv
        self._remove_synths_and_rf_up_from_rf_out(synths)

        # IF down - remove all Down conv
        self._remove_rf_down_from_if()

    def _remove_rf_down_from_if(self):
        rf_ins = [uc.index for uc in self.identity_response_filtered.rf_down_converters]
        if_convs = self.identity_response_filtered.if_down_converters
        for if_conv in if_convs[:]:
            if_source_fields: List[IfSource] = [
                if_source for if_source in vars(if_conv.connectivity).values() if isinstance(if_source, IfSource)
            ]

            for if_source in if_source_fields:
                source_type = get_if_source_type(if_source)
                if source_type == IfSourceType.rf_downconv_if_source:
                    if if_source.rf_downconv_if_source.index not in rf_ins:
                        clear_ifsource_down_conv_oneof(if_source)
                        if_source.constant_source = ConstantSource.CONSTANT_SOURCE_OPEN

    def _remove_synths_and_rf_up_from_rf_out(self, synths):
        rf_outs = [uc.index for uc in self.identity_response_filtered.rf_up_converters]
        down_convs = self.identity_response_filtered.rf_down_converters
        for down_conv in down_convs[:]:
            rf_source_fields: List[RfSource] = [
                rf_source for rf_source in vars(down_conv.connectivity).values() if isinstance(rf_source, RfSource)
            ]

            for rf_source in rf_source_fields:
                source_type = get_rf_source_type(rf_source)
                if source_type == RfSourceType.synth_output:
                    if rf_source.synth_output.index not in synths:
                        clear_rfsource_synth_output_oneof(rf_source)
                        rf_source.constant_source = ConstantSource.CONSTANT_SOURCE_OPEN
                elif source_type == RfSourceType.rf_up_conv_output and rf_source.rf_up_conv_output.index not in rf_outs:
                    clear_rfsource_up_conv_oneof(rf_source)
                    rf_source.constant_source = ConstantSource.CONSTANT_SOURCE_OPEN

    def _remove_synths_from_rf_up(self, synths):
        up_convs = self.identity_response_filtered.rf_up_converters
        for up_conv in up_convs[:]:
            source = up_conv.connectivity.lo_input
            source_type = get_rf_source_type(source)
            if source_type == RfSourceType.synth_output:
                if source.synth_output.index not in synths:
                    up_conv.connectivity.lo_input = RfSource(constant_source=ConstantSource.CONSTANT_SOURCE_OPEN)
            elif source_type == RfSourceType.rf_up_conv_output:
                raise ValueError(f"LO Source {source_type} is not supported")

    def _remove_synths_from_panel_output(self, synths):
        synth_outputs = self.identity_response_filtered.panel_identity.synth_outputs
        remove_list = []
        for panel_synth in synth_outputs:
            source = get_rf_source_from_synth_panel_output(panel_synth.source)
            if source.index not in synths:
                remove_list.append(panel_synth)

        for panel_synth in remove_list:
            synth_outputs.remove(panel_synth)

    def _filter_by_identity_module_and_explore_module(self, identity_modules, explore_modules: ExploreResult):
        index_list = [i for i, v in enumerate(explore_modules) if v is not None]
        remove_list = []
        for module in identity_modules[:]:
            if (module.index - 1) not in index_list:
                self.missing_modules.append(
                    ModuleReference(type=identity_object_to_module_ref_type_mapping[type(module)], index=module.index)
                )
                remove_list.append(module)

        for module in remove_list:
            identity_modules.remove(module)
