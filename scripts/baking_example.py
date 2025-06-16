from matplotlib import pyplot as plt
from qm import SimulationConfig
from qm import QuantumMachinesManager
from qm.qua import *
from qualang_tools.bakery import baking
from configuration import *

qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

with baking(config, padding_method="symmetric_r") as b:
    mixInput_sample = [[0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45], [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45]]

    b.add_op("baked_Op", "NV", mixInput_sample, digital_marker=None)

    b.play("baked_Op", "NV")

with program() as bakery_is_fun:
    b.run()

qm = qmm.open_qm(config)
job = qm.simulate(bakery_is_fun, SimulationConfig(int(200)))  # in clock cycles, 4 ns

samples = job.get_simulated_samples()
samples.con1.plot()
plt.show()
