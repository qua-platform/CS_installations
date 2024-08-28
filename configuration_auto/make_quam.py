from qualang_tools.wirer import Instruments, Connectivity, allocate_wiring, visualize

instruments = Instruments()
instruments.add_lf_fem(con=1, slots=1)
instruments.add_mw_fem(con=1, slots=2)

qubits = [1, 2, 3, 4, 5, 6]
connectivity = Connectivity()
connectivity.add_resonator_line(qubits=qubits)
connectivity.add_qubit_drive_lines(qubits=qubits)
connectivity.add_qubit_flux_lines(qubits=qubits)

allocate_wiring(connectivity, instruments)

visualize(connectivity.elements, available_channels=instruments.available_channels)

host_ip = "123.456.789.12"
cluster_name = "Cluster_1"
