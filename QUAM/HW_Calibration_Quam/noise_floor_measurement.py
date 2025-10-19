import sys
sys.path.append(
    "/Users/kalidu_laptop/QUA/CS_installations/HW_Calibration_Quam"
)
from QUAM_setup import BaseQuam
from qm.qua import *
import numpy as np
from qualang_tools.config.helper_tools import get_full_scale_power_dBm_and_amplitude
from qualang_tools.results import fetching_tool
from qualang_tools.units import unit


u = unit(coerce_to_integer=True)

QM_OUTPUT = 1
QM_INPUT = 1
IF = 10e6
DURATION = 10000
RF_FREQUENCY = 2e9
READOUT_POWER = 1


def QM_readout_noise_floor_setup(
    QM_machine: BaseQuam,
    QM_readout_output: int,
    QM_readout_input: int,
    intermediate_frequency: float,
    readout_duration: float,
    rf_frequency: float,
    readout_power: int,
) -> None:
    s = 1 + 1j * 0
    fsp_dbm, amp = get_full_scale_power_dBm_and_amplitude(
        readout_power, max_amplitude=np.abs(s)
    )

    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    QM_machine.add_mw_readout_channel(
        output_port_id=QM_readout_output,
        input_port_id=QM_readout_input,
        intermediate_frequency=intermediate_frequency,
        rf_frequency=rf_frequency,
        rf_power=fsp_dbm,
    )

    QM_machine.add_mw_readout_pulse(
        port_id=QM_readout_output,
        pulse_name="readout",
        amplitude=amp,
        duration=readout_duration,
        phase=float(np.angle(s)),
    )

    mw_ch = QM_machine.mw_channels[str(1)]

    with program() as QM_machine.qua_program:
        adc_st = declare_stream(adc_trace=True)

        mw_ch.measure("readout", stream=adc_st)
        with stream_processing():
            adc_st.input1().real().save("adc_I")
            adc_st.input1().image().save("adc_Q")


machine = BaseQuam()
machine.connect(host="172.16.33.115", cluster_name="CS_4")
machine.mw_fem = 1

QM_readout_noise_floor_setup(
    QM_machine=machine,
    QM_readout_output=QM_OUTPUT,
    QM_readout_input=QM_INPUT,
    intermediate_frequency=IF,
    readout_duration=DURATION,
    rf_frequency=RF_FREQUENCY,
    readout_power=READOUT_POWER,
)
results = machine.open_new_QM_and_execute(fetch_results=True)

import matplotlib.pyplot as plt

plt.figure()
plt.plot(results["adc_I"] / 4096)
plt.plot(results["adc_Q"] / 4096)
