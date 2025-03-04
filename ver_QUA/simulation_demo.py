import math
import time
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig, LoopbackInterface
from configuration_11 import *
import matplotlib.pyplot as plt
from qm.logger import logger
import numpy as np
import matplotlib.pyplot as plt
import logging 
from pprint import pprint

from qop_saas_simulator import QoPSaaS, QoPSaaSInstance, QoPVersion

# These are static and should usually not be changed.
saas_port = 9000
saas_host = "simulator.qm-saas.dev.quantum-machines.co"

# These should be changed to your credentials.
email = "fabio@quantum-machines.co"
password = "123456789"


# Initialize QOP simulator client
client = QoPSaaS(email=email, password=password)

version = QoPVersion.v2_2_0 # Specify the QOP version
with client.simulator(version) as instance:
    # Initialize QuantumMachinesManager with the simulation instance details
    qmm = QuantumMachinesManager(
        host=instance.sim_host, port=instance.sim_port, connection_headers=instance.default_connection_headers
    )

    set_pt = -0.011
    T = 100  # Integral gain time constant
    alpha = 1 / T
    kp = 1
    ki = 5
    kd = 0
    initial_amp = 0.1
    with program() as prog:
        point = declare(fixed, value=0)
        set_point = declare(fixed, value=set_pt)
        error = declare(fixed, value=0.002)
        prev_error = declare(fixed, value=0)  # previous step error
        accum = declare(fixed, value=0)
        gradient = declare(fixed, value=0.017)
        a = declare(fixed, value=initial_amp)
        b = declare(fixed)
        c = Random()
        with for_(b,0,b<1,b+0.1):

            frame_rotation_2pi(c.rand_fixed(),'readout_demod')
            measure('rr1', 'readout_demod', None, integration.full('cos', point))
            align()
            # save(point, p_st)
            assign(prev_error, error)
            assign(error, (point - set_point) << 1)
            # save(error, 'debug1')
            assign(accum, (1 - alpha) * accum + alpha * error)
            # save(accum, 'debug2')
            assign(gradient, error - prev_error)
            assign(a, a + kp * error + 5 * (5 * (ki * accum)) + kd * gradient)
            # save(a, 'debug3')
            play('const'*amp(a),'q1_xy')




    job = qmm.simulate(config, prog, 
        SimulationConfig(8000,simulation_interface=LoopbackInterface([("con1", 4, "con1", 1)])))
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    # waveform_report.create_plot(samples, plot=True, save_path="./")
    samples.con1.plot()
    plt.show()
