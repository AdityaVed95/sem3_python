import re


password = "A322adityaD17A#"

if len(password) < 8:
    print("Length of password is less than 8, please enter bigger length next time")
    exit()

if len(password) >15:
    print("Length of password is greater than 15, please enter smaller password next time")
    exit()

if re.findall(r'[a-z]',password) and re.findall(r'[A-Z]',password) and re.findall(r'[0-9]',password) and re.findall(r'[$#@]',password):
    print("Password_Approved")
else:
    print("Invalid password")
