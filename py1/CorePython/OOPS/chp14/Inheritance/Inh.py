from teacher import Teacher
obj = Teacher() # object of Teacher class

obj.setid(10)
inh_identity = obj.getid()
obj.setname("Aditya")
inh_name = obj.getname()

print(inh_name)
print(inh_identity)

