import os

print("Enter the name of the file that you want to read")
file_name = input()

if os.path.isfile(file_name):
    f1 = open(file_name, "r")
    string1 = f1.read()
    print(string1.upper())

else:
    print("The requested file does not exist")
    print("Please try again later")
