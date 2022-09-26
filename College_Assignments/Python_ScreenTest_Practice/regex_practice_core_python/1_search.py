import re

str_in_which_search_is_done = "eat Cat Hat Pat Lat nat forcat ConMatskill"

result = re.search(r'M\w\w',str_in_which_search_is_done)

if result is not None:
    print(result.group())
else:
    print("Not found")


# result.group() is used to print

