from q2 import Student


def main():
    Student1 = Student()

    print("enter roll number of 1st student:")
    roll_num = int(input())
    Student1.set_rollnum(roll_num)

    print("enter marks in 1st subject")
    marks1 = int(input())
    Student1.set_marks1(marks1)

    print("enter marks in 2nd subject")
    marks2 = int(input())
    Student1.set_marks2(marks2)

    print("enter marks in 3rd subject")
    marks3 = int(input())
    Student1.set_marks3(marks3)

    print("enter marks in 4th subject")
    marks4 = int(input())
    Student1.set_marks4(marks4)

    print("Student Details are : ")
    Student1.get_rollnum()
    Student1.get_marks1()
    Student1.get_marks2()
    Student1.get_marks3()
    Student1.get_marks4()
    Student1.get_total_marks()
    Student1.get_percentage()


if __name__ == "__main__":
    main()
