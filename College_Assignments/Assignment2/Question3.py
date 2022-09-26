import string

print("Input Anything")

input1 = input()

alphabet_string1 = string.ascii_letters
alphabet_list1 = list(alphabet_string1)

dict1 = {}

for i in alphabet_list1:
    dict1.update({i: 0})

for i in input1:
    if i in dict1:
        dict1[i] = dict1[i] + 1

print(dict1)
