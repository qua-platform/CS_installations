from quam.components import *
from quam.examples.superconducting_qubits import Transmon, Quam



machine = Quam()

num_qubits = 2
for idx in range(num_qubits):

    # Create transmon qubit component
    transmon = Transmon(id=idx)
    machine.qubits[transmon.name] = transmon

    # Add xy drive line channel
    transmon.xy = IQChannel(
        opx_output_I=("con1", 3 * idx + 3),
        opx_output_Q=("con1", 3 * idx + 4),
        frequency_converter_up=FrequencyConverter(
            mixer=Mixer(),
            local_oscillator=LocalOscillator(power=10, frequency=6e9),
        ),
        intermediate_frequency=100e6,
    )

    # Add transmon flux line channel
    transmon.z = SingleChannel(opx_output=("con1", 3 * idx + 5))

    # Add resonator channel
    transmon.resonator = InOutIQChannel(
        id=idx,
        opx_output_I=("con1", 1),
        opx_output_Q=("con1", 2),
        opx_input_I=("con1", 1),
        opx_input_Q=("con1", 2,),
        frequency_converter_up=FrequencyConverter(
            mixer=Mixer(), local_oscillator=LocalOscillator(power=10, frequency=6e9)
        ),
    )




from quam.components.pulses import GaussianPulse
# Create a Gaussian pulse
gaussian_pulse = GaussianPulse(length=20, amplitude=0.2, sigma=3)

# Attach the pulse to the XY channel of the first qubit
machine.qubits["q0"].xy.operations["X90"] = gaussian_pulse





from quam.components.pulses import SquareReadoutPulse
# Create a Readout pulse
readout_pulse = SquareReadoutPulse(length=1000, amplitude=0.1)

# Attach the pulse to the resonator of the first qubit
machine.qubits["q0"].resonator.operations["readout"] = readout_pulse




# What would the config look like at this stage? Let's see:
print(machine.generate_config())



machine.print_summary()
machine.save("/Users/kalidu_laptop/QUA/CS_installations/quam_documentation")