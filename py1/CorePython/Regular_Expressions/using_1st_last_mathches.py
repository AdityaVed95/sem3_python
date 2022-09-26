import re

str1 = "one two three"

result = re.findall(r'\bt[\w]*\Z', str1)
print(result)

str2 = "three one two"
result2 = re.findall(r'\At[\w]*', str2)
print(result2)

# \Z is at the end of the regular expression
# \A is at the start of the regular expression
