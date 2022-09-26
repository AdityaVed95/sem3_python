class Student:
    def setid(self,id):
        self.id = id

    def getid(self):
        return self.id

    def setname(self,name):
        self.name = name

    def getname(self):
        return self.name

    # difference is below
    def setmarks(self, marks):
        self.marks = marks

    def getmarks(self):
        return self.marks


# note : most of the code in teacher.py is the same as the code in student.py
# thus reuse the already existing code
# let Teacher class be the Base class and the Student class be the sub class
# syntax is :: class Subclass(Baseclass):
# or :: class Derivedclass(Superclass):


# thus create Student class from the Teacher class : this is called inheritance


