import re

str1 = "Hello aditya Ved 55555 chara lengt lon is it nows"
result = re.findall(r'\b\w{4,}\b', str1)

for i in result:
    print(i)
