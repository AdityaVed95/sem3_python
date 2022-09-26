import re

str1 = "Aditya Ved: 7045733241"

result = re.findall(r'\d+', str1)
print("Phone number is : ")

for i in result:
    print(i)

result2 = re.search(r'\D+', str1)
print(result2.group())
