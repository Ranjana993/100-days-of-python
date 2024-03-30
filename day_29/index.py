
# function

#  ... abstraction
# ...decomposition

# ! Components of the function 

# def is_even(i):
    #  code 
    # return 
# is_even(3)

# def is_even(num):
#   if type(num) ==int:
#       if num%2 == 0:
#         return "Even"
#       else: 
#         return "ODD"
#   else:
#     return "NOT Allowed"

# res = is_even(4)
# print(res)
# res = is_even("4")
# print(res)


# ! Parameters Vs Arguments:

# 1. Default argument:
# def power(a =1, b=1 ):
#   return a**b
# print(power(2,3))
# print(power(2))
# print(power())

# 2. Positional arguments
# print(power(a = 3 , b = 2))

# 3. Keyword arguments
# 4. Arbitrary arguments
# print(1,2,3,4) 




# def flexi(*number):
#   print(number)
#   product = 1
#   for i in number :
#     product = product* i
#   print(product)

# flexi(1,2,3,4)

# ! Global Var and Local Var 



# In Python, variables can be either global or local in scope. Here's an explanation of each:

#! Global Variables:
# 1. Global variables are defined outside of any function or class.
# 2. They can be accessed and modified from anywhere within the program, including inside functions.
# 3. To declare a global variable within a function, you need to use the global keyword to indicate that the variable is global rather than local to the function.


# global_var = 10

# def my_function():
#   print("Global variable inside function:", global_var)

# my_function() 

#! Local Variables:
# 1. Local variables are defined within a function and are only accessible within that function's scope.
# 2. They cannot be accessed or modified from outside the function in which they are defined.
# 3. Each function call creates its own scope, and variables defined within that scope are local to that function call.

# def my_function():
#   local_var = 20
#   print("Local variable inside function:", local_var)

# my_function()


# x = 10  # Global variable

# def my_function():
#   x = 20  # Local variable
#   print("Local variable inside function:", x)

# my_function()  # Output: Local variable inside function: 20
# print("Global variable outside function:", x) 

# ! Nested function :
# ? In Python, you can define functions inside other functions. These are called nested functions. 

def outer_function():
  print("Outer function is called.")
    
  def inner_function():
    print("Inner function is called.")
  inner_function()

outer_function()
















