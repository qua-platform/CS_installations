"""
Example on how to measure raw ADC traces with the OPX+.
"""

import time

from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *

meas_len = 1000
resolution = 1000  # ps
t_vec = np.arange(0, meas_len * 1e3, 1)

###################
# The QUA program #
###################
with program() as adc_trace:
    adc_st = declare_stream(adc_trace=True)

    measure("readout", "SNSPD", adc_st)

    with stream_processing():
        adc_st.input1().save_all("adc_trace")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=opx_ip, port=None, cluster_name=cluster_name, octave=octave_config
)

###########################
# Run or Simulate Program #
###########################


simulate = False

volt_unit = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, adc_trace, simulation_config)
    # Plot the simulated samples
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(adc_trace)

    res = job.result_handles
    job.result_handles.wait_for_all_values()
    adc_res = res.get("adc_trace").fetch_all()["value"]
    adc_volts = u.raw2volts(adc_res)  # converts ADC units to volts

    plt.figure()
    plt.plot(adc_res[0, :] if not volt_unit else adc_volts[0, :])
    plt.title("ADC trace")
    plt.xlabel("t [ns]")
    plt.ylabel("ADC trace [a.u.]" if not volt_unit else "ADC trace [V]")
    plt.tight_layout()
    plt.show()
