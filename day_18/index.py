
#! what is modules ?
# consider a module to be the same as a code library 
#  A file containing a set of function you want to include in your application.

#  Example of python modules 
# Math 
#  Random
#  os
# time 

import math
res = math.floor(4.5)
# print(res)

res1 = math.ceil(2.64)
# print(res1)


import random
res2 = random.randint(1,50)
a = [1,2,3,4,6,7,8]
res4 = random.shuffle(a)

import time
timetoday = time.time()
# print(timetoday)
res6 = time.ctime()
# print(res6)

#  os module 
import os
ans = os.getcwd()
# print(ans)
ans2 = os.listdir()
# print(ans2)