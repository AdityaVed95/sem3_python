import re

str1 = "one two three four five six seven eight nine ten eleven on I kingisit "

result1 = re.findall(r'\b\w{3,5}\b', str1)

for i in result1:
    print(i)

# print words with length 3 or 4 or 5
