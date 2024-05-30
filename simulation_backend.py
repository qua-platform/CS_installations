# %%
from typing import List

import qm

from qualang_tools.simulator.quantum.architectures import TransmonSettings
from qualang_tools.simulator.quantum.architectures.from_qua_channels import (
    TransmonPairBackendChannelIQ, ChannelType, TransmonPairBackendChannelReadout)
from qualang_tools.simulator.quantum.architectures.transmon_pair import TransmonPair
from qualang_tools.simulator.quantum.architectures.transmon_pair_backend_from_qua import TransmonPairBackendFromQUA
from qualang_tools.simulator.quantum.architectures.transmon_pair_settings import TransmonPairSettings
from qualang_tools.simulator.quantum import simulate
from macros import freq_from_qua_config
from configuration_with_octave import config

qubit_1_freq = freq_from_qua_config("q1_xy", config)
qubit_2_freq = freq_from_qua_config("q2_xy", config)
print(f"Simulating with q1 resonant frequency {qubit_1_freq}")
print(f"Simulating with q2 resonant frequency {qubit_2_freq}")

transmon_pair_settings = TransmonPairSettings(
    TransmonSettings(
        resonant_frequency=qubit_1_freq,
        anharmonicity=-320000000.0,
        rabi_frequency=0.22e9
    ),
    TransmonSettings(
        resonant_frequency=qubit_2_freq,
        anharmonicity=-320000000.0,
        rabi_frequency=0.26e9
    ),
    coupling_strength=0.002e9
)

transmon_pair = TransmonPair(transmon_pair_settings)


channel_map = {
    "q1_xy": TransmonPairBackendChannelIQ(
        qubit_index=0,
        carrier_frequency=qubit_1_freq,
        operator_i=transmon_pair.transmon_1_drive_operator(quadrature='I'),
        operator_q=transmon_pair.transmon_1_drive_operator(quadrature='Q'),
        type=ChannelType.DRIVE
    ),
    "cr_c1t2": TransmonPairBackendChannelIQ(
        qubit_index=0,
        carrier_frequency=qubit_2_freq,
        operator_i=transmon_pair.transmon_1_drive_operator(quadrature='I'),
        operator_q=transmon_pair.transmon_1_drive_operator(quadrature='Q'),
        type=ChannelType.CONTROL
    ),
    "q2_xy": TransmonPairBackendChannelIQ(
        qubit_index=1,
        carrier_frequency=qubit_2_freq,
        operator_i=transmon_pair.transmon_2_drive_operator(quadrature='I'),
        operator_q=transmon_pair.transmon_2_drive_operator(quadrature='Q'),
        type=ChannelType.DRIVE
    ),
    "cr_cancel_c1t2": TransmonPairBackendChannelIQ(
        qubit_index=1,
        carrier_frequency=qubit_2_freq,
        operator_i=transmon_pair.transmon_2_drive_operator(quadrature='I'),
        operator_q=transmon_pair.transmon_2_drive_operator(quadrature='Q'),
        type=ChannelType.CONTROL
    ),
    "rr1": TransmonPairBackendChannelReadout(0),
    "rr2": TransmonPairBackendChannelReadout(1),
}


backend = TransmonPairBackendFromQUA(transmon_pair, channel_map)


def simulate_program(qua_program: qm.Program, num_shots: int, plot_schedules: List[int] = None):
    return simulate.simulate_program(
        qua_program=qua_program,
        qua_config=config,
        qua_config_to_backend_map=channel_map,
        backend=backend,
        num_shots=num_shots,
        schedules_to_plot=plot_schedules,
    )

# %%
