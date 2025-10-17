import matplotlib.pyplot as plt
from qualang_tools.wirer.wirer.channel_specs import *
from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize
from quam_builder.builder.qop_connectivity import build_quam_wiring
from quam_builder.builder.superconducting import build_quam
from quam_config import Quam
from quam_builder.architecture.superconducting.qubit.fixed_frequency_transmon import FixedFrequencyTransmon
from quam_builder.architecture.superconducting.qubit_pair.fixed_frequency_transmon_pair import FixedFrequencyTransmonPair
from quam_builder.architecture.superconducting.qpu.fixed_frequency_quam import FixedFrequencyQuam

lf_fem1 = 1
lf_fem2 = 2

mw_fem1 = 3
mw_fem2 = 4
mw_fem3 = 5


########################################################################################################################
# %%                                              Define static parameters
########################################################################################################################
host_ip = "127.0.0.1"  # QOP IP address
port = None  # QOP Port
cluster_name = "Cluster_1"  # Name of the cluster

########################################################################################################################
# %%                                      Define the available instrument setup
########################################################################################################################
instruments = Instruments()
instruments.add_mw_fem(controller=1, slots=[mw_fem1, mw_fem2, mw_fem3])
instruments.add_lf_fem(controller=1, slots=[lf_fem1, lf_fem2])

########################################################################################################################
# %%                                 Define which qubit ids are present in the system
########################################################################################################################
qubits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

# index of qubits with different resonator port 
# from main (MW-FEM 1, AO1, AI1) to alt (MW-FEM 1, AO8, AI2)
qubit_alt_rr_idx = [3, 4, 8, 12, 16, 20, 21]
qubit_main_rr_idx = list(set(qubits) - set(qubit_alt_rr_idx))
########################################################################################################################
# %%                                 Define any custom/hardcoded channel addresses
########################################################################################################################
# Main readout channel MW-FEM 1 (in slot 3), AO1, AI1
qMain_res_ch = mw_fem_spec(con=1, slot=mw_fem1, in_port=1, out_port=1)
# Second readout channel MW-FEM 1 (in slot 3), AO8, AI2
qAlt_res_ch = mw_fem_spec(con=1, slot=mw_fem1, in_port=2, out_port=8)
# individual xy drive for qubits 1 to 4 on MW-FEM 1
q1to3_drive_ch = mw_fem_spec(con=1, slot=mw_fem1, in_port=None, out_port=2)
q4to6_drive_ch = mw_fem_spec(con=1, slot=mw_fem2, in_port=None, out_port=1)
q7_9_drive_ch = mw_fem_spec(con=1, slot=mw_fem3, in_port=None, out_port=1)
q8_13_drive_ch = mw_fem_spec(con=1, slot=mw_fem1, in_port=None, out_port=4)
q10_19_drive_ch = mw_fem_spec(con=1, slot=mw_fem2, in_port=None, out_port=2)
q11_17_drive_ch = mw_fem_spec(con = 1, slot = mw_fem1, in_port = None, out_port = 5)
q12_18_drive_ch = mw_fem_spec(con = 1, slot = mw_fem1, in_port = None, out_port = 6)
q14_20_drive_ch = mw_fem_spec(con = 1, slot = mw_fem2, in_port = None, out_port = 3)
q15_drive_ch = mw_fem_spec(con = 1, slot = mw_fem1, in_port = None, out_port = 7)
q16_drive_ch = mw_fem_spec(con = 1, slot = mw_fem1, in_port = None, out_port = 3)
qC6_drive_ch = mw_fem_spec(con = 1, slot = mw_fem2, in_port = None, out_port = 2)

c1_parametric_ch = lf_fem_spec( con = 1, out_slot = lf_fem1, in_port = None, out_port = 1)
c2_parametric_ch = lf_fem_spec( con = 1, out_slot = lf_fem1, in_port = None, out_port = 3)
c3_parametric_ch = lf_fem_spec( con = 1, out_slot = lf_fem1, in_port = None, out_port = 4)
c4_parametric_ch = lf_fem_spec( con = 1, out_slot = lf_fem1, in_port = None, out_port = 2)
c5_parametric_ch = lf_fem_spec( con = 1, out_slot = lf_fem1, in_port = None, out_port = 2) # c4 and c5 share
c6_parametric_ch = lf_fem_spec( con = 1, out_slot = lf_fem2, in_port = None, out_port = 1)
c7_parametric_ch = lf_fem_spec( con = 1, out_slot = lf_fem2, in_port = None, out_port = 1) # c6 and c7 share
c8_parametric_ch = lf_fem_spec( con = 1, out_slot = lf_fem2, in_port = None, out_port = 2)
c9_parametric_ch = lf_fem_spec( con = 1, out_slot = lf_fem1, in_port = None, out_port = 1) # c1 and c9 share
c10_parametric_ch = lf_fem_spec( con = 1, out_slot = lf_fem2, in_port = None, out_port = 2) # c8 and c10 share

########################################################################################################################
# %%                Allocate the wiring to the connectivity object based on the available instruments
########################################################################################################################
connectivity = Connectivity()

# The readout lines
connectivity.add_resonator_line(qubits=qubit_main_rr_idx, constraints=qMain_res_ch)
connectivity.add_resonator_line(qubits=qubit_alt_rr_idx, constraints=qAlt_res_ch)

# The xy drive lines  
for qubit in [1,2,3]:  
    connectivity.add_qubit_drive_lines(qubits=qubit, constraints=q1to3_drive_ch)
    allocate_wiring(connectivity, instruments, block_used_channels=False)
for qubit in [4,5,6]:
    connectivity.add_qubit_drive_lines(qubits=qubit, constraints=q4to6_drive_ch)
    allocate_wiring(connectivity, instruments, block_used_channels=False)
for qubit in [7,9]:
    connectivity.add_qubit_drive_lines(qubits=qubit, constraints=q7_9_drive_ch)
    allocate_wiring(connectivity, instruments, block_used_channels=False)
for qubit in [8, 13]:
    connectivity.add_qubit_drive_lines(qubits=qubit, constraints=q8_13_drive_ch)
    allocate_wiring(connectivity, instruments, block_used_channels=False)
for qubit in [10, 19]:
    connectivity.add_qubit_drive_lines(qubits=qubit, constraints=q10_19_drive_ch)
    allocate_wiring(connectivity, instruments, block_used_channels=False)
for qubit in [11, 17]:
    connectivity.add_qubit_drive_lines(qubits=qubit, constraints=q11_17_drive_ch)
    allocate_wiring(connectivity, instruments, block_used_channels=False)
for qubit in [12, 18]:
    connectivity.add_qubit_drive_lines(qubits=qubit, constraints=q12_18_drive_ch)
    allocate_wiring(connectivity, instruments, block_used_channels=False)
for qubit in [14, 20]:
    connectivity.add_qubit_drive_lines(qubits=qubit, constraints=q14_20_drive_ch)
    allocate_wiring(connectivity, instruments, block_used_channels=False)
    
connectivity.add_qubit_drive_lines(qubits=[21], constraints=qC6_drive_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_drive_lines(qubits=[15], constraints=q15_drive_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_drive_lines(qubits=[16], constraints=q16_drive_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)

# The parametric drive lines for 2-qubit gates
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (2,1), constraints = c1_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (1,2), constraints = c1_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (5,1), constraints = c1_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (1,5), constraints = c1_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (6,1), constraints = c1_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (1,6), constraints = c1_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (5,2), constraints = c1_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (2,5), constraints = c1_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (6,2), constraints = c1_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (2,6), constraints = c1_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (6,5), constraints = c1_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (5,6), constraints = c1_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)

# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (3,2), constraints = c2_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (2,3), constraints = c2_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (6,2), constraints = c2_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (2,6), constraints = c2_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (7,2), constraints = c2_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (2,7), constraints = c2_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (6,3), constraints = c2_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (3,6), constraints = c2_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (7,3), constraints = c2_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (3,7), constraints = c2_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (7,6), constraints = c2_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (6,7), constraints = c2_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)

# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (4,3), constraints = c3_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (3,4), constraints = c3_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (7,3), constraints = c3_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (3,7), constraints = c3_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (8,3), constraints = c3_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (3,8), constraints = c3_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (7,4), constraints = c3_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (4,7), constraints = c3_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (8,4), constraints = c3_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (4,8), constraints = c3_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (8,7), constraints = c3_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (7,8), constraints = c3_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)

###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (6,5), constraints = c4_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (5,6), constraints = c4_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# ###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (9,5), constraints = c4_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (5,9), constraints = c4_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (10,5), constraints = c4_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (5,10), constraints = c4_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (9,6), constraints = c4_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (6,9), constraints = c4_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (10,6), constraints = c4_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (6,10), constraints = c4_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (10,9), constraints = c4_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (9,10), constraints = c4_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)

# ###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (8,7), constraints = c5_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (7,8), constraints = c5_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (11,7), constraints = c5_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (7,11), constraints = c5_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (12,7), constraints = c5_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (7,12), constraints = c5_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (11,8), constraints = c5_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (8,11), constraints = c5_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (12,8), constraints = c5_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (8,12), constraints = c5_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (12,11), constraints = c5_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (11,12), constraints = c5_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)

###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (10,9), constraints = c6_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (9,10), constraints = c6_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (13,9), constraints = c6_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (9,13), constraints = c6_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (14,9), constraints = c6_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (9,14), constraints = c6_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (13,10), constraints = c6_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (10,13), constraints = c6_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (14,10), constraints = c6_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (10,14), constraints = c6_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (14,13), constraints = c6_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (13,14), constraints = c6_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)

###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (12,11), constraints = c7_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (11,12), constraints = c7_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (15,11), constraints = c7_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (11,15), constraints = c7_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (16,11), constraints = c7_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (11,16), constraints = c7_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (15,12), constraints = c7_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (12,15), constraints = c7_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (16,12), constraints = c7_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (12,16), constraints = c7_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (16,15), constraints = c7_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (15,16), constraints = c7_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)

###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (14,13), constraints = c8_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (13,14), constraints = c8_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (17,13), constraints = c8_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (13,17), constraints = c8_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (18,13), constraints = c8_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (13,18), constraints = c8_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (17,14), constraints = c8_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (14,17), constraints = c8_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (18,14), constraints = c8_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (14,18), constraints = c8_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (18,17), constraints = c8_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (17,18), constraints = c8_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)

# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (15,14), constraints = c9_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (14,15), constraints = c9_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (18,14), constraints = c9_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (14,18), constraints = c9_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (19,14), constraints = c9_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (14,19), constraints = c9_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (18,15), constraints = c9_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (15,18), constraints = c9_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (19,15), constraints = c9_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (15,19), constraints = c9_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (19,18), constraints = c9_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (18,19), constraints = c9_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)

###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (16,15), constraints = c10_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (15,16), constraints = c10_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (19,15), constraints = c10_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (15,19), constraints = c10_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
###
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (20,15), constraints = c10_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (15,20), constraints = c10_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (19,16), constraints = c10_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (16,19), constraints = c10_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (20,16), constraints = c10_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (16,20), constraints = c10_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)
# connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (20,19), constraints = c10_parametric_ch)
# allocate_wiring(connectivity, instruments, block_used_channels=False)
connectivity.add_qubit_pair_parametric_drive_lines(qubit_pairs = (19,20), constraints = c10_parametric_ch)
allocate_wiring(connectivity, instruments, block_used_channels=False)

# Allocate the wiring
allocate_wiring(connectivity, instruments)

# View wiring schematic
#visualize(connectivity.elements, available_channels=instruments.available_channels)
#plt.show(block=False)

########################################################################################################################
# %%                                   Build the wiring and QUAM
########################################################################################################################
user_input = input("Do you want to save the updated QUAM? (y/n)")
if user_input.lower() == "y":
    machine = FixedFrequencyQuam()
    # Build the wiring (wiring.json) and initiate the QUAM
    build_quam_wiring(connectivity, host_ip, cluster_name, machine)

    # Reload QUAM, build the QUAM object and save the state as state.json
    machine = Quam.load()
    machine.qubit_type = FixedFrequencyTransmon
    machine.qubit_pair_type = FixedFrequencyTransmonPair
    build_quam(machine)
    print("QUAM saved successfully")