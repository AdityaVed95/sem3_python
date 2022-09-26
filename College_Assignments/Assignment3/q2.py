print("Enter number :")
num = int(input())

str1 = str(num)
sum = 0

for i in str1:
    j = int(i)
    sum += j ** 3

if sum == num:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
