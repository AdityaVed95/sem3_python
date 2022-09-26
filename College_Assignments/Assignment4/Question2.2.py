import re

print("Enter credit card number: ")
credit_num = input()

if len(credit_num) == 19:
    result2 = re.findall(r'[4-6]\d{3}[-]\d{4}[-]\d{4}[-]\d{4}', credit_num)
    print(result2)
    if len(result2) == 1:
        print("Valid Credit Card Number")
    else:
        print("Invalid credit card number")

else:
    print("Invalid credit card number")
