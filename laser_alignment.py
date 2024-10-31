"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from configuration_opx import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.video_mode.videomode import VideoMode

###################
# The QUA program #
###################


def qua_prog(vm: VideoMode):
    with program() as video:
        dc_1 = declare(fixed)
        dc_2 = declare(fixed)
        dc_1_st = declare_stream()
        dc_2_st = declare_stream()
        amp_aom_r, amp_aom_c = vm.declare_variables()
        with infinite_loop_():
            vm.load_parameters()
            # update_frequency("readout_aom", 0.0)
            # update_frequency("control_aom", 0.0)
            align()
            play("readout" * amp(amp_aom_r), "readout_aom")
            play("control" * amp(amp_aom_c), "control_aom")
            measure(
                "readout", "SNSPD", None, integration.full("constant", dc_1, "out1")
            )
            measure("readout", "APD", None, integration.full("constant", dc_2, "out2"))
            save(dc_1, dc_1_st)
            save(dc_2, dc_2_st)

        with stream_processing():
            dc_1_st.buffer(1000).save("signal1")
            dc_2_st.buffer(1000).save("signal2")

    return video


if __name__ == "__main__":
    # Open the Quantum Machine Manager
    qmm = QuantumMachinesManager(qop_ip, cluster_name=cluster_name)
    # Open the Quantum Machine
    qm = qmm.open_qm(config)
    # Define the parameters to be updated in video mode with their initial value and QUA type
    param_dict = {
        "amp_aom_r": (0.0, fixed),
        "amp_aom_c": (0.0, fixed),
    }
    # Initialize the video mode
    video_mode = VideoMode(qm, param_dict)
    # Get the QUA program
    qua_prog = qua_prog(video_mode)
    # Execute the QUA program in video mode
    job = video_mode.execute(qua_prog)
    # Get the results from the OPX in live mode
    results = fetching_tool(job, ["signal1", "signal2"], mode="live")
    # Live plotting
    fig = plt.figure()
    while results.is_processing():
        # Fetch data from the OPX
        signal1, signal2 = results.fetch_all()
        # Convert the data into Volt
        signal1 = -u.demod2volts(signal1, snspd_readout_len)
        signal2 = -u.demod2volts(signal2, apd_readout_len)
        # Plot the data
        plt.cla()
        plt.plot(signal1, "b-")
        plt.plot(signal2, "r-")
        plt.title("Error signal [a.u.]")
        plt.xlabel("Time [μs]")
        plt.ylabel("Amplitude Error [arb. units]")
        plt.ylim((-0.5, 0.5))
        plt.pause(0.1)
        # plt.show()
