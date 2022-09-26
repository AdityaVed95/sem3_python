class Scope:

    def __init__(self, x, y, z):
        self.__privates = x
        self._protecteds = y
        self.publics = z

    def display(self):
        print(self.publics)
        print(self.__privates)
        print(self._protecteds)
        print(self._Scope__privates)


s1 = Scope(1, 2, 3)

print(s1.publics)
print(s1._protecteds)  # gives weak warning but runs
print(s1._Scope__privates)  # gives weak warning but runs # this is the way of accessing a private
# variable : instancename._classname.__variablename

# this is wrong syntax : we don't access protected variable like this : print(s1._Scope_protecteds)

# print(s1.privates)  # gives error on running

s1.display()
