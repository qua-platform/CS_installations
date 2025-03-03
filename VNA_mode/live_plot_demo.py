from qm.qua import *
from qm_config import qm, rf1_LO, pulse_len, pulse_amp
from live_plot import LivePlotWindow
from matplotlib.backends.qt_compat import QtWidgets
import os.path

from qualang_tools.loops import from_array
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)
import numpy as np

###################
# The QUA program #
###################
# The frequency sweep parameters
f_min = 30 * u.MHz
f_max = 330 * u.MHz
df = 100 * u.kHz
frequencies = np.arange(f_min, f_max + 0.1, df)  # The frequency vector (+ 0.1 to add f_max to frequencies)
n_points = len(frequencies)


with program() as prog:
    f = declare(int)  # QUA variable for the spectro frequency
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    
    with infinite_loop_():
        with for_(*from_array(f, frequencies)):  # QUA for_ loop for sweeping the frequency
            # Update the frequency of the digital oscillator 
            update_frequency("rf1", f)
            # Demodulate the signals to get the 'I' & 'Q' quadratures)
            measure(
                "readout",
                "rf1",
                None,
                dual_demod.full("cos", "sin", I),
                dual_demod.full("minus_sin", "cos", Q),
            )
            # Save the 'I' & 'Q' quadratures to their respective streams
            save(I, I_st)
            save(Q, Q_st)

    with stream_processing():
        # Cast the data into a 1D vector, and store the results on the OPX processor
        I_st.buffer(n_points).zip(Q_st.buffer(n_points)).save("IQ")

####################
# Live plot        #
####################
class myLivePlot(LivePlotWindow):
    def create_axes(self):
        # Create plot 
        self.ax = self.canvas.figure.subplots()
        self.spectrum = self.ax.plot((rf1_LO + frequencies)/1e6,np.zeros(len(frequencies)))[0]
        self.ax.set_xlabel('Frequency (MHz)')
        self.ax.set_ylabel('Magnitude (dB)')
        self.ax.set_ylim(-60,0)
        self.canvas.figure.tight_layout()

    def polldata(self):
        # Fetch the data and plot 
        IQ = self.job.result_handles.get("IQ").fetch(1)
        if IQ is None:
            return        
        I = IQ['value_0']
        Q = IQ['value_1']
        self.spectrum.set_ydata(10*np.log10(I**2+Q**2))
        self.canvas.draw()
    
        

#######################
# Execute the program #
#######################
job = qm.execute(prog)
window = myLivePlot(job)
window.show()
