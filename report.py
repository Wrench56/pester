class Report():
    def __init__(self, func) -> None:
        self.report(func)

    def report(self, func):
        try:
            if func.__doc__:
                print(func.__doc__)
            func()
            print("[+] Passed")
        except AssertionError:
            print("[-] Failed")