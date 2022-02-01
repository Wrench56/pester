import pyster
from experiment import bar

class FooBar(bar.Bar, pyster.Test):
    def __init__(self) -> None:
        super().__init__()
    def my_test(self):
        """Testing an obvious thing with classes"""
        assert "Hello World" == self.static()
    
    @staticmethod
    def non_tested():
        return "Hello World"

#pyster.run()


report = pyster.EndReport()
@pyster.wrapper(endreport=report)


def test():
    """Testing an obvious thing with wrapper"""
    assert False == False

@pyster.wrapper(endreport=report)
def x():
    """Testing an obvious thing with CLI pyster tool"""
    assert False == False

print(report.data)

