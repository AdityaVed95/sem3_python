lst1 = [10, 20, 30, 45, 79, 43, 56]
lst2 = [4, 45, 4, 325, 4523, 6, 23463]

lst_main = list(map(lambda x: x % 2 == 0, lst1))
print(lst_main)
for item in lst_main:
    print(type(item))
    print(id(item))

ans = lst_main[0] is lst_main[1]
print(ans)
ans2 = lst_main[0] == lst_main[1]
print(ans2)

lst_main2 = list(map(lambda x, y: x + y, lst1, lst2))
print(lst_main2)
