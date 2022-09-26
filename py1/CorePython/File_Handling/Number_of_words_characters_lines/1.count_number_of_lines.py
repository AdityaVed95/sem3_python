f = open("sample", "r")

i = 0
for line in f:
    i += 1
    print("Line Number is : ", i)
    print("Line Content is :")
    print(line)
    print("-------------")

print("Number of lines are: ", i)

f.close()
