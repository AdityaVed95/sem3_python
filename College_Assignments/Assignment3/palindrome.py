print("Enter anything")

response = input()

list1 = []

for i in response:
    list1.append(i)

list2 = list(reversed(list1))

if list2 == list1:
    print("Is palindrome")

else:
    print("Not Palindrome")
