# %%
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_opxplus import *
from qualang_tools.results import progress_counter, fetching_tool, wait_until_job_is_paused
from qualang_tools.plot import interrupt_on_close
from qualang_tools.addons.variables import assign_variables_to_element
import matplotlib.pyplot as plt
from configuration_20250626 import *
from macros import RF_reflectometry_macro, DC_current_sensing_macro


###################
# The QUA program #
###################
total_duration = 60 * u.s

sub_duration = 5 * u.s
num_outer = total_duration // sub_duration  # Number of averaging loops

with program() as reflectometry_spectro:
    m = declare(int)  # QUA variable for the averaging loop
    n = declare(int)  # QUA variable for the averaging loop
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature

    with for_(n, 0, n < num_outer, n + 1):
        # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
        # Please choose the right "out1" or "out2" according to the connectivity
        measure(
            # "long_readout_trimmed",
            "readout",
            # "long_readout",
            "tank_circuit",
            None,
            demod.full("cos", I, "out1"),
            demod.full("sin", Q, "out1"),
        )

        save(I, I_st)
        save(Q, Q_st)
        save(n, n_st)

        pause()

        wait(5 *u.s)  

    with stream_processing():
        I_st.save("I")
        Q_st.save("Q")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name
)


#######################
# Simulate or execute #
#######################
simulate = False
save_data = True
qm = None

def solve_for_voltage(amplitude, A, gamma, Vpeak, B):
    # 安全性チェック
    if amplitude <= B or amplitude >= A + B:
        raise ValueError("amplitude must be between B and A + B for real solution")

    inside_sqrt = A / (amplitude - B)
    arccosh_arg = np.sqrt(inside_sqrt)
    delta = np.arccosh(arccosh_arg) / gamma

    # 2つの解（対称性により ±）
    # V1 = Vpeak + delta
    V2 = Vpeak - delta

    return V2

try:
    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
        # Simulate blocks python until the simulation is done
        job = qmm.simulate(config, reflectometry_spectro, simulation_config)
        # Plot the simulated samples
        job.get_simulated_samples().con1.plot()
        plt.show()

    else:
        # Open the quantum machine
        qm = qmm.open_qm(config)
        # Send the QUA program to the OPX, which compiles and executes it
        job = qm.execute(reflectometry_spectro)

        Is = []
        Qs = []
        V_changes = []
        amplitudes = []

        amplitude = 0.001 # initial value
        print("    start!!")
        results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
        for z in range(num_outer):
            print(f"\nrep={z}")

            print("    here1")
            I, Q, iteration = results.fetch_all()
            
            Is.append(I)
            Qs.append(Q)
            print(f"        I={I:9.8f}")
            print(f"        Q={Q:9.8f}")
            
            I = I / 2**12
            Q = Q / 2**12

            V_change = 2.036 # solve_for_voltage(amplitude=amplitude, A=1.0382e-4, gamma=451.233302, Vpeak=2.040795, B=9.313e-5)
            amplitude = np.sqrt(I**2 + Q**2)
            
            V_changes.append(V_change)
            amplitudes.append(amplitude)
            print(f"        V_change={V_change:9.8f}")
            print(f"        amplitude={amplitude}")
            
            if V_change < 2.035 :
                raise ValueError("Outside the voltage range!")

            #################################
            # Here, update the QDACII voltage
            #################################
            # s.v_LDG.voltage = V_change # Feedback voltage
            # s.v_LDG.voltage = 2.039

            job.resume()

            print("    here2")
            if z + 1 == num_outer:
                print("break!!")
                break
P
            print("    here3")
            # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
            wait_until_job_is_paused(job)
            print("    here4")

        if save_data:
            from qualang_tools.results.data_handler import DataHandler

            # Save results
            script_name = "meas_Genbu_20250522_w_OPX.ipynb"  # 実際のNotebook名に変更
            data_handler = DataHandler(root_data_folder=save_dir)
            data_handler.create_data_folder(name="monitoring_reflectometry_feedback")

            # Data to save
            save_data_dict = {}
            # save_data_dict["elapsed_time"] =  np.array([elapsed_time])
            save_data_dict["I"] = np.array(Is)
            save_data_dict["Q"] = np.array(Qs)
            save_data_dict["V_change"] = np.array(V_changes)
            save_data_dict["amplitude"] = np.array(amplitudes)

            # Save results
            # save_data_dict.update({"fig_live": fig})
            data_handler.additional_files = {
                script_name: script_name,
                **default_additional_files,
            }
            data_handler.save_data(data=save_data_dict)
finally:
    if qm is not None:
        qm.close()
# %%
