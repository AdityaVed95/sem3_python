# print a new list containing the square of even numbers of the list

lst = [10,5,53,4,8,21,22]

lst_filtered = list(filter(lambda x: x%2==0,lst))

lst_mapped = list(map(lambda x: x**2,lst_filtered))

print(lst_mapped)


