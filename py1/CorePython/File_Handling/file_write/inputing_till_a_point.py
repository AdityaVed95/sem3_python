f = open("file_read/sample2", "w")

print("Enter text (@ at end): ")

while True:
    str1 = input()

    if str1 != "@":
        f.write(str1 + "\n")
    else:
        break

f.close()
