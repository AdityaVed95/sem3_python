import json

f = open("json_check_write", "r")
json_object = f.read()
python_object = json.loads(json_object)
print(python_object)
