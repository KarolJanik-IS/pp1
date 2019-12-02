#7
class University():
    def __init__(self):
        self.name = "UEK"
        self.fullname = "Uniwersytet ekonomiczny"
    def print_name(self):
        print(self.name)
    def set_name(self, new_name):
        self.name = new_name
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self,new_name):
        self.fullname = new_name
test = University()
test.print_name()
test.set_name("AGH")
test.print_name()
test.print_fullname()
test.set_fullname("Akademia Górniczo-Hutnicza")
test.print_fullname()