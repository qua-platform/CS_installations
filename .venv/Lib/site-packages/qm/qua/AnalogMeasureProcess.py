from qm._loc import _get_loc


class AnalogTimeDivision(object):
    def __init__(self, loc: str):
        self.loc = loc


class SlicedAnalogTimeDivision(AnalogTimeDivision):
    def __init__(self, loc: str, samples_per_chunk: int):
        super(SlicedAnalogTimeDivision, self).__init__(loc)
        self.samples_per_chunk = samples_per_chunk


class AccumulatedAnalogTimeDivision(AnalogTimeDivision):
    def __init__(self, loc: str, samples_per_chunk: int):
        super(AccumulatedAnalogTimeDivision, self).__init__(loc)
        self.samples_per_chunk = samples_per_chunk


class MovingWindowAnalogTimeDivision(AnalogTimeDivision):
    def __init__(self, loc: str, samples_per_chunk: int, chunks_per_window: int):
        super(MovingWindowAnalogTimeDivision, self).__init__(loc)
        self.samples_per_chunk = samples_per_chunk
        self.chunks_per_window = chunks_per_window


class AnalogProcessTarget(object):
    def __init__(self, loc: str):
        self.loc = loc


class ScalarProcessTarget(AnalogProcessTarget):
    def __init__(self, loc: str, target) -> None:
        super().__init__(loc)
        self.target = target


class VectorProcessTarget(AnalogProcessTarget):
    def __init__(self, loc: str, target, time_division: AnalogTimeDivision):
        AnalogProcessTarget.__init__(self, loc)
        self.target = target
        self.time_division = time_division


class AnalogMeasureProcess(object):
    def __init__(self, loc: str):
        self.loc = _get_loc()


class BareIntegration(AnalogMeasureProcess):
    def __init__(self, loc: str, element_output: str, iw: str, target: AnalogProcessTarget):
        super(BareIntegration, self).__init__(loc)
        self.element_output = element_output
        self.iw = iw
        self.target = target


class DualBareIntegration(AnalogMeasureProcess):
    def __init__(
        self,
        loc: str,
        element_output1: str,
        element_output2: str,
        iw1: str,
        iw2: str,
        target: AnalogProcessTarget,
    ):
        super(DualBareIntegration, self).__init__(loc)
        self.element_output1 = element_output1
        self.element_output2 = element_output2
        self.iw1 = iw1
        self.iw2 = iw2
        self.target = target


class DemodIntegration(AnalogMeasureProcess):
    def __init__(self, loc: str, element_output: str, iw: str, target: AnalogProcessTarget):
        super(DemodIntegration, self).__init__(loc)
        self.element_output = element_output
        self.iw = iw
        self.target = target


class DualDemodIntegration(AnalogMeasureProcess):
    def __init__(
        self,
        loc: str,
        element_output1: str,
        element_output2: str,
        iw1: str,
        iw2: str,
        target: AnalogProcessTarget,
    ):
        super(DualDemodIntegration, self).__init__(loc)
        self.element_output1 = element_output1
        self.element_output2 = element_output2
        self.iw1 = iw1
        self.iw2 = iw2
        self.target = target


class RawTimeTagging(AnalogMeasureProcess):
    def __init__(self, loc: str, element_output: str, target, targetLen, max_time):
        super(RawTimeTagging, self).__init__(loc)
        self.element_output = element_output
        self.target = target
        self.targetLen = targetLen
        self.max_time = max_time


class HighResTimeTagging(AnalogMeasureProcess):
    def __init__(self, loc: str, element_output: str, target, targetLen, max_time):
        super(HighResTimeTagging, self).__init__(loc)
        self.element_output = element_output
        self.target = target
        self.targetLen = targetLen
        self.max_time = max_time
