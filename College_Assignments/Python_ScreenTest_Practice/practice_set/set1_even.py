import math

print("Enter the number:")
num = float(input())
fractional, integer = math.modf(num)
integer_main = int(integer)
print("Number before decimal place is: ", integer_main)
str_integer = str(integer_main)
print("Number of digits before decimal place is: ", len(str_integer))

num_str = str(num)
position = None

for i in range(0, len(num_str)):
    if num_str[i] != ".":
        continue
    else:
        position = i
        break

print("Number after decimal point: ", end="")
for i in range(position + 1, len(num_str)):
    print(num_str[i], end="")

print()
print("Number of digits after decimal point is: ", len(num_str) - (position + 1))
