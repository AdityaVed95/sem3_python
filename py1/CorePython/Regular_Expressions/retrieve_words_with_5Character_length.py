import re

str1 = "Hello aditya Ved 55555 chara lengt lon is it nows"
result = re.findall(r'\b\w{5}\b', str1)

for i in result:
    print(i)

print("----------------------")
result2 = re.search(r'\b\w{5}\b', str1)
print(result2.group())
