# %%
import json
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.quam_builder.machine import save_machine
import numpy as np
from quam_libs.macros import *

path = "./quam_state"

machine = QuAM.load()


def write_parameters_to_csv(param_dict):
    import csv
    with open('oqc_graph_1x8_04012025.csv', 'w', newline='') as file:
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
params_oqc = []

qu_pairs = ["q1-2", "q2-3", "q3-4", "q5-4", "q5-6", "q6-7", "q7-8", "q7-8"]

fro = [10.033, 9.621, 9.946, 9.423, 9.747, 9.325, 9.842, 9.517]
f01 = [4.602, 4.371, 4.351, 4.104, 4.511, 4.457, 4.513, 4.319]
f12 = [4.602, 4.371, 4.351, 4.104, 4.511, 4.457, 4.513, 4.319]
T1 = [18.8, 24.2, 49.7, 26.7, 25.2, 27.8, 18.2, 28.0]
T2e = [40.5, 43.4, 64.8, 64.2, 39.8, 32.3, 20.3, 29.8]
RO = [95.9, 89.5, 94.0, 96.8, 95.1, 95.4, 87.4, 96.1]
RB1q = [99.94, 99.58, 99.67, 99.91, 99.94, 99.76, 99.92, 99.91]
RB2q = [95.5, 84.0, 95.7, 95.3, 95.5, 97.2, 82.6, 87.4]

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
                   "2Q": machine.qubit_pairs[qu_pairs[i]].cross_resonance.bell_state_fidelity
                   })
    params_oqc.append({"qubit": mapping[qb.name],
                   "R_freq": fro[i],
                   "01_freq": f01[i],
                   "12_freq": f12[i],
                   "T1": T1[i],
                   "T2e": T2e[i],
                   "RO": RO[i],
                   "1Q": RB1q[i],
                   "2Q": RB2q[i]
                   })

write_parameters_to_csv(params)

fro2 = [params[k]['R_freq'] for k in range(len(params))]
f012 = [params[k]['01_freq'] for k in range(len(params))]
f122 = [params[k]['12_freq'] for k in range(len(params))]
T12 = [params[k]['T1'] for k in range(len(params))]
T2e2 = [params[k]['T2e'] for k in range(len(params))]
RO2 = [params[k]['RO'] for k in range(len(params))]
RB1q2 = [params[k]['1Q'] for k in range(len(params))]
RB2q2 = [params[k]['2Q'] for k in range(len(params))]; RB2q2[-1] = 0

import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 4, figsize=(15, 7))
plt.suptitle(f"Benchmarking comparison")
ax[0, 0].bar(["A", "B", "C", "D", "E", "F", "G", "H"], fro, color='red', edgecolor='red', alpha=0.2)
ax[0, 0].bar(["A", "B", "C", "D", "E", "F", "G", "H"], fro2, color='skyblue', edgecolor='navy', alpha=0.2)
ax[0, 0].set_title("Readout frequency [GHz]")
ax[0, 0].set_ylim((9.2, 10.2))
ax[0, 0].legend(("OQC", "QM"))

ax[0, 1].bar(["A", "B", "C", "D", "E", "F", "G", "H"], f01, color='red', edgecolor='red', alpha=0.2)
ax[0, 1].bar(["A", "B", "C", "D", "E", "F", "G", "H"], f012, color='skyblue', edgecolor='navy', alpha=0.2)
ax[0, 1].set_title("Qubit frequency 01 [GHz]")
ax[0, 1].set_ylim((4.0, 4.7))

# ax[0, 2].bar(["A", "B", "C", "D", "E", "F", "G", "H"], f12, color='red', edgecolor='red', alpha=0.2)
ax[0, 2].bar(["A", "B", "C", "D", "E", "F", "G", "H"], f122, color='skyblue', edgecolor='navy', alpha=0.2)
ax[0, 2].set_title("Qubit frequency 12 [GHz]")
ax[0, 2].set_ylim((3.5, 4.5))

ax[0, 3].bar(["A", "B", "C", "D", "E", "F", "G", "H"], T1, color='red', edgecolor='red', alpha=0.2)
ax[0, 3].bar(["A", "B", "C", "D", "E", "F", "G", "H"], T12, color='skyblue', edgecolor='navy', alpha=0.2)
ax[0, 3].set_title("T1 [µs]")

ax[1, 0].bar(["A", "B", "C", "D", "E", "F", "G", "H"], T2e, color='red', edgecolor='red', alpha=0.2)
ax[1, 0].bar(["A", "B", "C", "D", "E", "F", "G", "H"], T2e2, color='skyblue', edgecolor='navy', alpha=0.2)
ax[1, 0].set_title("T2 echo [µs]")

ax[1, 1].bar(["A", "B", "C", "D", "E", "F", "G", "H"], RO, color='red', edgecolor='red', alpha=0.2)
ax[1, 1].bar(["A", "B", "C", "D", "E", "F", "G", "H"], RO2, color='skyblue', edgecolor='navy', alpha=0.2)
ax[1, 1].set_title("Readout fidelity [%]")
ax[1, 1].set_ylim((85, 100))

ax[1, 2].bar(["A", "B", "C", "D", "E", "F", "G", "H"], RB1q, color='red', edgecolor='red', alpha=0.2)
ax[1, 2].bar(["A", "B", "C", "D", "E", "F", "G", "H"], RB1q2, color='skyblue', edgecolor='navy', alpha=0.2)
ax[1, 2].set_title("Single qubit gate fidelity [%]")
ax[1, 2].set_ylim((99.5, 100))

ax[1, 3].bar(["A", "B", "C", "D", "E", "F", "G", "H"], RB2q, color='red', edgecolor='red', alpha=0.2)
ax[1, 3].bar(["A", "B", "C", "D", "E", "F", "G", "H"], np.array(RB2q2)*100, color='skyblue', edgecolor='navy', alpha=0.2)
ax[1, 3].set_title("CNOT gate fidelity [%]")
ax[1, 3].set_ylim((80, 100))
plt.show()



