# Pyster - a python unit testing library

pyster is an easy to use python unit tester. The main idea behind it is to provide
a user friendly unit testing library for python. The library offers three different
kind of testing types however each of the types can output the same message, statistic.
The only difference is the way of implementation.

## 1. Class based unit testing

```py
import pyster

class FooBar(parent, pyster.Test):
    def __init__(self) -> None:
        pass
    def my_test(self):
        """Testing an obvious thing with classes"""
        assert "Hello World" == self.static()
    
    @staticmethod
    def non_tested():
        return "Hello World"

pyster.run()
```

Note that static methods won't be tested at all. They are used to provide extra functionality for other methods like the above example:
the non-tested static method only returns a string thus creating a cleaner code. Note that the methods of the parent class(es) won't run.
Also note that any other functions which is outside of a class with the parent `Test` won't be tested. The only function which you can't use is
the _run. The function shouldn't be overwritten. If you try so, you will get an exception

## 2. Wrapper based unit testing

```py
import pyster

@pyster.wrapper
def test():
    """Testing an obvious thing with wrapper"""
    assert True == True

```

This approach looks much simpler than the first one. Why should you still use the class based unit testing? Well you can use inheritance, which is a great thing in python. Also it makes your code much more readable since you can structure each "unit" into different classes. The wrapper
tests are easy to use but it might get too complicated after a while.

## 3. Terminal based unit testing

```py
def test():
    """Testing an obvious thing with terminal"""
    assert True == True
```

> py pyster.py -run

This will import the file and get all of its functions. Then pyster will run all of the functions. This is the most simple solution, although you can't write "clean code" with this approach. You can only have "testable" functions. Functions which are only for helping you divide tasks into smaller ones shouldn't exist in this approach.
