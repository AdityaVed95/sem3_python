import re

str1 = "anant akhil abhi arun arati ananya akhilesh an ak"

result = re.findall(r'a[nk][\w]*', str1)
print(result)

result2 = re.findall(r'a[nk][\w]+', str1)
print(result2)

# * : 0 or more repetitions of the preceding regexp
# + : 1 or more repetitions of the preceding regexp
# a[nk] represents : a is the 1st letter and then after a, we have n or k
