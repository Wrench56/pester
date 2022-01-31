from errors import non_overridable_error as nomo

class NonOverridable(type):
    def __new__(self, name, bases, dct):
        if bases and "_run" in dct:
            raise nomo.NonOverridableError("Overriding _run is not allowed")
        return type.__new__(self, name, bases, dct)