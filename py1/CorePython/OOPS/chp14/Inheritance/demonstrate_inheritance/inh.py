from student import Student

s = Student()

s.setid(10)
s.setname("Aditya")
s.setmarks(100)

x = s.getid()
y = s.getname()
z = s.getmarks()



s.setsalary(1000) # what if we dont want to do this : is there a way to not let s.setsalary() happen
sal = s.getsalary()


print("x: {}  y: {}    z: {}".format(x, y, z))
print("salary is : ", sal)
