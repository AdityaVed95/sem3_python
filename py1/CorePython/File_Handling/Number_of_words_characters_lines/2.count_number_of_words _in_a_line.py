f = open("sample", "r")

list_of_all_words = []
list_of_words_in_this_line = []

i = 0
for line in f:
    i += 1
    print("Contents of line {} are ".format(i))
    print(line)
    list_of_all_words.extend(line.split())
    words_in_this_line = line.split()
    print("Number of words in this line {} are {} : ".format(i, len(list_of_words_in_this_line)))
    print()

print("All the words are :")
print(list_of_all_words)

print("Total Number of words: ", len(list_of_all_words))

f.close()
