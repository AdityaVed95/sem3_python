import re
str1 = "an apple a day keeps a doctor away"

result = re.findall(r'\ba[\w]*\b',str1)
print(result)
