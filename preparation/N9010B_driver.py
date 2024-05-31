class CommandAccumulator:

    def __init__(self, sa):
        self._sa = sa

    def __enter__(self):
        self._cmds = None
        self._sa._accumulator = self

    def __exit__(self, exception_type, exception_value, traceback):
        if self._cmds is not None:
            self._sa.sa.write(self._cmds)

        self._sa._accumulator = None

    def accumulate(self, cmd):
        if self._cmds is None:
            self._cmds = cmd
        
        else:
            self._cmds += f"; {cmd}"

class KeysightXSeries:
    def __init__(self, sa):
        self.sa = sa
        self._accumulator = None


    def write(self, cmd):
        if self._accumulator:
            self._accumulator.accumulate(cmd)
        else:
            self.sa.write(cmd)

    def batch(self):
        return CommandAccumulator(self)

    def get_amp(self):
        self.get_single_trigger()
        if self.method == 1:  # Channel power
            sig = self.get_measurement_data()
        elif self.method == 2:  # Marker
            sig = self.query_marker(1)
        else:
            sig = float("NaN")
        return sig

    def set_automatic_video_bandwidth(self, state: int):
        # State should be 1 or 0
        self.write(f":SENS:BAND:VID:AUTO {int(state)}")

    def set_automatic_bandwidth(self, state: int):
        # State should be 1 or 0
        self.write(f":SENS:BAND:AUTO {int(state)}")

    def set_bandwidth(self, bw: int):
        # Sets the bandwidth
        self.write(f":SENS:BAND {int(bw)}")

    def set_video_bandwidth(self, bw: int):
        # Sets the bandwidth
        self.write(f":SENS:BAND:VID {int(bw)}")

    def set_sweep_points(self, n_points: int):
        # Sets the number of points for a sweep
        self.write(f":SENS:SWE:POIN {int(n_points)}")

    def set_sweep_time(self, value):
        self.write(f":SENS:SWE:TIME {value} s")

    def set_center_freq(self, freq: int):
        # Sets the central frequency
        self.write(f":SENS:FREQ:CENT {int(freq)}")

    def set_span(self, span: int):
        # Sets the span
        self.write(f":SENS:FREQ:SPAN {int(span)}")

    def set_cont_off(self):
        return self.sa.query("INIT:CONT OFF;*OPC?")

    def set_cont_on(self):
        # Sets continuous mode on
        return self.sa.query("INIT:CONT ON;*OPC?")

    def get_single_trigger(self):
        # Performs a single sweep
        return self.sa.query("INIT:IMM;*OPC?")

    def active_marker(self, marker: int):
        # Active the given marker
        self.write(f"CALC:MARK{int(marker)}:MODE POS")

    def set_marker_freq(self, marker: int, freq: int):
        # Sets the marker's frequency
        self.get_single_trigger()
        self.write(f"CALC:MARK{int(marker)}:X {int(freq)}")

    def query_marker(self, marker: int):
        # Query the marker
        return float(self.sa.query(f"CALC:MARK{int(marker)}:Y?"))

    def get_full_trace(self):
        # Returns the full trace
        ff_SA_Trace_Data = self.sa.query("TRACE:DATA? TRACE1")
        # Data from the Keysight comes out as a string separated by ',':
        # '-1.97854112E+01,-3.97854112E+01,-2.97454112E+01,-4.92543112E+01,-5.17254112E+01,-1.91254112E+01...\n'
        # The code below turns it into an a python list of floats

        # Use split to turn long string to an array of values
        ff_SA_Trace_Data_Array = ff_SA_Trace_Data.split(",")
        amp = [float(i) for i in ff_SA_Trace_Data_Array]
        return amp

    def enable_measurement(self):
        # Sets the measurement to channel power
        self.write(":CONF:CHP")

    def disables_measurement(self):
        # Sets the measurement to none
        self.write(":CONF:CHP NONE")

    def sets_measurement_integration_bw(self, ibw: int):
        # Sets the measurement integration bandwidth
        self.write(f":SENS:CHP:BAND:INT {int(ibw)}")

    def disables_measurement_averaging(self):
        # disables averaging in the measurement
        self.write(":SENS:CHP:AVER 0")

    def set_mode_preset(self):
        # disables averaging in the measurement
        self.write("SYST:PRES:FULL")

    def get_measurement_data(self):
        # Returns the result of the measurement
        return float(self.sa.query("READ:CHP?").split(",")[0])
        # Data from the Keysight comes out as a string separated by ',':
        # '-1.97854112E+01,-3.97854112E+01\n'
        # The code above takes the first value and converts to float.

    def set_peak_th(self, peak: int):
        self.write(f"CALC:MARK:PEAK:THR {int(peak)}")
        # sets the peak TH value

    def set_ref_value(self, ref: int):
        self.write(f":DISP:WIND:TRAC:Y:RLEV {int(ref)}")
        # sets the peak TH value

    def get_peak_table(self):
        # get peak tables
        peak_table = self.sa.query(":TRAC:MATH:PEAK?")
        peak_table_Array = peak_table.split(",")
        peaks = [float(i) for i in peak_table_Array]
        return peaks