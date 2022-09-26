# it is optional to pass the second parameter here , if we dont pass it then default value is assumed
# which is already in the function definition and if we pass 2nd argument then it uses that  as the
# function argument


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("hello")
print()
banner("hey there", '*')
print()


def banner2(messsage, border='-', key="$"):
    line1 = border * len(messsage)
    line2 = key * len(messsage)

    print(line1)
    print(line2)
    print(messsage)
    print(line2)
    print(line1)


banner2("aditya", "%")
print()
banner2("ravindra", "!", "&")
print()
banner2("the 1st trick", "#")
print()
# banner2("the main trick", , "#")
banner2("the main trick type", border="*", key="#")
