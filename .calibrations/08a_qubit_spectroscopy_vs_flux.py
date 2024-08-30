# %%
"""
        QUBIT SPECTROSCOPY VERSUS FLUX
This sequence involves doing a qubit spectroscopy for several flux biases in order to exhibit the qubit frequency
versus flux response.

Prerequisites:
    - Identification of the resonator's resonance frequency when coupled to the qubit in question (referred to as "resonator_spectroscopy").
    - Calibration of the IQ mixer connected to the qubit drive line (whether it's an external mixer or an Octave port).
    - Identification of the approximate qubit frequency ("qubit_spectroscopy").

Before proceeding to the next node:
    - Update the qubit frequency, labeled as "f_01", in the state.
    - Update the relevant flux points in the state.
    - Save the current state by calling machine.save("quam")
"""

from pathlib import Path

from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
from lib.plot_utils import QubitGrid, grid_iter
from lib.save_utils import fetch_results_as_xarray
from lib.fit import peaks_dips

matplotlib.use("TKAgg")


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components
qubits = machine.active_qubits
num_qubits = len(qubits)

###################
# The QUA program #
###################

operation = "saturation"  # The qubit operation to play, can be switched to "x180" when the qubits are found.
n_avg = 100  # Number of averaging loops
cooldown_time = max(q.thermalization_time for q in qubits)

# Adjust the pulse duration and amplitude to drive the qubit into a mixed state
saturation_len = 20 * u.us  # In ns
saturation_amp = 0.01  # pre-factor to the value defined in the config - restricted to [-2; 2)

# Qubit detuning sweep with respect to their resonance frequencies
dfs = np.arange(-25e6, 20e6, 0.25e6)
# Flux bias sweep
dcs = np.linspace(-0.015, 0.015, 26)

flux_point = "joint"  # "independent", "joint" or "zero"
# Adjust the qubits IFs locally to help find the qubits
# q1.xy.intermediate_frequency = 340e6
# q2.xy.intermediate_frequency = 0

with program() as multi_qubit_spec_vs_flux:
    # Macro to declare I, Q, n and their respective streams for a given number of qubit (defined in macros.py)
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    df = declare(int)  # QUA variable for the qubit frequency
    dc = declare(fixed)  # QUA variable for the flux dc level

    for i, q in enumerate(qubits):

        # Bring the active qubits to the minimum frequency point
        if flux_point == "independent":
            machine.apply_all_flux_to_min()
            q.z.to_independent_idle()
        elif flux_point == "joint":
            machine.apply_all_flux_to_joint_idle()
        else:
            machine.apply_all_flux_to_zero()
        wait(1000)

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)

            with for_(*from_array(df, dfs)):
                # Update the qubit frequencies for all qubits
                update_frequency(q.xy.name, df + q.xy.intermediate_frequency)

                with for_(*from_array(dc, dcs)):
                    # Flux sweeping for a qubit
                    if flux_point == "independent":
                        q.z.set_dc_offset(dc + q.z.independent_offset)
                    elif flux_point == "joint":
                        q.z.set_dc_offset(dc + q.z.joint_offset)
                    else:
                        raise RuntimeError(f"unknown flux_point")                  
                    wait(100)  # Wait for the flux to settle

                    # Apply saturation pulse to all qubits
                    q.xy.play(
                        operation,
                        amplitude_scale=saturation_amp,
                        duration=saturation_len * u.ns,
                    )

                    # QUA macro to read the state of the active resonators
                    q.resonator.measure("readout", qua_vars=(I[i], Q[i]))

                    # save data
                    save(I[i], I_st[i])
                    save(Q[i], Q_st[i])

                    # Wait for the qubits to decay to the ground state
                    wait(cooldown_time * u.ns)

        align(*([q.xy.name for q in qubits] + [q.resonator.name for q in qubits]))    

    with stream_processing():
        n_st.save("n")
        for i, q in enumerate(qubits):
            I_st[i].buffer(len(dcs)).buffer(len(dfs)).average().save(f"I{i + 1}")
            Q_st[i].buffer(len(dcs)).buffer(len(dfs)).average().save(f"Q{i + 1}")
# %%
#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, multi_qubit_spec_vs_flux, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(multi_qubit_spec_vs_flux)
    # Get results from QUA program

    data_list = ["n"] + sum([[f"I{i + 1}", f"Q{i + 1}"] for i in range(num_qubits)], [])
    results = fetching_tool(job, data_list, mode="live")
    # Live plotting
    # fig = plt.figure()
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        fetched_data = results.fetch_all()
        n = fetched_data[0]
        # I = fetched_data[1::2]
        # Q = fetched_data[2::2]

        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)

        # plt.suptitle("Qubit spectroscopy vs flux")
        # s_data = []
        # for i, q in enumerate(qubits):
        #     s = u.demod2volts(I[i] + 1j * Q[i], q.resonator.operations["readout"].length)
        #     s_data.append(s)
        #     plt.subplot(2, num_qubits, i + 1)
        #     plt.cla()
        #     plt.pcolor(dcs, (q.xy.intermediate_frequency + dfs) / u.MHz, np.abs(s))
        #     plt.plot(q.z.min_offset, q.xy.intermediate_frequency / u.MHz, "r*")
        #     plt.xlabel("Flux [V]")
        #     plt.ylabel(f"{q.name} IF [MHz]")
        #     plt.title(f"{q.name} (f_01: {q.f_01 / u.MHz} MHz)")
        #     plt.subplot(2, num_qubits, num_qubits + i + 1)
        #     plt.cla()
        #     plt.pcolor(dcs, (q.xy.intermediate_frequency + dfs) / u.MHz, np.unwrap(np.angle(s)))
        #     plt.plot(q.z.min_offset, q.xy.intermediate_frequency / u.MHz, "r*")
        #     plt.xlabel("Flux [V]")
        #     plt.ylabel(f"{q.name} IF [MHz]")
        #     plt.tight_layout()
        #     plt.pause(0.1)

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    # while not job.status == 'completed':
    #     pass
    qm.close()

    # Set the relevant flux points
    # qubits[0].z.min_offset = 0.0
    # qubits[1].z.min_offset = 0.0
    # qubits[2].z.min_offset = 0.0
    # qubits[3].z.min_offset = 0.0
    # qubits[4].z.min_offset = 0.0

    # Save data from the node
    # data = {}
    # for i, q in enumerate(qubits):
    #     data[f"{q.name}_flux_bias"] = dcs
    #     data[f"{q.name}_frequency"] = dfs + q.xy.intermediate_frequency
    #     data[f"{q.name}_R"] = np.abs(s_data[i])
    #     data[f"{q.name}_phase"] = np.angle(s_data[i])
    #     data[f"{q.name}_min_offset"] = q.z.min_offset
    # data["figure"] = fig
    # node_save(machine, "qubit_spectroscopy_vs_flux", data, additional_files=True)

# %%
handles = job.result_handles
ds = fetch_results_as_xarray(handles, qubits, {"flux": dcs, "freq": dfs})
# %%
ds = ds.assign({'IQ_abs': np.sqrt(ds['I'] ** 2 + ds['Q'] ** 2)})
def abs_freq(q):
    def foo(freq):
        return freq + q.resonator.intermediate_frequency + q.resonator.LO_frequency
    return foo

ds = ds.assign_coords({'freq_full' : (['qubit','freq'],np.array([abs_freq(q)(dfs) for q in qubits]))})

ds.freq_full.attrs['long_name'] = 'Frequency'
ds.freq_full.attrs['units'] = 'GHz'

# %%


# %%
# %%
data = {}
data['ds'] = ds

peaks = peaks_dips(ds.I, dim = 'freq',prominence_factor=10)
parabolic_fit_results = peaks.position.polyfit('flux',2)
coeff = parabolic_fit_results.polyfit_coefficients
fitted = coeff.sel(degree = 2) * ds.flux ** 2 + coeff.sel(degree = 1) * ds.flux + coeff.sel(degree = 0)
flux_shift = -coeff[1] / ( 2 * coeff[0])
freq_shift = coeff.sel(degree = 2) * flux_shift ** 2 + coeff.sel(degree = 1) * flux_shift + coeff.sel(degree = 0)



fit_results = {}

for q in machine.active_qubits:
    fit_results[q.name] = {}
    if not np.isnan(flux_shift.sel(qubit = q.name).values):
        if flux_point == "independent":
            offset = q.z.independent_offset
        elif flux_point == "joint":
            offset = q.z.joint_offset        
        print(f'flux offset for qubit {q.name} is {offset*1e3 + flux_shift.sel(qubit = q.name).values*1e3:.0f} mV')
        print(f'a shift of  {flux_shift.sel(qubit = q.name).values*1e3:.0f} mV')
        print(
            f"Drive frequency for {q.name} is {(freq_shift.sel(qubit = q.name).values + q.xy.intermediate_frequency + q.xy.LO_frequency)/1e9:.3f} GHz")
        print(
            f"(shift of {freq_shift.sel(qubit = q.name).values/1e6:.0f} MHz)")
        print(
            f'quad term for qubit {q.name} is {float(coeff.sel(degree = 2, qubit = q.name)/1e9):.3e} GHz/V^2 \n')
        fit_results[q.name]['flux_shift'] = float(flux_shift.sel(qubit = q.name).values)
        fit_results[q.name]['drive_freq'] = float(freq_shift.sel(qubit = q.name).values) 
        fit_results[q.name]['quad_term'] = float(coeff.sel(degree = 2, qubit = q.name))
    else:
        print(f'No fit for qubit {q.name}')
        fit_results[q.name]['flux_shift'] = np.nan
        fit_results[q.name]['drive_freq'] = np.nan
        fit_results[q.name]['quad_term'] = np.nan
data['fit_results'] = fit_results



# %%
grid = QubitGrid(ds, [f'q-{i}_0' for i in range(num_qubits)])

for ax, qubit in grid_iter(grid):
    ds.assign_coords(freq_GHz=ds.freq / 1e0).loc[qubit].I.plot(ax=ax, add_colorbar=False,
                                                                            x='flux', y='freq_GHz', robust=True)
    fitted.loc[qubit].plot(ax = ax,linewidth = 0.5, ls = '--',color = 'r')
    ax.plot(flux_shift.loc[qubit], freq_shift.loc[qubit], 'r*')
    peaks.position.loc[qubit].plot(ax = ax, ls = '', marker = '.', color = 'r')
    ax.set_ylabel('Freq (GHz)')
    ax.set_xlabel('Flux (V)')
    ax.set_title(qubit['qubit'])
grid.fig.suptitle('Resonator spectroscopy vs flux ')

plt.tight_layout()
plt.show()
data["figure"] = grid.fig

# %%
for q in machine.active_qubits:
    if not np.isnan(flux_shift.sel(qubit = q.name).values):
        if flux_point == 'independent':
            q.z.independent_offset += fit_results[q.name]['flux_shift']
        elif flux_point == 'joint':
            q.z.joint_offset += fit_results[q.name]['flux_shift']
        q.xy.intermediate_frequency += fit_results[q.name]['drive_freq']
        q.freq_vs_flux_01_quad_term = fit_results[q.name]['quad_term']

# %%
node_save(machine, "qubit_spectroscopy_vs_flux", data, additional_files=True)

# %%