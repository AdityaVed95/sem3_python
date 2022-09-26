# better method

list1 = [10, 20, 30, 40, 50, 30, 80, 90, 30, 70]
# replace all the 30's with 100

indices = []  # 2,5,8

for i in range(0, (len(list1) - 1)):
    if list1[i] == 30:
        indices.append(i)

for index in indices:
    list1.pop(index)

for index in indices:
    list1.insert(index, 100)

print(list1)
