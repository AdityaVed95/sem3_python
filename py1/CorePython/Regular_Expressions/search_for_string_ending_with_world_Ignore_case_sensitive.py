import re

str1 = "Hello to this World!"

res1 = re.search(r'world!$', str1)

if res1:
    print("res1 : string ends with : ", res1.group())

res2 = re.search(r'world!$', str1, re.IGNORECASE)

if res2:
    print("res2 : string ends with: ", res2.group())
