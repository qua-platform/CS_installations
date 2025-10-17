from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from importlib import reload
# import configuration_for_QM
# reload(configuration_for_QM)
# from configuration_for_QM import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
from qualang_tools.plot.fitting import Fit
import numpy as np
from quam_config import Quam
from qualang_tools.addons.variables import assign_variables_to_element
from qm_saas import QmSaas, QOPVersion, ClusterConfig        
from qualang_tools.units import unit
from pathlib import Path

u = unit(coerce_to_integer=True)

def qua_declaration(nb_of_qubits):
    """
    Macro to declare the necessary QUA variables

    :param nb_of_qubits: Number of qubits used in this experiment
    :return:
    """
    n = declare(int)
    n_st = declare_stream()
    I = [declare(fixed) for _ in range(nb_of_qubits)]
    Q = [declare(fixed) for _ in range(nb_of_qubits)]
    I_st = [declare_stream() for _ in range(nb_of_qubits)]
    Q_st = [declare_stream() for _ in range(nb_of_qubits)]
    # Workaround to manually assign the results variables to the readout elements
    for i in range(nb_of_qubits):
        assign_variables_to_element(f"q{i + 1}.resonator", I[i], Q[i])
    return I, I_st, Q, Q_st, n, n_st

def multiplexed_readout(I, I_st, Q, Q_st, resonators, sequential=False, amplitude=1.0, weights="iw"):
    """Perform multiplexed readout on two resonators"""
    if type(resonators) is not list:
        resonators = [resonators]

    for ind, res in enumerate(resonators):
        measure(
            "readout" * amp(amplitude),
            f"q{res}.resonator",
            dual_demod.full(weights + "1", weights + "2", I[ind]),
            dual_demod.full(weights + "3", weights + "1", Q[ind]),
        )

        if I_st is not None:
            save(I[ind], I_st[ind])
        if Q_st is not None:
            save(Q[ind], Q_st[ind])

        if sequential and ind < len(resonators) - 1:
            align(f"q{res}.resonator", f"q{res+1}.resonator")

qubit_IF_q1 = (110) * u.MHz 
qubit_IF_q2 = (120) * u.MHz 
qubit_IF_q3 = (130) * u.MHz 
qubit_IF_q4 = (140) * u.MHz 
qubit_IF_q5 = (150) * u.MHz
qubit_IF_q6 = (160) * u.MHz 
qubit_IF_q7 = (170) * u.MHz 
qubit_IF_q8 = (180) * u.MHz
qubit_IF_q9 = (190) * u.MHz
qubit_IF_q10 = (200) * u.MHz
qubit_IF_q11 = (210) * u.MHz
qubit_IF_q12 = (220) * u.MHz
qubit_IF_q13 = (230) * u.MHz
qubit_IF_q14 = (240) * u.MHz
qubit_IF_q15 = (250) * u.MHz
qubit_IF_q16 = (260) * u.MHz
qubit_IF_q17 = (270) * u.MHz
qubit_IF_q18 =  (280) * u.MHz 
qubit_IF_q19 = (290) * u.MHz
qubit_IF_q20 = (300) * u.MHz
qubit_LO_q1 = 5.5 * u.GHz
qubit_LO_q2 = 5.0 * u.GHz
qubit_LO_q3 = 5.5 * u.GHz

qubit_LO_q4 = 5.0 * u.GHz
qubit_LO_q5 = 5.5 * u.GHz
qubit_LO_q6 = 5.0 * u.GHz 

qubit_LO_q7 = 5.0 * u.GHz 
qubit_LO_q8 = 5.0 * u.GHz
qubit_LO_q9 = 5.5 * u.GHz
qubit_LO_q10 = 5.0 * u.GHz
qubit_LO_q11 = 5.5 * u.GHz
qubit_LO_q12 = 5.5 * u.GHz
qubit_LO_q13 = 5.0 * u.GHz
qubit_LO_q14 = 5.5 * u.GHz
qubit_LO_q15 = 5.0 * u.GHz
qubit_LO_q16 = 5.5 * u.GHz
qubit_LO_q17 = 5.0 * u.GHz
qubit_LO_q18 = 5.5 * u.GHz
qubit_LO_q19 = 5.0 * u.GHz
qubit_LO_q20 = 5.5 * u.GHz

# C12_1001 in q1q2 format
parametric_IF_C12_1001 = int(50e6) 
parametric_IF_C12_1102 = int(60e6) 
parametric_IF_C12_1120 = int(70e6) 


const_flux_len_C12_1102 = 100
const_flux_len_C12_1120 = 160

gauss_flux_len = 160


const_flux_amp_C12_1102 = 1.0 
const_flux_amp_C12_1120 = 1.5

gauss_flux_amp = 1.8

######################### new below

parametric_const_len = 500 

#C1
parametric_const_len_C1_Q12_1001 = parametric_const_len
parametric_const_len_C1_Q12_1102 = parametric_const_len
parametric_const_len_C1_Q12_1120 = parametric_const_len

parametric_const_len_C1_Q15_1001 = parametric_const_len
parametric_const_len_C1_Q15_1102 = parametric_const_len
parametric_const_len_C1_Q15_1120 = parametric_const_len

parametric_const_len_C1_Q16_1001 = parametric_const_len
parametric_const_len_C1_Q16_1102 = parametric_const_len
parametric_const_len_C1_Q16_1120 = parametric_const_len

parametric_const_len_C1_Q25_1001 = parametric_const_len
parametric_const_len_C1_Q25_1102 = parametric_const_len
parametric_const_len_C1_Q25_1120 = parametric_const_len

parametric_const_len_C1_Q26_1001 = parametric_const_len
parametric_const_len_C1_Q26_1102 = parametric_const_len
parametric_const_len_C1_Q26_1120 = parametric_const_len

parametric_const_len_C1_Q56_1001 = parametric_const_len
parametric_const_len_C1_Q56_1102 = parametric_const_len
parametric_const_len_C1_Q56_1120 = parametric_const_len

#C4
parametric_const_len_C4_Q56_1001 = parametric_const_len
parametric_const_len_C4_Q56_1102 = parametric_const_len
parametric_const_len_C4_Q56_1120 = parametric_const_len

parametric_const_len_C4_Q59_1001 = parametric_const_len
parametric_const_len_C4_Q59_1102 = parametric_const_len
parametric_const_len_C4_Q59_1120 = parametric_const_len

parametric_const_len_C4_Q510_1001 = parametric_const_len
parametric_const_len_C4_Q510_1102 = parametric_const_len
parametric_const_len_C4_Q510_1120 = parametric_const_len

parametric_const_len_C4_Q69_1001 = parametric_const_len
parametric_const_len_C4_Q69_1102 = parametric_const_len
parametric_const_len_C4_Q69_1120 = parametric_const_len

parametric_const_len_C4_Q610_1001 = parametric_const_len
parametric_const_len_C4_Q610_1102 = parametric_const_len
parametric_const_len_C4_Q610_1120 = parametric_const_len

parametric_const_len_C4_Q910_1001 = parametric_const_len
parametric_const_len_C4_Q910_1102 = parametric_const_len
parametric_const_len_C4_Q910_1120 = parametric_const_len

#C6
parametric_const_len_C6_Q910_1001 = parametric_const_len
parametric_const_len_C6_Q910_1102 = parametric_const_len
parametric_const_len_C6_Q910_1120 = parametric_const_len

parametric_const_len_C6_Q913_1001 = parametric_const_len
parametric_const_len_C6_Q913_1102 = parametric_const_len
parametric_const_len_C6_Q913_1120 = parametric_const_len

parametric_const_len_C6_Q914_1001 = parametric_const_len
parametric_const_len_C6_Q914_1102 = parametric_const_len
parametric_const_len_C6_Q914_1120 = parametric_const_len

parametric_const_len_C6_Q1013_1001 = parametric_const_len
parametric_const_len_C6_Q1013_1102 = parametric_const_len
parametric_const_len_C6_Q1013_1120 = parametric_const_len

parametric_const_len_C6_Q1014_1001 = parametric_const_len
parametric_const_len_C6_Q1014_1102 = parametric_const_len
parametric_const_len_C6_Q1014_1120 = parametric_const_len

parametric_const_len_C6_Q1314_1001 = parametric_const_len
parametric_const_len_C6_Q1314_1102 = parametric_const_len
parametric_const_len_C6_Q1314_1120 = parametric_const_len

#C8
parametric_const_len_C8_Q1314_1001 = parametric_const_len
parametric_const_len_C8_Q1314_1102 = parametric_const_len
parametric_const_len_C8_Q1314_1120 = parametric_const_len

parametric_const_len_C8_Q1317_1001 = parametric_const_len
parametric_const_len_C8_Q1317_1102 = parametric_const_len
parametric_const_len_C8_Q1317_1120 = parametric_const_len

parametric_const_len_C8_Q1318_1001 = parametric_const_len
parametric_const_len_C8_Q1318_1102 = parametric_const_len
parametric_const_len_C8_Q1318_1120 = parametric_const_len

parametric_const_len_C8_Q1417_1001 = parametric_const_len
parametric_const_len_C8_Q1417_1102 = parametric_const_len
parametric_const_len_C8_Q1417_1120 = parametric_const_len

parametric_const_len_C8_Q1418_1001 = parametric_const_len
parametric_const_len_C8_Q1418_1102 = parametric_const_len
parametric_const_len_C8_Q1418_1120 = parametric_const_len

parametric_const_len_C8_Q1718_1001 = parametric_const_len
parametric_const_len_C8_Q1718_1102 = parametric_const_len
parametric_const_len_C8_Q1718_1120 = parametric_const_len

# ---- C3 lengths ----
parametric_const_len_C3_Q34_1001 = parametric_const_len
parametric_const_len_C3_Q34_1102 = parametric_const_len
parametric_const_len_C3_Q34_1120 = parametric_const_len

parametric_const_len_C3_Q38_1001 = parametric_const_len
parametric_const_len_C3_Q38_1102 = parametric_const_len
parametric_const_len_C3_Q38_1120 = parametric_const_len

parametric_const_len_C3_Q37_1001 = parametric_const_len
parametric_const_len_C3_Q37_1102 = parametric_const_len
parametric_const_len_C3_Q37_1120 = parametric_const_len

parametric_const_len_C3_Q48_1001 = parametric_const_len
parametric_const_len_C3_Q48_1102 = parametric_const_len
parametric_const_len_C3_Q48_1120 = parametric_const_len

parametric_const_len_C3_Q47_1001 = parametric_const_len
parametric_const_len_C3_Q47_1102 = parametric_const_len
parametric_const_len_C3_Q47_1120 = parametric_const_len

parametric_const_len_C3_Q78_1001 = parametric_const_len
parametric_const_len_C3_Q78_1102 = parametric_const_len
parametric_const_len_C3_Q78_1120 = parametric_const_len

# ---- C5 lengths ----
parametric_const_len_C5_Q78_1001 = parametric_const_len
parametric_const_len_C5_Q78_1102 = parametric_const_len
parametric_const_len_C5_Q78_1120 = parametric_const_len

parametric_const_len_C5_Q712_1001 = parametric_const_len
parametric_const_len_C5_Q712_1102 = parametric_const_len
parametric_const_len_C5_Q712_1120 = parametric_const_len

parametric_const_len_C5_Q711_1001 = parametric_const_len
parametric_const_len_C5_Q711_1102 = parametric_const_len
parametric_const_len_C5_Q711_1120 = parametric_const_len

parametric_const_len_C5_Q812_1001 = parametric_const_len
parametric_const_len_C5_Q812_1102 = parametric_const_len
parametric_const_len_C5_Q812_1120 = parametric_const_len

parametric_const_len_C5_Q811_1001 = parametric_const_len
parametric_const_len_C5_Q811_1102 = parametric_const_len
parametric_const_len_C5_Q811_1120 = parametric_const_len

parametric_const_len_C5_Q1112_1001 = parametric_const_len
parametric_const_len_C5_Q1112_1102 = parametric_const_len
parametric_const_len_C5_Q1112_1120 = parametric_const_len

# ---- C7 lengths ----
parametric_const_len_C7_Q1112_1001 = parametric_const_len
parametric_const_len_C7_Q1112_1102 = parametric_const_len
parametric_const_len_C7_Q1112_1120 = parametric_const_len

parametric_const_len_C7_Q1116_1001 = parametric_const_len
parametric_const_len_C7_Q1116_1102 = parametric_const_len
parametric_const_len_C7_Q1116_1120 = parametric_const_len

parametric_const_len_C7_Q1115_1001 = parametric_const_len
parametric_const_len_C7_Q1115_1102 = parametric_const_len
parametric_const_len_C7_Q1115_1120 = parametric_const_len

parametric_const_len_C7_Q1216_1001 = parametric_const_len
parametric_const_len_C7_Q1216_1102 = parametric_const_len
parametric_const_len_C7_Q1216_1120 = parametric_const_len

parametric_const_len_C7_Q1215_1001 = parametric_const_len
parametric_const_len_C7_Q1215_1102 = parametric_const_len
parametric_const_len_C7_Q1215_1120 = parametric_const_len

parametric_const_len_C7_Q1516_1001 = parametric_const_len
parametric_const_len_C7_Q1516_1102 = parametric_const_len
parametric_const_len_C7_Q1516_1120 = parametric_const_len

# ---- C10 lengths ----
parametric_const_len_C10_Q1516_1001 = parametric_const_len
parametric_const_len_C10_Q1516_1102 = parametric_const_len
parametric_const_len_C10_Q1516_1120 = parametric_const_len

parametric_const_len_C10_Q1520_1001 = parametric_const_len
parametric_const_len_C10_Q1520_1102 = parametric_const_len
parametric_const_len_C10_Q1520_1120 = parametric_const_len

parametric_const_len_C10_Q1519_1001 = parametric_const_len
parametric_const_len_C10_Q1519_1102 = parametric_const_len
parametric_const_len_C10_Q1519_1120 = parametric_const_len

parametric_const_len_C10_Q1620_1001 = parametric_const_len
parametric_const_len_C10_Q1620_1102 = parametric_const_len
parametric_const_len_C10_Q1620_1120 = parametric_const_len

parametric_const_len_C10_Q1619_1001 = parametric_const_len
parametric_const_len_C10_Q1619_1102 = parametric_const_len
parametric_const_len_C10_Q1619_1120 = parametric_const_len

parametric_const_len_C10_Q1920_1001 = parametric_const_len
parametric_const_len_C10_Q1920_1102 = parametric_const_len
parametric_const_len_C10_Q1920_1120 = parametric_const_len

parametric_const_len_C2_Q37_1001 = parametric_const_len
parametric_const_len_C2_Q37_1102 = parametric_const_len
parametric_const_len_C2_Q37_1120 = parametric_const_len

parametric_const_len_C2_Q36_1001 = parametric_const_len
parametric_const_len_C2_Q36_1102 = parametric_const_len
parametric_const_len_C2_Q36_1120 = parametric_const_len

parametric_const_len_C2_Q67_1001 = parametric_const_len
parametric_const_len_C2_Q67_1102 = parametric_const_len
parametric_const_len_C2_Q67_1120 = parametric_const_len

parametric_const_len_C9_Q1519_1001 = parametric_const_len
parametric_const_len_C9_Q1519_1102 = parametric_const_len
parametric_const_len_C9_Q1519_1120 = parametric_const_len

parametric_const_len_C9_Q1415_1001 = parametric_const_len
parametric_const_len_C9_Q1415_1102 = parametric_const_len
parametric_const_len_C9_Q1415_1120 = parametric_const_len

parametric_const_len_C9_Q1419_1001 = parametric_const_len
parametric_const_len_C9_Q1419_1102 = parametric_const_len
parametric_const_len_C9_Q1419_1120 = parametric_const_len





#C1
parametric_IF_C1_Q12_1001 = (50) * u.MHz
parametric_IF_C1_Q12_1102 = (100) * u.MHz
parametric_IF_C1_Q12_1120 = (150) * u.MHz

parametric_IF_C1_Q15_1001 = (200) * u.MHz
parametric_IF_C1_Q15_1102 = (250) * u.MHz
parametric_IF_C1_Q15_1120 = (300) * u.MHz

parametric_IF_C1_Q16_1001 = (350) * u.MHz
parametric_IF_C1_Q16_1102 = (400) * u.MHz
parametric_IF_C1_Q16_1120 = (450) * u.MHz

parametric_IF_C1_Q25_1001 = (50) * u.MHz
parametric_IF_C1_Q25_1102 = (100) * u.MHz
parametric_IF_C1_Q25_1120 = (150) * u.MHz

parametric_IF_C1_Q26_1001 = (200) * u.MHz
parametric_IF_C1_Q26_1102 = (250) * u.MHz
parametric_IF_C1_Q26_1120 = (300) * u.MHz

parametric_IF_C1_Q56_1001 = (350) * u.MHz
parametric_IF_C1_Q56_1102 = (400) * u.MHz
parametric_IF_C1_Q56_1120 = (450) * u.MHz



#C4
parametric_IF_C4_Q56_1001 = (50) * u.MHz
parametric_IF_C4_Q56_1102 = (100) * u.MHz
parametric_IF_C4_Q56_1120 = (150) * u.MHz

parametric_IF_C4_Q59_1001 = (200) * u.MHz
parametric_IF_C4_Q59_1102 = (250) * u.MHz
parametric_IF_C4_Q59_1120 = (300) * u.MHz

parametric_IF_C4_Q510_1001 = (350) * u.MHz
parametric_IF_C4_Q510_1102 = (400) * u.MHz
parametric_IF_C4_Q510_1120 = (450) * u.MHz

parametric_IF_C4_Q69_1001 = (50) * u.MHz
parametric_IF_C4_Q69_1102 = (100) * u.MHz
parametric_IF_C4_Q69_1120 = (150) * u.MHz

parametric_IF_C4_Q610_1001 = (200) * u.MHz
parametric_IF_C4_Q610_1102 = (250) * u.MHz
parametric_IF_C4_Q610_1120 = (300) * u.MHz

parametric_IF_C4_Q910_1001 = (350) * u.MHz
parametric_IF_C4_Q910_1102 = (400) * u.MHz
parametric_IF_C4_Q910_1120 = (450) * u.MHz




#C6
parametric_IF_C6_Q910_1001 = (50) * u.MHz
parametric_IF_C6_Q910_1102 = (100) * u.MHz
parametric_IF_C6_Q910_1120 = (150) * u.MHz

parametric_IF_C6_Q913_1001 = (200) * u.MHz
parametric_IF_C6_Q913_1102 = (250) * u.MHz
parametric_IF_C6_Q913_1120 = (300) * u.MHz

parametric_IF_C6_Q914_1001 = (350) * u.MHz
parametric_IF_C6_Q914_1102 = (400) * u.MHz
parametric_IF_C6_Q914_1120 = (450) * u.MHz

parametric_IF_C6_Q1013_1001 = (50) * u.MHz
parametric_IF_C6_Q1013_1102 = (100) * u.MHz
parametric_IF_C6_Q1013_1120 = (150) * u.MHz

parametric_IF_C6_Q1014_1001 = (200) * u.MHz
parametric_IF_C6_Q1014_1102 = (250) * u.MHz 
parametric_IF_C6_Q1014_1120 = (300) * u.MHz

parametric_IF_C6_Q1314_1001 = (350) * u.MHz
parametric_IF_C6_Q1314_1102 = (400) * u.MHz
parametric_IF_C6_Q1314_1120 = (450) * u.MHz




#C8

parametric_IF_C8_Q1314_1001 = (50) * u.MHz
parametric_IF_C8_Q1314_1102 = (100) * u.MHz
parametric_IF_C8_Q1314_1120 = (150) * u.MHz

parametric_IF_C8_Q1317_1001 = (200) * u.MHz
parametric_IF_C8_Q1317_1102 = (250) * u.MHz
parametric_IF_C8_Q1317_1120 = (300) * u.MHz


parametric_IF_C8_Q1318_1001 = (350) * u.MHz
parametric_IF_C8_Q1318_1102 = (400) * u.MHz
parametric_IF_C8_Q1318_1120 = (450) * u.MHz

parametric_IF_C8_Q1417_1001 = (50) * u.MHz
parametric_IF_C8_Q1417_1102 = (100) * u.MHz
parametric_IF_C8_Q1417_1120 = (150) * u.MHz

parametric_IF_C8_Q1418_1001 = (200) * u.MHz
parametric_IF_C8_Q1418_1102 = (250) * u.MHz
parametric_IF_C8_Q1418_1120 = (300) * u.MHz

parametric_IF_C8_Q1718_1001 = (350) * u.MHz
parametric_IF_C8_Q1718_1102 = (400) * u.MHz
parametric_IF_C8_Q1718_1120 = (450) * u.MHz

# ---- C3 coupling frequencies (Δ/2) ----

# Q3–Q4
parametric_IF_C3_Q34_1001 = (50) * u.MHz   
parametric_IF_C3_Q34_1102 = (100) * u.MHz  
parametric_IF_C3_Q34_1120 = (150) * u.MHz   

# Q3–Q8
parametric_IF_C3_Q38_1001 = (200) * u.MHz   
parametric_IF_C3_Q38_1102 = (250) * u.MHz  
parametric_IF_C3_Q38_1120 = (300) * u.MHz 

# Q3–Q7 (provided)
parametric_IF_C3_Q37_1001 = (350) * u.MHz 
parametric_IF_C3_Q37_1102 = (400) * u.MHz  
parametric_IF_C3_Q37_1120 = (450) * u.MHz  

# Q4–Q8
parametric_IF_C3_Q48_1001 = (50) * u.MHz 
parametric_IF_C3_Q48_1102 = (100) * u.MHz  
parametric_IF_C3_Q48_1120 = (150) * u.MHz  

# Q4–Q7
parametric_IF_C3_Q47_1001 = (200) * u.MHz  
parametric_IF_C3_Q47_1102 = (250) * u.MHz  
parametric_IF_C3_Q47_1120 = (300) * u.MHz  

# Q7–Q8
parametric_IF_C3_Q78_1001 = (350) * u.MHz 
parametric_IF_C3_Q78_1102 = (400) * u.MHz  
parametric_IF_C3_Q78_1120 = (450) * u.MHz 

# ---- Corrected C5 coupling frequencies (Δ/2) ----

# C5_Q78 (Q7–Q8)
parametric_IF_C5_Q78_1001 = (50) * u.MHz 
parametric_IF_C5_Q78_1102 = (100) * u.MHz   
parametric_IF_C5_Q78_1120 = (150) * u.MHz  

# C5_Q712 (Q7–Q12)
parametric_IF_C5_Q712_1001 = (200) * u.MHz  
parametric_IF_C5_Q712_1102 = (250) * u.MHz  
parametric_IF_C5_Q712_1120 = (300) * u.MHz  

# C5_Q711 (Q7–Q11)
parametric_IF_C5_Q711_1001 = (350) * u.MHz 
parametric_IF_C5_Q711_1102 = (400) * u.MHz 
parametric_IF_C5_Q711_1120 = (450) * u.MHz  

# C5_Q812 (Q8–Q12)
parametric_IF_C5_Q812_1001 = (50) * u.MHz  
parametric_IF_C5_Q812_1102 = (100) * u.MHz  
parametric_IF_C5_Q812_1120 = (150) * u.MHz  

# C5_Q811 (Q8–Q11)
parametric_IF_C5_Q811_1001 = (200) * u.MHz  
parametric_IF_C5_Q811_1102 = (250) * u.MHz  
parametric_IF_C5_Q811_1120 = (300) * u.MHz  

# C5_Q1112 (Q11–Q12)
parametric_IF_C5_Q1112_1001 = (350) * u.MHz  
parametric_IF_C5_Q1112_1102 = (400) * u.MHz  
parametric_IF_C5_Q1112_1120 = (450) * u.MHz  

# ---- C7 coupling frequencies (Δ/2) ----

# Q11–Q12
parametric_IF_C7_Q1112_1001 = (50) * u.MHz 
parametric_IF_C7_Q1112_1102 = (100) * u.MHz 
parametric_IF_C7_Q1112_1120 = (150) * u.MHz 

# Q11–Q16
parametric_IF_C7_Q1116_1001 = (200) * u.MHz  
parametric_IF_C7_Q1116_1102 = (250) * u.MHz   
parametric_IF_C7_Q1116_1120 = (300) * u.MHz   

# Q11–Q15
parametric_IF_C7_Q1115_1001 = (350) * u.MHz 
parametric_IF_C7_Q1115_1102 = (400) * u.MHz   
parametric_IF_C7_Q1115_1120 = (450) * u.MHz  

# Q12–Q16
parametric_IF_C7_Q1216_1001 = (50) * u.MHz   
parametric_IF_C7_Q1216_1102 = (100) * u.MHz   
parametric_IF_C7_Q1216_1120 = (150) * u.MHz   

# Q12–Q15
parametric_IF_C7_Q1215_1001 = (200) * u.MHz   
parametric_IF_C7_Q1215_1102 = (250) * u.MHz   
parametric_IF_C7_Q1215_1120 = (300) * u.MHz    

# Q15–Q16
parametric_IF_C7_Q1516_1001 = (350) * u.MHz   
parametric_IF_C7_Q1516_1102 = (400) * u.MHz   
parametric_IF_C7_Q1516_1120 = (450) * u.MHz  

# ---- C10 coupling frequencies (Δ/2) ----

# C10_Q1516 (Q15–Q16)
parametric_IF_C10_Q1516_1001 = (50) * u.MHz 
parametric_IF_C10_Q1516_1102 = (100) * u.MHz 
parametric_IF_C10_Q1516_1120 = (150) * u.MHz   

# C10_Q1520 (Q15–Q20)
parametric_IF_C10_Q1520_1001 = (200) * u.MHz 
parametric_IF_C10_Q1520_1102 = (250) * u.MHz 
parametric_IF_C10_Q1520_1120 = (300) * u.MHz   

# C10_Q1519 (Q15–Q19)
parametric_IF_C10_Q1519_1001 = (350) * u.MHz 
parametric_IF_C10_Q1519_1102 = (400) * u.MHz 
parametric_IF_C10_Q1519_1120 = (450) * u.MHz   

# C10_Q1620 (Q16–Q20)
parametric_IF_C10_Q1620_1001 = (50) * u.MHz 
parametric_IF_C10_Q1620_1102 = (100) * u.MHz 
parametric_IF_C10_Q1620_1120 = (150) * u.MHz 

# C10_Q1619 (Q16–Q19)
parametric_IF_C10_Q1619_1001 = (200) * u.MHz   
parametric_IF_C10_Q1619_1102 = (250) * u.MHz
parametric_IF_C10_Q1619_1120 = (300) * u.MHz 

# C10_Q1920 (Q19–Q20)
parametric_IF_C10_Q1920_1001 = (350) * u.MHz 
parametric_IF_C10_Q1920_1102 = (400) * u.MHz   
parametric_IF_C10_Q1920_1120 = (450) * u.MHz   

# C2_Q37 (Q3–Q7)
parametric_IF_C2_Q37_1001 = (50) * u.MHz 
parametric_IF_C2_Q37_1102 = (100) * u.MHz   
parametric_IF_C2_Q37_1120 = (150) * u.MHz  

# C2_Q36 (Q3–Q6)
parametric_IF_C2_Q36_1001 = (200) * u.MHz  
parametric_IF_C2_Q36_1102 = (250) * u.MHz   
parametric_IF_C2_Q36_1120 = (300) * u.MHz   

# C2_Q67 (Q6–Q7)
parametric_IF_C2_Q67_1001 = (350) * u.MHz 
parametric_IF_C2_Q67_1102 = (400) * u.MHz   
parametric_IF_C2_Q67_1120 = (450) * u.MHz   

# C9_Q1519 (Q15–Q19)
parametric_IF_C9_Q1519_1001 = (50) * u.MHz 
parametric_IF_C9_Q1519_1102 = (100) * u.MHz 
parametric_IF_C9_Q1519_1120 = (150) * u.MHz 

# C9_Q1415 (Q14–Q15)
parametric_IF_C9_Q1415_1001 = (200) * u.MHz 
parametric_IF_C9_Q1415_1102 = (250) * u.MHz 
parametric_IF_C9_Q1415_1120 = (300) * u.MHz 

# C9_Q1419 (Q14–Q19)
parametric_IF_C9_Q1419_1001 = (350) * u.MHz 
parametric_IF_C9_Q1419_1102 = (400) * u.MHz 
parametric_IF_C9_Q1419_1120 = (450) * u.MHz 


#C1
parametric_const_amp_C1_Q12_1001 = 2.5
parametric_const_amp_C1_Q12_1102 = 2.5
parametric_const_amp_C1_Q12_1120 = 2.5

parametric_const_amp_C1_Q15_1001 = 2.5
parametric_const_amp_C1_Q15_1102 = 2.5
parametric_const_amp_C1_Q15_1120 = 2.5

parametric_const_amp_C1_Q16_1001 = 2.5
parametric_const_amp_C1_Q16_1102 = 2.5
parametric_const_amp_C1_Q16_1120 = 2.5

parametric_const_amp_C1_Q25_1001 = 2.5
parametric_const_amp_C1_Q25_1102 = 2.5
parametric_const_amp_C1_Q25_1120 = 2.5

parametric_const_amp_C1_Q26_1001 = 2.5
parametric_const_amp_C1_Q26_1102 = 2.5
parametric_const_amp_C1_Q26_1120 = 2.5

parametric_const_amp_C1_Q56_1001 = 2.5
parametric_const_amp_C1_Q56_1102 = 2.5
parametric_const_amp_C1_Q56_1120 = 2.5

#C4
parametric_const_amp_C4_Q56_1001 = 2.5
parametric_const_amp_C4_Q56_1102 = 2.5
parametric_const_amp_C4_Q56_1120 = 2.5

parametric_const_amp_C4_Q59_1001 = 2.5
parametric_const_amp_C4_Q59_1102 = 2.5
parametric_const_amp_C4_Q59_1120 = 2.5

parametric_const_amp_C4_Q510_1001 = 2.5
parametric_const_amp_C4_Q510_1102 = 2.5
parametric_const_amp_C4_Q510_1120 = 2.5

parametric_const_amp_C4_Q69_1001 = 2.5
parametric_const_amp_C4_Q69_1102 = 2.5
parametric_const_amp_C4_Q69_1120 = 2.5

parametric_const_amp_C4_Q610_1001 = 2.5
parametric_const_amp_C4_Q610_1102 = 2.5
parametric_const_amp_C4_Q610_1120 = 2.5

parametric_const_amp_C4_Q910_1001 = 2.5
parametric_const_amp_C4_Q910_1102 = 2.5
parametric_const_amp_C4_Q910_1120 = 2.5

#C6
parametric_const_amp_C6_Q910_1001 = 2.5
parametric_const_amp_C6_Q910_1102 = 2.5
parametric_const_amp_C6_Q910_1120 = 2.5

parametric_const_amp_C6_Q913_1001 = 2.5
parametric_const_amp_C6_Q913_1102 = 2.5
parametric_const_amp_C6_Q913_1120 = 2.5

parametric_const_amp_C6_Q914_1001 = 2.5
parametric_const_amp_C6_Q914_1102 = 1.8
parametric_const_amp_C6_Q914_1120 = 2.5

parametric_const_amp_C6_Q1013_1001 = 2.5
parametric_const_amp_C6_Q1013_1102 = 2.5
parametric_const_amp_C6_Q1013_1120 = 2.5

parametric_const_amp_C6_Q1014_1001 = 2.5
parametric_const_amp_C6_Q1014_1102 = 2.5
parametric_const_amp_C6_Q1014_1120 = 2.5

parametric_const_amp_C6_Q1314_1001 = 2.5
parametric_const_amp_C6_Q1314_1102 = 2.5
parametric_const_amp_C6_Q1314_1120 = 2.5

#C8
parametric_const_amp_C8_Q1314_1001 = 2.5
parametric_const_amp_C8_Q1314_1102 = 2.5
parametric_const_amp_C8_Q1314_1120 = 2.5

parametric_const_amp_C8_Q1317_1001 = 2.5
parametric_const_amp_C8_Q1317_1102 = 2.5
parametric_const_amp_C8_Q1317_1120 = 2.5

parametric_const_amp_C8_Q1318_1001 = 2.5
parametric_const_amp_C8_Q1318_1102 = 2.5
parametric_const_amp_C8_Q1318_1120 = 2.5

parametric_const_amp_C8_Q1417_1001 = 2.5
parametric_const_amp_C8_Q1417_1102 = 2.5
parametric_const_amp_C8_Q1417_1120 = 2.5

parametric_const_amp_C8_Q1418_1001 = 2.5
parametric_const_amp_C8_Q1418_1102 = 2.5
parametric_const_amp_C8_Q1418_1120 = 2.5

parametric_const_amp_C8_Q1718_1001 = 2.5
parametric_const_amp_C8_Q1718_1102 = 2.5
parametric_const_amp_C8_Q1718_1120 = 2.5

# ---- C3 amplitudes ----
parametric_const_amp_C3_Q34_1001 = 2.5
parametric_const_amp_C3_Q34_1102 = 2.5
parametric_const_amp_C3_Q34_1120 = 2.5

parametric_const_amp_C3_Q38_1001 = 2.5
parametric_const_amp_C3_Q38_1102 = 2.5
parametric_const_amp_C3_Q38_1120 = 2.5

parametric_const_amp_C3_Q37_1001 = 2.5
parametric_const_amp_C3_Q37_1102 = 2.5
parametric_const_amp_C3_Q37_1120 = 2.5

parametric_const_amp_C3_Q48_1001 = 2.5
parametric_const_amp_C3_Q48_1102 = 2.5
parametric_const_amp_C3_Q48_1120 = 2.5

parametric_const_amp_C3_Q47_1001 = 2.5
parametric_const_amp_C3_Q47_1102 = 2.5
parametric_const_amp_C3_Q47_1120 = 2.5

parametric_const_amp_C3_Q78_1001 = 2.5
parametric_const_amp_C3_Q78_1102 = 2.5
parametric_const_amp_C3_Q78_1120 = 2.5

# ---- C5 amplitudes ----
parametric_const_amp_C5_Q78_1001 = 2.5
parametric_const_amp_C5_Q78_1102 = 2.5
parametric_const_amp_C5_Q78_1120 = 2.5

parametric_const_amp_C5_Q712_1001 = 2.5
parametric_const_amp_C5_Q712_1102 = 2.5
parametric_const_amp_C5_Q712_1120 = 2.5

parametric_const_amp_C5_Q711_1001 = 2.5
parametric_const_amp_C5_Q711_1102 = 2.5
parametric_const_amp_C5_Q711_1120 = 2.5

parametric_const_amp_C5_Q812_1001 = 2.5
parametric_const_amp_C5_Q812_1102 = 2.5
parametric_const_amp_C5_Q812_1120 = 2.5

parametric_const_amp_C5_Q811_1001 = 2.5
parametric_const_amp_C5_Q811_1102 = 2.5
parametric_const_amp_C5_Q811_1120 = 2.5

parametric_const_amp_C5_Q1112_1001 = 2.5
parametric_const_amp_C5_Q1112_1102 = 2.5
parametric_const_amp_C5_Q1112_1120 = 2.5

# ---- C7 amplitudes ----
parametric_const_amp_C7_Q1112_1001 = 2.5
parametric_const_amp_C7_Q1112_1102 = 2.5
parametric_const_amp_C7_Q1112_1120 = 2.5

parametric_const_amp_C7_Q1116_1001 = 2.5
parametric_const_amp_C7_Q1116_1102 = 2.5
parametric_const_amp_C7_Q1116_1120 = 2.5

parametric_const_amp_C7_Q1115_1001 = 2.5
parametric_const_amp_C7_Q1115_1102 = 2.5
parametric_const_amp_C7_Q1115_1120 = 2.5

parametric_const_amp_C7_Q1216_1001 = 2.5
parametric_const_amp_C7_Q1216_1102 = 2.5
parametric_const_amp_C7_Q1216_1120 = 2.5

parametric_const_amp_C7_Q1215_1001 = 2.5
parametric_const_amp_C7_Q1215_1102 = 2.5
parametric_const_amp_C7_Q1215_1120 = 2.5

parametric_const_amp_C7_Q1516_1001 = 2.5
parametric_const_amp_C7_Q1516_1102 = 2.5
parametric_const_amp_C7_Q1516_1120 = 2.5

# ---- C10 amplitudes ----
parametric_const_amp_C10_Q1516_1001 = 2.5 
parametric_const_amp_C10_Q1516_1102 = 2.5
parametric_const_amp_C10_Q1516_1120 = 2.5

parametric_const_amp_C10_Q1520_1001 = 2.5
parametric_const_amp_C10_Q1520_1102 = 2.5
parametric_const_amp_C10_Q1520_1120 = 2.5

parametric_const_amp_C10_Q1519_1001 = 2.5
parametric_const_amp_C10_Q1519_1102 = 2.5
parametric_const_amp_C10_Q1519_1120 = 2.5

parametric_const_amp_C10_Q1620_1001 = 2.5
parametric_const_amp_C10_Q1620_1102 = 2.5
parametric_const_amp_C10_Q1620_1120 = 2.5

parametric_const_amp_C10_Q1619_1001 = 2.5
parametric_const_amp_C10_Q1619_1102 = 2.5
parametric_const_amp_C10_Q1619_1120 = 2.5

parametric_const_amp_C10_Q1920_1001 = 2.5
parametric_const_amp_C10_Q1920_1102 = 2.5
parametric_const_amp_C10_Q1920_1120 = 2.5

parametric_const_amp_C2_Q37_1001 = 2.5
parametric_const_amp_C2_Q37_1102 = 2.5
parametric_const_amp_C2_Q37_1120 = 2.5

parametric_const_amp_C2_Q36_1001 = 2.5
parametric_const_amp_C2_Q36_1102 = 2.5 
parametric_const_amp_C2_Q36_1120 = 2.5 

parametric_const_amp_C2_Q67_1001 = 2.5
parametric_const_amp_C2_Q67_1102 = 2.5 
parametric_const_amp_C2_Q67_1120 = 2.5 

parametric_const_amp_C9_Q1519_1001 = 2.5
parametric_const_amp_C9_Q1519_1102 = 2.5
parametric_const_amp_C9_Q1519_1120 = 2.5

parametric_const_amp_C9_Q1415_1001 = 2.5
parametric_const_amp_C9_Q1415_1102 = 2.5
parametric_const_amp_C9_Q1415_1120 = 2.5

parametric_const_amp_C9_Q1419_1001 = 2.5
parametric_const_amp_C9_Q1419_1102 = 2.5
parametric_const_amp_C9_Q1419_1120 = 2.5

ge_threshold_q1 = 1e-04
ge_threshold_q2 = 2e-04
ge_threshold_q3 = 3e-04
ge_threshold_q4 = 4e-04
ge_threshold_q5 = 5e-04
ge_threshold_q6 = 6e-04
ge_threshold_q7 = 7e-04
ge_threshold_q8 = 8e-04
ge_threshold_q9 = 9e-04
ge_threshold_q10 = 1e-03
ge_threshold_q11 = 1.1e-03
ge_threshold_q12 = 1.2e-03
ge_threshold_q13 = 1.3e-03
ge_threshold_q14 = 1.4e-03
ge_threshold_q15 =  1.5e-03
ge_threshold_q16 = 1.6e-03
ge_threshold_q17 = 1.7e-03
ge_threshold_q18 = 1.8e-03
ge_threshold_q19 = 1.9e-03
ge_threshold_q20 = 2.0e-03
ge_threshold_q_C6 = 2.1e-03


coupler_num = 5
rr_C = 11
rr_T = 12
Q_C_xy =f"q{rr_C}.xy"
Q_T_xy =f"q{rr_T}.xy"
coupler_QCQT_1102 = f"c{coupler_num}_Q{rr_C}{rr_T}"
print(coupler_QCQT_1102)
# Relaxation time
qubit1_T1 = 50 * u.us
qubit2_T1 = 50 * u.us
thermalization_time = 5 * max(qubit1_T1, qubit2_T1)
qubit_IF_q_C = globals()[f"qubit_IF_q{rr_C}"]
qubit_LO_q_C = globals()[f"qubit_LO_q{rr_C}"]
qubit_IF_q_T = globals()[f"qubit_IF_q{rr_T}"]
qubit_LO_q_T = globals()[f"qubit_LO_q{rr_T}"]
parametric_const_amp_C_QCQT_1102=globals()[f"parametric_const_amp_C{coupler_num}_Q{rr_C}{rr_T}_1102"]
ge_threshold_q_C =globals()[f"ge_threshold_q{rr_C}"]
ge_threshold_q_T =globals()[f"ge_threshold_q{rr_T}"]

const_flux_len_C12_1102 = 100
###################
# The QUA program #
###################
n_avg = 2000  # Number of averages 2000
phasediff2pi = np.arange(0, 1, 0.01)  # phase diff of swap pulses.
sqrtswap_time = const_flux_len_C12_1102
            
readout_len = 2000 


with program() as ramsey:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    t = declare(int)  # QUA variable for the idle time
    phi = declare(fixed)  # Phase to apply the virtual Z-rotation
    state = [declare(bool) for _ in range(2)]
    state_st = [declare_stream() for _ in range(2)]

    with for_(n, 0, n < n_avg, n + 1):
        with for_each_(phi, phasediff2pi):

            reset_global_phase()
            reset_frame(Q_C_xy) 
            reset_frame(Q_T_xy)
            reset_frame(coupler_QCQT_1102)

            play("x180", Q_C_xy )
            # align()
            # wait(4)
            play("y90", Q_T_xy )
            align()
            wait(4)
            play("const_1102", coupler_QCQT_1102)
            wait(4)
            frame_rotation_2pi(phi, coupler_QCQT_1102)
            wait(4)
            play("const_1102", coupler_QCQT_1102)
            wait(4)
            align()
            play("-y90", Q_T_xy )


            # Align the elements to measure after having waited a time "tau" after the qubit pulses.
            align()
            # Measure the state of the resonators
            multiplexed_readout(I, I_st, Q, Q_st, resonators=[rr_C, rr_T])
            assign(state[0], I[0] > ge_threshold_q_C)
            assign(state[1], I[1] > ge_threshold_q_T)
            save(state[0], state_st[0])
            save(state[1], state_st[1])
            # Reset the frame of the qubit in order not to accumulate rotations
            reset_frame(Q_C_xy)
            reset_frame(Q_T_xy)
            # Wait for the qubit to decay to the ground state
            wait(thermalization_time * u.ns)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

#####################################
#  Open Communication with the QOP  #
#####################################
#qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
machine = Quam.load("C:/Users/BenjaminSafvati/OneDrive - QM Machines LTD/Documents/GitHub/quam_state")
###########################
# Run or Simulate Program #
###########################
# Generate the OPX and Octave configurations
import json

config = json.loads(Path("qua_config.json").read_text())
simulate = True
client = QmSaas(
    host="qm-saas.dev.quantum-machines.co",
    email="benjamin.safvati@quantum-machines.co",
    password="ubq@yvm3RXP1bwb5abv"
)
if simulate:
    cluster_config = ClusterConfig()
    controller = cluster_config.controller()
    controller.lf_fems(1, 2)
    controller.mw_fems(3, 4, 5)

    with client.simulator(QOPVersion("v3_5_0"), cluster_config) as inst: 
        #inst.spawn()        # boot the virtual QOP

        qmm = QuantumMachinesManager(
            host=inst.host,
            port=inst.port,
            connection_headers=inst.default_connection_headers, log_level="DEBUG"
        )
        simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
        job = qmm.simulate(config, ramsey, simulation_config)
        job.get_simulated_samples().con1.plot()
        waveform_report = job.get_simulated_waveform_report()
        # Cast the waveform report to a python dictionary
        waveform_dict = waveform_report.to_dict()
        # Visualize and save the waveform report
        samples = job.get_simulated_samples()

        waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ramsey)
    # Prepare the figure for live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["n", "I1", "Q1", "state1", "I2", "Q2", "state2"], mode="live")
    # Live plotting
    while results.is_processing():
        # Fetch results
        n, I1, Q1, state1, I2, Q2, state2 = results.fetch_all()
        # Convert the results into Volts
        I1, Q1 = u.demod2volts(I1, readout_len), u.demod2volts(Q1, readout_len)
        I2, Q2 = u.demod2volts(I2, readout_len), u.demod2volts(Q2, readout_len)
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # Plot
        plt.subplot(221)
        plt.cla()
        plt.plot(phasediff2pi, I1)
        plt.ylabel("I quadrature [V]")
        plt.title("Qubit C")
        plt.subplot(223)
        plt.cla()
        plt.plot(phasediff2pi, state1)
        plt.ylabel("State [V]")
        plt.xlabel("Swap pulse phase difference [2$\pi$]")
        plt.subplot(222)
        plt.cla()
        plt.plot(phasediff2pi, I2)
        plt.title("Qubit T")
        plt.subplot(224)
        plt.cla()
        plt.plot(phasediff2pi, state2)
        plt.title("Q_T")
        plt.xlabel("Swap pulse phase difference [2$\pi$]")
        plt.tight_layout()
        plt.pause(2)
    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()
    # try:
    #     fit = Fit()
    #     plt.figure()
    #     plt.suptitle(f"Ramsey measurement with detuning={detuning} Hz")
    #     plt.subplot(221)
    #     fit.ramsey(phasediff2pi, I1, plot=True)
    #     plt.xlabel("Idle times [ns]")
    #     plt.ylabel("I quadrature [V]")
    #     plt.title("Qubit 1")
    #     plt.subplot(223)
    #     fit.ramsey(phasediff2pi, state1, plot=True)
    #     plt.xlabel("Idle times [ns]")
    #     plt.ylabel("I quadrature [V]")
    #     plt.title("Qubit 2")
    #     plt.subplot(222)
    #     fit.ramsey(phasediff2pi, I2, plot=True)
    #     plt.xlabel("Idle times [ns]")
    #     plt.ylabel("I quadrature [V]")
    #     plt.subplot(224)
    #     fit.ramsey(phasediff2pi, state2, plot=True)
    #     plt.xlabel("Idle times [ns]")
    #     plt.ylabel("I quadrature [V]")
    #     plt.tight_layout()
    # except (Exception,):
    #     pass
    plt.show()