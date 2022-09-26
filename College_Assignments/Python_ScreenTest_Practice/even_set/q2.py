# aim is to create a program to convert postive real number into binary number
# positive real number is base 10 and the binary number generated is base 2

import math

print("Input positive Number [in base 10 system] or a [number in decimal system]")
num = float(input())
fractional, integer = math.modf(num)

print("Enter the base system to which you want to convert")  # assuming 2 in this case
base_convert_to = int(input())

# base_convert_to = 2

copy = integer
remainder_integer = []

while True:
    Quotient = copy // base_convert_to
    if Quotient == 0:
        remainder_integer.append("1")
        break

    remainder = copy % base_convert_to
    temp = int(remainder)
    remainder_integer.append(str(temp))
    copy = Quotient

remainder_integer.reverse()

sum = ""
for item in remainder_integer:
    sum = sum + item

# integer_part_of_ans = int(sum)

copy2 = fractional
remainder_fractional = []

while True:
    number = copy2 * 2
    frac1, temp_inte1 = math.modf(number)
    inte1 = int(temp_inte1)
    remainder_fractional.append(str(inte1))
    if frac1 == 0:
        break
    copy2 = frac1

sum2 = ""
for item in remainder_fractional:
    sum2 = sum2 + item
print("{}.{}".format(sum, sum2))
