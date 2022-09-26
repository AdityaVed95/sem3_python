print("Enter any number :")
num = int(input())
square = num ** 2

str_square = str(square)
str_num = str(num)

if str_square.endswith(str_num):
    print("Automorphic Number")

else:
    print("Not Automorphic")
