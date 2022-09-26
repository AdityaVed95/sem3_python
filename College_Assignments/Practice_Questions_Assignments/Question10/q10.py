import re

text = """
Name: Patel Umang Jayantibhai
Account number: 10101010101010
IFSC code: UNIN00897
email id: xyz@gh.com
pin code: 401101 
mob no: 9870765910 

Name: Shah Umang Jayantibhai
Account number: 10101010102022
IFSC code: UNIN00997
email id: pqr@gh.com
pin code: 400001 
mob no: 1234567890 
MICR code: UNINN8907

Name: Shah ritik
Account number: 10201010102022
IFSC code: UNIN00997
email id: pqr@gmail.com
pin code: 400001 
mob no: 6789678998 

email id: taha@gmail.com
pin code: 400001 
mob no: 6789678998 
Name: taha zubain
Account number: 10201010102022
IFSC code: UNIN00997
MICR code: UNNIN0909
"""

# Account number: start with "10" and length of 14.
# mobile number: start with 6 or 7 or 8 or 9 and length of 10.
# name of person: minimum length will be 3.
# IFSC code: first four alphabets and next five numerical. total length 9

# result1 = re.findall(r'[A-Za-z]', text)

mobile_number = re.findall(r'[6-9]\d{9}', text)
print("Mobile numbers extracted are:")
print(mobile_number)

account_number = re.findall(r'10\d{12}', text)
print("Account numbers extracted are:")
print(account_number)

ifsc_code = re.findall(r'[A-Za-z]{4}\d{5}', text)
print("IFSC code extracted are:")
print(ifsc_code)

pincode = re.findall(r'[4]\d{5}', text)
print("Pin Code extracted are:")
print(pincode)

names = []

for i in range(0, len(text)):
    if text[i] == 'N':

        if text[i + 1] == 'a':

            if text[i + 2] == 'm':

                if text[i + 3] == 'e':

                    if text[i + 4] == ':':
                        j = i + 6

                        str1 = ""
                        while (text[j] != "\n"):
                            str1 = str1 + text[j]
                            j += 1

                        names.append(str1)



                    else:
                        continue

                else:
                    continue

            else:
                continue

        else:
            continue

    else:
        continue

print("The names extracted are:")
print(names)
