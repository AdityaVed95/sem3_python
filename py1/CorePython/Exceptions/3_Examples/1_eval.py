try:
    print("Enter date :")
    date = eval(input())
    # date = eval(input("Enter date: "))

except SyntaxError:
    print("invalid date entered")
else:
    print("you entered :", date)
