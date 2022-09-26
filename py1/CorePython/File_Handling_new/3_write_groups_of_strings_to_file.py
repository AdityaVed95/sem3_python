file_handler = open("sample_directory_to_store_files/test_me_edit_me", 'w')

print("Keep on entering text to be appended to the file.")
print("To stop appending , type @")

string1 = ""

while string1 != "@":
    string1 = input()

    if string1 != "@":
        file_handler.write(string1 + "\n")

file_handler.close()

file_object = open("sample_directory_to_store_files/test_me_edit_me", "r")
print("Reading the data that you just wrote to the file")

string2 = file_object.read()
print(string2)
# observation : the below code is not executed maybe because we can call only
# one method per file_object or per file_handler
#
#
# list1 = file_object.readlines()
# for item in list1:
#     print(item)
#     print("================")

# but instead if we create another file_handler say f: we can get the
# same above code working


# now i realised why the above code did not work : it is because the position
# of the file handler is at the end of the file after we have completed the above
# read operation ,
# now if we try to read from the end of the file then it is obviously going
# to read nothing,


file_object.close()

f = open("sample_directory_to_store_files/test_me_edit_me", 'r')
list1 = f.readlines()
for item in list1:
    print(item)
    print("=============")

print(list1)

# in order to suppress the \n characters that are printed in the above list, we can use the splitlines() function

# the below code will again not work (list2 will be empty) because we are again trying to a call a function
# using a file object which is already used once to call a function
# f : file object , is already used once to call the f.readlines() function thus we cannot again use f.<any_fxn>()
# we should close the file object then open it once again by same or different name


# list2 = f.read().splitlines()
#
# print(list2)


# we might be thinking about the problem that what if a single line is very long,
# then will that line be written as multiple lines inside the text document while
# using the write() method, the answer to this question is no, however huge a
# single line maybe , it is going to be a single line only and it might spawn
# in huge length horizontally , it is still considered as a single line

# thus the integrity of a single line cannot be broken by its own length
f.close()

f2 = open("sample_directory_to_store_files/test_me_edit_me", "r")
list2 = f2.read().splitlines()
print(list2)
