with open("sample", "w") as f:
    f.write("I am using with statement\n")
    f.write("To print these lines")

with open("sample", "r") as f:
    print("Reading from the file:")
    for line in f:
        print(line)

# an observation here is that when we use for line in f:
# the lines are printed but there is an additional blanck line between
# the required printed lines
