from iqcc_cloud_client import IQCC_Cloud
from qm import QuantumMachinesManager, DictQuaConfig, program
from qm.qua import *
from configuration import config

with program() as hello_QUA:
    a = declare(fixed)
    r1 = declare_stream()
    r2 = declare_stream()
    v2 = declare(
        bool,
    )

    with for_(a, 0, a < 1.1, a + 0.05):

        # play("pi" * amp(a), "qubit")
        save(a, r1)
        assign(v2, (a > 0.2))
        save(v2, r2)
    with stream_processing():
        r1.save_all("measurements")
        r2.save_all("state")

# https://cloud.i-qcc.com  qc_galilee  <token - who are you, what you can use, when you can use>
c = IQCC_Cloud(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiaWVlZV91c2VyMSIsImV4cGlyZXMiOjE3MjYwNTgyMjkuODQwMTAzOX0.lYarOxsx9KyFNC5UYk5Pe6VgN6Qp7K9z0kK1-dIu1cQ"
)
results = c.execute(hello_QUA, config)
print(results)
