from employee_new import Emp
import json

id = "100"
name = "Aditya"
sal = "100000000"

employee1_python_object = Emp(id, name, sal)

f = open("store_here", "w")

employee1_json_object = json.dumps(employee1_python_object)
f.write(employee1_json_object)
f.close()
