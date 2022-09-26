f = open("sample2", 'r')
list1 = f.readlines()
print(list1)

str1 = f.read()
print(str1)

f.close()

# if we try to read the same file two times between its opening and closing then the
# second read is unsuccessful, i.e if stored in string then string is empty
# or if stored in a list then the list is empty

# the above is because the file pointer f is at the end of the file.
# we should use the seek method to take the file pointer at the start of the file and then read
