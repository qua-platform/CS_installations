# %%

import numpy as np
import matplotlib.pyplot as plt

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_mwfem_lffem import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
from qdac2_driver import QDACII, load_voltage_list
from macros import RF_reflectometry_macro, DC_current_sensing_macro
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.voltage_gates import VoltageGateSequence

##################
#   Parameters   #
##################

# Points in the charge stability map [V1, V2]
level_empty = [-0.2, 0.0]
duration_empty = 5000
mult_duration = 1

seq = VoltageGateSequence(config, ["P1_sticky", "P2_sticky"])
seq.add_points("empty", level_empty, duration_empty*mult_duration)
seq.add_points("initialization", level_init, duration_init*mult_duration)
seq.add_points("readout", level_readout, duration_readout*mult_duration)

###################
# The QUA program #
###################
with program() as PSB_search_prog:
    adc_dc_st = declare_stream(
        adc_trace=True
    )  # The stream to store the raw ADC trace for the DC lin
    
    with infinite_loop_():
        seq.add_step(voltage_point_name="empty")
        seq.add_step(voltage_point_name="initialization")
        seq.add_step(voltage_point_name="readout")
        seq.add_compensation_pulse(duration=duration_compensation_pulse*mult_duration)
        
        # seq.add_step(voltage_point_name="empty", ramp_duration=duration_empty*mult_duration)
        # seq.add_step(voltage_point_name="initialization", ramp_duration=duration_empty*mult_duration)
        # seq.add_compensation_pulse(duration=duration_compensation_pulse*mult_duration)
        seq.ramp_to_zero()

        wait(1_000_000)

    # measure(
    #     "readout",
    #     "tank_circuit",
    #     adc_dc_st,
    # )
    # wait((duration_empty - readout_len) * u.ns, "tank_circuit")
    # measure(
    #     "readout",
    #     "tank_circuit",
    #     adc_dc_st,
    # )
    # wait((duration_init - readout_len) * u.ns, "tank_circuit")
    # measure(
    #     "readout",
    #     "tank_circuit",
    #     adc_dc_st,
    # )
    # wait((duration_readout - readout_len) * u.ns, "tank_circuit")
    # measure(
    #     "readout",
    #     "tank_circuit",
    #     adc_dc_st,
    # )


    # wait((duration_init + duration_empty) * u.ns, "tank_circuit")
    # measure(
    #     "readout",
    #     "tank_circuit",
    #     None,
    #     # demod.full("cos", I, "out2"),
    #     # demod.full("sin", Q, "out2"),
    # )

    # Ramp the voltage down to zero at the end of the triangle (needed with sticky elements)

    # with stream_processing():
    #     adc_dc_st.input2().save_all('raw_adc')


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, cluster_name=cluster_name
)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=4_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PSB_search_prog, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # span for duration_empty, duration_init,duration_readout
    t0_list = [
        np.nonzero(samples.con1.analog[k])[0] for k in samples.con1.analog.keys()
    ]
    t0_list = [t0[0] for t0 in t0_list if len(t0) > 0]
    # each point is 0.5 ns
    t0 = min(t0_list) / 2
    durations = np.array([
        duration_empty,
        duration_init,
        duration_readout,
        duration_compensation_pulse,
    ])*mult_duration
    texts = [
        "Empty",
        "Initialization",
        "Readout",
        "Compensation",
    ]
    colors = ["blue", "green", "orange", "red"]
    for duration, color, text in zip(durations, colors, texts):
        t1 = t0 + duration
        plt.axvspan(t0, t1, color=color, alpha=0.3)
        plt.text(
            (t0 + t1) / 2,
            -0.1,
            text,
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=12,
            color=color,
            rotation="vertical",
        )
        t0 = t1

    # # Get the waveform report object
    # waveform_report = job.get_simulated_waveform_report()
    # # Cast the waveform report to a python dictionary
    # waveform_dict = waveform_report.to_dict()
    # # Visualize and save the waveform report
    # waveform_report.create_plot(
    #     samples, plot=True, save_path=str(Path(__file__).resolve())
    # )
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PSB_search_prog)
    # Get results from QUA program and initialize live plotting
    res = job.result_handles
    # dc_vals = res.adc_results.fetch_all()['value']

# %%
