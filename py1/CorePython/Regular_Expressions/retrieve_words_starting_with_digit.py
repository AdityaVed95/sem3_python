import re

str1 = "Meeting at 1st and 21st of this month"

result = re.findall(r'\d[\w]*', str1)

for i in result:
    print(i)
