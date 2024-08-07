from qm._loc import _get_loc


class DigitalMeasureProcess(object):
    def __init__(self, loc: str):
        self.loc = _get_loc()


class RawTimeTagging(DigitalMeasureProcess):
    def __init__(self, loc: str, element_output: str, target, targetLen, max_time):
        super(RawTimeTagging, self).__init__(loc)
        self.element_output = element_output
        self.target = target
        self.targetLen = targetLen
        self.max_time = max_time


class Counting(DigitalMeasureProcess):
    def __init__(self, loc: str, element_outputs, target, max_time):
        super(Counting, self).__init__(loc)
        self.element_outputs = element_outputs
        self.target = target
        self.max_time = max_time
