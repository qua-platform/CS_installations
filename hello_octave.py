from qm import QuantumMachinesManager
from qm.qua import *
from qm.octave import *
from configuration import *
from qm import SimulationConfig
import time
from qm_saas import QmSaas, QOPVersion          


# ---------------------------------------------------------------------------
# 1.  SaaS login
# ---------------------------------------------------------------------------
client = QmSaas(
    host="qm-saas.dev.quantum-machines.co",
    email="benjamin.safvati@quantum-machines.co",
    password="ubq@yvm3RXP1bwb5abv"
)


with client.simulator(QOPVersion("v2_4_4")) as inst: 
    inst.spawn()                                                  # boot the virtual QOP

    qmm = QuantumMachinesManager(
        host=inst.host,
        port=inst.port,
        connection_headers=inst.default_connection_headers,
    )
###################################
# Open Communication with the QOP #
###################################
#qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, octave=octave_config)

    ###################
    # The QUA program #
    ###################
    with program() as hello_octave:
        with infinite_loop_():
            play("const" * amp(0.5), 'flux_tls1')
            play("const" * amp(0.5), 'flux_tls23')
            play("const" * amp(0.5), "tls1")
            play("const" * amp(0.5), "tls2")
            play("const" * amp(0.5), "tls3")

    #######################################
    # Execute or Simulate the QUA program #
    #######################################
    simulate = True
    if simulate:
        simulation_config = SimulationConfig(duration=400)  # in clock cycles
        job = qmm.simulate(config, hello_octave, simulation_config)
        job.get_simulated_samples().con1.plot()
        samples = job.get_simulated_samples()
        # Get the waveform report object
        waveform_report = job.get_simulated_waveform_report()
        # Cast the waveform report to a python dictionary
        waveform_dict = waveform_report.to_dict()
        # Visualize and save the waveform report
        waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
    else:
        qm = qmm.open_qm(config)
        job = qm.execute(hello_octave)
        # Execute does not block python! As this is an infinite loop, the job would run forever.
        # In this case, we've put a 10 seconds sleep and then halted the job.
        time.sleep(10)
        job.halt()