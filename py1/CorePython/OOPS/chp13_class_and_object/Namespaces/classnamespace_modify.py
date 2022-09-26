# refer fig 1.1 and fig 1.2

class Student:
    n = 10


print(Student.n)  # accessing class variable without creating an instance of the class

s1 = Student()
print(s1.n)  # accessing class variable from the instance namespace
Student.n += 1  # modifying class variable from class namespace

# class variable is modified :
print(Student.n)
print(s1.n)
