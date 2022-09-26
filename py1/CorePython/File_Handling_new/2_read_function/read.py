# read(n) function takes an optional argument : n : number of bytes to be
# read from the file
# if we do not specify any mode then the by default mode is read mode
file_handler = open(
    "/Users/adityaved/prj_ws/Semester2_main/py1/CorePython/File_Handling_new/sample_directory_to_store_files"
    "/test_me_edit_me", "r")

string1 = file_handler.read()
print(string1)
file_handler.close()

file_object = open("../sample_directory_to_store_files/test_me_edit_me", 'r')
string2 = file_object.read(10)
print(string2)
file_object.close()
