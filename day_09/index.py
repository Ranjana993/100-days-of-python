
# !  Operator in Python
# 1. Arithmatic operator
# 2. Assignment operator
# 3. Comparision Operator
# 4. Logical operator
# 5. Identity Operator
# 6. Membership operator

# 1. Arithmatic Operator :
# Arithmetic operators are used with numeric values to perform common mathematical operations.

# Eg Addition , Substraction , multiplication , division , exponentaition , floor division


num1 = 12
num2 = 12
sum = num1+num2
print("sum",sum)
sub = num1-num2
print("sub",sub)
mult = num1*num2
print("mult",mult)
divi = num1/num2
print("divi",divi)
mod = num1%num2
print("mod",mod)

# 1. Assignment Operator
# Assignment operators are used to assign values to variables

# Eg. = , += , -= , = , /= , %= , //= , *= , &= , != , <<= , >>=

a = 10
print(a)
a += 10
print (a)
a -= 10
print(a)

# 3. Comparision Operator
# Comparison operators are used to compare two values .

# eg. == , != , > , < , <= , >=


first = 12
second = 24
print ("== ",first == second)
print("!= " ,first != second)
print(">  ",first > second)
print("< " ,first < second)
print("<= ",first <= second)
print(">= ",first >= second)

# 4. Logical Operator
# Logical operators are used to combine conditional statements

# Eg. and , or , not


x =  5
print("and =>", x < 5 and x < 10)
print("or =>",x < 5 or x < 4 )
print("not =>", not(x < 5 and x < 10))

# 5. Identity Operator
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location .

# eg. is , is not


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# 6. Membership operator
# Membership operators are used to test if a sequence is presented in an object

# eg. in , not in


x = ["apple", "banana"]

print("banana" in x)
print("bananas"not in x)
