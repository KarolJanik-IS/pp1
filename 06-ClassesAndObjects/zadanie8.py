#7
class University():
    def __init__(self):
        self.name = "UEK"
    def print_name(self):
        print(self.name)
    def set_name(self, new_name):
        self.name = new_name
test = University()
test.print_name()
test.set_name("AGH")
test.print_name()