# %%
"""
        RESONATOR SPECTROSCOPY VERSUS FLUX
This sequence involves measuring the resonator by sending a readout pulse and demodulating the signals to
extract the 'I' and 'Q' quadratures. This is done across various readout intermediate frequencies and flux biases.
The resonator frequency as a function of flux bias is then extracted and fitted so that the parameters can be stored in the configuration.

This information can then be used to adjust the readout frequency for the maximum frequency point.

Prerequisites:
    - Calibration of the time of flight, offsets, and gains (referenced as "time_of_flight").
    - Calibration of the IQ mixer connected to the readout line (be it an external mixer or an Octave port).
    - Identification of the resonator's resonance frequency (referred to as "resonator_spectroscopy_multiplexed").
    - Configuration of the readout pulse amplitude and duration.
    - Specification of the expected resonator depletion time in the configuration.

Before proceeding to the next node:
    - Update the readout frequency, labeled as "resonator_IF", in the configuration.
    - Adjust the flux bias to the maximum frequency point, labeled as "max_frequency_point", in the configuration.
    - Update the resonator frequency versus flux fit parameters (amplitude_fit, frequency_fit, phase_fit, offset_fit) in the configuration
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from macros import qua_declaration, multiplexed_readout
from qualang_tools.callable_from_qua import *
import matplotlib.pyplot as plt
from scipy import signal
from scipy.optimize import curve_fit


###################
# The QUA program #
###################
n_avg = 100
# The frequency sweep around the resonators' frequency "resonator_IF_q"
span = 10 * u.MHz
df = 100 * u.kHz
dfs = np.arange(-span, +span + 0.1, df)
# Flux bias sweep in V
flux_min = -2.0e-3
flux_max = 2.0e-3
step = 0.5e-3
flux = np.arange(flux_min, flux_max + step / 2, step)

resonators = ["rr1", "rr2", "rr3", "rr4", "rr5"]
resonators_IF = [resonator_IF_q1, resonator_IF_q2, resonator_IF_q3, resonator_IF_q4, resonator_IF_q5]


###################
#     Callable    #
###################
import sys
sys.path.append(r'C:\Program Files\Keysight\Labber\Script)')
sys.path.append(r'C:\Users\SQC\Desktop\QM\CS_installations-HI_15Aug2024\labber_toolv2.py')
from labber_toolv2 import InstrManager
# import pprint
import Labber
a = InstrManager(server_ip='192.168.10.252')
# client = Labber.connectToServer('192.168.10.252')

a.add_instrument(sHardware='Yokogawa GS200 DC Source',
                    dComCfg={'name':'globalFlux',
                            'address': '0x0B21::0x0039::90ZB35282',
                            'interface': 'USB'})
state=[True, False]
yoko_cfg = {'Output': state[0],
        'Function': 'Current',
        'Range (I)': '10 mA',
        'Current - Sweep rate':10e-6}
a.ctrl.globalFlux.setInstrConfig(yoko_cfg)
sweep_rate = 10e-6
print(a.config)

# Patch to add the callable from qua functions to the main SDK
patch_qua_program_addons()

# Define your callable_from_qua functions
# Note that this framework can be easily adapted to update parameters from other instruments using their dedicated API
@callable_from_qua
def set_yoko_offset(actrl, value=0, sweep_rate=10e-6):
    actrl.globalFlux.setValue('Current', value, rate=sweep_rate)
    print(f"setting the yoko to {value} A ")


with program() as multi_res_spec_vs_flux:
    # QUA macro to declare the measurement variables and their corresponding streams for a given number of resonators
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=5)
    df = declare(int)  # QUA variable for sweeping the readout frequency detuning around the resonance
    dc = declare(fixed)  # QUA variable for sweeping the flux bias

    with for_(*from_array(dc, flux)):
        set_yoko_offset(a.ctrl, value=dc, sweep_rate=sweep_rate)
        with for_(*from_array(df, dfs)):
            for rr, resonator_IF in zip(resonators, resonators_IF):
                update_frequency(rr, df + resonator_IF)  # Update the frequency the rr element

            with for_(n, 0, n < n_avg, n + 1):
                # Flux sweeping
                wait(flux_settle_time * u.ns)  # Wait for the flux to settle
                # Macro to perform multiplexed readout on the specified resonators
                # It also save the 'I' and 'Q' quadratures into their respective streams
                multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2, 3, 4, 5], sequential=False)
                # wait for the resonators to relax
                wait(depletion_time * u.ns, *resonators)
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        for i, rr in enumerate(resonators):
            I_st[i].buffer(n_avg).map(FUNCTIONS.average()).buffer(len(dfs)).buffer(len(flux)).save(f"I{i+1}")
            Q_st[i].buffer(n_avg).map(FUNCTIONS.average()).buffer(len(dfs)).buffer(len(flux)).save(f"Q{i+1}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, multi_res_spec_vs_flux, simulation_config)
    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(multi_res_spec_vs_flux)
    # Prepare the figure for live plotting
    fig, axss = plt.subplots(2, 5, figsize=(20, 7))
    interrupt_on_close(fig, job)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["I1", "Q1", "I2", "Q2", "I3", "Q3", "I4", "Q4", "I5", "Q5", "iteration"])
    # Live plotting
    # while results.is_processing():
    # Fetch results
    I1, Q1, I2, Q2, I3, Q3, I4, Q4, I5, Q5, iteration = results.fetch_all()
    # Progress bar
    # progress_counter(iteration, n_avg, start_time=results.get_start_time())
    # Data analysis
    S1 = u.demod2volts(I1.T + 1j * Q1.T, readout_len)
    S2 = u.demod2volts(I2.T + 1j * Q2.T, readout_len)
    S3 = u.demod2volts(I3.T + 1j * Q3.T, readout_len)
    S4 = u.demod2volts(I4.T + 1j * Q4.T, readout_len)
    S5 = u.demod2volts(I5.T + 1j * Q5.T, readout_len)
    R1 = np.abs(S1)
    phase1 = np.angle(S1)
    R2 = np.abs(S2)
    phase2 = np.angle(S2)
    R3 = np.abs(S3)
    phase3 = np.angle(S3)
    R4 = np.abs(S4)
    phase4 = np.angle(S4)
    R5 = np.abs(S5)
    phase5 = np.angle(S5)
    # Plots
    plt.suptitle("Resonator spectroscopy")

    axss[0, 0].pcolor(flux, (resonator_IF_q1 + dfs) / u.MHz, R1)
    plt.title(f"Resonator 1 - LO: {resonator_LO / u.GHz} GHz")
    plt.ylabel("Readout IF [MHz]")
    axss[0, 1].pcolor(flux, (resonator_IF_q2 + dfs) / u.MHz, R2)
    plt.title(f"Resonator 2 - LO: {resonator_LO / u.GHz} GHz")
    axss[0, 2].pcolor(flux, (resonator_IF_q3 + dfs) / u.MHz, R3)
    plt.title(f"Resonator 3 - LO: {resonator_LO / u.GHz} GHz")
    axss[0, 3].pcolor(flux, (resonator_IF_q4 + dfs) / u.MHz, R4)
    plt.title(f"Resonator 4 - LO: {resonator_LO / u.GHz} GHz")
    axss[0, 4].pcolor(flux, (resonator_IF_q5 + dfs) / u.MHz, R5)
    plt.title(f"Resonator 5 - LO: {resonator_LO / u.GHz} GHz")
    axss[1, 0].pcolor(flux, (resonator_IF_q1 + dfs) / u.MHz, signal.detrend(np.unwrap(phase1)))
    plt.xlabel("Flux bias [V]")
    plt.ylabel("Readout IF [MHz]")
    axss[1, 1].pcolor(flux, (resonator_IF_q2 + dfs) / u.MHz, signal.detrend(np.unwrap(phase2)))
    plt.xlabel("Flux bias [V]")
    axss[1, 2].pcolor(flux, (resonator_IF_q3 + dfs) / u.MHz, signal.detrend(np.unwrap(phase3)))
    plt.xlabel("Flux bias [V]")
    plt.ylabel("Phase [rad]")
    axss[1, 3].pcolor(flux, (resonator_IF_q4 + dfs) / u.MHz, signal.detrend(np.unwrap(phase4)))
    plt.xlabel("Flux bias [V]")
    axss[1, 4].pcolor(flux, (resonator_IF_q5 + dfs) / u.MHz, signal.detrend(np.unwrap(phase5)))
    plt.xlabel("Flux bias [V]")
    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

    # Save results
    save_data_dict = {"fig_live": fig}
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name=Path(__file__).stem)


# %%
