
# conditional statements (if , elif , else )

email = input("Provide your email address : ")
password  = input("Enter your password :")

if "@" in email:
  if email == "ranjana@gmail.com" and password == "12345":
    print("Welcome ")
  elif email == "ranjana@gmail.com" and password  != "12345":
    print("Password fir se galat hai idiot ")
    password = input("Firse bol password : ")
    if  password== "12345":
      print("Sahi hai ")
    else : 
      print("Nonsene galat hai password ")  
  else:
    print("Invalid credentials ")  
else:
  print("Incorrect gmail credentials")

