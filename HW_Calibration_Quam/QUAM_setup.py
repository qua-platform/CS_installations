from typing import Dict, ClassVar, Optional, List
from dataclasses import field
import numpy as np
from quam.core import quam_dataclass, QuamRoot
from quam.components.channels import (
    MWChannel,
    InOutMWChannel,
    SingleChannel,
    StickyChannelAddon,
)
from quam.components import DigitalOutputChannel
from quam.components.ports import (
    FEMPortsContainer,
    LFFEMAnalogOutputPort,
    MWFEMAnalogOutputPort,
    MWFEMAnalogInputPort,
    FEMDigitalOutputPort,
)
from quam.components.pulses import SquarePulse, SquareReadoutPulse

from qm import QuantumMachinesManager, QuantumMachine
from qualang_tools.config.helper_tools import get_band


@quam_dataclass
class BaseQuam(QuamRoot):
    mw_channels: Dict[str, MWChannel] = field(default_factory=dict)
    dc_channels: Dict[str, SingleChannel] = field(default_factory=dict)
    network: dict = field(default_factory=dict)
    qmm: ClassVar[Optional[QuantumMachinesManager]] = None
    qm: ClassVar[Optional[QuantumMachine]] = None
    qua_program = None
    lf_fem: int = 1
    mw_fem: int = 2

    @classmethod
    def load(cls, *args, **kwargs) -> "BaseQuam":
        return super().load(*args, **kwargs)

    def connect(self, host: str, cluster_name: str) -> QuantumMachinesManager:
        """Open a Quantum Machine Manager with the credentials ("host" and "cluster_name") as defined in the network file.

        Returns:
            QuantumMachinesManager: The opened Quantum Machine Manager.
        """

        self.qmm = QuantumMachinesManager(host, cluster_name=cluster_name)
        return self.qmm

    def add_dc_channel(
        self,
        port_id: int,
        voltage_offset: float = 0.0,
        intermediate_frequency: float = 0.0,
        controller: str = "con1",
        upsampling_mode: str = "pulse",
        output_mode: str = "direct",
        sampling_rate: float = 1e9,
        digital_port_id: int = 1,
    ) -> None:
        digital_outputs = dict()
        digital_outputs[f"scope_trigger_dc"] = DigitalOutputChannel(
            opx_output=FEMDigitalOutputPort(controller, self.lf_fem, digital_port_id),
            delay=57,  # 57ns for QOP222 and above
            buffer=18,  # 18ns for QOP222 and above
            # shareable=True
        )
        self.dc_channels[str(port_id)] = SingleChannel(
            id=f"dc{port_id}",
            opx_output=LFFEMAnalogOutputPort(
                controller, self.lf_fem, port_id, offset=voltage_offset
            ),
            digital_outputs=digital_outputs,
            opx_output_offset=voltage_offset,
            intermediate_frequency=intermediate_frequency,
        )
        dc_ch = self.dc_channels[str(port_id)]
        dc_ch.opx_output.output_mode = output_mode
        dc_ch.opx_output.upsampling_mode = upsampling_mode
        dc_ch.opx_output.sampling_rate = sampling_rate
        dc_ch.opx_output.shareable = True
        dc_ch.opx_output_offset = voltage_offset

    def add_mw_channel(
        self,
        port_id: int,
        intermediate_frequency: float,
        rf_frequency: float,
        rf_power: float,
        controller: str = "con1",
        upconverter: int = 1,
        digital_port_id: int = 1,
        id: str = None,
    ) -> None:

        if id is None:
            id = f"mw{port_id}"
            quam_id = str(port_id)
        else:
            id = f"{id}{port_id}"
            quam_id = str(port_id) + "_twin"
        if str(port_id) in self.mw_channels.keys():
            upconverters = {
                1: {
                    "frequency": self.mw_channels[str(port_id)].opx_output.upconverters[
                        1
                    ]["frequency"]
                },
                2: {"frequency": rf_frequency - intermediate_frequency},
            }

        else:
            upconverters = {
                1: {"frequency": rf_frequency - intermediate_frequency},
                2: {"frequency": rf_frequency - intermediate_frequency},
            }
        digital_outputs = dict()
        digital_outputs[f"scope_trigger_mw"] = DigitalOutputChannel(
            opx_output=FEMDigitalOutputPort(controller, self.mw_fem, digital_port_id),
            delay=57,  # 57ns for QOP222 and above
            buffer=18,  # 18ns for QOP222 and above
            # shareable=True
        )
        self.mw_channels[quam_id] = MWChannel(
            id=id,
            opx_output=MWFEMAnalogOutputPort(
                controller,
                self.mw_fem,
                port_id,
                band=get_band(rf_frequency),
                upconverters=upconverters,
            ),
            digital_outputs=digital_outputs,
        )

        self.mw_channels[quam_id].RF_frequency = None
        self.mw_channels[quam_id].RF_frequency = rf_frequency
        self.mw_channels[quam_id].intermediate_frequency = intermediate_frequency
        self.mw_channels[quam_id].opx_output.full_scale_power_dbm = rf_power
        self.mw_channels[quam_id].upconverter = upconverter
        self.mw_channels[quam_id].opx_output.shareable = True

    def add_mw_readout_channel(
        self,
        output_port_id: int,
        input_port_id: int,
        intermediate_frequency: float,
        rf_frequency: float,
        rf_power: float,
        controller: str = "con1",
        upconverter: int = 1,
        input_gain_db: int = 0,
        digital_port_id: int = 1,
        id: str = None,
    ) -> None:

        if id is None:
            id = f"mw{output_port_id}"
            quam_id = str(output_port_id)
        else:
            id = f"{id}{output_port_id}"
            quam_id = str(output_port_id) + "_twin"
        if str(output_port_id) in self.mw_channels.keys():
            upconverters = {
                1: {
                    "frequency": self.mw_channels[
                        str(output_port_id)
                    ].opx_output.upconverters[1]["frequency"]
                },
                2: {"frequency": rf_frequency - intermediate_frequency},
            }

        else:
            upconverters = {
                1: {"frequency": rf_frequency - intermediate_frequency},
                2: {"frequency": rf_frequency - intermediate_frequency},
            }

        digital_outputs = dict()
        digital_outputs[f"scope_trigger_readout"] = DigitalOutputChannel(
            opx_output=FEMDigitalOutputPort(controller, self.mw_fem, digital_port_id),
            delay=57,  # 57ns for QOP222 and above
            buffer=18,  # 18ns for QOP222 and above
            # shareable=True
        )
        self.mw_channels[quam_id] = InOutMWChannel(
            id=id,
            opx_output=MWFEMAnalogOutputPort(
                controller,
                self.mw_fem,
                output_port_id,
                band=get_band(rf_frequency),
                upconverters=upconverters,
            ),
            opx_input=MWFEMAnalogInputPort(
                controller,
                self.mw_fem,
                input_port_id,
                band=get_band(rf_frequency),
                downconverter_frequency=rf_frequency - intermediate_frequency,
                gain_db=input_gain_db,
            ),
            digital_outputs=digital_outputs,
            time_of_flight=300,
        )

        self.mw_channels[quam_id].RF_frequency = None
        self.mw_channels[quam_id].RF_frequency = rf_frequency
        self.mw_channels[quam_id].intermediate_frequency = intermediate_frequency
        self.mw_channels[quam_id].opx_output.full_scale_power_dbm = rf_power
        self.mw_channels[quam_id].upconverter = upconverter
        self.mw_channels[quam_id].opx_output.shareable = True
        self.mw_channels[quam_id].opx_input.shareable = True

    def add_mw_drive_pulse(
        self,
        port_id: int,
        pulse_name: str,
        duration: float,
        amplitude: float,
        axis_angle: float = 0.0,
    ) -> None:
        """Add a microwave pulse to the specified channel."""
        if str(port_id) not in self.mw_channels:
            raise ValueError(f"MW channel {port_id} does not exist.")

        mw_channel = self.mw_channels[str(port_id)]
        mw_channel.operations[pulse_name] = SquarePulse(
            amplitude=amplitude, axis_angle=axis_angle, length=duration, digital_marker="ON"
        )

    def add_dc_flux_pulse(
        self,
        port_id: int,
        pulse_name: str,
        duration: float,
        amplitude: float,
    ) -> None:
        """Add a microwave pulse to the specified channel."""
        if str(port_id) not in self.dc_channels:
            raise ValueError(f"DC channel {port_id} does not exist.")

        dc_channel = self.dc_channels[str(port_id)]
        dc_channel.operations[pulse_name] = SquarePulse(
            amplitude=amplitude, length=duration, digital_marker="ON"
        )

    def add_mw_readout_pulse(
        self,
        port_id: int,
        pulse_name: str,
        duration: float,
        amplitude: float,
        phase: float = None,
    ) -> None:
        """Add a microwave pulse to the specified channel."""
        if str(port_id) not in self.mw_channels:
            raise ValueError(f"MW channel {port_id} does not exist.")

        mw_channel = self.mw_channels[str(port_id)]
        mw_channel.operations[pulse_name] = SquareReadoutPulse(
            amplitude=amplitude, axis_angle=phase, length=duration, digital_marker="ON"
        )

    def update_dc_offset(
        self,
        port_id: int,
        offset: float,
    ) -> None:
        """Update the offset of a DC channel."""
        if str(port_id) not in self.dc_channels:
            raise ValueError(f"DC channel {port_id} does not exist.")
        self.qm.update_config(
            {
                "version": 1,
                "controllers": {
                    "con1": {
                        "fems": {
                            self.lf_fem: {
                                "type": "LF",
                                "analog_outputs": {port_id: {"offset": offset}},
                            }
                        }
                    }
                },
            }
        )

    def update_drive_frequency(
        self,
        port_id: int,
        drive_frequency: float,
        oscillator: int = 1,
    ) -> None:
        """Update the frequency of a microwave channel."""
        band = get_band(drive_frequency)
        if band != self.mw_channels[str(port_id)].opx_output.band:
            self.qm.close()
            self.mw_channels[str(port_id)].opx_output.band = band
            self.mw_channels[str(port_id)].opx_output.upconverters[1]["frequency"] = (
                drive_frequency - self.mw_channels[str(port_id)].intermediate_frequency
            )
            self.mw_channels[str(port_id)].opx_output.upconverters[2]["frequency"] = (
                drive_frequency - self.mw_channels[str(port_id)].intermediate_frequency
            )
            self.qm = self.qmm.open_qm(self.generate_config())
            job = self.qm.execute(self.qua_program)

        else:
            running_jobs = self.qm.get_jobs(status=["Running"])
            if len(running_jobs) == 1:
                job = self.qm.get_job(running_jobs[0].id)
                job.set_converter_frequency(
                    self.mw_channels[str(port_id)].name,
                    drive_frequency
                    - self.mw_channels[str(port_id)].intermediate_frequency,
                    "upconverter",
                )

        return job

    def open_new_QM_and_execute(
        self, 
        fetch_results: bool = False,
    ):
        self.qm = self.qmm.open_qm(self.generate_config())
        job = self.qm.execute(self.qua_program)

        if fetch_results:
            res = job.result_handles
            streams = res.fetch_results()
            return streams


    def halt_running_jobs(
        self, 
    ) -> None: 
        running_jobs = self.qm.get_jobs(status = ["Running"])
        if len(running_jobs) > 0:  
            for job_object in running_jobs:
                job = self.qm.get_job(job_object.id)
                job.cancel()



# machine = BaseQuam()
# machine.add_dc_channel(1)
# machine.add_dc_channel(2)
# machine.add_mw_channel(2, intermediate_frequency=5e9, rf_frequency=4.5e9, rf_power=1)
# machine.add_mw_drive_pulse(
#     port_id=2, pulse_name="drive_pulse", duration=1000, amplitude=0.5
# )
# machine.generate_config()