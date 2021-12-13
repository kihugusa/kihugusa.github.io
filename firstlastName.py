userName = input("Please enter your full name: ")
charSpace = userName.find(" ")
firstName = userName[0:charSpace]
lastName = userName[(charSpace+1):len(userName)]
print("Your first name is:", firstName)
print("Your last name is:", lastName)
