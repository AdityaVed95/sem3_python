# use [ ]*.py

# * is used to represent 0 or more repetitions of characters after the required character

import re

str1 = "an An apple a dayss keeps the doctor awayaa"
result = re.findall(r'a[\w]*', str1)

for word in result:
    print(word)

print("---------------------------------------------------------------------")

result2 = re.findall(r'\ba[\w]*\b', str1)
# \b is to represent a space before and after a word

for word in result2:
    print(word)
