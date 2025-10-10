import sys
sys.path.append(
    "/Users/kalidu_laptop/QUA/CS_installations/HW_Calibration_Quam"
)
from QUAM_setup import BaseQuam
from qm.qua import *
import numpy as np
from qualang_tools.units import unit



u = unit(coerce_to_integer=True)



def QM_mw_max_output_setup(
    QM_machine: BaseQuam,
    QM_output: int, 
    intermediate_frequency: float, 
    duration: float, 
    rf_frequency: float, 
    full_scale_mw_power: int = 16,
) -> None:
    
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    QM_machine.add_mw_channel(
        port_id = QM_output, 
        intermediate_frequency = intermediate_frequency, 
        rf_frequency = rf_frequency, 
        rf_power = full_scale_mw_power
    )

    QM_machine.add_mw_drive_pulse(
        port_id = QM_output, 
        pulse_name = "drive_pulse", 
        amplitude = 1, 
        duration = duration,
    )

    mw_ch = QM_machine.mw_channels[str(1)]

    with program() as QM_machine.qua_program: 
        with infinite_loop_():
            mw_ch.play(
                "drive_pulse"
            )
        
def QM_execute_and_retrieve_data(
    QM_machine:BaseQuam,
): 
    results = QM_machine.open_new_QM_and_execute(
                    fetch_results = False
                )
    return results

machine = BaseQuam()
machine.connect(host = "172.16.33.115", cluster_name = "CS_4")
machine.mw_fem = 1
QM_mw_max_output_setup(
    QM_machine = machine, 
    QM_output = 1, 
    intermediate_frequency = 10e6, 
    duration = 10000,
    rf_frequency = 2e9, 
    full_scale_mw_power= 16
)
results = machine.open_new_QM_and_execute(fetch_results = False)

# machine.halt_running_jobs()


