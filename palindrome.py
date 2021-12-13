# 2) Palindrome (sequence of chars that read the same back and forward)

str = input("Please enter a string: ").lower()

if len(str)%2 == 0:
    
    if str[:] == str[::-1]:
        print(str, "is a palindrome.")
    else:
        print(str, "is not a palindrome.")
else:
    middle = round(int(len(str)/2))
    str1 = str[:middle]
    str2 = str[middle+1:len(str)]
    
    if str1[:] == str2[::-1]:
        print(str, "is a palindrome.")
    else:
        print(str, "is not a palindrome.")
    

## Professor's result

str = input("Please enter a string: ")

if str.lower() == str[::-1].lower():
    print(str, "is a palindrome")
else:
    print(str, "is not a palindrome")
