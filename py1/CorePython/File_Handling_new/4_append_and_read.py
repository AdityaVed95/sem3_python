# purpose is to append something to a file and then read the contents of a file
f = open("sample_directory_to_store_files/test_me_edit_me", "a+")
# now we can use the write() method to append string to the file
# seek method is used to place the file handler at a particular position in the file
# f.seek(offset,fromwhere)
# offset represents how many bytes to move
# fromwhere : takes 3 valuse : 0,1,2
# 0: represents from beginning of file
# 1: represents from current positon
# 2: represents from end of file
f.seek(10, 0)
print("Reading 'after' the 10th byte from start of the file")
print(f.tell())
string1 = f.read()
print(string1)
f.close()
# Note: Reference point at current position / end of file cannot be set
# in text mode except when offset is equal to 0.

# Seek() function with negative offset only works when file is opened in binary mode

# https://www.geeksforgeeks.org/python-seek-function/

# rb is to read a binary file


f = open("sample_directory_to_store_files/test_me_edit_me", "rb")

f.seek(-10, 2)
print(f.tell())
print("Reading :")
string2 = f.read().decode('utf-8')
print(string2)
f.close()

# copy the below line into test_me file
# b'Code is like humor. When you have to explain it, its bad.'


#  note that b' are also considered as the characters of the string
