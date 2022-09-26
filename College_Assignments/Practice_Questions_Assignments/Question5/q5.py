def add(n):
    final_ans = n
    while int(final_ans) > 9:
        list1 = list(final_ans)
        sum = 0
        for item in list1:
            item = int(item)
            sum = sum + item

        final_ans = str(sum)

    print("Final Answer is : ", final_ans)


def main():
    print("Enter the number :")
    num = input()
    add(num)


if __name__ == "__main__":
    main()
