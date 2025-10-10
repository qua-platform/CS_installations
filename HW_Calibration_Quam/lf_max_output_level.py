import sys
sys.path.append(
    "/Users/kalidu_laptop/QUA/CS_installations/HW_Calibration_Quam"
)
from QUAM_setup import BaseQuam
from qm.qua import *
import numpy as np
from qualang_tools.units import unit


u = unit(coerce_to_integer=True)


def QM_lf_max_output_setup(
    QM_machine: BaseQuam,
    QM_output: int, 
    duration: float, 
    output_mode: str = "direct", 
    intermediate_frequency: float = 0, 
) -> None:
    
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    if output_mode == "direct": 
        maxamp = 0.5
    elif output_mode == "amplified":
        maxamp = 2.5
    else: 
        raise ValueError(f"output_mode not valid. Received {output_mode}, not in ['direct', 'amplified]")

    QM_machine.add_dc_channel(
        port_id = QM_output, 
        intermediate_frequency = intermediate_frequency, 
        output_mode = output_mode
    )

    QM_machine.add_dc_flux_pulse(
        port_id = QM_output, 
        pulse_name = "const_pulse", 
        duration = duration, 
        amplitude = maxamp
    )
    dc_ch = QM_machine.dc_channels[str(1)]

    with program() as QM_machine.qua_program: 
        with infinite_loop_():
            dc_ch.play(
                "const_pulse"
            )
            wait(duration)


machine = BaseQuam()
machine.connect(host = "172.16.33.115", cluster_name = "CS_4")
machine.lf_fem = 5

QM_lf_max_output_setup(
    QM_machine = machine, 
    QM_output = 1, 
    intermediate_frequency = 0, 
    duration = 10000,
    output_mode = "amplified"
)

results = machine.open_new_QM_and_execute(fetch_results = False)

# machine.halt_running_jobs()
