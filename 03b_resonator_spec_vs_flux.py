from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
import os
from scipy.optimize import curve_fit
from qualang_tools.results.data_handler import DataHandler
from qm_saas import QmSaas, QOPVersion

##################
#   Parameters   #
##################
# Parameters Definition
n_avg = 1000  # The number of averages
# The frequency sweep around the resonator frequency "resonator_IF"
span = 10 * u.MHz
df = 100 * u.kHz
dfs = np.arange(-span, +span + 0.1, df)
# Flux bias sweep in V
flux_min = -0.49
flux_max = 0.49
step = 0.01
flux_array = np.arange(flux_min, flux_max+step/2, step)

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "dfs": dfs,
    "flux": flux_array,
    "config": config,
}

# Choice of element for resonator spectroscopy (rr1, rr2, rr3)
RR_ELEM = "rr1"

###################
# The QUA program #
###################
with program() as resonator_spec_flux_2D:
    n = declare(int)  # QUA variable for the averaging loop
    df = declare(int)  # QUA variable for the readout frequency
    dc = declare(fixed)  # QUA variable for the readout amplitude pre-factor
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_(*from_array(df, dfs)):  # QUA for_ loop for sweeping the frequency
            # Update the frequency of the digital oscillator linked to the resonator element
            update_frequency(RR_ELEM, df + IF_RR1)
            with for_each_(dc, flux_array):
                set_dc_offset("flux_tls1", "single", dc)
                wait(FLUX_SETTLE_TIME * u.ns, RR_ELEM, "tls1")
                measure(
                    "readout",
                    RR_ELEM,
                    dual_demod.full("cos", "sin", I),
                    dual_demod.full("minus_sin", "cos", Q),
                )
                # Wait for the resonator to deplete
                wait(DEPLETION_TIME * u.ns, RR_ELEM)
                # Save the 'I' & 'Q' quadratures to their respective streams
                save(I, I_st)
                save(Q, Q_st)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        # Cast the data into a 2D matrix, average the 2D matrices together and store the results on the OPX processor
        # Note that the buffering goes from the most inner loop (left) to the most outer one (right)
        I_st.buffer(len(flux_array)).buffer(len(dfs)).average().save("I")
        Q_st.buffer(len(flux_array)).buffer(len(dfs)).average().save("Q")
        n_st.save("iteration")

#######################
# Simulate or execute #
#######################
simulate = True

if simulate:
    # --- SaaS login ---
    client = QmSaas(
    host="qm-saas.dev.quantum-machines.co",
    email="benjamin.safvati@quantum-machines.co",
    password="ubq@yvm3RXP1bwb5abv"
    )

    with client.simulator(QOPVersion(os.environ.get("QM_QOP_VERSION", "v2_4_4"))) as inst:
        inst.spawn()
        qmm = QuantumMachinesManager(
            host=inst.host,
            port=inst.port,
            connection_headers=inst.default_connection_headers,
        )    # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
        # Simulate blocks python until the simulation is done
        job = qmm.simulate(config, resonator_spec_flux_2D, simulation_config)
        # Get the simulated samples
        samples = job.get_simulated_samples()
        # Plot the simulated samples
        samples.con1.plot()
        # Get the waveform report object
        waveform_report = job.get_simulated_waveform_report()
        # Cast the waveform report to a python dictionary
        waveform_dict = waveform_report.to_dict()
        # Visualize and save the waveform report
        waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))

else:
    qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(resonator_spec_flux_2D)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  #  Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Convert results into Volts and normalize
        S = u.demod2volts(I + 1j * Q, READOUT_LEN)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Normalize data
        row_sums = R.sum(axis=0)
        R /= row_sums[np.newaxis, :]
        # 2D spectroscopy plot
        plt.subplot(211)
        plt.suptitle(f"Resonator spectroscopy - LO = {LO_RR / u.GHz} GHz & IF = {IF_RR1 / u.MHz} MHz")
        plt.cla()
        plt.title("Phase")
        plt.pcolor(flux_array, (dfs + IF_RR1) / u.MHz, signal.detrend(np.unwrap(phase)))
        plt.xlabel("Flux bias [V]")
        plt.ylabel("Readout IF [MHz]")
        plt.pause(0.1)
        plt.tight_layout()

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

    # Fitting to cosine resonator frequency response
    def cosine_func(x, amplitude, frequency, phi, offset):
        return amplitude * np.cos(2 * np.pi * frequency * x + phi) + offset

    # Find the resonator frequency vs flux minima
    minima = np.zeros(len(flux_array))
    for i in range(len(flux_array)):
        minima[i] = dfs[np.argmin(R.T[i])] + IF_RR1
    # Cosine fit
    initial_guess = [1, 1 / 0.4, 0, 0]  # Initial guess for the parameters
    fit_params, _ = curve_fit(cosine_func, flux_array, minima, p0=initial_guess)
    # Get the fitted values
    amplitude_fit, frequency_fit, phase_fit, offset_fit = fit_params
    print("fitting parameters", fit_params)
    # Generate the fitted curve using the fitted parameters
    fitted_curve = cosine_func(flux_array, amplitude_fit, frequency_fit, phase_fit, offset_fit)

    plt.figure()
    plt.suptitle(f"Resonator spectroscopy - LO = {LO_RR / u.GHz} GHz")
    plt.pcolor(flux_array, (dfs + IF_RR1) / u.MHz, R)
    plt.plot(flux_array, minima / u.MHz, "x-", color="red", label="Flux minima")
    plt.plot(flux_array, fitted_curve / u.MHz, label="Fitted Cosine", color="orange")
    plt.xlabel("Flux bias [V]")
    plt.ylabel("Readout IF [MHz]")
    plt.legend()

    print("DC flux value corresponding to the maximum frequency point", flux_array[np.argmax(fitted_curve)])
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"I_data": I})
    save_data_dict.update({"Q_data": Q})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])