"""
Example Script for Real-Time Parameter Updates in QUA Programs

This script demonstrates how to perform live updates of parameters in a running QUA (Quantum Universal Assembler) program. It serves as an example for dynamically changing a program parameter, such as amplitude, during execution. This functionality is useful for applications requiring adaptive control or iterative optimization within an experiment.

Requirements
- Played elements must already exist in the QUA program (e.g., oscillators, pulses, or any other QUA-defined elements)

To-Do
- Define the specific parameters to be updated in the actual use case. The script currently updates amplitude, but it can be easily modified to update other parameters, such as:
    - Frequency (`update_frequency`)
    - Phase (`reset_frame / frame_rotation`)
    - Duration, etc.

"""

from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.video_mode.videomode import VideoMode

###################
# The QUA program #
###################

def qua_prog(vm: VideoMode):
    with program() as video:
        dc = declare(fixed)
        dc_st = declare_stream()
        amp_aom_r, amp_aom_c = vm.declare_variables()
        with infinite_loop_():
            vm.load_parameters()
            align()
            play("readout" * amp(amp_aom_r), "readout_aom")
            play("control" * amp(amp_aom_c), "control_aom")
            measure("readout", "SNSPD", None, integration.full("constant", dc, "out1"))
            save(dc, dc_st)

        with stream_processing():
            dc_st.buffer(1000).save("signal")
    return video

if __name__ == "__main__":
    # Open the Quantum Machine Manager
    qmm = QuantumMachinesManager(opx_ip, cluster_name=cluster_name, octave=octave_config)
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
    results = fetching_tool(job, ["signal"], mode="live")
    # Live plotting
    fig = plt.figure()
    while results.is_processing():
        # Fetch data from the OPX
        signal = results.fetch_all()
        # Convert the data into Volt
        signal = -u.demod2volts(signal, snspd_readout_len)
        # Plot the data
        plt.cla()
        plt.plot(signal1, "b-")
        plt.title("Error signal [a.u.]")
        plt.xlabel("Time [μs]")
        plt.ylabel("Amplitude Error [arb. units]")
        plt.ylim((-0.5, 0.5))
        plt.pause(0.1)
        # plt.show()