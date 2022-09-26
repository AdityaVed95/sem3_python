import re

str1 = "The time is 1am , 2am , 10pm ,,,12am 433pm 424am"

res1 = re.findall(r'\b\d{1,2}am\b|\b\d{1,2}pm\b', str1)

print(res1)

# note : \b represents space around words
# doubt: why did 12am be a part of res1 , there is no whitespace before 12am
