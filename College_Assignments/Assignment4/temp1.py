import re

substring = "hello"
string_main = "This is hello!"
print(re.search(substring, string_main))
print(re.match(substring, string_main))
