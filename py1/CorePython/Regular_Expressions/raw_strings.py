str1 = 'This is a normal\nstring'
str2 = r'This is a raw\nstring'
print(str1)
print(str2)

# regular expressions are strings containing special symbols and characters
# regular expression are called as regex
# regex are generally written as raw strings

regex1 = r'm\w\w'  # preferred method
regex2 = 'm\\w\\w'  # alternative to using raw strings
print(regex1)
print(regex2)
print(regex1 == regex2)

# in regex1 :
# character m represents that