import re

str_in_which_search_is_done = "eat Cat Hat Pat Lat nat format Conmatskill mac m#2 m@4 mt#"

result = re.findall(r'm\w\w',str_in_which_search_is_done)

print("Result is :",result)

# if not found then the result list is empty 
