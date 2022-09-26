def inputting():
    print("Input string s:")
    input_string = input()
    return input_string


def matched(s):
    input_string = s
    # result_list1 = re.findall(r"[(]",input_string) # result_list2 = re.findall(r')',input_string)
    length1 = 0
    length2 = 0

    for item in input_string:
        if item == "(":
            length1 += 1

        elif item == ")":
            length2 += 1

    if length1 != length2:
        return False

    main_list = []

    for character in input_string:
        if character == "(":
            main_list.append(0)
        if character == ")":
            main_list.reverse()
            for i in range(0, len(main_list)):
                if main_list[i] == 1:
                    continue
                if main_list[i] == 0:
                    main_list[i] = 1
                    break
            main_list.reverse()

    for item in main_list:
        if item == 0:
            return False

    return True


def main():
    input_string = inputting()
    result = matched(input_string)
    if result == True:
        print("True : The string is matched")
    elif result == False:
        print("False : The string is not matched")


if __name__ == "__main__":
    main()
