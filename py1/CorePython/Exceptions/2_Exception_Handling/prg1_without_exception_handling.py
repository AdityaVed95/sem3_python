f = open("myfile", "w")

print("Enter the two numbers")

x = input()

a, b = x.split()
c = int(a) / int(b)

f.write("Writing %d into myfile" % c)

f.close()
print("file closed")

# now what if we enter 10 and zero , we have to make a provision for zero division error
# and make sure that the opened file is also closed
