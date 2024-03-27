
# !  what is a list
# =>>> Lists are used to store multiple items in a single variable.

#! List VS array 
# array are homogeneous .
#  array store  elemnt in continuous manner 
# array are much faster 
#  List are more programmer friendly 




#!  create  list
list_1 = []
list_1 = [1,2,3,4 ]
list_2 = ["a" , 23 , 43  , False]
list_3 = [1,2,3,4, [5,6]]

#! access 
# print(list_1[1])
# print(list_2[1:])
# print(list_3[-1][1])


#! edit 
# list_1[0] =100
# print(list_1) 
# list_1[1:] = [100, 200 , 300 , 400]
# print (list_1)


# !add
# list_1.append(300)
# print(list_1)
# list_1.extend(["hello" , 400 , 300 , 800])
# print(list_1)
# list_1.insert(5, 5000)
# print(list_1)

# ! delete
#  del , remove , pop, clear
# del list_1
# del list_1[2]
# list_1.remove(4)
# list_1.pop()
# list_1.clear()
# print(list_1)



#!  operation
# 
# L = [1,2,3,4,5]
# L1 = [9,8,7]
# print(L+L1)
# print(L*2)
# for i in L:
#   print(i)

# print(15 in L)

# !function
L = [1,2,3,4,5,9,8,7]
# print(len(L))
# print(min(L))
# print(sorted(L))
# print(max(L))
# print(L.index(3))

# ! SAMPLE QUESTION.....
# intro = "my name is ranjana"
# print(intro.title())
# intro1 = intro.split(" ")
# print(intro1)
# print(type(intro1))
# list_intro = []
# for i in intro1 :
#   print(i.capitalize())
#   list_intro.append(i.capitalize())
  # print(i)

# print(list_intro)
# print(" ".join(list_intro))


# ! SAMPLE QUESTION.....
email = "abc@gmail.com"
# print("abc" in email)
# print(email[:email.find("@")])

item = [1,2,3,4,5,5,4]
# 1st way ..
# item1 = set(item)
# # print(item1)
# item2= list(item1)
# print(item2)

# 2nd way

res =[]
for i in item:
  if i not in res:
    res.append(i)

print(res)

