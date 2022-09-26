import re

string1 = "aditya.ved@somaiya.edu"
result = re.split(r'\W+', string1)
print(result)

result2 = re.sub(r'\W+', " go ", string1)
print(string1)
print(result2)
