from qualang_tools.units import unit

qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "Cluster_83"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

# Path to save data
octave_config = None

u = unit(coerce_to_integer=True)

#############################################
#        Time-tagging Parameters            #
#############################################
# Whether it is triggered when RISING (rising edge) or FALLING (falling edge)
polarity = 'FALLING'
# Minimal time between pulses to register a new one (should be between 4ns and 16ns)
deadtime = 16
# Time-tagging voltage threshold (in Volts)
threshold = 0.5

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
                # 2: {},
                # 3: {},
                # 4: {},
                # 5: {},
                # 6: {},
                # 7: {},
                # 8: {},
            },
            'digital_inputs': {
                1: {'polarity': polarity, 'deadtime': deadtime, "threshold": threshold},  # Alice,  Horizontal
                # 2: {'polarity': polarity, 'deadtime': deadtime, "threshold": threshold},  # Alice,  Vertical
                # 3: {'polarity': polarity, 'deadtime': deadtime, "threshold": threshold},  # Alice,  Diagonal
                # 4: {'polarity': polarity, 'deadtime': deadtime, "threshold": threshold},  # Alice,  Anti-diagonal
                # 5: {'polarity': polarity, 'deadtime': deadtime, "threshold": threshold},  # Bob,    Horizontal
                # 6: {'polarity': polarity, 'deadtime': deadtime, "threshold": threshold},  # Bob,    Vertical
                # 7: {'polarity': polarity, 'deadtime': deadtime, "threshold": threshold},  # Bob,    Diagonal
                # 8: {'polarity': polarity, 'deadtime': deadtime, "threshold": threshold},  # Bob,    Anti-diagonal
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},
            },
        },
    },
    "elements": {
        "alice_h": {
            # dummy OPX analog output
            'singleInput': {
                'port': ('con1', 1),
            },
            # dummy OPX analog input (for TOF)
            "outputs": {
                'port': ('con1', 1)
            },
            'intermediate_frequency': 0,
            # targeting OPD digital input
            'digitalOutputs': { 'out1': ('con1', 1) },
            # to read a count
            'operations': {
                'read_count': 'read_count',
            },
            "time_of_flight": 36,
            "smearing": 0
        },
        # "alice_v": {'digitalOutputs': {'out1': ('con1', 2)}, },
        # "alice_d": {'digitalOutputs': {'out1': ('con1', 3)}, },
        # "alice_a": {'digitalOutputs': {'out1': ('con1', 4)}, },
        # "bob_h": {'digitalOutputs': {'out1': ('con1', 5)}, },
        # "bob_v": {'digitalOutputs': {'out1': ('con1', 6)}, },
        # "bob_d": {'digitalOutputs': {'out1': ('con1', 7)}, },
        # "bob_a": {'digitalOutputs': {'out1': ('con1', 8)}, },

        # dummy elements for simulation purposes
        "spcm_alice_h": {
            'singleInput': {
                'port': ('con1', 1),
            },
            # to send a fake count (rising-edge) from the OPX digital output
            'digitalInputs': {
                'output_switch': {
                    'port': ('con1', 1),
                    'delay': 100,
                    'buffer': 1,
                },
            },
            'operations': {
                'fake_count': 'fake_count',  # to send a fake count
            },
        },
    },
    "pulses": {
        'fake_count': {
            'operation': 'control',
            'length': 200,  # ns
            # these purposefully don't generate anything
            'waveforms': {
                'single': 'zero_wf',
            },
            'digital_marker': 'spcm_wf'
        },
        'read_count': {
            'operation': 'measure',
            'length': 200,  # ns
            # these purposefully don't generate anything
            'waveforms': {
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