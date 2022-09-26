# retrive those strings with 4 to 6 characters only
import re
str = "one two three four five six seven eigth nine ten thisisit forme now a on sixcha sevench"

result = re.findall(r'\b\w{4,6}\b',str)
print(result)
