from octave_sdk.grpc.quantummachines.octave.api.v1 import (
    SynthUpdate,
    OctaveModule,
    SingleUpdate,
    ModuleReference,
)


# This function is shared between the octave and the octave_conflicts module, so it moved to this shared location
def _get_synth_state(client, synth_index):
    response: SingleUpdate = client.aquire_modules(
        [ModuleReference(type=OctaveModule.OCTAVE_MODULE_SYNTHESIZER, index=synth_index)]
    )
    synth_state = response.synth
    if isinstance(synth_state, SynthUpdate):
        return synth_state
    else:
        raise Exception("could not get synth state")
