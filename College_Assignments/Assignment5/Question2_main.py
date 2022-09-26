print("Enter string: ")
str1 = input()


def is_palindrome(str1):
    if len(str1) <= 1:
        return True
    else:
        if str1[0] == str1[-1]:
            return is_palindrome(str1[1:-1])
        else:
            return False


if is_palindrome(str1) == True:
    print("Is Palindrome")

else:
    print("Is not Palindrome")
