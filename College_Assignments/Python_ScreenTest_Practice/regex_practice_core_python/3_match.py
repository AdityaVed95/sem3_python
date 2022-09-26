import re
from tkinter.messagebox import NO

str_in_which_search_is_done = "eat Cat Hat Pat Lat nat format Conmatskill mac m#2 m@4 mt#"

str_in_which_search_is_done_2 = "ma3 Cat Hat Pat Lat nat format Conmatskill mac m#2 m@4 mt#"

result1 = re.match(r'm\w\w',str_in_which_search_is_done)
result2 = re.match(r'm\w\w',str_in_which_search_is_done_2)

if result1 is not None:
    print("result1 :", result1.group)
else:
    print("result 1 not found")

if result2 is not None:
    print("result 2 is : ",result2.group())

else:
    print("result 2 not found")


