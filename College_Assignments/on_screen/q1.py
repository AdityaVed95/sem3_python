def calculating(num_list): number_of_positive = 0


number_of_negative = 0
number_of_zeros = 0
for item in num_list: if
item > 0:
number_of_positive += 1
elif item < 0: number_of_negative += 1
else: number_of_zeros += 1
list_final = []
list_final.append(number_of_positive)
list_final.append(number_of_negative)
list_final.append(number_of_zeros)
tuple_final = tuple(list_final)
return tuple_final


def inputting_list(): num_list = []


while (True):
    print("Press 1 to add an element to the list and Press 2 to stop inserting elements to the list :")
response = int(input())
if response == 2:
    break
elif response == 1:
    print("input the number you want to insert in the list")
num_input = float(input())
num_list.append(num_input)
else:
print("Invalid Input , please try again:")
return num_list


def main():
    print("Taking input in the form of list : ") num_list = inputting_list()
    tuple_final = calculating(num_list)
    print("Number of Positive Numbers, Negative Numbers, Zeros respectively are :") print(tuple_final)
if __name__ == "__main__": main()
