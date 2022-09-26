import json

python_object_list1 = ["hello", "there"]
json_object_list1 = json.dumps(python_object_list1)

f = open("store_here_now", "w")
f.write(json_object_list1)
f.close()
