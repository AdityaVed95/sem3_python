def multiply(x, y):
    return x * y


lst1 = [10, 15, 151, 32, 53521, 523532, 32145, 31532]
lst2 = [12, 4, 523, 52, 21, 5621, 351, 532]

# taking 1 element from each list one at a time
lst3 = list(map(multiply, lst1, lst2))
print(lst3)

lst4 = list(map(lambda x, y: x * y, lst1, lst2))
print(lst4)

print(lst3 == lst4)

lst_test = []
for i, j in zip(lst1, lst2):
    lst_test.append(i * j)

print(lst3 == lst_test)
