from student import Student

import pickle

f = open("student.dat", 'wb')
roll_number1 = 8
name1 = "Aditya"
marks1 = 100

roll_number2 = 12
name2 = "Unknown"
marks2 = 80

student1 = Student(roll_number1, name1, marks1)
student2 = Student(roll_number2, name2, marks2)

pickle.dump(student1, f)
pickle.dump(student2, f)

f.close()
