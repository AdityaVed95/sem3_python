f = open("count_me", "r")

for line in f:
    print(type(line))
    print(line)
    print("================")

f.seek(0, 0)
for line in f:
    print(line)
    words = line.s

f.close()
