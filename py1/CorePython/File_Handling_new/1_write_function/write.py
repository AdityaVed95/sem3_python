# general syntax to open a file:
# <file_handler_or_file_object> = open("file_name","open_mode","buffering")

# buffering is used to determine the size of the buffer memory(temporary memory block)
# that is going to be used to read and write the files

# write() function is used to store characters or group of characters(called strings)
# into a file

# write function will just delete the existing data of the file and then write the data it
# is supposed to write to the file


file_handler = open("../sample_directory_to_store_files/test_me_edit_me", "w")
string1 = "this is used to test the writing mechanism, this is the 1st line"
file_handler.write(string1)

file_handler.close()
