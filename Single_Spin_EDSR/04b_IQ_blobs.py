"""
        IQ BLOBS
This sequence involves measuring the state of the resonator 'N' times, first after thermalization (with the qubit
in the |g> state) and then after applying a pi pulse to the qubit (bringing the qubit to the |e> state) successively.
The resulting IQ blobs are displayed, and the data is processed to determine:
    - The rotation angle required for the integration weights, ensuring that the separation between |g> and |e> states
      aligns with the 'I' quadrature.
    - The threshold along the 'I' quadrature for effective qubit state discrimination.
    - The readout fidelity matrix, which is also influenced by the pi pulse fidelity.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.

Next steps before going to the next node:
    - Update the rotation angle (rotation_angle) in the configuration.
    - Update the g -> e threshold (ge_threshold) in the configuration.
"""

from qm.qua import *
from qm import SimulationConfig
from qm import QuantumMachinesManager
from configuration import *
from qualang_tools.analysis.discriminator import two_state_discriminator

###################
# The QUA program #
###################

n_runs = 10000  # Number of runs

with program() as IQ_blobs:
    n = declare(int)
    Ig = [declare(fixed) for _ in range(nb_of_tank_circuits)]
    Qg = [declare(fixed) for _ in range(nb_of_tank_circuits)]
    Ig_st = [declare_stream() for _ in range(nb_of_tank_circuits)]
    Qg_st = [declare_stream() for _ in range(nb_of_tank_circuits)]
    Ie = [declare(fixed) for _ in range(nb_of_tank_circuits)]
    Qe = [declare(fixed) for _ in range(nb_of_tank_circuits)]
    Ie_st = [declare_stream() for _ in range(nb_of_tank_circuits)]
    Qe_st = [declare_stream() for _ in range(nb_of_tank_circuits)]

    with for_(n, 0, n < n_runs, n + 1):
        for i in range(nb_of_tank_circuits):
            reset_if_phase(f"tank_circuit{i + 1}")
            # Measure the state of the resonator
            measure("readout", f"tank_circuit{i + 1}", demod.full("rotated_cos", Ig[i], "out1"), demod.full("rotated_sin", Qg[i], "out1"))
            # Wait for the qubit to decay to the ground state in the case of measurement induced transitions
            wait(duration_init * u.ns, f"tank_circuit{i + 1}")
            # Save the 'I' & 'Q' quadratures to their respective streams for the ground state
            save(Ig[i], Ig_st[i])
            save(Qg[i], Qg_st[i])
            align("qubit", f"tank_circuit{i + 1}")
            # Play the x180 gate to put the qubit in the excited state
            play("pi", "qubit")
            frame_rotation_2pi(0.125, f"tank_circuit{i + 1}")
            # Align the two elements to measure after playing the qubit pulse.
            align("qubit", f"tank_circuit{i + 1}")
            # Measure the state of the resonator
            measure("readout", f"tank_circuit{i + 1}", demod.full("rotated_cos", Ie[i], "out1"), demod.full("rotated_sin", Qe[i], "out1"))
            # Wait for the qubit to decay to the ground state
            wait(duration_init * u.ns, f"tank_circuit{i + 1}")
            # Save the 'I' & 'Q' quadratures to their respective streams for the excited state
            save(Ie[i], Ie_st[i])
            save(Qe[i], Qe_st[i])
            reset_frame(f"tank_circuit{i + 1}")
    with stream_processing():
        # Save all streamed points for plotting the IQ blobs
        for i in range(nb_of_tank_circuits):
            Ig_st[i].save_all(f"Ig{i+1}")
            Qg_st[i].save_all(f"Qg{i+1}")
            Ie_st[i].save_all(f"Ie{i+1}")
            Qe_st[i].save_all(f"Qe{i+1}")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, IQ_blobs, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(IQ_blobs)
    # Creates a result handle to fetch data from the OPX
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    res_handles.wait_for_all_values()
    # Fetch the 'I' & 'Q' points for the qubit in the ground and excited states
    IQ_data = {}
    for i in range(nb_of_tank_circuits):
        IQ_data[f"tank_circuit{i + 1}"] = {
            "Ig": res_handles.get(f"Ig{i+1}").fetch_all()["value"],
            "Qg": res_handles.get(f"Qg{i+1}").fetch_all()["value"],
            "Ie": res_handles.get(f"Ie{i + 1}").fetch_all()["value"],
            "Qe": res_handles.get(f"Qe{i + 1}").fetch_all()["value"],
        }
        angle, threshold, fidelity, gg, ge, eg, ee = two_state_discriminator(IQ_data[f"tank_circuit{i + 1}"]["Ig"], IQ_data[f"tank_circuit{i + 1}"]["Qg"], IQ_data[f"tank_circuit{i + 1}"]["Ie"], IQ_data[f"tank_circuit{i + 1}"]["Qe"], b_print=True, b_plot=True)
        IQ_data[f"tank_circuit{i + 1}"]["angle"] = angle
        IQ_data[f"tank_circuit{i + 1}"]["threshold"] = threshold
        IQ_data[f"tank_circuit{i + 1}"]["fidelity"] = fidelity
        IQ_data[f"tank_circuit{i + 1}"]["confusion"] = [[gg, ge], [eg, ee]]

    # Plot the IQ blobs, rotate them to get the separation along the 'I' quadrature, estimate a threshold between them
    # for state discrimination and derive the fidelity matrix

    #########################################
    # The two_state_discriminator gives us the rotation angle which makes it such that all of the information will be in
    # the I axis. This is being done by setting the `rotation_angle` parameter in the configuration.
    # See this for more information: https://qm-docs.qualang.io/guides/demod#rotating-the-iq-plane
    # Once we do this, we can perform active reset using:
    #########################################
    #
    # # Active reset:
    # with if_(I > threshold):
    #     play("x180", "qubit")
    #
    #########################################
    #
    # # Active reset (faster):
    # play("x180", "qubit", condition=I > threshold)
    #
    #########################################
    #
    # # Repeat until success active reset
    # with while_(I > threshold):
    #     play("x180", "qubit")
    #     align("qubit", "resonator")
    #     measure("readout", "resonator", None,
    #                 dual_demod.full("rotated_cos", "rotated_sin", I))
    #
    #########################################
    #
    # # Repeat until success active reset, up to 3 iterations
    # count = declare(int)
    # assign(count, 0)
    # cont_condition = declare(bool)
    # assign(cont_condition, ((I > threshold) & (count < 3)))
    # with while_(cont_condition):
    #     play("x180", "qubit")
    #     align("qubit", "resonator")
    #     measure("readout", "resonator", None,
    #                 dual_demod.full("rotated_cos", "rotated_sin", I))
    #     assign(count, count + 1)
    #     assign(cont_condition, ((I > threshold) & (count < 3)))
    #
    #########################################
