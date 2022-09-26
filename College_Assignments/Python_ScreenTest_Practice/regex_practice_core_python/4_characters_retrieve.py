import re
str = "one two three four five six seven eigth nine ten"
result = re.findall(r'\b\w{4}\b',str)
print(result)
