class _EndReport():
    def __init__(self) -> None:
        self.use = False
        self.data = {}

    def add_time(self, name, time):
        if name in self.data:
            self.data[name]["time"] = time
        else:
            self.data[name] = {}
            self.data[name]["time"] = time
    
    def print_data(self):
        if self.use:
            print(self.data)

# create global object
Endreport = _EndReport()
