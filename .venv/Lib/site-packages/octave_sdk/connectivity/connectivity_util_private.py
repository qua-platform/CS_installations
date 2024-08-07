import betterproto
from enum import Enum
from octave_sdk.grpc.quantummachines.octave.api.v1 import (
    RfSource,
    IfSource,
    SynthRfOutput,
    RfUpConvIdentity,
    RfDownConvIdentity,
    IfDownConvIdentity,
    SynthIdentity,
    OctaveModule,
)

from octave_sdk.connectivity.exceptions import (
    ConnectivityException,
    InvalidIdentityException,
    RfSourceTypeException,
    ExternalInputTypeException,
)
from octave_sdk.connectivity.connectivity_util import RFInputRFSource


# Found in grpc, but not in betterproto :/, should be used for connectivity identify parsing and NOT grpc communication
def clear_rfsource_synth_output_oneof(rf_source: RfSource):
    rf_source.synth_output.index = 0
    rf_source.synth_output.output_port = 0


# Found in grpc, but not in betterproto :/, should be used for connectivity identify parsing and NOT grpc communication
def clear_rfsource_up_conv_oneof(rf_source: RfSource):
    rf_source.rf_up_conv_output.index = 0


# Found in grpc, but not in betterproto :/, should be used for connectivity identify parsing and NOT grpc communication
def clear_ifsource_down_conv_oneof(if_source: IfSource):
    if_source.rf_downconv_if_source.index = 0
    if_source.if_downconv_if_source.channel_index = 0


# Convert gRPC RfSource oneof to local enum
class RfSourceType(str, Enum):
    rf_up_conv_output = "rf_up_conv_output"
    synth_output = "synth_output"
    external_input = "external_input"
    constant_source = "constant_source"


# Convert gRPC IfSource oneof to local enum
class IfSourceType(str, Enum):
    rf_downconv_if_source = "rf_downconv_if_source"
    if_downconv_if_source = "if_downconv_if_source"
    external_if_input = "external_if_input"
    constant_source = "constant_source"


def get_rf_source_type(rf_source: RfSource) -> RfSourceType:
    one_of, _ = betterproto.which_one_of(rf_source, "source")
    return one_of


def get_if_source_type(if_source: IfSource) -> IfSourceType:
    one_of, _ = betterproto.which_one_of(if_source, "source")
    return one_of


def validate_rf_source_type(rf_source, rf_source_types, message):
    one_of, value = betterproto.which_one_of(rf_source, "source")
    if one_of not in rf_source_types:
        raise InvalidIdentityException(f"{message} - {one_of}")


def get_rf_source_name(rf_source: RfSource) -> RFInputRFSource:
    one_of, value = betterproto.which_one_of(rf_source, "source")

    if one_of == "rf_up_conv_output":
        try:
            return RFInputRFSource(value.index)
        except KeyError:
            raise ConnectivityException("up converter index is not valid")
    elif one_of == "external_input":
        external_one_of, external_value = betterproto.which_one_of(value, "input")
        if external_one_of == "rf_in_index":
            return RFInputRFSource.RF_in
        else:
            raise ExternalInputTypeException("external input is not valid")
    elif one_of == "constant_source":
        return RFInputRFSource.Off
    else:
        # "synth_output" not supported
        raise RfSourceTypeException("rf source is not supported")


def get_rf_source_from_synth_panel_output(rf_source: RfSource) -> SynthRfOutput:
    one_of, value = betterproto.which_one_of(rf_source, "source")

    if one_of == "synth_output":
        return value
    else:
        # "rf_up_conv_output" and "constant_source"
        # and "external_input" are not supported
        raise RfSourceTypeException("rf source is not supported")


identity_object_to_module_ref_type_mapping = {
    RfUpConvIdentity: OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER,
    RfDownConvIdentity: OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER,
    IfDownConvIdentity: OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER,
    SynthIdentity: OctaveModule.OCTAVE_MODULE_SYNTHESIZER,
}
