class QmOctaveException(Exception):
    pass


class ConflictException(QmOctaveException):
    pass


class InternalShareConflictException(ConflictException):
    pass


class InternalExternalOverrideException(ConflictException):
    pass


class CouplingConflictException(ConflictException):
    pass


class LoopbackInternalShareConflictException(ConflictException):
    pass
