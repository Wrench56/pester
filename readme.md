# Pyster - a python unit testing library

Pyster is an easy to use python unit tester. The main idea behind it is to provide
a user friendly unit testing library for python. The library offers two different
kind of testing types however both of the types offer the same functionality.
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

## Using Style to create custom outputs

Pyster gives you the opportunity to use custom styles. Using styles is mandatory but you can greatly customize your output.
I do recommend taking a look how they look like, but using the default style is also a good practice.

### Creating a style instance

Style instances are only needed for the wrapper and class based unit testing. When you use the terminal to do testing, you can define your custom style with switches and arguments. Generally it is harder to use the terminal based styling.\

With that said let's see how the Style class looks like

```py
class Style():
    DEFAULT_STYLE = {
        "passed_message": "[+] Passed",
        "failed_message": "[-] Failed",
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

    def print_passed(self):
        print(self.get("passed_message"))

    def print_failed(self):
        print(self.get("failed_message"))
```

(A shortened version of the Style class)\
\
When you create a custom style you can basically rewrite the DEFAULT_STYLE dictionary. If you want to change something in the code part you have to create a child class of Style and use that as the style with overwritten functions. The `get` and `__init__` function mustn't be overwritten.\

### Using styles with wrapper

To use a new style simply use the following syntax:

```py
style = pyster.Style(style_dict={
    "passed_message": "PASSED",
    "failed_message": "FAILED"
})

@pyster.wrapper(style=style)
def test():
    """Testing an obvious thing with wrapper"""
    assert False == False
```

This custom style will overwrite the default message for the `print_passed` and `print_failed`. So in this case, instead of the default `[+] Passed` you will see the following message: `PASSED`.

### Using styles with classes

To use a new style for the unit testing classes use the following syntax:

```py
style = pyster.Style(style_dict={
    "passed_message": "PASSED",
    "failed_message": "FAILED"
})

class FooBar(bar.Bar, pyster.Test):
    def __init__(self) -> None:
        super().__init__()
    def my_test(self):
        """Testing an obvious thing with classes"""
        assert "Hello World" == self.non_tested()
    
    @staticmethod
    def non_tested():
        return "Hello World"

pyster.run(style=style)
```

As with the above example on wrappers, this will result with the output being `PASSED` instead of `[+] Passed`
