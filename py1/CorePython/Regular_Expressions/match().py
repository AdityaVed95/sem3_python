import re

str1 = 'man cat'
str2 = 'cat man'

result1 = re.match(r'm\w\w', str1)
result2 = re.match(r'm\w\w', str2)

if result1:
    print(result1.group())
else:
    print(None)

if result2:
    print(result2.group())
else:
    print(None)
