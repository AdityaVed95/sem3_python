print("Student Details Storage Program: ")

f1 = open("student_record", "a")
f1.write("Roll No : Name : Department\n\n")
f1.close()

while True:
    print("Enter 1 to add Student Details to the file")
    print("Enter 2 to exit the program")
    response1 = input()

    if response1 == "1":
        print("Enter the roll number of the student")
        roll_num = input()

        print("Enter the Name of the student")
        name = input()

        print("Enter the Department of the student")
        department = input()

        f2 = open("student_record", "a")
        f2.write(roll_num)
        f2.write("  :  ")
        f2.write(name)
        f2.write("  :  ")
        f2.write(department)
        f2.write("\n\n")
        f2.close()


    elif response1 == "2":
        break
    else:
        print("Invalid Input")
        print("Please Try again", end="\n\n")
