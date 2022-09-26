f = open("sample1", "w")
print("Enter anything")
str1 = input()
dict1 = {123: "av", 456: "there"}
f.write(str1)
str2 = str(dict1)
str3 = "\n"
f.write(str3)
f.write(str2)
f.close()
