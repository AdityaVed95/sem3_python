import re

str1 = "this is it! for now or ne##ver i @m gonn@ livE for e$$v&&"
result = re.split(r'\W+', str1)
print(result)

test = 'hello "core" pythonista\'s '
print(test)

str2 = "Name1 is scam"
result2 = re.sub('Name1', 'Name2', str2)
print(result2)
