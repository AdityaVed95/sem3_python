import re

txt = "The rain in Spain"
x = re.search(r"\s", txt)
print(x.group())
print("The first white-space character is located in position:", x.start())
print("The last white-space character is located in position:", x.end())
