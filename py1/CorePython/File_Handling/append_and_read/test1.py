f = open("Sample", "a+")

while True:
    print("Input a Line")
    str1 = input()

    if str1 != "@":
        f.write(str1 + "\n")
    else:
        break

f.seek(0, 0)
print("The contents of the file are : ")
str2 = f.read()
print(str2)
f.close()
