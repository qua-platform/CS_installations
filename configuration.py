from qualang_tools.units import unit

qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "Cluster_83"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

# Path to save data
octave_config = None

u = unit(coerce_to_integer=True)

#############################################
#        Config Generator Functions         #
#############################################

# Whether it is triggered when RISING (rising edge) or FALLING (falling edge)
polarity = 'FALLING'
# Minimal time between pulses to register a new one (should be between 4ns and 16ns)
deadtime = 16
# Time-tagging voltage threshold (in Volts)
threshold = 0.5


def configure_digital_input(channel_index: int):
    """ This function configures a digital input (OPD) channel """
    return {
        channel_index: {
            'polarity': polarity,
            'deadtime': deadtime,
            'threshold': threshold
        }
    }


def configure_element(element_name: str, channel_index: int):
    """ Configures elements for each SPCM branch. """
    return {
        element_name: {
            # OPD channel input from the SPCM
            'digitalOutputs': {
                'out1': ('con1', channel_index)
            },
            # OPX digital output port to send a TTL signal (for testing purposes)
            'digitalInputs': {
                'output_switch': {
                    'port': ('con1', channel_index),
                    'delay': 100,
                    'buffer': 1,
                },
            },
            'operations': {
                'read_count': 'read_count',  # operation to detect a count in the OPD input
                'test_count': 'fake_count',  # operation to send a TTL signal from the OPX (for testing purposes)
            },
            # dummy OPX analog output (this doesn't get used)
            'singleInput': {
                'port': ('con1', 1),
            },
            # dummy OPX analog input (this doesn't get used)
            "outputs": {
                'port': ('con1', 1)
            },
            # dummy IF (this doesn't get used)
            'intermediate_frequency': 0,
            # dummy parameters (these don't get used)
            "time_of_flight": 36,
            "smearing": 0,
        }
    }


#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},
            },
            "digital_outputs": {
                1: {},
                2: {},
                3: {},
                4: {},
                5: {},
                6: {},
                7: {},
                8: {},
            },
            'digital_inputs': {
                **configure_digital_input(1),  # Alice,  Horizontal
                **configure_digital_input(2),  # Alice,  Vertical
                **configure_digital_input(3),  # Alice,  Diagonal
                **configure_digital_input(4),  # Alice,  Anti-diagonal
                **configure_digital_input(5),  # Bob,    Horizontal
                **configure_digital_input(6),  # Bob,    Vertical
                **configure_digital_input(7),  # Bob,    Diagonal
                **configure_digital_input(8),  # Bob,    Anti-diagonal
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},
            },
        },
    },
    "elements": {
        **configure_element("alice_h", 1),
        **configure_element("alice_v", 2),
        **configure_element("alice_d", 3),
        **configure_element("alice_a", 4),
        **configure_element("bob_h", 5),
        **configure_element("bob_v", 6),
        **configure_element("bob_d", 7),
        **configure_element("bob_a", 8),
    },
    "pulses": {
        'fake_count': {
            'operation': 'control',
            'length': 200,  # ns
            'waveforms': {
                # these purposefully don't generate anything
                'single': 'zero_wf',
            },
            'digital_marker': 'spcm_wf'
        },
        'read_count': {
            'operation': 'measure',
            'length': 200,  # ns
            'waveforms': {
                # these purposefully don't generate anything
                'single': 'zero_wf',
            },
            'digital_marker': 'spcm_wf'
        },
    },
    'digital_waveforms': {
        'spcm_wf': {
            'samples': [(1, 0)]  # rising edge
        },
    },
    "waveforms": {
        "zero_wf": {"type": "constant", "sample": 0.0},
    }
}