import pickle
from employee import Emp

f = open('employee.dat', 'rb')

obj = pickle.load(f)
obj.display()
f.close()
