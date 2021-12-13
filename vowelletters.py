## Assignment 7
# 1) Vowel and letters
vowel = ["a","e","i","o","u"]

letter = input("Enter a letter: ")

if letter.lower() in vowel:
    print(letter, "is a vowel.")
elif letter.isalpha():
    print(letter, "is not a vowel.")
else:
    print("You did not enter a letter.")
    

# 2) Weather Forecast

color = input("What is the color, red or blue? ").lower()
mode = input("Is the light flashing or steady? ").lower()

if color == "red":
    if mode == "flashing":
        print("The forecast is snow instead.")
    else:
        print("The forecast is rain ahead.")
else:
    if mode == "flashing":
        print("The forecast is clouds due.")
    else:
        print("The forecast is clear view.")
    

# 3) Listed values

lst1 = []
lst2 = []

value = input("Enter the 1st value for List 1: ")
lst1.append(value)
value = input("Enter the 2st value for List 1: ")
lst1.append(value)
value = input("Enter the 3st value for List 1: ")
lst1.append(value)

value1 = input("Enter the 1st value for List 2: ")
lst2.append(value1)
value1 = input("Enter the 2st value for List 2: ")
lst2.append(value1)
value1 = input("Enter the 3st value for List 2: ")
lst2.append(value1)

print(lst1)
print(lst2)

if lst1 == lst2:
    print("The values in the list are identical")
else:
    print("The values in the list are not identical")

if lst1[0].isnumeric() == True and lst2[0].isnumeric():
    print("The first values in the list are numbers.")
else:
    print("The first values in the list are not numbers.")

lst1.reverse()
if lst1 == lst2:
    print("The values in the list are reversed.")
else:
    print("The values in the list are not reversed.")





