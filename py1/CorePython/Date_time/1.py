import datetime

e = datetime.datetime.now()
str1 = e.strftime("%d/%m/%Y")

str2 = e.strftime("%I:%M:%S %p")

print(str1)
print(str2)
print(type(str1))
print(type(str2))
