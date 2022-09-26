import re

# r'[a-z]+[A-Z]+\d+[$,#,@]'

# str1 = "this$@life"
# result = re.search(r'[#$@]',str1)

# if result is not None:
#     print(result.group())

# else:
#     print("Not found")



# print("Enter password:")
# password = input()

password = "adityaD17A#"

if len(password) < 8:
    print("Length of password is less than 8, please enter bigger length next time")
    exit()

if len(password) >15:
    print("Length of password is greater than 15, please enter smaller password next time")
    exit()

result = re.findall(r'[a-z]+[0-9]+[A-Z]+[$#@]+',password) 
# the problem is that the search is performed in the order in which it is defined 
# in the regular expression , thus for this each and every individual test has 
# to be performed seperately by using re.search or re.findall 



if result is not None:
    print(result)
else:
    print("Not found")
