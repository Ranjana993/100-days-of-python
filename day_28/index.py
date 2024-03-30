
# ! Variable and memory references


#  aliasing
# a = 12 
# b = a 
# c = b 
# print(id(a))
# print(id(b))
# print(id(c))



#  reference counting
import sys
# a = "corona" 
# b = a 
# c = b 
# d =c 

# print(sys.getrefcount(a))




# ! garbage collection 


# !weird stuff 
a = 2
b = a 
c = b
print(sys.getrefcount(a)) 












