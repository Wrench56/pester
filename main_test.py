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
style = pyster.Style(style_dict={
    "passed_message": "PASSED",
    "failed_message": "FAILED"
})

@pyster.wrapper(endreport=report, style=style)
def test():
    """Testing an obvious thing with wrapper"""
    assert False == False

@pyster.wrapper(endreport=report, style=style)
def x():
    """Testing an obvious thing with wrapper"""
    assert False == False

print(report.data)


