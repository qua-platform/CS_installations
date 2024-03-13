# %%
"""
        CHARGE STABILITY MAP - fast and slow axes: external source (DC)
The goal of the script is to acquire the charge stability map.
Here the charge stability diagram is acquired by sweeping the voltages using an external DC source (QDAC or else).
This is done by pausing the QUA program, updating the voltages in Python using the instrument API and resuming the QUA program.

The OPX is simply measuring, either via dc current sensing or RF reflectometry, the charge occupation of the dot.
On top of the DC voltage sweeps, the OPX can output a continuous square wave (Coulomb pulse) through the AC line of the
bias-tee. This allows to check the coupling of the fast line to the sample and measure the lever arms between the DC and
AC lines.

A single-point averaging is performed and the data is extracted while the program is running to display the results line-by-line.

Prerequisites:
    - Readout calibration (resonance frequency for RF reflectometry and sensor operating point for DC current sensing).
    - Setting the parameters of the external DC source using its driver.
    - Connect the two plunger gates (DC line of the bias-tee) to the external dc source.
    - (optional) Connect the OPX to the fast line of the plunger gates for playing the Coulomb pulse and calibrate the
      lever arm.

Before proceeding to the next node:
    - Identify the different charge occupation regions.
    - Update the config with the lever-arms.
"""
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool, wait_until_job_is_paused
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
import warnings
import matplotlib
import matplotlib.pyplot as plt
from macros import RF_reflectometry_macro, DC_current_sensing_macro

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


###################
# The QUA program #
###################
n_avg = 10
n_points_slow = 5
n_points_fast = 6

voltages_slow = np.linspace(-1.0, 1.0, n_points_slow)
voltages_fast = np.linspace(-0.5, 0.5, n_points_fast)
num_voltage_points = n_points_slow * n_points_fast

with program() as charge_stability_prog:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_ij = declare(int)  # QUA integer used as an index for the averaging loop
    i = declare(int)  # QUA integer used as an index to loop over the voltages
    j = declare(int)  # QUA integer used as an index to loop over the voltages
    counter = declare(int)  # QUA integer used as an index for the Coulomb pulse
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)

    assign_variables_to_element("tank_circuit", I, Q)
    
    with for_(i, 0, i < n_points_slow + 1, i + 1):
        with for_(j, 0, j < n_points_fast, j + 1):
            # pause to change the DC voltage outside QUA
            pause()

            # wait to stabilize the voltages           
            wait(1 * u.ms)
            
            # TODO: consider to include Coulomb pulses?
            # # Play the Coulomb pulse continuously for the whole sequence
            # #      ____      ____      ____      ____
            # #     |    |    |    |    |    |    |    |
            # # ____|    |____|    |____|    |____|    |...
            # with for_(counter, 0, counter < N, counter + 1):
            #     # The Coulomb pulse
            #     play("step" * amp(Coulomb_amp / P1_step_amp), "P1")
            #     play("step" * amp(-Coulomb_amp / P1_step_amp), "P1")
            
            with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
                # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
                # frequency and the integrated quadratures are stored in "I" and "Q"
                I, Q, I_st, Q_st = RF_reflectometry_macro(I=I, Q=Q)
                # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
                # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
                # process them which can cause the OPX to crash.
                wait(1_000 * u.ns)  # in ns
        
            assign(n_ij, i * n_points_fast + j)
            save(n_ij, n_st)
    
    with stream_processing():
        n_st.save("iteration")
        # Perform a single point averaging and cast the data into a 1D array. "save_all" is used here to store all
        # received 1D arrays, and eventually form a 2D array, which enables line-by-line live plotting
        # RF reflectometry
        # I_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(n_points_fast).buffer(n_points_slow).save("I")
        # Q_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(n_points_fast).buffer(n_points_slow).save("Q")
        I_st.buffer(n_avg).map(FUNCTIONS.average()).save_all("I")
        Q_st.buffer(n_avg).map(FUNCTIONS.average()).save_all("Q")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # simulates the QUA program for a specified duration
    simulation_config = SimulationConfig(duration=10_000)
    job = qmm.simulate(config, charge_stability_prog, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(charge_stability_prog)
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    for i in range(n_points_slow):  # Loop over y-voltages
        for j in range(n_points_fast):
            # Set voltage
            # TODO: implement changing voltages using the DC source's API
            print(f"voltage_slow: {i:3d}, voltage_fast: {j:3d}\n")
            job.resume()
            wait_until_job_is_paused(job)
            if i == 0 and j == 0:
                results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")

            # Fetch the data from the last OPX run corresponding to the current slow axis iteration
            I, Q, iteration = results.fetch_all()
            # Convert results into Volts
            S = u.demod2volts(I + 1j * Q, reflectometry_len)
            S = np.linspace(0, 1, len(S))
            
            num_zeros = num_voltage_points - iteration - 1
            R = np.abs(S)
            R = np.pad(R, (0, num_zeros), mode='constant').reshape(n_points_slow, n_points_fast)
            
            phase = np.angle(S)
            phase = np.pad(phase, (0, num_zeros), mode='constant').reshape(n_points_slow, n_points_fast)
            
            # Progress bar
            progress_counter(iteration, n_points_slow * n_points_fast, start_time=results.start_time)
            # Plot data
            plt.subplot(121)
            plt.cla()
            plt.title(r"$R=\sqrt{I^2 + Q^2}$ [V]")
            plt.pcolor(voltages_fast, voltages_slow, R)
            plt.xlabel("Fast voltage axis [V]")
            plt.ylabel("Slow voltage axis [V]")
            plt.subplot(122)
            plt.cla()
            plt.title("Phase [rad]")
            plt.pcolor(voltages_fast, voltages_slow, phase)
            plt.xlabel("Fast voltage axis [V]")
            plt.ylabel("Slow voltage axis [V]")
            plt.tight_layout()
            plt.pause(0.1)
            
            


# %%
