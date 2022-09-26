list1 = [123, 432, 5123, 5, 2165, 436, 43623, 46, 2346, 436, 2346, 2346, 464, 6236, 646, 4, 543, 623463, 54, 632, 642,
         66643, 642367, 78249]
print("enter which occurence of even integer you need")
k = int(input())
counter = 0

for item in list1:
    if item % 2 == 0:
        counter += 1
        if counter == k:
            print(item)
            break
