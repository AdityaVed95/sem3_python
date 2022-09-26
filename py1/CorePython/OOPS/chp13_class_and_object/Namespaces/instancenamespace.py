class Student:
    n = 10


s1 = Student()
print("instance namespace of s1 before modification : ", s1.n)
s1.n += 1  # trying to modify from instance namespace , but s1.n doesnt remain class variable
print("instance namespace of s1 after modification :", s1.n)

s2 = Student()
print("instance namespace of s2 remains unchanged : ", s2.n)
print("Class namespace remains unchanged :", Student.n)

print("id of s1.n : ", id(s1.n))
print("id of s2.n : ", id(s2.n))
print("id of Student.n : ", id(Student.n))

# thus, s1.n is no longer a class variable
# refer onenote ss of debugger
