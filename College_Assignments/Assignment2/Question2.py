list1 = []
while 1:
    print("Press 1 to append anything to the list")
    print("Press 2 to exit")

    choice = int(input())
    if choice == 1:
        print("Enter anything")
        x = input()

        if x.isdigit():
            list1.append(int(x))
            continue

        try:
            y = float(x)
            list1.append(y)
            continue

        except ValueError:
            list1.append(x)


    else:
        break

set1 = set(list1)
list2 = list(set1)

print(list2)

#
# list1 =[]
# while 1:
#     print("Press 1 to append anything to the list")
#     print("Press 2 to exit")
#
#     choice = int(input())
#     if choice==1:
#         print("Enter anything")
#         x = input()
#
#         if x.isalnum():
#
#             if x.isdigit():
#                 list1.append(int(x))
#                 continue
#
#             list1.append(x)
#             continue
#
#
#         if x[0] == "[" and x[-1] == "]":
#             list1.append(list(x))
#             continue
#
#         if x[0] == "(" and x[-1] == ")":
#             list1.append(tuple(x))
#             continue
#
#         if x[0] == "{" and x[-1] == "}":
#             if ":" in x:
#                 list1.append(dict(x))
#                 continue
#
#             else:
#                 list1.append(set(x))
#                 continue
#
#         list1.append(float(x))
#
#     else:
#         break
#
# print(list1)
# set1 = set(list1)
# list2 = list(set1)
#
# print(list2)
#
#
#
#
#
#
#
#
