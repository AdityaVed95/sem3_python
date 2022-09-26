x = (i for i in range(3))

for i in x:
    print(i)

for i in x:
    print(i)

print("2nd case :")

y = list(x)
for i in y:
    print(i)

for i in y:
    print(i)

print("this is happening because x is a generator")
