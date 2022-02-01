import inspect
from errors import non_overridable_error as nomo
import timeit
import types
import typing
import sys


class Style():
    DEFAULT_STYLE = {
        "print_doc": True,
        "measure_time": True,
        "passed_message": "[+] Passed",
        "failed_message": "[-] Failed",
        "runtime_message": "The function ran in => %s <="

    }
    def __init__(self, style_dict={}, **kwargs):
        self.style = {}
        self.style.update(self.DEFAULT_STYLE)

        # Either use the style_dict or kwargs! BUT not both
        if style_dict != {}:
            self.style.update(style_dict)
        elif kwargs != {}:
            self.style.update(style_dict)
    
    def get(self, field) -> object:
        return self.style.get(field)

    def print_runtime(self, time):
        time = round(time, 4)
        if float(time) > 1 and float(time) < 2:
            time = f"{time:.4f}sec"
        elif float(time) > 2:
            time = f"{time:.4f}secs"
        else:
            time = f"{time:.4f}ms"
        print(self.get("runtime_message")%time)

    def print_doc(self, str_):
        """ Print the __doc__ of the test. (In pyster its used for describing the task)"""
        print(str_)
    
    def print_passed(self):
        print(self.get("passed_message"))

    def print_failed(self):
        print(self.get("failed_message"))


class NonOverridable(type):
    def __new__(self, name, bases, dct):
        if bases and "_run" in dct:
            raise nomo.NonOverridableError("Overriding _run is not allowed")
        return type.__new__(self, name, bases, dct)
class Test(metaclass=NonOverridable):
    def __init__(self) -> None:
        pass

    def _run(self, class_, style) -> None:
        methods = [x for x, y in class_.__dict__.items() if isinstance(y, (types.FunctionType))]
        
        #methods = [getattr(self, m) for m in dir(self) if not m.startswith('__') and not m.startswith("run")]
        for method_str in methods:
            if not method_str.startswith("__") and not method_str.endswith("__"):
                method = getattr(self, method_str)
                if isinstance(method, typing.Callable):
                    #print(f"Calling method {method.__name__}()")
                    Report(method, style=style)

class Report():
    def __init__(self, func, endreport=None, style=None) -> None:
        if style != None:
            self.style = style
        else:
            self.style = Style()
        self.endreport = endreport
        self.report(func)

    def report(self, func):
        try:
            if self.style.get("print_doc") and func.__doc__:
                self.style.print_doc(func.__doc__)
            
            if self.endreport:
                time = timeit.timeit(stmt = func)
                self.endreport.add_time(func.__name__, time)
                if self.style.get("measure_time"):
                    self.style.print_runtime(time) # Execution time actually
            else:
                if self.style.get("measure_time"):
                    time = timeit.timeit(stmt = func)
                    self.style.print_runtime(time) # Execution time actually
                else:
                    func()

            self.style.print_passed()
        except AssertionError:
            self.style.print_failed()

class EndReport():
    def __init__(self) -> None:
        self.data = {}

    def add_time(self, name, time):
        if name in self.data:
            self.data[name]["time"] = time
        else:
            self.data[name] = {}
            self.data[name]["time"] = time

def run(style=None) -> None:
    if style != None:
        custom_style = style
    else:
        custom_style = Style()

    # The module from where the main is called from
    module = inspect.getmodule(inspect.stack()[1][0])
    all_classes = (obj for name, obj in inspect.getmembers(sys.modules[module.__name__], inspect.isclass)
          if obj.__module__ is module.__name__)
    for class_ in all_classes:
        for parent in class_.__mro__:
            if parent == Test:
                test_instance = class_()
                test_instance._run(class_, style=custom_style)



def wrapper(*args, **kwargs):
    if "endreport" in kwargs:
        endreport_obj = kwargs["endreport"]
        def inner(func):
            Report(func, endreport=endreport_obj, style=kwargs.get("style"))
        return inner
    else:
        Report(args[0], style=kwargs.get("style"))
    





if __name__ == "__main__":
    # Create custom style from input params
    custom_style = Style()
    module = __import__("main_test", globals(), locals())
    for tpl in inspect.getmembers(module, inspect.isfunction):
        func = tpl[1]
        Report(func, style=custom_style) 
        
