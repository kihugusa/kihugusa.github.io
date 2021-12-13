# Problem 1
# a) 5 grades inputted
# b) average after dropping the two lowest grades

grades = []
num1 = float(input("Enter the first grade: "))
num2 = float(input("Enter the second grade: "))
num3 = float(input("Enter the third grade: "))
num4 = float(input("Enter the fourth grade: "))
num5 = float(input("Enter the fifth grade: "))

grades.append(num1)
grades.append(num2)
grades.append(num3)
grades.append(num4)
grades.append(num5)
print("The grades are:", grades)

grades.remove(min(grades))
grades.remove(min(grades))
print("The average with the two lowest grades removed is:", sum(grades)/len(grades))


# Problem 2
# a) print code as before but...
# b) grades sorted from low to high
# c) print them out from high to low


grades = []
num1 = float(input("Enter the first grade: "))
num2 = float(input("Enter the second grade: "))
num3 = float(input("Enter the third grade: "))
num4 = float(input("Enter the fourth grade: "))
num5 = float(input("Enter the fifth grade: "))

grades.append(num1)
grades.append(num2)
grades.append(num3)
grades.append(num4)
grades.append(num5)
print("The grades are:", grades)
grades.sort()
print("The grades sorted from lowest to highest:", grades)
grades.reverse()
print("The grades sorted from highest to lowest:", grades)

grades.remove(min(grades))
grades.remove(min(grades))
print("The average with the two lowest grades removed is:", sum(grades)/len(grades))




