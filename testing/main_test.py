import pyster as pyster
from experiment import bar
import time

style = pyster.Style(style_dict={
    "measure_time": False
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

#pyster.run(style=style)


#report = pyster.EndReport()

@pyster.wrapper
def test():
    """Testing an obvious thing with wrapper"""
    #time.sleep(1.0)
    assert False == False

@pyster.wrapper
def x():
    """Testing an obvious thing with wrapper"""
    print("DEBUG TEST!")
    time.sleep(3.0)
    ad = []
    ad[1]
    assert True == False

@pyster.wrapper
def y():
    """Testing an obvious thing with wrapper"""
    print("Init...")
    print("Done!")
    time.sleep(3.0)
    assert False == False


 #print(report.print_data())