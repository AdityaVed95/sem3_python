print("Enter all the numbers of the list:")
str_input = input()
str_list = str_input.split()

int_list = []

for i in range(len(str_list)):
    int_list.append(int(str_list[i]))

even_list = list(filter(lambda x: (x % 2) == 0, int_list))
odd_list = list(filter(lambda x: (x % 2) != 0, int_list))

print("All the even numbers are from the input are:")
print(even_list)
print("All the odd number from the list are: ")
print(odd_list)
