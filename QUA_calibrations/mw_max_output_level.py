from qm import QuantumMachinesManager
from configuration import *
from qm.qua import *

N = 1000
scales = np.linspace(0.1, 1.99, 21)

# Should play a stepped square wave output 
with program() as mw_output_test: 
    n = declare(int)
    s = declare(fixed)
    with for_(n, 0, n<N, n+1):
        with for_each_(s, scales):
            play("cw"*amp(s), "MW_test")
            wait(100)

qmm = QuantumMachinesManager(host = qop_ip, cluster_name = cluster_name)
qm = qmm.open_qm(config)
job = qm.execute(mw_output_test)

# res = job.result_handles
# res.wait_for_all_values()
# i_vals = np.array(res.get("i_st").fetch_all())