try:
    print("Enter the name of the file you want to read")
    name = input()
    f = open(name, "r")

except IOError:
    print("File not found")

else:
    n = len(f.readlines())
    print(name, "has", n, "lines")
    f.close()
