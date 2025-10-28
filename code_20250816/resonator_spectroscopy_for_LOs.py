# %%
"""
        RESONATOR SPECTROSCOPY INDIVIDUAL RESONATORS
This sequence involves measuring the resonator by sending a readout pulse and demodulating the signals to extract the
'I' and 'Q' quadratures across varying readout intermediate frequencies.
The data is then post-processed to determine the resonator resonance frequency.
This frequency can be used to update the readout intermediate frequency in the configuration under "resonator_IF".

Prerequisites:
    - Ensure calibration of the time of flight, offsets, and gains (referenced as "time_of_flight").
    - Calibrate the IQ mixer connected to the readout line (whether it's an external mixer or an Octave port).
    - Define the readout pulse amplitude and duration in the configuration.
    - Specify the expected resonator depletion time in the configuration.

Before proceeding to the next node:
    - Update the readout frequency, labeled as "resonator_IF_q1" and "resonator_IF_q2", in the configuration.
"""

from copy import deepcopy
from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_mw_fem import *
from qualang_tools.results import fetching_tool
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.results.data_handler import DataHandler
import matplotlib

# matplotlib.use('TkAgg')

##################
#   Parameters   #
##################

rl = "rl1"
rr = "q1_rr"
rr_LOs = [lo * u.GHz for lo in range(2, 11, 1)]
amplitude = 1.0
full_scale_power_dbm = -11

n_avg = 100  # The number of averages
frequencies = np.arange(-400e6, +400e6, 100e3)

print("Number of frequencies is", len(frequencies))
# assert len(frequencies) <= 534, "check your frequencies"

save_data_dict = {
    "resonator": rr,
    "resonator_LO": rr_LOs,
    "frequencies": frequencies,
    "n_avg": n_avg,
    "config": config,
}


###################
#   QUA Program   #
###################


with program() as PROGRAM:
    n = declare(int)  # QUA variable for the averaging loop
    f = declare(int)  # QUA variable for the readout frequency --> Hz int 32 up to 2^32
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature --> signed 4.28 [-8, 8)
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature --> signed 4.28 [-8, 8)
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_(*from_array(f, frequencies)):  # QUA for_ loop for sweeping the frequency
            # Update the frequency of the digital oscillator linked to the resonator element
            update_frequency(rr, f + RR_CONSTANTS[rr]["IF"])
            # Measure the resonator (send a readout pulse and demodulate the signals to get the 'I' & 'Q' quadratures)
            measure(
                "readout" * amp(1),
                rr,
                None,
                dual_demod.full("cos", "sin", I),
                dual_demod.full("minus_sin", "cos", Q),
            )
            # Wait for the resonator to deplete
            wait(1 * u.us, rr)
            # Save the 'I' & 'Q' quadratures to their respective streams
            save(I, I_st)
            save(Q, Q_st)

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_st.buffer(len(frequencies)).average().save("I")
        Q_st.buffer(len(frequencies)).average().save("Q")


if __name__ == "__main__":

    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)
    qmm.close_all_qms()

    #######################
    # Simulate or execute #
    #######################

    rr_ao_port = RL_CONSTANTS["rl1"]["ao"]
    rr_ai_port = RL_CONSTANTS["rl1"]["ai"]

    for rr_LO in rr_LOs:
        this_config = deepcopy(config)
        # fem
        config_fem = this_config["controllers"]["con1"]["fems"][mwfem_slot]
        this_config["waveforms"][f"readout_wf_{rr}"]["sample"] = amplitude
        # output
        config_rr_ao_port = config_fem["analog_outputs"][rr_ao_port]
        config_rr_ao_port["upconverters"][1]["frequency"] = rr_LO
        config_rr_ao_port["band"] = get_band(rr_LO)
        config_rr_ao_port["full_scale_power_dbm"] = full_scale_power_dbm
        # input
        config_rr_ai_port = config_fem["analog_inputs"][rr_ai_port]
        config_rr_ai_port["downconverter_frequency"] = rr_LO
        config_rr_ai_port["band"] = get_band(rr_LO)

        # Open a quantum machine to execute the QUA program
        qm = qmm.open_qm(this_config)
        # Send the QUA program to the OPX, which compiles and executes it
        job = qm.execute(PROGRAM)
        # Get results from QUA program
        results = fetching_tool(job, data_list=["I", "Q"]) # this one already waits for all values

        # plotting
        fig = plt.figure()
        I, Q = results.fetch_all()
        # Convert results into Volts
        S = I + 1j * Q
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        cable_length = " 2M" if mwfem_slot == 2 else ""
        plt.suptitle(f"""
            LO = {rr_LO / u.GHz} GHz - MWSlot{mwfem_slot} Loopback{cable_length} AO{rr_ao_port}->AI{rr_ai_port}\n
            full_scale_power_dbm={full_scale_power_dbm}, amplitude={amplitude}
        """)
        ax1 = plt.subplot(211)
        plt.plot((frequencies + RR_CONSTANTS[rr]["IF"])/ u.MHz, R, ".")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(212, sharex=ax1)
        plt.plot((frequencies + RR_CONSTANTS[rr]["IF"])/ u.MHz, signal.detrend(np.unwrap(phase)), ".")
        plt.xlabel("Intermediate frequency [MHz]")
        plt.ylabel("Phase [rad]")
        plt.tight_layout()
        plt.show(block=False)
        qm.close()

        save_data_dict[f"{rr}_I_LO={rr_LO/u.GHz:1.3f}GHz".replace(".", "-")] = I
        save_data_dict[f"{rr}_Q_LO={rr_LO/u.GHz:1.3f}GHz".replace(".", "-")] = Q
        save_data_dict[f"fig_live_LO={rr_LO/u.GHz:1.3f}GHz".replace(".", "-")] = deepcopy(fig)

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="resonator_spectroscopy_for_LOs")


# %%