import re

str1 = "this is my 1 and only 1 day 2 live 4 ever 10 100 1000 any length number"

result = re.findall(r'\b\d{2}\b', str1)

for i in result:
    print(i)
