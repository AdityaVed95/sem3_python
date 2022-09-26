import re
from pprint import pprint as pp

str1 = """
Rahul got 75 marks
Ram got 85 marks
Karan got 95 marks
Mohan got 50 marks
"""

print(str1)

result1 = re.findall(r'[A-Z][a-z]*', str1)
result2 = re.findall(r'\b\d{1,2}\b', str1)

for (i, j) in zip(result1, result2):
    print(i + ": " + str(j))
