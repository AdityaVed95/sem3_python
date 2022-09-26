f1 = open("edit_me", "w")
x = f1.write("Hello")
print(x)
f1.close()

list1 = ["hello there\n", "writing multiple strings\n", "this is 3rd one", 45, 324]
# the int in list1 will generate error
# TypeError: write() argument must be str, not int

f2 = open("edit_me", "w")
f2.writelines(list1)
f2.close()
