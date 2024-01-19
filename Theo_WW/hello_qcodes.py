import os
import qcodes as qc
from qcodes import initialise_or_create_database_at, load_or_create_experiment
from qcodes.utils.dataset.doNd import do2d, do1d, do0d
from qcodes import Parameter
from qm.qua import *
from qualang_tools.external_frameworks.qcodes.opx_driver import OPX
from configuration import *


#####################################
#           Qcodes set-up           #
#####################################
db_name = "QM_demo.db"  # Database name
sample_name = "demo"  # Sample name
exp_name = "OPX_qcodes_drivers"  # Experiment name

# Initialize qcodes database
db_file_path = os.path.join(os.getcwd(), db_name)
qc.config.core.db_location = db_file_path
initialise_or_create_database_at(db_file_path)
# Initialize qcodes experiment
experiment = load_or_create_experiment(
    experiment_name=exp_name, sample_name=sample_name
)
# Initialize the qcodes station to which instruments will be added
station = qc.Station()
# Create the OPX instrument class
opx_instrument = OPX(config, name="OPX_demo", host=qop_ip, cluster_name=cluster_name, octave=octave_config)
# Add the OPX instrument to the qcodes station
station.add_component(opx_instrument)


# Create fake parameters for do1d and do2d scan demonstration, can be replaced by external instrument parameters
class MyCounter(Parameter):
    def __init__(self, name, label):
        # only name is required
        super().__init__(
            name=name,
            label=label,
            unit="V",
            docstring="Dummy counter for scanning a variable with qcodes",
        )
        self._count = 0

    # you must provide a get method, a set method, or both.
    def get_raw(self):
        self._count += 1
        return self._count

    def set_raw(self, val):
        self._count = val
        return self._count


VP1 = MyCounter("counter1", "Vp1")
VP2 = MyCounter("counter2", "Vp2")

#####################################
run = "datasaver"
# Pass the readout length (in ns) to the class to convert the demodulated/integrated data into Volts
# and create the setpoint Parameter for raw adc trace acquisition
opx_instrument.readout_pulse_length(readout_len)

#####################################
#     1D OPX SWEEP & datasaver      #
#####################################
# Show how to perform a 1D sweep with averaging on the OPX
# while scanning an external parameter using the qcodes Measurement framework instead of do1d.
from qualang_tools.loops import from_array
from qcodes.dataset import plot_dataset

frequencies = np.arange(65e6, 75e6, 10e3)
n_avg = 1000


# QUA sequence
def OPX_reflectometry(simulate=False):
    with program() as prog:
        f = declare(int)
        n = declare(int)
        I = declare(fixed)
        Q = declare(fixed)
        Q_st = declare_stream()
        I_st = declare_stream()
        with infinite_loop_():
            if not simulate:
                pause()
            with for_(n, 0, n < n_avg, n + 1):
                with for_(*from_array(f, frequencies)):
                    update_frequency("FTR", f)
                    measure(
                        "readout",
                        "FTR",
                        None,
                        dual_demod.full("cos", "out1", "sin", "out2", I),
                        dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
                    )
                    wait(depletion_time * u.ns, "FTR")
                    save(I, I_st)
                    save(Q, Q_st)

        with stream_processing():
            I_st.buffer(len(frequencies)).buffer(n_avg).map(FUNCTIONS.average()).save_all("I")
            Q_st.buffer(len(frequencies)).buffer(n_avg).map(FUNCTIONS.average()).save_all("Q")
    return prog


if run == "datasaver":
    # Axis1 is the most inner loop
    opx_instrument.set_sweep_parameters("axis1", frequencies, "Hz", "Readout frequency")
    # Add the custom sequence to the OPX
    opx_instrument.qua_program = OPX_reflectometry(simulate=True)
    # Simulate program
    opx_instrument.sim_time(10_000)
    opx_instrument.simulate()
    opx_instrument.plot_simulated_wf()
    # Execute program
    opx_instrument.qua_program = OPX_reflectometry(simulate=False)
    # Initialize the measurement
    meas = qc.Measurement(exp=experiment, name="reflectometry")
    # Register the qcodes parameter that we'll sweep
    meas.register_parameter(VP1)
    # Get the Result parameters from the OPX scan
    OPX_param = opx_instrument.get_measurement_parameter()
    # Register all the involved parameters
    meas.register_parameter(OPX_param, setpoints=[VP1])
    # Start the sequence (Send the QUA program to the OPX which compiles and executes it)
    opx_instrument.run_exp()
    # Start the qcodes measurement
    with meas.run() as datasaver:
        # Loop over an external parameter
        for gate_v in np.arange(0, 0.01, 0.001):
            # Update ethe external parameter
            VP1(gate_v)
            # Run the QUA sequence
            opx_instrument.resume()
            # Get the results from the OPX
            data = opx_instrument.get_res()
            # Store the results in the qcodes database
            datasaver.add_result(
                (VP1, VP1()), (OPX_param, np.array(list(data.values())))
            )
        # Halt the OPX program at the end
        opx_instrument.halt()
        # Get the full dataset
        dataset = datasaver.dataset
    # Plot the dataset
    plot_dataset(dataset)
