import math

print("Enter the length of the rectangular prism :")
length = float(input())
print("Enter the width of the rectangular prism :")
width = float(input())
print("Enter the height of the rectangular prism :")
height = float(input())
print("Enter the unit of the rectangular prism :")
unit = input()

volume = length * width * height
length_diagonal = math.sqrt(math.pow(length, 2) + math.pow(width, 2) + math.pow(height, 2))

# printing without using the format function :

vol = str(volume)
len_dia = str(length_diagonal)

print("The volume of the rectangular prism is " + vol + " cubic " + unit)

print("Diagonal length of the rectangular cube is " + len_dia + " " + unit)

