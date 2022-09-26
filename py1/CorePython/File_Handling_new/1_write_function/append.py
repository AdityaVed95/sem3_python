file_handler = open("../sample_directory_to_store_files/test_me_edit_me", "a")
string1 = """This data is getting appended to the file now, append rate is 5 bytes
at a time as 5 bytes is the value of the temporary memory buffer allocated 
for appending operation"""

file_handler.close()
