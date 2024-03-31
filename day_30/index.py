
# recursion 
#  Recursion is a function that call itself 

# def sum(a , b):
#   res = 0 ; 
#   for i in range(1 ,b+1):
#     res = res + i

#   return res
# #   1 + 2 + 3 + 4 
  
# print(sum(1,4))


# ! multiplication of 1 to n 
# def mult(a, b):
#   if(b==1):
#     return a
#   else:
#     return b * mult(a , b-1)

# print(mult(1,4))



# !factorial 

# def fact(num):
#   if num == 1 :
#     return 1
#   else:
#     return num*fact(num-1)

# print(fact(5) ) 


#! Palindrome 

def is_palindrome(string):
  if(len(string) == 1):
    print("Palindrome")
  else:
    if string[0] == string[-1]:
      is_palindrome(string[1:-1])
    else:
      print("Not palindrome")
      
is_palindrome("lol0")
is_palindrome("abba")


















