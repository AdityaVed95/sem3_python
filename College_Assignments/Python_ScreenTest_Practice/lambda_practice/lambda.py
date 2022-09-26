# lambda function takes arguments and return something
# lambda <variable names of the arguments taken by the function> : <expression returned by the function>


f1 = lambda x: x**2
value1 = f1(9.2)
print(value1)

f2 = lambda x,y : x**y
value2 = f2(2,5)
print(value2)




max = lambda x,y:x if x>y else y

print("Enter two numbers seperated by commma")
response = input()
num_str = response.split(',')
num_int = []

for item in num_str:
    num_int.append(int(item))

a = num_int[0]
b = num_int[1]

print("bigger num is: ",max(a,b))
