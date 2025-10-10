from qm import QuantumMachinesManager
from qm.qua import *
import numpy as np
from configuration import *


offsets = np.linspace(-0.2, 0.2, 21)

with program() as prog:
    i_dc = declare(fixed)
    off  = declare(fixed)

    i_st = declare_stream()
    with for_each_(off, offsets):
        play("const" * amp(off), "tx")
        measure("meas", "rx", None,
                demod.full("cos",  i_dc))
        save(i_dc, i_st)

qmm = QuantumMachinesManager(host = qop_ip, cluster_name = cluster_name)
qm = qmm.open_qm(config)
job = qm.execute(prog)

res = job.result_handles
res.wait_for_all_values()
i_vals = np.array(res.get("i_st").fetch_all())



