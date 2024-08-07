class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    @classmethod
    def delete_instances_for_type(mcs, type_to_delete: type):
        if type_to_delete in mcs._instances:
            inst = mcs._instances.pop(type_to_delete)  # noqa
            del inst
