class State:
    def __init__(self) -> None:
        self.current_test = None
        self.tests = []

    def count_tests(self):
        pass

    @current_test.setter
    def current_test(self, inp):
        self.tests.pop(self.tests.index(self.current_test)) # Deleting element which already was
        self.current_test = inp
    
    
