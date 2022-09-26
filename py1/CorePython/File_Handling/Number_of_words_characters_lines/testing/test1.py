f = open("../sample", "r")
for line in f:
    print(line)
    print(len(line))

f.close()
# this also considers the escape sequences like \n at the end of each line
# thus we should do len - 1 to get the final ans
