import re

regex1 = r' m\w\w'
prog1 = re.compile(regex1)
str1 = "sat cat format"
result1 = prog1.search(str1)
print(result1)

if result1:
    print(result1.group())
