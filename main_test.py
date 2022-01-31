import pester
from experiment import bar
import types
class FooBar(bar.Bar, pester.Test):
    def __init__(self) -> None:
        super().__init__()
    def my_test(self):
        """Testing an obvious thing with classes"""
        assert "Hello World" == self.static()
    
    @staticmethod
    def non_tested():
        return "Hello World"

pester.main()


#@pester.wrapper
def test():
    """Testing an obvious thing with wrapper"""
    assert False == False


def x():
    """Testing an obvious thing with CLI pester tool"""
    assert False == False


