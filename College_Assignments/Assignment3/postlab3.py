import string

alphabet_string1 = string.ascii_letters
alphabet_list1 = list(alphabet_string1)

print("Input anything :")
response = input()

no_of_digits = 0
no_of_letters = 0

for item in response:
    if item.isdigit():
        no_of_digits += 1

    elif item in alphabet_list1:
        no_of_letters += 1

print("Number of letters are : ", no_of_letters)
print("Number of digits are : ", no_of_digits)
