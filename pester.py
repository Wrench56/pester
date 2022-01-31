import inspect
import sys
import typing, types
from errors import NonOverridableMethodOverride as nomo

class NonOverridable(type):
    def __new__(self, name, bases, dct):
        if bases and "_run" in dct:
            raise nomo.NonOverridableMethodOverride("Overriding _run is not allowed")
        return type.__new__(self, name, bases, dct)

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

class Report():
    def __init__(self, func) -> None:
        self.report(func)

    def report(self, func):
        try:
            if func.__doc__:
                print(func.__doc__)
            func()
            print("[+] Passed")
        except AssertionError:
            print("[-] Failed")

class Statistics():
    def __init__(self) -> None:
        pass



def main():
    
    # The module from where the main is called from
    module = inspect.getmodule(inspect.stack()[1][0])
    all_classes = (obj for name, obj in inspect.getmembers(sys.modules[module.__name__], inspect.isclass)
          if obj.__module__ is module.__name__)
    for class_ in all_classes:
        for parent in class_.__mro__:
            if parent == Test:
                test_instance = class_()
                test_instance._run(class_)


def wrapper(func):
    Report(func)




if __name__ == "__main__":
    module = __import__("main_test", globals(), locals())
    for tpl in inspect.getmembers(module, inspect.isfunction):
        func = tpl[1]
        Report(func)

        
        
