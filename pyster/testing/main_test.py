import pyster
from experiment import bar
import time

style = pyster.Style(style_dict={
    "measure_time": False
})

class FooBar(bar.Bar, pyster.Test):
    def __init__(self) -> None:
        super().__init__()
    
    @pyster.ignore
    def non_tested(self):
        return "Hello World"
    
    def my_test(self):
        """Testing an obvious thing with classes"""
        assert "Hello World" == self.non_tested()

pyster.run(style=style)


@pyster.wrapper(style=style)
def test():
    """Testing an obvious thing with wrapper 1"""
    #time.sleep(1.0)
    assert False == False

@pyster.wrapper
def x():
    """Testing an obvious thing with wrapper 2"""
    print("DEBUG TEST!")
    time.sleep(3.0)
    assert True == False

@pyster.wrapper
def y():
    """Testing an obvious thing with wrapper 3"""
    print("Init...")
    print("Done!")
    time.sleep(3.0)
    assert False == False