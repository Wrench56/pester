import inspect
import sys
import typing, types

class Test():
    def __init__(self) -> None:
        pass

    def run(self):
        methods = [getattr(self, m) for m in dir(self) if not m.startswith('__') and not m.startswith("run")]
        for method in methods:
            if not isinstance(method, types.FunctionType):
                if isinstance(method, typing.Callable):
                    print(f"Calling method {method.__name__}()")
                    if method.__doc__:
                        print(method.__doc__)
                    try:
                        method()
                        print("[+] Passed")
                    except AssertionError:
                        print("[-] Failed")
        

def main():
    
    # The module from where the main is called from
    module = inspect.getmodule(inspect.stack()[1][0])
    all_classes = (obj for name, obj in inspect.getmembers(sys.modules[module.__name__], inspect.isclass)
          if obj.__module__ is module.__name__)
    for class_ in all_classes:
        for parent in class_.__mro__:
            if parent == Test:
                test_instance = class_()
                test_instance.run()


def wrapper(func):
    try:
        if func.__doc__:
            print(func.__doc__)
        func()
        print("[+] Passed")
    except AssertionError:
        print("[-] Failed")



if __name__ == "__main__":
    module = __import__("main_test", globals(), locals())
    for tpl in inspect.getmembers(module, inspect.isfunction):
        func = tpl[1]
        try:
            if func.__doc__:
                print(func.__doc__)
            func()
            print("[+] Passed")
        except AssertionError:
            print("[-] Failed")

        
        
