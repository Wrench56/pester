class _EndReport():
    def __init__(self) -> None:
        self.use = False
        self.data = {}

    def add_time(self, name, time):
        self.check_entry(name)
        self.data[name]["time"] = time
        
    
    def add_status(self, name, pass_):
        self.check_entry(name)
        self.data[name]["pass"] = pass_

    def print_data(self):
        if self.use:
            print(self.data)
        
    def check_entry(self, name):
        if name in self.data:
            return True
        else:
            self.data[name] = {}
            return False

# create global object
Endreport = _EndReport()
