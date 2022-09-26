f = open("sample", "r")

i = 0

list_of_characters_in_this_line = []
list_of_all_characters = []

for line in f:
    i += 1
    list_of_words_in_this_line = line.split()
    list_of_characters_in_this_line.extend(line)
    list_of_all_characters.extend(line)

    print("The Characters in line {} are: ".format(i))
    print(list_of_characters_in_this_line)

    print("Number of characters in line {} are: {} ".format(i, len(list_of_characters_in_this_line)))
    print("--------------------------------------------------------------")
    list_of_characters_in_this_line = []

print("All the characters in the entire file are :")
print(list_of_all_characters)

print("Number of characters in the entire file are: ", len(list_of_all_characters))

f.close()

# the characters list consists of escape sequences like \n , how to remove them
