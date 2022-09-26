import json

python_object = {"hello": 1, "there": 3, "now": 4}
json_object = json.dumps(python_object)
print(json_object)

f = open("json_check_write", "w")
f.write(json_object)
f.close()
