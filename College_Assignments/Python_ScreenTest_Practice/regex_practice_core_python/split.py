import re
str1 = "This, is, aditya, ved hello, here"
result = re.split(r',',str1)
print(result)

result_list_2 = str1.split(',')
print(result_list_2)
