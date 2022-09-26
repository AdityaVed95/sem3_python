# note that : employee.2.dat file contains the binary file with utf-16 encoding
# if we try unpickling from employee.2.dat , then it is not working
# but when we store the object in utf-8 format : in the employee.dat file
# and now when we unpickle then it works

class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def display(self):
        print("{} : {} : {}".format(self.id, self.name, self.sal))
