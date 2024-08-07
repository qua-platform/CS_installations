from octave_sdk.grpc.quantummachines.octave.api.v1 import (
    IdentifyResponse,
    RfUpConvIdentity,
    RfUpConvIdentityConnectivity,
    IfSource,
    ExternalIfInput,
    RfSource,
    SynthRfOutput,
    SynthRfOutputOutputPort,
    RfUpConvIdentityParameters,
    RfDownConvIdentity,
    RfDownConvIdentityConnectivity,
    UpConvRfOutput,
    ExternalRfInput,
    IfDownConvIdentity,
    IfDownConvIdentityConnectivity,
    IfDownConvIfSource,
    SynthIdentity,
    SynthIdentityConnectivity,
    SynthIdentityParameters,
    SynthIdentityParametersLowFrequencyFilter,
    SynthIdentityParametersParametrizedFilter,
    PanelIdentity,
    PanelIdentityRfOutput,
    PanelIdentitySynthOutput,
    RfDownConvIfSource,
    RfDownConvIfSourceOutputPort,
    ExploreResponse,
    ExploreResponseModuleId,
    ModuleReference,
)


def default_explore_response():
    return ExploreResponse(
        modules=[
            ExploreResponseModuleId(module=ModuleReference(type=1, index=1), id="0025_F"),
            ExploreResponseModuleId(module=ModuleReference(type=1, index=2), id="0024_F"),
            ExploreResponseModuleId(module=ModuleReference(type=1, index=3), id="01170A01F2226006012"),
            ExploreResponseModuleId(module=ModuleReference(type=1, index=4), id="0027_F"),
            ExploreResponseModuleId(module=ModuleReference(type=1, index=5), id="01170A01F2215017712"),
            ExploreResponseModuleId(module=ModuleReference(type=2, index=1), id="2"),
            ExploreResponseModuleId(module=ModuleReference(type=2, index=2), id="3"),
            ExploreResponseModuleId(module=ModuleReference(type=3, index=1), id="0005_A"),
            ExploreResponseModuleId(module=ModuleReference(type=3, index=2), id="0007_A"),
            ExploreResponseModuleId(module=ModuleReference(type=4, index=3), id="0008_B"),
            ExploreResponseModuleId(module=ModuleReference(type=4, index=4), id="22150030_B"),
            ExploreResponseModuleId(module=ModuleReference(type=4, index=5), id="0010_B"),
            ExploreResponseModuleId(module=ModuleReference(type=4, index=6), id="22150023_B"),
            ExploreResponseModuleId(module=ModuleReference(type=5, index=1)),
        ]
    )


def default_identify_response():
    rf_up_converters = [
        RfUpConvIdentity(
            index=1,
            connectivity=RfUpConvIdentityConnectivity(
                i_input=IfSource(external_if_input=ExternalIfInput(i_index=1)),
                q_input=IfSource(external_if_input=ExternalIfInput(q_index=1)),
                lo_input=RfSource(
                    synth_output=SynthRfOutput(index=3, output_port=SynthRfOutputOutputPort.OUTPUT_PORT_MAIN)
                ),
            ),
            parameters=RfUpConvIdentityParameters(0, 0),
        ),
        RfUpConvIdentity(
            index=2,
            connectivity=RfUpConvIdentityConnectivity(
                i_input=IfSource(external_if_input=ExternalIfInput(i_index=2)),
                q_input=IfSource(external_if_input=ExternalIfInput(q_index=2)),
                lo_input=RfSource(
                    synth_output=SynthRfOutput(
                        index=6,
                        output_port=SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY,
                    )
                ),
            ),
            parameters=RfUpConvIdentityParameters(0, 0),
        ),
        RfUpConvIdentity(
            index=3,
            connectivity=RfUpConvIdentityConnectivity(
                i_input=IfSource(external_if_input=ExternalIfInput(i_index=3)),
                q_input=IfSource(external_if_input=ExternalIfInput(q_index=3)),
                lo_input=RfSource(
                    synth_output=SynthRfOutput(index=6, output_port=SynthRfOutputOutputPort.OUTPUT_PORT_MAIN)
                ),
            ),
            parameters=RfUpConvIdentityParameters(0, 0),
        ),
        RfUpConvIdentity(
            index=4,
            connectivity=RfUpConvIdentityConnectivity(
                i_input=IfSource(external_if_input=ExternalIfInput(i_index=4)),
                q_input=IfSource(external_if_input=ExternalIfInput(q_index=4)),
                lo_input=RfSource(
                    synth_output=SynthRfOutput(
                        index=5,
                        output_port=SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY,
                    )
                ),
            ),
            parameters=RfUpConvIdentityParameters(0, 0),
        ),
        RfUpConvIdentity(
            index=5,
            connectivity=RfUpConvIdentityConnectivity(
                i_input=IfSource(external_if_input=ExternalIfInput(i_index=5)),
                q_input=IfSource(external_if_input=ExternalIfInput(q_index=5)),
                lo_input=RfSource(
                    synth_output=SynthRfOutput(index=5, output_port=SynthRfOutputOutputPort.OUTPUT_PORT_MAIN)
                ),
            ),
            parameters=RfUpConvIdentityParameters(0, 0),
        ),
    ]

    rf_down_converters = [
        RfDownConvIdentity(
            index=1,
            connectivity=RfDownConvIdentityConnectivity(
                # debug_rf_input_1=None,
                # debug_rf_input_2=None,
                # debug_rf_input_3=None,
                # debug_rf_input_4=None,
                # debug_rf_input_5=None,
                rf_main_input=RfSource(external_input=ExternalRfInput(rf_in_index=1)),
                lo_input_1=RfSource(
                    synth_output=SynthRfOutput(
                        index=4,
                        output_port=SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY,
                    )
                ),
                lo_input_2=RfSource(
                    synth_output=SynthRfOutput(
                        index=3,
                        output_port=SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY,
                    ),
                ),
            ),
        ),
        RfDownConvIdentity(
            index=2,
            connectivity=RfDownConvIdentityConnectivity(
                debug_rf_input_1=RfSource(rf_up_conv_output=UpConvRfOutput(1)),
                debug_rf_input_2=RfSource(rf_up_conv_output=UpConvRfOutput(2)),
                debug_rf_input_3=RfSource(rf_up_conv_output=UpConvRfOutput(3)),
                debug_rf_input_4=RfSource(rf_up_conv_output=UpConvRfOutput(4)),
                debug_rf_input_5=RfSource(rf_up_conv_output=UpConvRfOutput(5)),
                rf_main_input=RfSource(external_input=ExternalRfInput(rf_in_index=2)),
                lo_input_1=RfSource(
                    synth_output=SynthRfOutput(
                        index=4,
                        output_port=SynthRfOutputOutputPort.OUTPUT_PORT_MAIN,
                    )
                ),
                lo_input_2=RfSource(
                    synth_output=SynthRfOutput(
                        index=4,
                        output_port=SynthRfOutputOutputPort.OUTPUT_PORT_SYNTH,
                    ),
                ),
            ),
        ),
    ]

    if_down_converters = [
        IfDownConvIdentity(
            index=1,
            connectivity=IfDownConvIdentityConnectivity(
                channel_1_input=IfSource(
                    rf_downconv_if_source=RfDownConvIfSource(
                        index=1, output_port=RfDownConvIfSourceOutputPort.OUTPUT_PORT_I
                    )
                ),
                channel_1_lo_input=IfSource(external_if_input=ExternalIfInput(if_lo_i_index=1)),
                channel_2_input=IfSource(
                    rf_downconv_if_source=RfDownConvIfSource(
                        index=1, output_port=RfDownConvIfSourceOutputPort.OUTPUT_PORT_Q
                    )
                ),
                channel_2_lo_input=IfSource(external_if_input=ExternalIfInput(if_lo_q_index=1)),
            ),
        ),
        IfDownConvIdentity(
            index=2,
            connectivity=IfDownConvIdentityConnectivity(
                channel_1_input=IfSource(
                    rf_downconv_if_source=RfDownConvIfSource(
                        index=2, output_port=RfDownConvIfSourceOutputPort.OUTPUT_PORT_I
                    )
                ),
                channel_1_lo_input=IfSource(external_if_input=ExternalIfInput(if_lo_i_index=2)),
                channel_2_input=IfSource(
                    rf_downconv_if_source=RfDownConvIfSource(
                        index=2, output_port=RfDownConvIfSourceOutputPort.OUTPUT_PORT_Q
                    )
                ),
                channel_2_lo_input=IfSource(external_if_input=ExternalIfInput(if_lo_q_index=2)),
            ),
        ),
    ]

    synthesizers = [
        SynthIdentity(
            index=3,
            connectivity=SynthIdentityConnectivity(
                main_lo_input=RfSource(external_input=ExternalRfInput(lo_input_index=1)),
                secondary_lo_input=RfSource(external_input=ExternalRfInput(demod_lo_input_index=1)),
            ),
            parameters=SynthIdentityParameters(
                low_frequency_filters=[SynthIdentityParametersLowFrequencyFilter(index=0, filter_1="1", filter_2="2")],
                medium_frequency_filter=SynthIdentityParametersParametrizedFilter(),
                high_frequency_filter=SynthIdentityParametersParametrizedFilter(),
            ),
        ),
        SynthIdentity(
            index=6,
            connectivity=SynthIdentityConnectivity(
                main_lo_input=RfSource(external_input=ExternalRfInput(lo_input_index=3)),
                secondary_lo_input=RfSource(external_input=ExternalRfInput(lo_input_index=2)),
            ),
            parameters=SynthIdentityParameters(
                low_frequency_filters=[SynthIdentityParametersLowFrequencyFilter(index=0, filter_1="1", filter_2="2")],
                medium_frequency_filter=SynthIdentityParametersParametrizedFilter(),
                high_frequency_filter=SynthIdentityParametersParametrizedFilter(),
            ),
        ),
        SynthIdentity(
            index=5,
            connectivity=SynthIdentityConnectivity(
                main_lo_input=RfSource(external_input=ExternalRfInput(lo_input_index=5)),
                secondary_lo_input=RfSource(external_input=ExternalRfInput(lo_input_index=4)),
            ),
            parameters=SynthIdentityParameters(
                low_frequency_filters=[SynthIdentityParametersLowFrequencyFilter(index=0, filter_1="1", filter_2="2")],
                medium_frequency_filter=SynthIdentityParametersParametrizedFilter(),
                high_frequency_filter=SynthIdentityParametersParametrizedFilter(),
            ),
        ),
        SynthIdentity(
            index=4,
            connectivity=SynthIdentityConnectivity(
                # secondary_lo_input=None,
                main_lo_input=RfSource(external_input=ExternalRfInput(demod_lo_input_index=2)),
            ),
            parameters=SynthIdentityParameters(
                low_frequency_filters=[SynthIdentityParametersLowFrequencyFilter(index=0, filter_1="1", filter_2="2")],
                medium_frequency_filter=SynthIdentityParametersParametrizedFilter(),
                high_frequency_filter=SynthIdentityParametersParametrizedFilter(),
            ),
        ),
    ]

    panel_identity = PanelIdentity(
        rf_outputs=[
            PanelIdentityRfOutput(index=1, source=RfSource(rf_up_conv_output=UpConvRfOutput(index=1))),
            PanelIdentityRfOutput(index=2, source=RfSource(rf_up_conv_output=UpConvRfOutput(index=2))),
            PanelIdentityRfOutput(index=3, source=RfSource(rf_up_conv_output=UpConvRfOutput(index=3))),
            PanelIdentityRfOutput(index=4, source=RfSource(rf_up_conv_output=UpConvRfOutput(index=4))),
            PanelIdentityRfOutput(index=5, source=RfSource(rf_up_conv_output=UpConvRfOutput(index=5))),
        ],
        if_output_i=[IfSource(if_downconv_if_source=IfDownConvIfSource(0, 0))],
        if_output_q=[IfSource(if_downconv_if_source=IfDownConvIfSource(0, 1))],
        synth_outputs=[
            PanelIdentitySynthOutput(
                index=1,
                source=RfSource(
                    synth_output=SynthRfOutput(
                        index=3,
                        output_port=SynthRfOutputOutputPort.OUTPUT_PORT_SYNTH,
                    )
                ),
            ),
            PanelIdentitySynthOutput(
                index=2,
                source=RfSource(
                    synth_output=SynthRfOutput(
                        index=6,
                        output_port=SynthRfOutputOutputPort.OUTPUT_PORT_SYNTH,
                    )
                ),
            ),
            PanelIdentitySynthOutput(
                index=3,
                source=RfSource(
                    synth_output=SynthRfOutput(
                        index=5,
                        output_port=SynthRfOutputOutputPort.OUTPUT_PORT_SYNTH,
                    )
                ),
            ),
        ],
    )
    return IdentifyResponse(
        rf_up_converters,
        rf_down_converters,
        if_down_converters,
        synthesizers,
        panel_identity,
    )
