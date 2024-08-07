class ConnectivityException(Exception):
    pass


class InvalidIdentityException(ConnectivityException):
    pass


class LoopbackConfigException(ConnectivityException):
    pass


class ExploreResponseException(ConnectivityException):
    pass


class RfSourceTypeException(ConnectivityException):
    pass


class ExternalInputTypeException(ConnectivityException):
    pass


class LoSourceValueException(ConnectivityException):
    pass
