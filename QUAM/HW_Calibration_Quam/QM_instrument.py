
from qualang_tools.config.helper_tools import get_full_scale_power_dBm_and_amplitude
from qualang_tools.results import fetching_tool
from qualang_tools.units import unit
from .QUAM_setup import BaseQuam
from qm.qua import *
import numpy as np
import sys

sys.path.append(
    "/Users/kalidu_laptop/QUA/CS_installations/HW_Calibration_Quam"
)

u = unit(coerce_to_integer=True)


def QM_drive_turn_on(QM_machine: BaseQuam, QM_drive_Channel: int, ON):
    """
    Enable channel output and turn on sine generators if 'ON' is True. Turn off if 'ON' is False

    args:
        QM_machine: QM_drive device
        QM_drive_Channel: physical channel number
        ON: True or False for on or off
    """
    if not ON:
        QM_machine.qm.close()
    else:
        config = QM_machine.generate_config()
        QM_machine.qm = QM_machine.qmm.open_qm(config, close_other_machines=False)
        QM_machine.qm.execute(QM_machine.qua_program)


def QM_drive_output_continuous_tone_setup(
    QM_machine: BaseQuam,
    QM_drive_Channel: int,
    oscillator: int,
    drive_power: int,
    i_amplitude: float,
    q_amplitude: float,
    oscillator_frequency: float,
    drive_frequency: float,
):
    """
    Output a continuous tone to selected output channel of the selected QM_drive device

    args:
        QM_machine: QM_drive device
        QM_drive_Channel: physical channel number in dBm
        oscillator: oscillator number
        drive_power: output range in dB
        i_amplitude: amplitude of the sin wave (I)
        q_amplitude: amplitude of the cosine wave (Q)
        oscillator_frequency: local oscillator (LO) frequency in Hz
        drive_frequency: output frequency of tone signal (RF) in Hz
    """
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    s = i_amplitude + 1j * q_amplitude
    fsp_dbm, amp = get_full_scale_power_dBm_and_amplitude(
        drive_power, max_amplitude=np.abs(s)
    )

    QM_machine.add_mw_channel(
        port_id=QM_drive_Channel,
        intermediate_frequency=oscillator_frequency,
        rf_frequency=drive_frequency,
        rf_power=fsp_dbm,
        upconverter=oscillator,
    )
    QM_machine.add_mw_drive_pulse(
        port_id=QM_drive_Channel,
        pulse_name="cw",
        duration=1000,
        amplitude=amp,
        phase=float(np.angle(s)),
    )

    with program() as QM_machine.qua_program:
        with infinite_loop_():
            QM_machine.mw_channels[str(QM_drive_Channel)].play("cw")


def QM_drive_2_output_continuous_tones_setup(
    QM_machine: BaseQuam,
    QM_drive_Channel1: int,
    QM_drive_Channel2: int,
    drive_power1: int,
    drive_power2: int,
    i_amplitude: float,
    q_amplitude: float,
    oscillator_frequency1: float,
    oscillator_frequency2: float,
    drive_frequency1: float,
    drive_frequency2: float,
):
    """
    Output a continuous tone to selected output channel of the selected QM_drive device

    args:
        QM_machine: QM_drive device
        QM_drive_Channel: physical channel number in dBm
        oscillator: oscillator number
        drive_power: output range in dB
        i_amplitude: amplitude of the sin wave (I)
        q_amplitude: amplitude of the cosine wave (Q)
        oscillator_frequency: local oscillator (LO) frequency in Hz
        drive_frequency: output frequency of tone signal (RF) in Hz
    """
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    s = i_amplitude + 1j * q_amplitude
    fsp_dbm1, amp1 = get_full_scale_power_dBm_and_amplitude(
        drive_power1, max_amplitude=np.abs(s)
    )
    fsp_dbm2, amp2 = get_full_scale_power_dBm_and_amplitude(
        drive_power2, max_amplitude=1
    )
    QM_machine.add_mw_channel(
        port_id=QM_drive_Channel1,
        intermediate_frequency=oscillator_frequency1,
        rf_frequency=drive_frequency1,
        rf_power=fsp_dbm1,
        upconverter=1,
    )
    QM_machine.add_mw_drive_pulse(
        port_id=QM_drive_Channel1,
        pulse_name="cw",
        duration=1000,
        amplitude=amp1,
        phase=float(np.angle(s)),
    )
    QM_machine.add_mw_channel(
        port_id=QM_drive_Channel2,
        intermediate_frequency=oscillator_frequency2,
        rf_frequency=drive_frequency2,
        rf_power=fsp_dbm2,
        upconverter=2,
        id="mw_twin",
    )
    QM_machine.add_mw_drive_pulse(
        port_id=str(QM_drive_Channel2) + "_twin",
        pulse_name="cw",
        duration=1000,
        amplitude=amp2,
        phase=float(np.angle(s)),
    )

    with program() as QM_machine.qua_program:
        with infinite_loop_():
            QM_machine.mw_channels[str(QM_drive_Channel1)].play("cw")
            QM_machine.mw_channels[str(QM_drive_Channel2) + "_twin"].play("cw")


def QM_drive_output_chirp_pulse(
    QM_machine: BaseQuam,
    QM_drive_Channel: int,
    oscillator: int,
    drive_power: int,
    i_amplitude: float,
    q_amplitude: float,
    oscillator_frequency: float,
    drive_frequency: float,
    chirp_duration: int = 1000,  # in ns
    chirp_start_frequency: float = -400e6,  # in Hz
    chirp_stop_frequency: float = 400e6,  # in Hz
):
    """
    Output a chirp pulse with spectrum center at the modulation frequency +/- the frequency range,
    to selected output channel of the selected QM_drive device

    args:
        QM_machine: QM_drive device
        QM_drive_Channel: physical channel number in dBm
        oscillator: oscillator number
        i_amplitude: amplitude of the sin wave (I)
        q_amplitude: amplitude of the cosine wave (Q)
        oscillator_frequency: local oscillator (LO) frequency in Hz
        modulation_frequency: modulation frequency in Hz
        chirp_range: frequency range of the chirp pulse in Hz

    """
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    s = i_amplitude + 1j * q_amplitude
    QM_machine.add_mw_channel(
        port_id=QM_drive_Channel,
        intermediate_frequency=chirp_start_frequency,
        rf_frequency=drive_frequency + chirp_start_frequency,
        rf_power=drive_power,
        upconverter=oscillator,
    )
    QM_machine.add_mw_drive_pulse(
        port_id=QM_drive_Channel,
        pulse_name="cw",
        duration=chirp_duration,
        amplitude=np.abs(s),
        phase=float(np.angle(s)),
    )

    chirp_rate = (
        chirp_stop_frequency - chirp_start_frequency
    ) / chirp_duration  # Hz/nsec
    mw_ch = QM_machine.mw_channels[str(QM_drive_Channel)]
    with program() as QM_machine.qua_program:
        with infinite_loop_():
            mw_ch.update_frequency(chirp_start_frequency)
            mw_ch.wait(100)
            mw_ch.play(
                "cw", chirp=(chirp_rate, "Hz/nsec"), duration=chirp_duration // 4
            )


def QM_flux_turn_DC_on(QM_machine: BaseQuam, QM_flux_channel: int, ON: bool):
    """
    Enables channel output if 'ON'. Turn off if 'ON' is False

    args:
        QM_machine: QM_flux device
        QM_flux_channel: physical channel number
        ON: True or False for on or off
    """
    if not ON:
        QM_machine.qm.close()
    else:
        config = QM_machine.generate_config()
        QM_machine.qm = QM_machine.qmm.open_qm(config, close_other_machines=False)
        if QM_machine.qua_program is not None:
            QM_machine.qm.execute(QM_machine.qua_program)


def QM_flux_output_DC_voltage_offset(
    QM_machine: BaseQuam,
    QM_flux_channel: int,
    Voltage_range: float,
    Voltage_offset: float,
):
    """
    Set a voltage range and output a DC voltage to the selected QM_flux device and channel

    args:
        QM_machine: QM_flux device
        QM_flux_channel: physical channel number
        Voltage_offset: voltage offset to set in V
    """
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    QM_machine.add_dc_channel(
        QM_flux_channel, output_mode="amplified", upsampling_mode="pulse"
    )


def QM_flux_output_DC_voltage_pulse(
    QM_machine: BaseQuam,
    QM_flux_channel: int,
    Voltage_range: float,
    Voltage_offset: float,
    oscillator_frequency: float = 0.0,
):
    """
    Set a voltage range and output a DC voltage to the selected QM_flux device and channel

    args:
        QM_machine: QM_flux device
        QM_flux_channel: physical channel number
        Voltage_offset: voltage offset to set in V
    """
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    if oscillator_frequency == 0:
        QM_machine.add_dc_channel(
            QM_flux_channel, output_mode="amplified", upsampling_mode="pulse"
        )
        QM_machine.add_dc_flux_pulse(
            QM_flux_channel, "square", duration=1000, amplitude=Voltage_offset
        )
        dc_ch = QM_machine.dc_channels[str(QM_flux_channel)]
        with program() as QM_machine.qua_program:
            with infinite_loop_():
                dc_ch.play("square")
                # dc_ch.wait(25)
    else:
        QM_machine.add_dc_channel(
            QM_flux_channel,
            output_mode="amplified",
            upsampling_mode="mw",
            voltage_offset=Voltage_offset,
        )
        QM_machine.add_dc_flux_pulse(
            QM_flux_channel, "sine", duration=1000, amplitude=0.25
        )
        dc_ch = QM_machine.dc_channels[str(QM_flux_channel)]
        with program() as QM_machine.qua_program:
            with infinite_loop_():
                dc_ch.play("sine")
                dc_ch.wait(25)


def QM_flux_output_continuous_tone(
    QM_machine: BaseQuam,
    QM_flux_channel: int,
    digital_oscillator: int,
    drive_frequency: float,
    drive_amplitude: float,
    voltage_offset: float = 0.0,
):
    """
    Output a continuous tone to selected output channel of the selected QM_flux device

    args:
        QM_read: QM_read device
        QM_flux_channel: physical channel number
        digital_oscillator: oscillator number
        drive_frequency: output frequency of tone signal in Hz
        drive_amplitude: amplitude of the signal in V


    """
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    QM_machine.add_dc_channel(
        QM_flux_channel,
        output_mode="amplified",
        upsampling_mode="mw",
        voltage_offset=voltage_offset,
        intermediate_frequency=drive_frequency,
    )
    QM_machine.add_dc_flux_pulse(
        QM_flux_channel, "sine", duration=1000, amplitude=drive_amplitude
    )

    dc_ch = QM_machine.dc_channels[str(QM_flux_channel)]
    with program() as QM_machine.qua_program:
        with infinite_loop_():
            dc_ch.play("sine")
            # dc_ch.wait(25)


def QM_flux_output_continuous_tone_with_chirping(
    QM_machine: BaseQuam,
    QM_flux_channel: int,
    digital_oscillator: int,
    start_frequency: float,
    stop_frequency: float,
    drive_amplitude: float,
    drive_duration: int = 1000,
    voltage_offset: float = 0.0,
):
    """
    Output a continuous tone to selected output channel of the selected QM_flux device

    args:
        QM_read: QM_read device
        QM_flux_channel: physical channel number
        digital_oscillator: oscillator number
        drive_frequency: output frequency of tone signal in Hz
        drive_amplitude: amplitude of the signal in V


    """
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    QM_machine.add_dc_channel(
        QM_flux_channel,
        output_mode="direct",
        upsampling_mode="mw",
        voltage_offset=voltage_offset,
        intermediate_frequency=start_frequency,
        sampling_rate=2e9,
    )
    QM_machine.add_dc_flux_pulse(
        QM_flux_channel, "sine", duration=1000, amplitude=drive_amplitude
    )
    chirp_rate = (stop_frequency - start_frequency) * 1e6 / drive_duration
    dc_ch = QM_machine.dc_channels[str(QM_flux_channel)]
    with program() as QM_machine.qua_program:
        with infinite_loop_():
            dc_ch.play(
                "sine", chirp=(chirp_rate, "Hz/nsec"), duration=drive_duration // 4
            )
            # dc_ch.wait(25)


def QM_flux_output_chirp_pulse(
    QM_machine: BaseQuam,
    QM_flux_channel: int,
    digital_oscillator: int,
    drive_frequency: float,
    drive_amplitude: float,
    modulation_frequency: float,
    chirp_range: float,
):
    """
    Output a chirp pulse with spectrum center at the modulation frequency +/- the frequency range,
    to selected output channel of the selected QM_drive device

    args:
        QM_read: QM_read device
        QM_flux_channel: physical channel number
        digital_oscillator: oscillator number
        drive_frequency: output frequency of tone signal in Hz
        drive_amplitude: amplitude of the signal in V
        modulation_frequency: modulation frequency in Hz
        chirp_range: frequency range of the chirp pulse in Hz


    """


def QM_read_turn_on(QM_read, QM_read_Channel: int, ON: bool):
    """
    Enables channel output and turn on sine generator if ON is True. Turn off if ON is False

    args:
        QM_machine: QM_drive device
        QM_drive_Channel: physical channel number
        ON: True or False for on or off
    """


def QM_read_output_continuous_tone(
    QM_machine,
    QM_readout_Channel: int,
    readout_power: float,
    oscillator: int,
    oscillator_frequency: float,
    drive_frequency: float,
):
    """
    Output a continuous tone to selected output channel of the selected QM_machine device

    args:
        QM_machine: QM_read device
        QM_readout_Channel: physical channel number
        readout_power:  amplitude of the signal in dBm
        oscillator: oscillator number
        oscillator: oscillator number
        oscillator_frequency: local oscillator (LO) frequency in Hz
        drive_frequency: output frequency of tone signal (RF) in Hz

    """
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    s = 1.0 + 1j * 0.0
    fsp_dbm, amp = get_full_scale_power_dBm_and_amplitude(
        readout_power, max_amplitude=np.abs(s)
    )

    QM_machine.add_mw_readout_channel(
        output_port_id=QM_readout_Channel,
        input_port_id=1,
        intermediate_frequency=oscillator_frequency,
        rf_frequency=drive_frequency,
        rf_power=fsp_dbm,
        upconverter=oscillator,
    )
    QM_machine.add_mw_readout_pulse(
        port_id=QM_readout_Channel,
        pulse_name="readout",
        duration=10000,
        amplitude=amp * 0,
        phase=float(np.angle(s)),
    )

    with program() as QM_machine.qua_program:
        adc_st = declare_stream(adc_trace=True)

        QM_machine.mw_channels[str(QM_readout_Channel)].play("readout")


def QM_read_output_rawdata(
    QM_machine,
    QM_readout_Channel: int,
    readout_power: float,
    oscillator: int,
    oscillator_frequency: float,
    drive_frequency: float,
):
    """
    Output a continuous tone to selected output channel of the selected QM_machine device

    args:
        QM_machine: QM_read device
        QM_readout_Channel: physical channel number
        readout_power:  amplitude of the signal in dBm
        oscillator: oscillator number
        oscillator: oscillator number
        oscillator_frequency: local oscillator (LO) frequency in Hz
        drive_frequency: output frequency of tone signal (RF) in Hz

    """
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    s = 1.0 + 1j * 0.0
    fsp_dbm, amp = get_full_scale_power_dBm_and_amplitude(
        readout_power, max_amplitude=np.abs(s)
    )

    QM_machine.add_mw_readout_channel(
        output_port_id=QM_readout_Channel,
        input_port_id=1,
        intermediate_frequency=oscillator_frequency,
        rf_frequency=drive_frequency,
        rf_power=fsp_dbm,
        upconverter=oscillator,
    )
    QM_machine.add_mw_readout_pulse(
        port_id=QM_readout_Channel,
        pulse_name="readout",
        duration=10000,
        amplitude=amp * 0,
        phase=float(np.angle(s)),
    )

    with program() as QM_machine.qua_program:
        adc_st = declare_stream(adc_trace=True)

        QM_machine.mw_channels[str(QM_readout_Channel)].measure(
            "readout", stream=adc_st
        )

        with stream_processing():
            adc_st.input1().real().save("adc_I")
            adc_st.input1().image().save("adc_Q")


def QM_read_output_IQdata(
    QM_machine,
    QM_readout_Channel: int,
    readout_power: float,
    oscillator: int,
    oscillator_frequency: float,
    drive_frequency: float,
):
    """
    Output a continuous tone to selected output channel of the selected QM_machine device

    args:
        QM_machine: QM_read device
        QM_readout_Channel: physical channel number
        readout_power:  amplitude of the signal in dBm
        oscillator: oscillator number
        oscillator: oscillator number
        oscillator_frequency: local oscillator (LO) frequency in Hz
        drive_frequency: output frequency of tone signal (RF) in Hz

    """
    QM_machine.mw_channels = {}
    QM_machine.dc_channels = {}

    s = 1.0 + 1j * 0.0
    fsp_dbm, amp = get_full_scale_power_dBm_and_amplitude(
        readout_power, max_amplitude=np.abs(s)
    )

    QM_machine.add_mw_readout_channel(
        output_port_id=QM_readout_Channel,
        input_port_id=1,
        intermediate_frequency=oscillator_frequency,
        rf_frequency=drive_frequency,
        rf_power=fsp_dbm,
        upconverter=oscillator,
    )
    QM_machine.add_mw_readout_pulse(
        port_id=QM_readout_Channel,
        pulse_name="readout",
        duration=10000,
        amplitude=amp * 0,
        phase=float(np.angle(s)),
    )

    with program() as QM_machine.qua_program:
        I = declare(fixed)
        Q = declare(fixed)
        I_st = declare_stream()
        Q_st = declare_stream()

        QM_machine.mw_channels[str(QM_readout_Channel)].measure(
            "readout", qua_vars=(I, Q)
        )
        save(I, I_st)
        save(Q, Q_st)

        with stream_processing():
            I_st.save_all("I")
            Q_st.save_all("Q")


def QM_fetch_data_raw(QM_machine, port_id):
    job_id = QM_machine.qm.get_jobs(status=["Done"])[0].id
    job = QM_machine.qm.get_job(job_id)
    results = fetching_tool(job, data_list=["adc_I", "adc_Q"])
    I, Q = results.fetch_all()
    return u.raw2volts(I + 1j * Q)


def QM_fetch_data_IQ(QM_machine, port_id):
    job_id = QM_machine.qm.get_jobs(status=["Done"])[0].id
    job = QM_machine.qm.get_job(job_id)
    results = fetching_tool(job, data_list=["I", "Q"])
    I, Q = results.fetch_all()
    readout_len = QM_machine.mw_channels[str(port_id)].operations["readout"].length
    return u.demod2volts(I + 1j * Q, readout_len)
