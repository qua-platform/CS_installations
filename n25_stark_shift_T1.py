# %%
"""
        T1 MEASUREMENT
The sequence consists in putting the qubit in the excited stated by playing the x180 pulse and measuring the resonator
after a varying time. The qubit T1 is extracted by fitting the exponential decay of the measured quadratures.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - Update the qubit T1 (qubit_T1) in the configuration.
"""

import qm.qua as qua
import qm as qm_api
import numpy as np
from configuration import config, qop_ip, cluster_name, u, thermalization_time, readout_len, hittite_ip, hittite_port, ge_threshold
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array, get_equivalent_log_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler
from hittite_driver import HittiteHMCT2220
import time
from qualang_tools.callable_from_qua import patch_qua_program_addons, callable_from_qua

data_handler = DataHandler(root_data_folder="./")

hittite_module = HittiteHMCT2220(ip_address=hittite_ip, port=hittite_port)

hittite_module.connect()

patch_qua_program_addons()

data_handler = DataHandler(root_data_folder="./")

@callable_from_qua
def set_lo_power(element, power):
    # Here the LO frequency must be passed in kHz instead of Hz, 
    # because the QUA integer ranges in +/-2**31 ~ +/- 2.1e9
    print(f"setting the LO power of {element} to {power * 10} dBm")
    hittite_module.set_power(power * 10)
    time.sleep(1)

###################
# The QUA program #
###################
n_avg = 100
# The wait time sweep (in clock cycles = 4ns) - must be larger than 4 clock cycles
tau_min = 16 // 4
tau_max = 2_000_000 // 4
d_tau = 10_000 // 4
taus = np.arange(tau_min, tau_max + 0.1, d_tau)  # Linear sweep
# taus = np.logspace(np.log10(tau_min), np.log10(tau_max), 29)  # Log sweep

lo_min = -10
lo_max = 1
step_lo = 1
lo_values = np.arange(lo_min, lo_max, step_lo)

ac_stark_shift_data = {
    "n_avg": n_avg,
    "taus": taus,
    "config": config
}

with qua.program() as ac_stark_shift:
    n = qua.declare(int)  # QUA variable for the averaging loop
    t = qua.declare(int)  # QUA variable for the wait time
    I = qua.declare(qua.fixed)  # QUA variable for the measured 'I' quadrature
    Q = qua.declare(qua.fixed)  # QUA variable for the measured 'Q' quadrature
    state = qua.declare(bool)
    state_st = qua.declare_stream()
    lo_power = qua.declare(qua.fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = qua.declare_stream()  # Stream for the 'I' quadrature
    Q_st = qua.declare_stream()  # Stream for the 'Q' quadrature

    with qua.for_(*from_array(lo_power, lo_values / 10)):
        
        set_lo_power("resonator", lo_power)

        with qua.for_(n, 0, n < n_avg, n + 1):
            with qua.for_(*from_array(t, taus)):
                # Play the x180 gate to put the qubit in the excited state
                qua.play("x180", "qubit")
                # Wait a varying time after putting the qubit in the excited state
                qua.wait(t, "qubit")
                # Align the two elements to measure after having waited a time "tau" after the qubit pulse.
                qua.align("qubit", "resonator")
                # Measure the state of the resonator
                qua.measure(
                    "readout",
                    "resonator",
                    None,
                    qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I),
                    qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q),
                    # qua.dual_demod.full("opt_cos", "out1", "opt_sin", "out2", I),
                    # qua.dual_demod.full("opt_minus_sin", "out1", "opt_cos", "out2", Q),
                )
                qua.assign(state, I > ge_threshold)
                # Wait for the qubit to decay to the ground state
                qua.wait(thermalization_time * u.ns, "resonator")
                # Save the 'I_e' & 'Q_e' quadratures to their respective streams
                qua.save(I, I_st)
                qua.save(Q, Q_st)
                qua.save(state, state_st)

    with qua.stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        # If log sweep, then the swept values will be slightly different from np.logspace because of integer rounding in QUA.
        # get_equivalent_log_array() is used to get the exact values used in the QUA program.
        if np.isclose(np.std(taus[1:] / taus[:-1]), 0, atol=1e-3):
            taus = get_equivalent_log_array(taus)
            I_st.buffer(len(taus)).buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(len(lo_values)).save("I")
            Q_st.buffer(len(taus)).buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(len(lo_values)).save("Q")
            state_st.boolean_to_int().buffer(len(taus)).buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(len(lo_values)).save("state")
        else:
            I_st.buffer(len(taus)).buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(len(lo_values)).save("I")
            Q_st.buffer(len(taus)).buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(len(lo_values)).save("Q")
            state_st.boolean_to_int().buffer(len(taus)).buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(len(lo_values)).save("state")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = qm_api.QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = qm_api.SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, ac_stark_shift, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ac_stark_shift)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "state"])
    # Fetch results
    I, Q, state = results.fetch_all()
    # Convert the results into Volts
    S = u.demod2volts(I + 1j * Q, readout_len)
    R = np.abs(S)  # Amplitude
    phase = np.angle(S)  # Phase

    plt.figure()
    plt.title('AC stark shift - Power')
    plt.pcolor(taus, lo_values, state)
    plt.xlabel('Tau [ns]')
    plt.ylabel('LO Power [dBm]')

    ac_stark_shift_data['I'] = I
    ac_stark_shift_data['Q'] = Q
    ac_stark_shift_data['R'] = R
    ac_stark_shift_data['phase'] = phase
    ac_stark_shift_data['state'] = state
    data_handler.save_data(data=ac_stark_shift_data, name="ac_stark_shift")

    hittite_module.set_power(-20)  # dBm
    hittite_module.disconnect()

# %%
