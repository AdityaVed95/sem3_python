import re

regex1 = r'm\w\w'
prog = re.compile(regex1)
print(prog)

# regex1 is the regular expression , prog is an object that contains regular expression
str1 = 'cat bat mat rat'
result = prog.search(str1)
print(result)
print(result.group())

str2 = "Operating System format"
result2 = prog.search(str2)
print(result2.group())
