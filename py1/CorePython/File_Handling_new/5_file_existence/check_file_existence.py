import os
import sys

# if we directly try to access the file without it actually existing then it will give
# the : FileNotFoundError

# this search of os.path.isfile() is only done within the directory in which the program exists
# even if the fname file is in the parent directory of the current directory then too it would show not found


print("Enter the name of the file that you want to read:")
fname = input()

if os.path.isfile(fname) == True:
    print("Hurray the file exists")
else:
    print(fname + " file doesnt exist")
    sys.exit()

f = open(fname, "r")
str1 = f.read()
print(str1)

# now if we put fname as : check_file_existence.py
# then the source code of the program will be printed
