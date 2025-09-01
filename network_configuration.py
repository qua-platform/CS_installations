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
qop_ip = "192.168.88.249"  # Write the QM router IP address
octave_port = (
    11251  # Must be 11xxx, where xxx are the last three digits of the Octave IP address
)
cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220


#############
# Save Path #
#############
# Path to save data
save_dir = Path(__file__).parent.resolve() / "Data"
save_dir.mkdir(exist_ok=True)

default_additional_files = {
    Path(__file__).name: Path(__file__).name,
    "optimal_weights.npz": "optimal_weights.npz",
}

############################
# OPX/octave configuration #
############################
con = "con1"
oct = "oct1"

# Add the octaves
octaves = [OctaveUnit(oct, qop_ip, port=octave_port, con=con)]
# Configure the Octaves
octave_config = octave_declaration(octaves)
