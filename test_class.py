from non_overridable import NonOverridable
import typing
import types
from report import Report

class Test(metaclass=NonOverridable):
    def __init__(self) -> None:
        pass

    def _run(self, class_) -> None:
        methods = [x for x, y in class_.__dict__.items() if isinstance(y, (types.FunctionType))]
        
        #methods = [getattr(self, m) for m in dir(self) if not m.startswith('__') and not m.startswith("run")]
        for method_str in methods:
            if not method_str.startswith("__") and not method_str.endswith("__"):
                method = getattr(self, method_str)
                if isinstance(method, typing.Callable):
                    #print(f"Calling method {method.__name__}()")
                    Report(method)