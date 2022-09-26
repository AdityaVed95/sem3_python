print("Enter anything :")
input1 = input()

dict1 = {}

for i in input1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1

print(dict1)