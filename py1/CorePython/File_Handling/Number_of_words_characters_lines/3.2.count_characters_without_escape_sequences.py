f = open("sample", "r")

number_of_lines = 0
number_of_words = 0
number_of_characters = 0
for line in f:
    number_of_lines += 1
    list_of_words_in_this_line = line.split()
    number_of_words += len(list_of_words_in_this_line)
    number_of_characters += len(line)

print("Number of lines :", number_of_lines)
print("Number of words :", number_of_words)
print("Number of characters :", number_of_characters)

f.close()
