# %%
"""
        PDH PID with fixed frequency
PID loop with Pound Drever Hall technique to lock to a resonator frequency.
During the PID calculation, erors are treated as float, which has to be within [-8, 8).

Prerequisites:
    - Calibration of the time of flight, offsets, and gains (referenced as "time_of_flight").
    - Calibration of the IQ mixer connected to the readout line (be it an external mixer or an Octave port).
    - Identification of the resonator's resonance frequency (referred to as "resonator_spectroscopy_multiplexed").
    - Configuration of the readout pulse amplitude (the pulse processor will sweep up to twice this value) and duration.
    - Specification of the expected resonator depletion time in the configuration.
    - Calibration of phase shift for resonator
"""

from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.results import fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.results.data_handler import DataHandler
from configuration_with_octave import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import warnings

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


###################
# The QUA program #
###################

n_pid_loop = 1_000 # how many shots to run the PID loop
gain_P = 0.1
gain_I = 0.1
gain_D = 0.1
alpha = 0.1
bitshift_scale_factor = 9  ## scale_factor = 2**bitshift_scale_factor
f_init = 50 * u.MHz


def update_pdh_freqs(f, fm):
    update_frequency("rr", f)
    update_frequency("rr_sb_high", f + fm)
    update_frequency("rr_sb_low", f - fm)
    update_frequency("pdh_demod", f + fm)

def reset_pdh_phases():
    reset_phase("rr")
    reset_phase("rr_sb_high")
    reset_phase("rr_sb_low")
    reset_phase("pdh_demod")

def play_pdh_pulse():
    play("pdh_carrier", "rr")
    play("pdh_modulation", "rr_sb_high")
    play("pdh_modulation", "rr_sb_low")

with program() as PDH_PID:
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    R = declare(fixed)  # I ** 2 + Q ** 2
    error_P = declare(fixed)
    error_P_prev = declare(fixed, value=0.0)
    error_I = declare(fixed, value=0.0)
    error_D = declare(fixed)
    f = declare(int, value=f_init)  # initial resonator frequency
    fm = declare(int, value=pdh_mod_IF)
    n = declare(int)

    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    R_st = declare_stream()
    error_P_st = declare_stream()
    error_I_st = declare_stream()
    error_D_st = declare_stream()
    f_st = declare_stream()
    n_st = declare_stream()

    assign_variables_to_element("pdh_demod", I, Q, R)

    with for_(n, 0, n < n_pid_loop, n + 1):
        # update freq for the carrier and modulation
        update_pdh_freqs(f, fm)
        # reset frames for the carrier and modulation
        reset_pdh_phases()
        # shift the phase for resonator
        frame_rotation_2pi(resonator_phase, "rr")

        align()
        # play PDH pulse
        play_pdh_pulse()
        # measure at modulation freq
        measure(
            "readout",
            "pdh_demod",
            None,
            dual_demod.full("cos", "out1", "sin", "out2", I),
            dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
        )

        # PID calculation
        assign(R, I * I + Q * Q)
        # proportional
        assign(error_P, -R << bitshift_scale_factor)  # target = 0 is assumed (target - R)
        # integral
        assign(error_I, (1 - alpha) * error_I + alpha * error_P)
        # derivative
        assign(error_D, error_P_prev - error_P)
        # update frequency
        assign(f, f + Cast.to_int(gain_P * error_P + gain_I * error_I + gain_D * error_D))
        # update previous error
        assign(error_P_prev, error_P)

        save(I, I_st)
        save(Q, Q_st)
        save(R, R_st)
        save(error_P, error_P_st)
        save(error_I, error_I_st)
        save(error_D, error_D_st)
        save(f, f_st)
        save(n, n_st)
        wait(1 * u.us)

    # stream processing handling
    with stream_processing():
        I_st.save_all("I")
        Q_st.save_all("Q")
        R_st.save_all("R")
        error_P_st.save_all("error_P")
        error_I_st.save_all("error_I")
        error_D_st.save_all("error_D")
        f_st.save_all("freqs")
        n_st.save("iterations")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=None, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=5_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, PDH_PID, simulation_config)
    job.get_simulated_samples().con1.plot(analog_ports=['1', '2', '3', '4'])
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PDH_PID)
    # Get results from QUA program
    results = fetching_tool(
        job,
        data_list=[
            "I", "Q", "R",
            "error_P", "error_I", "error_D",
            "freqs", "iterations"
        ],
        mode="live",
    )
    # Live plotting
    fig = plt.figure(figsize=(12, 8))
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, R, error_P, error_I, error_D, freqs, iterations = results.fetch_all()
        shots = np.arange(iterations + 1)
        if np.any(np.power(2, bitshift_scale_factor) * R >= 8):
            print("reduce bitshift_scale_factor so that error_P stays within [-8, 8)")
        
        # Plot
        plt.suptitle("PDH Locking")

        plt.subplot(221)
        plt.cla()
        plt.plot(shots, resonator_LO + freqs)
        plt.title("Tracked Frequency", fontsize=12)
        plt.xlabel("iteration", fontsize=12)
        plt.ylabel("Frequency [Hz]", fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)

        plt.subplot(223)
        plt.cla()
        plt.plot(shots, error_P)
        plt.plot(shots, error_I)
        plt.plot(shots, error_D)
        plt.title("errors", fontsize=12)
        plt.xlabel("iteration", fontsize=12)
        plt.ylabel("Errors", fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(["proportional", "integral", "derivative"])

        plt.subplot(222)
        plt.cla()
        plt.plot(shots, I)
        plt.plot(shots, Q)
        plt.title("I, Q", fontsize=12)
        plt.xlabel("iteration", fontsize=12)
        plt.ylabel("PDH signal", fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.legend(["I", "Q"])

        plt.subplot(224)
        plt.cla()
        plt.plot(shots, R)
        plt.title("R = I**2 + Q**2", fontsize=12)
        plt.xlabel("iteration", fontsize=12)
        plt.ylabel("PDH signal power", fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)

        plt.tight_layout()
        plt.pause(0.1)
    
    plt.show()

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "I": I,
            "Q": Q,
            "R": R,
            "error_P": error_P,
            "error_I": error_I,
            "error_D": error_D,
            "freqs": freqs,
        }
        # Initialize the DataHandler
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {
            Path(__file__).name: Path(__file__).name,
            "configuration.py": "configuration.py",
        }
        # Save results
        data_folder = data_handler.save_data(data=data)

# %%
