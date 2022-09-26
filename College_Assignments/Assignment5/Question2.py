# import re
#
# x = "hello"
# y = "lo"
# print(re.search(y, x))
# print(re.match(y, x))


def fxn():
    global str1
    if str1[0] == str1[-1]:
        str1 = str1[1:-1]
        if len(str1) <= 1:
            return True
        else:
            fxn()

    else:
        print("Is Not Palindrome")
        exit()


print("Enter string:")
str1 = input()
y = fxn()
if y:
    print("Is Palindrome")
