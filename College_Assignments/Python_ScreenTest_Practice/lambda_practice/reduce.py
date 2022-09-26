# reduce(function,sequence)
# is used to reduce a sequence to a single element

from functools import *

exp1 = [1,2,3,4,5,6,7]

ans = reduce(lambda x,y : x*y,exp1)
print(ans)


ans2 = reduce(lambda x,y:x+y,range(1,51))
print(ans2)

# range functions
# range(start,stop,step)
# start is included , stop is not included so that we know from where to start next time

