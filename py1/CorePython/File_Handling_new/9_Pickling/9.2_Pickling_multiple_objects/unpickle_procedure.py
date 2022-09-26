import pickle
from student import Student

f = open('student.dat', 'rb')
obj1 = pickle.load(f)
obj2 = pickle.load(f)

obj1.displaying()
obj2.displaying()

obj3 = pickle.load(f)
