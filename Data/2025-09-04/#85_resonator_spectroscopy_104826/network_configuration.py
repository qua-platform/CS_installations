from set_octave import OctaveUnit, octave_declaration
from pathlib import Path


######################
# Network parameters #
######################
# qop_ip = "172.16.33.101"  # Write the QM router IP address
# octave_port = (
#     11232  # Must be 11xxx, where xxx are the last three digits of the Octave IP address
# )
# cluster_name = "CS_1"  # Write your cluster_name if version >= QOP220
qop_ip = "192.168.88.250"  # Write the QM router IP address
octave_port = (
    11246  # Must be 11xxx, where xxx are the last three digits of the Octave IP address
)
cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

############################
# OPX/octave configuration #
############################
con = "con1"
oct = "oct1"

# Add the octaves
octaves = [OctaveUnit(oct, qop_ip, port=octave_port, con=con)]
# Configure the Octaves
octave_config = octave_declaration(octaves)
