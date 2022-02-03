import pyster
from experiment import bar


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

pyster.run(style=style)


report = pyster.EndReport()

@pyster.wrapper(endreport=report)
def test():
    """Testing an obvious thing with wrapper"""
    assert False == False

@pyster.wrapper(endreport=report)
def x():
    """Testing an obvious thing with wrapper"""
    assert True == False

print(report.data)


