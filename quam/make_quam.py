import json
from quam import QuamDict, QuamComponent
from quam.components.ports import (
    MWFEMAnalogOutputPort,
    LFFEMAnalogOutputPort,
    LFFEMAnalogInputPort,
    FEMDigitalOutputPort,
)
from quam.components.channels import MWChannel, DigitalOutputChannel, StickyChannelAddon
from quam.components.pulses import SquarePulse, SquareReadoutPulse
from quam_builder.qpu import Quam
from quam_builder.qubit import Qubit
from quam_builder.components import TankCircuit, XYDrive, QDAC_trigger, PlungerGate


machine = Quam()  # or, Quam.load() if the state already exists

# vvv  delete these if using Quam.load()
machine.network.host = "172.16.33.115"
machine.network.cluster_name = "CS_3"
machine.wiring = QuamDict({})
# ^^^


qubits = [1, 2, 3, 4]
for q in qubits:
    machine.qubits[f"q{q}"] = Qubit(id=q)
    machine.qubits[f"q{q}"].resonator = TankCircuit(
        operations={
            "readout": SquareReadoutPulse(amplitude=0.1, length=1000),
        },
        opx_output=LFFEMAnalogOutputPort(
            controller_id="con1",
            fem_id=5,
            port_id=7,
            sampling_rate=int(2e9),
            upsampling_mode="mw",
        ),
        opx_input=LFFEMAnalogInputPort(
            controller_id="con1",
            fem_id=5,
            port_id=1,
            sampling_rate=int(2e9),
        ),
        time_of_flight=28,
        intermediate_frequency=10e6,
    )
    machine.qubits[f"q{q}"].xy = XYDrive(
        operations={
            "cw": SquarePulse(amplitude=0.5, length=1000),
        },
        opx_output=MWFEMAnalogOutputPort(
            controller_id="con1",
            fem_id=1,
            port_id=1,
            band=1,
            upconverter_frequency=int(3e9),
            full_scale_power_dbm=-8,
        ),
        upconverter=1,
        RF_frequency=3.1e9,
    )
    machine.qubits[f"q{q}"].qdac_trigger = QDAC_trigger(
        operations={
            "trigger": SquarePulse(amplitude=0.0, length=1000, digital_marker="ON"),
        },
        opx_output=MWFEMAnalogOutputPort(
            controller_id="con1",
            fem_id=1,
            port_id=1,
            band=1,
            upconverter_frequency=int(3e9),
            full_scale_power_dbm=-8,
        ),
        RF_frequency=3.0e9,
        digital_outputs={
            "qdac_trigger": DigitalOutputChannel(
                opx_output=FEMDigitalOutputPort("con1", 1, 1),
                delay=57,  # 57ns for QOP222 and above
                buffer=18,  # 18ns for QOP222 and above
            )
        },
    )
    machine.qubits[f"q{q}"].p1 = PlungerGate(
        operations={
            "step": SquarePulse(amplitude=0.25, length=100),
        },
        sticky=StickyChannelAddon(duration=16, digital=False),
        opx_output=LFFEMAnalogOutputPort(
            controller_id="con1",
            fem_id=5,
            port_id=1,
            sampling_rate=int(1e9),
            upsampling_mode="pulse",
            output_mode="amplified",
        ),
        level_init=0.1,
        level_idle=0.23,
        level_readout=0.05,
    )
    machine.qubits[f"q{q}"].p2 = PlungerGate(
        operations={
            "step": SquarePulse(amplitude=0.25, length=100),
        },
        sticky=StickyChannelAddon(duration=16, digital=False),
        opx_output=LFFEMAnalogOutputPort(
            controller_id="con1",
            fem_id=5,
            port_id=2,
            sampling_rate=int(1e9),
            upsampling_mode="pulse",
            output_mode="amplified",
        ),
        level_init=-0.1,
        level_idle=-0.23,
        level_readout=-0.05,
    )


config = machine.generate_config()
# save machine into state.json
machine.save("state.json")

# %%
# View the corresponding "raw-QUA" config
with open("dummy_qua_config.json", "w+") as f:
    json.dump(machine.generate_config(), f, indent=4)
