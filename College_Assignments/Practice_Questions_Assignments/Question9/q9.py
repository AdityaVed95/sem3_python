import re


def checking_username(username):
    if len(username) < 6:
        print("Incorrect username")
        print("As Length of username is less than 6")
        return False

    if len(username) > 10:
        print("Incorrect username")
        print("As Length of username is more than 10")
        return False

    result = re.search(r'[a-zA-Z]+', username)
    if result.group() == username:
        return True
    else:
        print("Incorrect username")
        print("Username should have alphabet only")
        return False


def checking_password(password):
    if len(password) < 6:
        print("Incorrect Password")
        print("length of password is less than 6")
        return False

    if len(password) > 15:
        print("Incorrect Password")
        print("length of password is more than 15")
        return False

    result1 = re.findall(r'[A-Z]', password)
    # as the special characters are already specified in the question thus taking only
    # those specific characters as special characters @,#,$,<,%,&
    result2 = re.findall(r'\d', password)
    result3 = re.findall(r'\W', password)

    if len(result1) == 0:
        print("Incorrect Password:")
        print("Upper Case Letter not found")
        return False

    if len(result2) == 0:
        print("Incorrect Password:")
        print("At-least one numerical should be present")
        return False

    if " " in result3:
        result3.remove(" ")

    if len(result3) == 0:
        print("Incorrect Password:")
        print("No Special Character Found")
        return False


def checking_email_id(email_id):
    result1 = re.findall(r'@', email_id)

    if len(result1) != 1:
        print("Incorrect Email id")
        print("email id should necessarily contain only one @ symbol")
        return False

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, email_id):
        return True

    else:
        print("Incorrect Email id")
        return False


def checking_mobile_number(mobile_number):
    if len(mobile_number) != 10:
        print("Incorrect length of mobile number:")
        return False

    allowed_start_numbers = ["6", "7", "8", "9"]
    if mobile_number[0] in allowed_start_numbers:
        return True

    else:
        print("Incorrect mobile number:")
        print("Mobile number should start with 6 or 7 or 8 or 9")
        return False


def main():
    print("Enter the username :")
    username = input()

    print("Enter Password :")
    password = input()

    print("Enter email id : ")
    email_id = input()

    print("Enter Mobile Number : ")
    mobile_number = input()

    if checking_username(username) == False:
        exit()

    if checking_password(password) == False:
        exit()

    if checking_email_id(email_id) == False:
        exit()

    if checking_mobile_number(mobile_number) == False:
        exit()

    print("Thank You for your valid inputs")


if __name__ == "__main__":
    main()
