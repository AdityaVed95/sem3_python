# when we want to create an another class which is similar to the class already created then
# we should not create another class, we can rather import the existing class and use it in a new
# file/module

class Teacher:
    def setid(self, id):
        self.id = id

    def getid(self):
        return self.id

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    # differnece is below

    def setsalary(self, salary):
        self.salary = salary

    def getsalary(self):
        return self.salary
