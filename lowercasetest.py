# 3) String lower case letter test

str = input("Enter your string: ")

if str.isalpha():
    if str.islower():
        print("Your string is comprised entirely of lower case letters.")
    else:
        print("Your string is comprised entirely of letters but some or all are upper case.")
else:
    print("Your string is not composed entirely of letters.")

