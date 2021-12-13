# 4) Entering a 9 character password with every 3rd character starting
# with 1st as the letter z.

password = input("Please enter a password: ")

str1 = password[::3]

if len(password) == 9 and str1 == "z"*len(str1):
    print("valid password")
else:
    print("invalid password")
