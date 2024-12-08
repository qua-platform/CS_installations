# %%
from QuaGST import QuaGST
from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from pygsti.modelpacks import smq1Q_XYI
from example_configuration import *

qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "Cluster_83"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
octave_config = None

qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

# different controls just for coloring of the generated samples
def x_pi2():
    align()
    play("x_pi/2", "x_control")


def y_pi2():
    align()
    play("y_pi/2" * amp(0.5), "y_control")


def id_gate():
    align()
    wait(pulse_len, "x_control")


def post_circuit(out_st):
    align()
    I = declare(fixed)
    measure("readoutOp", "readout", None, I)
    save(I, out_st)


GST_sequence_file = "/workspaces/HI_20250106_SeigoTarucha/gate_set_tomography/Circuits_before_results.txt"
# gate keys should match the model gates without the 'G' at the beginning.
gate_macros = {"xpi2:0": x_pi2, "ypi2:0": y_pi2, "[]": id_gate}
gst = QuaGST(
    GST_sequence_file,
    model=smq1Q_XYI,
    basic_gates_macros=gate_macros,
    N_shots=1,
    post_circuit=post_circuit,
    config=config,
    quantum_machines_manager=qmm,
    # simulate=SimulationConfig(int(1e5)),
)
gst.run(
    300,
    # plot_simulated_samples_con="con1",
)
# gst.last_job.get_simulated_samples().con1.plot()
# gst.run_IO()

gst_script = open("gst_qua.txt", "w")
print(*gst.qua_script, file=gst_script)
gst_script.close()

results = gst.results

# %%
