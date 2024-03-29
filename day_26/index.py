
# SETs
# 1. set do not allow duplicate 
# 2. set do not have indexing
# 3. set do not allow mutable datatypes
# 4. sets itself is a mutable datatype

# !  create 
# s = {}
# print(s)
# print(type(s))


# s1 = {1,2,3,4,5}
# print(s1)

# s2 = {"hello" , True , 1,2,3.4}
# print(s2)

# s3 = {1,2,3,3,3,4,5,5}
# print(s3)

# s4 = {[1,2,3],4,5}
# print(s4)

# s5 = {(1,2,3) , "hello"}
# print(s5)


# s6 = {1,2,3, {4,5,6}}

# ! accessing items

# print(s2[0])

# we can not access items in set 

# ! Edit items 
# s12 = list(s3)
# s12[2] = 100
# print(s12)

# we can not edit set items in set 

# !ADD
# s2.add(12)
# print(s2)


#!deleting => del remove , pop
# del s2
# res = s2.pop()
# res = s2.remove(2)
# print(s2)


# ! set operation
s1 = {1,2,3,4}
s2 = {6,5,9}
# res = s1+s2 
# print(res) 

# for i in s1 :
#   print(i)

# print(1 in s1)

# print(len(s1))
# print(min(s1))
# print(sorted(s1 , reverse=True))
res = s1.union(s2)
# print(res)
ans = s1.intersection(s2)
# print(ans)

res1 = s1.difference(s2)
# print(res1)

res2 = s1.symmetric_difference(s2)
# print(res2)
res3 = s1.issubset(s2)
# print(res3)












