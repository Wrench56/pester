import pester
from experiment import bar

class FooBar(bar.Bar, pester.Test):
    def __init__(self) -> None:
        super().__init__()
    def my_test(self):
        """Testing an obvious thing with classes"""
        assert "Hello World" == self.static()
    
    @staticmethod
    def static():
        return "Hello World"

#pester.run()

report = pester.EndReport()
@pester.wrapper(endreport=report)
def test():
    """Testing an obvious thing with wrapper"""
    assert False == False

@pester.wrapper(endreport=report)
def x():
    """Testing an obvious thing with CLI pester tool"""
    assert False == False

print(report.data)