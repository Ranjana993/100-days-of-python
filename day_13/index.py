
#  ! guessing number 

import random
res = random.randint(1 , 100)
# print(res)

num = int(input("Enter your number from 1 to 100 : "))
count = 0 
while num != res:
  if  num < res:
    print("Guess higher ")
  else:
    print("Guess lower")
  num = int(input("Enter your number from 1 to 100 : "))
  count +=1
print("You are right and you took ", count ,  " attempts " )



