from contextlib import contextmanager
from copy import deepcopy


from contextlib import contextmanager

from quam import QuamDict


@contextmanager
def tracked_updates(obj, auto_revert=True):
    """
    A context manager to temporarily update attributes of an object.

    :param obj: The object whose attributes are to be updated.
    :param auto_revert: If True, changes are automatically reverted after context exit.
                        If False, changes remain applied.
    :param unsafe: If True, any __getattr__ actions are allowed no matter the attribute type.
                   If False, __getattr__ actions are assumed to be used in order to set a
                   nested attribute, and if the type is unrecognized, it is skipped.
    """
    # Wrap the object in TrackableObject
    trackable_obj = TrackableObject(obj)

    try:
        # Yield control back with the trackable object
        yield trackable_obj
    finally:
        if auto_revert:
            # Revert any changes made to the attributes, including nested ones
            trackable_obj.revert_changes()
        # If auto_revert is False, changes remain applied


class TrackableObject:
    def __init__(self, obj):
        # Store the original object
        self._obj = obj
        # Store a map of original attribute values
        self._original_values = {}
        # Store a map of temporary attribute values
        self._temp_values = {}
        # Store nested TrackableObjects
        self._nested_trackables = {}

    def __getattr__(self, attr):
        original_attr = getattr(self._obj, attr)
        if attr not in self._nested_trackables:
            self._nested_trackables[attr] = TrackableObject(original_attr)
        return self._nested_trackables[attr]

    def __setattr__(self, attr, value):
        if attr.startswith('_'):
            super().__setattr__(attr, value)
        else:
            if attr not in self._original_values:
                # Store the original value if not already tracked
                self._original_values[attr] = deepcopy(getattr(self._obj, attr))
            # Store the temporary value
            self._temp_values[attr] = value
            setattr(self._obj, attr, value)

    def __getitem__(self, key):
        original_item = self._obj[key]
        if key not in self._nested_trackables:
            # Recursively wrap dicts and objects if not already wrapped
            self._nested_trackables[key] = TrackableObject(original_item)
        return self._nested_trackables[key]

    def __setitem__(self, key, value):
        if key not in self._original_values:
            # Store the original value if not already tracked
            self._original_values[key] = deepcopy(self._obj[key])
        # Store the temporary value
        self._temp_values[key] = value
        self._obj[key] = value

    def revert_changes(self):
        # Revert changes for the current level
        for attr, original_value in self._original_values.items():
            setattr(self._obj, attr, original_value)

        # Recursively revert changes in nested trackables
        for nested_trackable in self._nested_trackables.values():
            nested_trackable.revert_changes()

        # Clear the stored values as changes are reverted
        self._original_values.clear()
        self._temp_values.clear()

    def reapply_changes(self):
        # Re-apply all temporary changes for the current level
        for attr, temp_value in self._temp_values.items():
            setattr(self._obj, attr, temp_value)

        # Recursively re-apply changes in nested trackables
        for nested_trackable in self._nested_trackables.values():
            nested_trackable.reapply_changes()

    def __dir__(self):
        return dir(self._obj)
