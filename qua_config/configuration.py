######################
# Network parameters #
#######################
qop_ip = "127.0.0.1" # "192.168.88.252"  # Write the QM router IP address
cluster_name = "Cluster_1" # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": +0.0},
            },
        }
    },
    "elements": {
        "qe": {
            "singleInput": {"port": ("con1", 1)},
            "operations": {
                "cw": "const_pulse",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 1000,  # in ns
            "waveforms": {"single": "const_wf"},
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": 0.1},
    },
}
