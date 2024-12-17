# %%
import json
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine
import numpy as np


path = "./quam_state"

machine = QuAM.load()


def write_parameters_to_csv(param_dict):
    import csv
    with open('oqc_graph_2x2x2x2_16122024.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(param_dict[0].keys()))

        writer.writeheader()
        writer.writerows(param_dict)


mapping = {"q1": "A",
           "q2": "B",
           "q3": "C",
           "q4": "D",
           "q5": "E",
           "q6": "F",
           "q7": "G",
           "q8": "H",}
params = []
for i, q in enumerate(machine.qubits):
    qb = machine.qubits[q]
    if i < 7:
        j = i+2
    else:
        j = 1
    params.append({"qubit": mapping[qb.name],
                   "R_freq": qb.resonator.RF_frequency * 1e-9,
                   "01_freq": qb.xy.RF_frequency * 1e-9,
                   "12_freq": (qb.xy.RF_frequency - qb.anharmonicity) * 1e-9,
                   "T1": qb.T1 * 1e6,
                   "T2e": qb.T2echo * 1e6,
                   "RO": 0.5 * (qb.resonator.confusion_matrix[0][0] + qb.resonator.confusion_matrix[1][1]) * 100,
                   "1Q": qb.RB_fidelity * 100,
                   "2Q": machine.qubit_pairs[f"q{i+1}-{j}"].cross_resonance.bell_state_fidelity
                   })

write_parameters_to_csv(params)