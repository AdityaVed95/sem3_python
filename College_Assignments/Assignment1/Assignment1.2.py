var = "Python programming"
print(var[-3])  # Access the "i" from the variable by index and print it

# to get the 1st n characters of the string : string_name[:n]
# to get the last n characters of the string : string_name[-n:]
# print(var[:5])
# print(var[-5:])

print("Length of the string is : " + str(len(var)))
slice1 = var[0:6]
print('the slice "Python" from var is : ' + slice1)

slice2 = var[7:14]
print('the slice “program” from the variable is : ' + slice2)

slice3 = var[2:4] + var[15:]
print('the string “thing” from the variable is : ' + slice3)

var = var.upper()  # converting the string into uppercase

print(var)

var2 = " is interesting"

print("On concatenation : " + var + var2)

print(var.isupper())
var = var.lower()
print(var)

print(var.rindex("in"))

print(var.startswith("pytho"))

print(var.isspace())
print(var.isdigit())
print(var.isalpha())  # space is not an alphabet


