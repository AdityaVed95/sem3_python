from employee import Emp
import json

id = "100"
name = "Aditya"
sal = "100000000"

employee1_python_object = Emp(id, name, sal)

f = open("store_here_new", "w")
#
# employee1_json_object_of_id = json.dumps(employee1_python_object.id)
# employee1_json_object_of_name = json.dumps(employee1_python_object.name)
# employee1_json_object_of_sal = json.dumps(employee1_python_object.sal)
#
# f.write(employee1_json_object_of_id)
# f.write(employee1_json_object_of_name)
# f.write(employee1_json_object_of_sal)

employee1_dict_python_object = {"id": employee1_python_object.id, "name": employee1_python_object.name,
                                "sal": employee1_python_object.sal}
employee1_dict_json_object = json.dumps(employee1_dict_python_object)

f.write(employee1_dict_json_object)
