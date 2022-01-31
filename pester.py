import inspect
from errors import non_overridable_error as nomo


if __name__ == "__main__":
    module = __import__("main_test", globals(), locals())
    for tpl in inspect.getmembers(module, inspect.isfunction):
        func = tpl[1]
        Report(func)

        
        
