from qm import QuantumMachinesManager
from configuration import *
from qm.qua import *

# Choose AMPLIFIED or DIRECT
config["controllers"]["fems"][lf_fem]["analog_outputs"][1]["output_mode"] = "amplified"

N = 1000
scales = np.linspace(0.1, 1.99, 21)

# Should play a stepped square wave output 
with program() as lf_output_test: 
    n = declare(int)
    s = declare(fixed)
    with for_(n, 0, n<N, n+1):
        with for_each_(s, scales):
            play("const"*amp(s), "LF_test_output")
            wait(100)


qmm = QuantumMachinesManager(host = qop_ip, cluster_name = cluster_name)
qm = qmm.open_qm(config)
job = qm.execute(lf_output_test)

# res = job.result_handles
# res.wait_for_all_values()
# i_vals = np.array(res.get("i_st").fetch_all())