### Assignment 12

## 1) Number of vowels revisited

str = input("Please enter a string: ")
vowels = 0
lst = []

for i in str:
    if i in 'aeiou':
        vowels = vowels + 1
        index = str.index(i)
        lst.append(index)

if vowels > 1:
    print("The number of vowel occurrences in your string is:",vowels)
    print("The indexes of the vowels in your string are:", lst)
elif vowels == 1:
    print("The number of vowel occurrences in your string is:",vowels)
    print("The index of the vowel in your string is:",lst)
else:
    print("There are no vowels in your word.")


## 2) Palindrome revisited

str = input("Please enter a string to enter: ")

letters = []

for i in str.lower():
    if i.isalpha():
        letters.append(i)

if len(letters)%2 == 0:
    begin = letters[:(len(letters)/2)-1]
    end = letters[(len(letters)/2)-1:]
else:
    begin = letters[:int(len(letters)/2)]
    end = letters[int(len(letters)/2)+1:]

end.reverse()
if begin == end:
    print('The string "', str,'" is a palindrome.')
else:
    print('The string "',str,'"is not a palindrome.')


### Professor's Solution
str = input("Please enter a string: ").lower()
newStr = []

for ch in str:
    if ch.isalpha() == True:
        newStr.append(ch)

if str == str[::-1]:
    print("The string",str,"is a palindrome")
else:
    print("The string",str,"is not a palindrome")
    
    

## 3) End-of-year balances

principal = 1000
rate = 0.06

for i in range(1,6):
    print("Balance after year",i,"is",round(principal*(1+rate)**i,2))
    

    


