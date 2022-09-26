import re

str1 = "coolING this now go"
result = re.search(r"\Ac[\w]*", str1)
result2 = re.search(r"n[\w]*\Z", str1)

if result is not None:
    print(result.group())
else:
    print("NONE status")

if result2 is not None:
    print(result2.group())
else:
    print("NONE status")

str2 = "9am be char maru ke tane aaje pan 10pm na ke 11am na ke pachi 4pm na"
result3 = re.findall(r'\d+am|\d+pm', str2, re.IGNORECASE)
if result3:
    print(result3)
else:
    print("NONE status")
