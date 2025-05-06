import xarray as xr

ds = xr.open_dataset(r"C:\Git\CS_installations\qualibrate\data\2025-04-17\#18_03a_Qubit_Spectroscopy_164406\ds.h5")
print(ds)


### STARK SHIFT CALIBRATION PROTOCOL


if not node.parameters.simulate:
    if node.parameters.load_data_id is None:
        # Fetch the data from the OPX and convert it into a xarray with corresponding axes (from most inner to outer loop)
        # res = job.result_handles()
        # state1 = res.state1.fetch_all()["value"]
        # state2 = res.state2.fetch_all()["value"]
        # detunings = dfs

        # analysis_result1 = fit_alternating_pulse_train(detunings, N_pi_vec, state1)
        # analysis_result2 = fit_alternating_pulse_train(detunings, N_pi_vec, state2)

        QM_analysis = True
        if QM_analysis:
            ds = fetch_results_as_xarray(
                job.result_handles, qubits, {"freq": dfs, "N": N_pi_vec}
            )
            if not node.parameters.use_state_discrimination:
                # Convert IQ data into volts
                ds = convert_IQ_to_V(ds, qubits)
            else:
                node = node.load_from_id(node.parameters.load_data_id)
                ds = node.results["ds"]
            # Add the dataset to the node
            node.results = {"ds": ds}

# # %% {Data_analysis}
detuning = {
    qubit.name: fit_alternating_pulse_train(
        ds.freq.values, ds.N.values, ds.state[i].values, plot=False
    )[0]
    for i, qubit in enumerate(qubits)
}
# # Get the average along the number of pulses axis to identify the best pulse amplitude
# state_n = ds.state.mean(dim="N")
# data_max_idx = state_n.argmin(dim="freq")
# detuning = ds.freq[data_max_idx]

# # Save fitting results
fit_results = {
    qubit.name: {"detuning": float(detuning[qubit.name])} for qubit in qubits
}
for q in qubits:
    print(f"Detuning for {q.name} is {fit_results[q.name]['detuning']} Hz")
node.results["fit_results"] = fit_results

# %% {Plotting}
grid = QubitGrid(ds, [q.grid_location for q in qubits])
for ax, qubit in grid_iter(grid):
    ds.assign_coords(freq_MHz=ds.freq * 1e-6).loc[qubit].state.plot(
        ax=ax, x="freq_MHz", y="N"
    )
    ax.axvline(1e-6 * fit_results[qubit["qubit"]]["detuning"], color="r")
    ax.set_ylabel("num. of pulses")
    ax.set_xlabel("detuning [MHz]")
    ax.set_title(qubit["qubit"])
grid.fig.suptitle("Stark detuning")
plt.tight_layout()
plt.show()
node.results["figure"] = grid.fig

# %% {Update_state}
# Revert the change done at the beginning of the node

# for qubit in tracked_qubits:
#     qubit.revert_changes()

if node.parameters.load_data_id is None:
    with node.record_state_updates():
        for qubit in qubits:
            qubit.I.intermediate_frequency += float(fit_results[qubit.name]["detuning"])
            # qubit.I.operations["x90_Cosine"].detuning = float(
            #     fit_results[qubit.name]["detuning"]
            # )
            # qubit.I.operations["-x90_Cosine"].detuning = float(
            #     fit_results[qubit.name]["detuning"]
            # )

            # qubit.Q.operations[operation].detuning = float(fit_results[qubit.name]["detuning"])

# %% {Save_results}
node.outcomes = {q.name: "successful" for q in qubits}
node.results["initial_parameters"] = node.parameters.model_dump()
node.machine = machine
# node.save()