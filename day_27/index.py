
# ! Dictionary
#  dictionary has no indexing
# dictionary is a mutable type
# keys are immutable but value is mutable
# keys hould be unique

# ! mutable => List , Set , Dictionary
#! immutable => String , tuple , int , float , Boolean , complex


# a = {
#   "name":"Ranjana",
#   "age":23,
#   "gender":"female",
# }
# print(a)
# b = {[1,2,3]:"Ranjana"}
# b = {(1,2,3):"Ranjana"}
# print(b)

# c = a["name"] = "Rohit"
# print(a)

# d = {
#   "name":"rohit",
#   "hobbis":{
#     "playing":"footbal",
#     "singning":"yes"
#   },
#   "gender":"male"
# }
# print(d)


#! Accessing
# a = {
#   "name":"Ranjana",
#   "age":23,
#   "hobbis":{
#     "playing":"footbal",
#     "singning":"yes"
#   },
#   "gender":"female",
# }
# print(a["hobbis"]["playing"])


# ! Edit
# a = {
#   "name":"Ranjana",
#   "age":23,
#   "hobbis":{
#     "playing":"footbal",
#     "singning":"yes"
#   },
#   "gender":"female",
# }

# res = a["name"]="rohit"

#! Add new keys to dict
# a["State"]="Haryana"
# print(a)

# !deleting
# del a 
# del a["name"]
# a.clear()
# print(a)


# ! operation
a = {"name":"ranjana"  , " age" : 12}
b = { "gender":"female"}
# c = a+ b ;
# print(c)

# for i in a :
#   print(i)

# for i in a :
#   print(a[i])

print("name" in a) 
print(a.keys())
print(a.values())











