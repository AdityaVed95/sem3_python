import re

# ^ is used to check if a string is starting with a substring or not


str1 = "This is heman , he is very powerful"
str2 = "This is Heman , He is very powerful"

# both the above strings not starting with He or he

result = re.findall(r'^He', str1)
result2 = re.findall(r'^He', str2)

print(result)
print(result2)

str3 = "Heman on the run"

res1 = re.search(r'^He', str3)
res2 = re.search(r'^he', str3)

if res1:
    print("res1 : ", res1.group())
if res2:
    print("res2 : ", res2.group())
