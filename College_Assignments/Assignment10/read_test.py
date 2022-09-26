f1 = open("edit_me", "r")
string1 = f1.read()
print("The position of file handler is: ", f1.tell())
# note that the \n is also considered as the character of the string
# so the output of the above is 52 , 52 includes two \n characters
f1.seek(0, 0)  # putting the file handler position back to the start of the file

string2 = f1.readline(7)
f1.seek(0, 0)

string3 = f1.readline(20)
f1.seek(0, 0)

list1 = f1.readlines()
f1.seek(0, 0)

print(string1, end="\n===========\n")
print(string2, end="\n===========\n")
print(string3, end="\n===========\n")
print(list1, end="\n===========\n")
f1.close()
print(type(string1))

