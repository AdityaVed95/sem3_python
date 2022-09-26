import os, sys

print("Enter the name of the file you want to read")
fname = input()

if os.path.isfile(fname):
    print("Hurray!!! the file exits ")
    f = open(fname, "r")
else:
    print("NO such file found")
    sys.exit()

print("The file contents are :")
file_read = f.read()
print(file_read)
f.close()
