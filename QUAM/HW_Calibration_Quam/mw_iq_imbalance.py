import sys, time
import numpy as np
sys.path.append("/Users/kalidu_laptop/QUA/CS_installations/HW_Calibration_Quam")

from QUAM_setup import BaseQuam
from qm.qua import *
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)


RF_FREQUENCY_HZ = 2e9
IF_FREQUENCY_HZ = 50e6
PULSE_DURATION_NS = 2000
REPS = 500
FULL_SCALE_DBM = 16
ADC_PORT = 1
MW_PORT = 1


def setup_iq_loopback_check(
    QM_machine: BaseQuam,
    mw_output_port: int,
    mw_input_port: int,
    rf_frequency: float,
    intermediate_frequency: float,
    duration: int,
    rf_power: int
):
    # Keep the machine clean
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}
    QM_machine.add_mw_readout_channel(
        output_port_id = mw_output_port, 
        input_port_id = mw_input_port, 
        rf_frequency = rf_frequency, 
        intermediate_frequency=intermediate_frequency,
        rf_power = rf_power, 
        input_gain_db=1
    )

    QM_machine.add_mw_readout_pulse(
        port_id = mw_output_port, 
        pulse_name = "drive_readout", 
        duration = duration, 
        amplitude = 1
    )

    mw_readout = QM_machine.mw_channels[str(mw_output_port)]

    with program() as QM_machine.qua_program:
        i = declare(fixed)
        q = declare(fixed)
        n = declare(int, value=0)
        i_st = declare_stream()
        q_st = declare_stream()

        with for_(n, 0, n < REPS, n + 1):

            mw_readout.measure("drive_readout",
                qua_vars = (i,q))
            save(i, i_st)
            save(q, q_st)
            mw_readout.wait(100)  # small gap between shots

        with stream_processing():
            i_st.buffer(REPS).save("I")
            q_st.buffer(REPS).save("Q")


machine = BaseQuam()
machine.connect(host="172.16.33.115", cluster_name="CS_4")
machine.mw_fem = 1

setup_iq_loopback_check(
    QM_machine=machine,
    mw_output_port=MW_PORT,
    mw_input_port=ADC_PORT,
    rf_frequency=RF_FREQUENCY_HZ,
    intermediate_frequency=IF_FREQUENCY_HZ,
    duration=PULSE_DURATION_NS,
    rf_power=FULL_SCALE_DBM
)


#waveform_report = machine.open_new_QM_and_simulate(duration = 20000)

# machine.halt_running_jobs()

results = machine.open_new_QM_and_execute(fetch_results=True)

I = np.array(results.get("I"))
Q = np.array(results.get("Q"))

import matplotlib.pyplot as plt
plt.figure()
plt.plot(I)
plt.plot(Q)


S = 4096

I0, Q0 = I - np.mean(I), Q - np.mean(Q)
I_mean, Q_mean = np.mean(I) *S, np.mean(Q)*S


amp_imbalance = (I_mean - Q_mean)
phi_deg = np.degrees(np.angle(np.mean(I + 1j*Q)))

print("Relative phase {:.3f} I = {:.3f}, Q = {:.3f}, Imbalance = {:.3f}".format(phi_deg, I_mean, Q_mean, amp_imbalance))



