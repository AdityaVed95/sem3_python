import re

str1 = "Aditya Ved 19 17-11-2002 , Ravindra Ved 45 24-01-1976 , Stud 100 1-8-2001 "

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str1)

print(result)
