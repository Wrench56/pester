import inspect
import sys
from report import Report
from test_class import Test

def test_units():
    
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
