f = open("sample2", "r")
for line in f:
    print(line)
    print(len(line))

f.close()
# this also considers the escape sequences like \n at the end of each line
# thus
