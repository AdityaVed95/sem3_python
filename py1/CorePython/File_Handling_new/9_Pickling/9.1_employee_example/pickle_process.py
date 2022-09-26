from employee import Emp
import pickle

f = open("employee.dat", "wb")

id = "100"
name = "Aditya"
sal = "100000000"

employee1 = Emp(id, name, sal)
pickle.dump(employee1, f)

f.close()
