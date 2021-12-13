# 3) Calculates the GPA for a student in a semester.

count = 1
total = 0
ncredits = 0
ncourses = int(input("Enter the number of courses: "))
while ncourses <= 0 or ncourses > 6:
    print("Error - invalid number of courses")
    ncourses = int(input("Enter the number of courses: "))

while count <= ncourses:
    grade = input("Enter grade: ")
    while grade.lower() not in ["a","b","c","d","f"]:
        print("Invalid letter grade entered")
        grade = input("Enter grade: ")
        
    credit = int(input("Enter number of credits: "))
    while credit < 0:
        print("Error - invalid number of credits")
        credit = int(input("Enter number of credits: "))

    if grade.lower() == "a":
        num = 4
    elif grade.lower() == "b":
        num = 3
    elif grade.lower() == "c":
        num = 2
    elif grade.lower() == "d":
        num = 1
    else:
        num = 0

    count = count + 1
    ncredits = credit + ncredits
    total = num*credit + total

gpa = total/ncredits
print("Your GPA is",round(gpa,3))
