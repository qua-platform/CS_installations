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

# Get previous calibration if it exists
current_dir = os.path.dirname(os.path.realpath(__file__))
cal_file = os.path.join(current_dir,'cal.npz')
if os.path.isfile(cal_file):
    with np.load(cal_file) as c:
        cal = c['cal'] * pulse_amp/c['pulse_amp'] * pulse_len/c['pulse_len']
    if len(cal)!=n_points:
        cal = np.ones(n_points, dtype=complex)
else:
    cal = np.ones(n_points, dtype=complex)
    

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
                "readout"*amp(IO1),
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
        self.spectrum = self.ax.plot((rf1_LO + frequencies)/1e6, np.zeros(len(frequencies)))[0]
        self.ax.set_xlabel('Frequency (MHz)')
        self.ax.set_ylabel('Transmission (dB)')
        self.ax.set_ylim(-100,10)
        self.canvas.figure.tight_layout()
        # Add spinboxes for MW settings : LO frequency and attenuation
        LO_frequency = QtWidgets.QSpinBox()
        LO_frequency.setRange(2000,18000)
        LO_frequency.setValue(int(rf1_LO/1e6))        
        LO_frequency.setSingleStep(100)
        LO_frequency.setKeyboardTracking(False)
        attenuation = QtWidgets.QSpinBox()
        attenuation.setRange(0,100)
        attenuation.setValue(0)
        self.attenuation = 0
        attenuation.setKeyboardTracking(False)
        self.layout_buttons.addWidget(QtWidgets.QLabel("LO Freq."))
        self.layout_buttons.addWidget(LO_frequency)
        self.layout_buttons.addWidget(QtWidgets.QLabel("MHz"))
        self.layout_buttons.addWidget(QtWidgets.QLabel("Attenuation"))
        self.layout_buttons.addWidget(attenuation)
        self.layout_buttons.addWidget(QtWidgets.QLabel("dB"))
        self.layout_buttons.addStretch()
        LO_frequency.valueChanged.connect(self.update_LO)
        attenuation.valueChanged.connect(self.update_attenuation)
        # Add phase/mag radiobutton
        self.group = QtWidgets.QButtonGroup()
        self.radio_button_mag = QtWidgets.QRadioButton("Mag.")
        self.radio_button_phase = QtWidgets.QRadioButton("Phase")
        self.radio_button_mag.setChecked(True)
        self.layout_buttons.addWidget(self.radio_button_mag)
        self.layout_buttons.addWidget(self.radio_button_phase)
        self.layout_buttons.addStretch()
        self.group.addButton(self.radio_button_mag)
        self.group.addButton(self.radio_button_phase)
        self.radio_button_mag.toggled.connect(self.replot_and_scale)
        # Add autoscale button
        autoscale = QtWidgets.QPushButton('Autoscale')    
        self.layout_buttons.addWidget(autoscale)
        autoscale.clicked.connect(self.autoscale)
        # Add calibration button
        calibrate = QtWidgets.QPushButton('Calibrate')    
        self.layout_buttons.addWidget(calibrate)
        calibrate.clicked.connect(self.calibrate)

    def calibrate(self):
        new_cal = self.S*cal
        np.savez(cal_file,cal=new_cal,pulse_amp=pulse_amp,pulse_len=pulse_len)
        cal[:] = new_cal
                
    def autoscale(self):
        ydata = self.spectrum.get_ydata()
        self.ax.set_ylim(ydata.min()-2,ydata.max()+2)
        self.canvas.draw()

    def update_LO(self, value):
        qm.octave.set_lo_frequency('rf1', value*1e6)
        self.spectrum.set_xdata(value + frequencies/1e6)
        self.ax.set_xlim(value + frequencies[0]/1e6-10, value + frequencies[-1]/1e6+10)
        
    def update_attenuation(self, value):
        self.attenuation = value
        qm.set_io1_value(10**(-value/20))

    def polldata(self):
        # Fetch the data and plot 
        IQ = self.job.result_handles.get("IQ").fetch(1)
        if IQ is None:
            return        
        I = IQ['value_0']
        Q = IQ['value_1']
        self.S = (I+1j*Q)/cal * 10**(self.attenuation/20)
        self.replot()
        self.canvas.draw()
    
    def replot(self):
        if self.radio_button_mag.isChecked():
            self.spectrum.set_ydata(20*np.log10(np.abs(self.S)))
        else:
            self.spectrum.set_ydata(np.angle(self.S)/np.pi*180)
            
    def replot_and_scale(self):
        self.replot()
        if self.radio_button_mag.isChecked():
            self.ax.set_ylabel('Transmission (dB)')
        else:
            self.ax.set_ylabel('Phase (deg)')
        self.autoscale()
        

#######################
# Execute the program #
#######################
job = qm.execute(prog)
qm.set_io1_value(1.0)
window = myLivePlot(job)
window.show()
