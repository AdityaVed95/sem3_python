import re

str1 = "cat mat bat rat format mop"

result = re.search(r'm\w\w', str1)
# above line is compiling and searching in one line : above line is equivalent to :
# prog1 = re.compile(r'm\w\w')
# result = prog1.search(str1)

# result - re.search('expression', 'string')

if result:  # if result is not None
    print(result.group())

# result will be None when the entire str1 didn't contain the regular expression we
# are searching for

# search method only gives 1st occurrence of regex but to get all of them use findall()
# method

# findall method returns the result as a list
# no need to do result.group() while using findall()

str2 = "man sum mop run formats mam mom mon meme mal"
result2 = re.findall(r'm\w\w', str2)
print(result2)

for i in result2:
    print(i)
