# %%
"""
        CZ CHEVRON - 4ns granularity
The goal of this protocol is to find the parameters of the CZ gate between two flux-tunable qubits.
The protocol consists in flux tuning one qubit to bring the |11> state on resonance with |20>.
The two qubits must start in their excited states so that, when |11> and |20> are on resonance, the state |11> will
start acquiring a global phase when varying the flux pulse duration.

By scanning the flux pulse amplitude and duration, the CZ chevron can be obtained and post-processed to extract the
CZ gate parameters corresponding to a single oscillation period such that |11> pick up an overall phase of pi (flux
pulse amplitude and interation time).

This version sweeps the flux pulse duration using real-time QUA, which means that the flux pulse can be arbitrarily long
but the step must be larger than 1 clock cycle (4ns) and the minimum pulse duration is 4 clock cycles (16ns).

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having found the qubits maximum frequency point (qubit_spectroscopy_vs_flux).
    - Having calibrated qubit gates (x180) by running qubit spectroscopy, rabi_chevron, power_rabi, Ramsey and updated the state.
    - (Optional) having corrected the flux line distortions by running the Cryoscope protocol and updating the filter taps in the state.

Next steps before going to the next node:
    - Update the CZ gate parameters in the state.
    - Save the current state by calling machine.save("quam")
"""

from pathlib import Path
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.units import unit

import matplotlib.pyplot as plt
import numpy as np
import os

from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save


import matplotlib

matplotlib.use("TKAgg")

###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Define a path relative to this script, i.e., ../configuration/quam_state
config_path = Path(__file__).parent.parent / "configuration" / "quam_state"
# Instantiate the QuAM class from the state file
machine = QuAM.load(config_path)
# Generate the OPX and Octave configurations
config = machine.generate_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components
q1 = machine.qubits["q4"]
q2 = machine.qubits["q5"]
coupler = (q1 @ q2).coupler
# compensations = {
#     q1: coupler.opx_output.crosstalk[q1.z.opx_output.port_id],
#     q2: coupler.opx_output.crosstalk[q2.z.opx_output.port_id]
# }

import numpy as np
compensation_arr = np.array([[1, 0.177], [0.408, 1]])
inv_arr = np.linalg.inv(compensation_arr)

###################
# The QUA program #
###################
qb = q1  # The qubit whose flux will be swept

n_avg = 100
# The flux pulse durations in clock cycles (4ns) - Must be larger than 4 clock cycles.
ts = np.arange(4, 300, 1) # in cycles
# The flux bias sweep in V
amps = np.linspace(-1.5, 1.5, 301)
# amps = np.linspace(-0.0392, -0.0396, 25)
# amps = np.linspace(-0.045, -0.025, 701)
# cz_point = -0.0394572
wait_time = 40
scale = 1

with program() as cz:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=2)
    t = declare(int)  # QUA variable for the flux pulse duration
    dc = declare(fixed)  # QUA variable for the flux pulse amplitude
    a = declare(fixed)

    # Bring the active qubits to the minimum frequency point
    machine.apply_all_flux_to_min()
    coupler.set_dc_offset(0)

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        with for_(*from_array(t, ts)):
            with for_(*from_array(a, amps)):
                # assign(v1, Cast.mul_fixed_by_int(-0.15, dc))
                # Put the two qubits in their excited states
                q1.xy.play("x180")
                q2.xy.play("x180")

                align()
                # Wait some time to ensure that the flux pulse will arrive after the x90 pulse
                wait(20 * u.ns)
                # Play a flux pulse on the qubit with the highest frequency to bring it close to the excited qubit while
                # varying its amplitude and duration in order to observe the SWAP chevron.
                
                # vals = inv_arr @ [compensations[q1] * dc, compensations[q2] * dc]
                # q1.z.set_dc_offset(0.0175 + vals[0])
                # q2.z.set_dc_offset(q2.z.min_offset + vals[1])
                
                # q1.z.set_dc_offset(0.0175 + 0.05 * dc)
                # q1.z.play("const", amplitude_scale=4*(1.127 * 0.0175 - 0.0394572 * 0.05 * amp - q1.z.min_offset), duration=t) # 1.127 = (0.01189 - 0.0024)/0.00842
                q1.z.play("const", amplitude_scale=-0.048 + scale * a * coupler.operations["const"].amplitude, duration=t) # 1.127 = (0.01189 - 0.0024)/0.00842

                # q2.z.set_dc_offset(q2.z.min_offset)
                # q2.z.set_dc_offset(q2.z.min_offset + 0.01 * dc)

                # coupler.set_dc_offset(dc)
                coupler.play("const", amplitude_scale=a, duration=t)

                align()
                
                # Put back the qubit to the max frequency point
                # coupler.set_dc_offset(-0.033)
                # q1.z.set_dc_offset(q1.z.min_offset + 0.051 * -0.033)
                # q2.z.set_dc_offset(q2.z.min_offset + 0.01 * -0.033)

                # Wait some time to ensure that the flux pulse will end before the readout pulse
                wait(20 * u.ns)
                # Align the elements to measure after having waited a time "tau" after the qubit pulses.
                align()
                # Measure the state of the resonators
                multiplexed_readout([q1, q2], I, I_st, Q, Q_st)
                # Wait for the qubits to decay to the ground state
                wait(machine.thermalization_time * u.ns)

    with stream_processing():
        # for the progress counter
        n_st.save("n")
        # resonator 1
        I_st[0].buffer(len(amps)).buffer(len(ts)).average().save("I1")
        Q_st[0].buffer(len(amps)).buffer(len(ts)).average().save("Q1")
        # resonator 2
        I_st[1].buffer(len(amps)).buffer(len(ts)).average().save("I2")
        Q_st[1].buffer(len(amps)).buffer(len(ts)).average().save("Q2")


###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, cz, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(cz)
    # Prepare the figure for live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["n", "I1", "Q1", "I2", "Q2"], mode="live")
    # Live plotting
    while results.is_processing():
        # Fetch results
        n, I1, Q1, I2, Q2 = results.fetch_all()
        # Convert the results into Volts
        I1 = u.demod2volts(I1, q1.resonator.operations["readout"].length)
        Q1 = u.demod2volts(Q1, q1.resonator.operations["readout"].length)
        I2 = u.demod2volts(I2, q2.resonator.operations["readout"].length)
        Q2 = u.demod2volts(Q2, q2.resonator.operations["readout"].length)
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # Plot
        plt.suptitle("CZ chevron")
        plt.subplot(241)
        plt.cla()
        plt.pcolor(amps * coupler.operations["const"].amplitude, ts, I1)
        # plt.plot(cz_point, wait_time, color="r", marker="*")
        # plt.title(f"{q1.name} - I, f_01={int(q1.f_01 / u.MHz)} MHz")
        plt.ylabel("Interaction time [ns]")
        plt.subplot(243)
        plt.cla()
        plt.pcolor(amps * coupler.operations["const"].amplitude, ts, Q1)
        # plt.plot(cz_point, wait_time, color="r", marker="*")
        plt.title(f"{q1.name} - Q")
        plt.xlabel("Flux amplitude [V]")
        plt.ylabel("Interaction time [ns]")
        plt.subplot(242)
        plt.cla()
        plt.pcolor(amps * coupler.operations["const"].amplitude, ts, I2)
        # plt.plot(cz_point, wait_time, color="r", marker="*")
        # plt.title(f"{q2.name} - I, f_01={int(q2.f_01 / u.MHz)} MHz")
        plt.subplot(244)
        plt.cla()
        plt.pcolor(amps * coupler.operations["const"].amplitude, ts, Q2)
        # plt.plot(cz_point, wait_time, color="r", marker="*")
        plt.title(f"{q2.name} - Q")
        plt.xlabel("Flux amplitude [V]")

        plt.subplot(245)
        plt.cla()
        for j, t in enumerate(ts):
            plt.plot(amps * coupler.operations["const"].amplitude, I1[j, :])
        # plt.title(f"{q1.name} - I, f_01={int(q1.f_01 / u.MHz)} MHz")
        plt.ylabel("I1 [V]")
        plt.legend([f"{4 * t}" for t in ts])
        plt.subplot(247)
        plt.cla()
        for j, t in enumerate(ts):
            plt.plot(amps * coupler.operations["const"].amplitude, Q1[j, :])
        plt.title(f"{q1.name} - Q")
        plt.xlabel("Flux amplitude [V]")
        plt.ylabel("Q1 [V]")
        plt.subplot(246)
        plt.cla()
        for j, t in enumerate(ts):
            plt.plot(amps * coupler.operations["const"].amplitude, I2[j, :])
        plt.ylabel("I2 [V]")
        # plt.title(f"{q2.name} - I, f_01={int(q2.f_01 / u.MHz)} MHz")
        plt.subplot(248)
        plt.cla()
        for j, t in enumerate(ts):
            plt.plot(amps * coupler.operations["const"].amplitude, Q2[j, :])
        plt.ylabel("Q2 [V]")
        plt.title(f"{q2.name} - Q")
        plt.xlabel("Flux amplitude [V]")
        plt.tight_layout()
        plt.pause(0.1)

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

    plt.show()

    # q1.z.cz.length =
    # q1.z.cz.level =

    # Save data from the node
    data = {
        f"{q1.name}_flux_pulse_amplitude": amps,
        f"{q1.name}_flux_pulse_duration": ts,
        f"{q1.name}_I": I1.T,
        f"{q1.name}_Q": Q1.T,
        f"{q2.name}_flux_pulse_amplitude": amps,
        f"{q2.name}_flux_pulse_duration": ts,
        f"{q2.name}_I": I2.T,
        f"{q2.name}_Q": Q2.T,
        f"qubit_flux": q1.name,
        "figure": fig,
    }
    node_save(machine, "cz_chevron_coupler_pulsed", data, additional_files=True)

# %%
