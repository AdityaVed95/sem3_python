for i in range(0, 11, 1):
    if i % 2 == 0:
        continue
    else:
        print(i)

while True:
    print("Press 1 to continue and 2 to exit")
    choice = input()
    if choice == 2:
        break
