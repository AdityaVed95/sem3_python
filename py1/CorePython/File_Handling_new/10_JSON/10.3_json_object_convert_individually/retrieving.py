import json

f = open("store_here_new", "r")
employee1_dict_json_object = f.read()
f.close()
employee1_dict_python_object = json.loads(employee1_dict_json_object)
for key in employee1_dict_python_object:
    print(key, end="  ::  ")
    print(employee1_dict_python_object[key])
