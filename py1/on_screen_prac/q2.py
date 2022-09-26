import re

print("Enter any Sentence")

sentence = input()
no_of_numeric = 0
no_of_lowercase = 0
no_of_uppercase = 0
no_of_special_characters = 0

for item in sentence:
    if item.isnumeric():
        no_of_numeric += 1

    elif item.isupper():
        no_of_uppercase += 1

    elif item.islower():
        no_of_lowercase += 1

result = re.findall(r'\W', sentence)
no_of_special_characters = len(result)

print("Numeric : ", no_of_numeric)
print("Upper Case : ", no_of_uppercase)
print("Lower Case : ", no_of_lowercase)
print("Special Character : ", no_of_special_characters)
