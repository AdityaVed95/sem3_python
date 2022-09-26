import pickle
from employee import Emp

f = open('employee.2.dat', 'rb')

obj = pickle.load(f)
obj.display()
