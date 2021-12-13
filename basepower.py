## Assignment 10

### 1) Test user's understanding of raising a number to a power

count = 1
correct = 0

problems = int(input("Enter the number of problems: "))
while problems < 0:
    print("Error",problems,"is an invalid number of problems")
    problems = int(input("Enter the number of problems: "))

while count <= problems:
    base = float(input("Enter the number: "))
    power = float(input("Enter the power: "))
    ans = float(input("Enter your answer: "))

    if ans == base**power:
        print("You got it")
        correct = correct + 1
    else:
        print("Incorrect - the correct answer is ", int(base**power))
    
    count = count + 1
print("You got", correct, "out of", problems, "problems correct")

# 2) An additional check that the power to raise is greater than or
## equal to 0 and less than or equal to 50

count = 1
correct = 0

problems = int(input("Enter the number of problems: "))
while problems < 0:
    print("Error",problems,"is an invalid number of problems")
    problems = int(input("Enter the number of problems: "))

while count <= problems:
    base = float(input("Enter the number: "))
    power = float(input("Enter the power: "))
    while power < 0 or power > 50:
        print("Error - the power must be 0 or greater")
        power = float(input("Enter the power: "))
        
    ans = float(input("Enter your answer: "))
    
    if ans == base**power:
        print("You got it")
        correct = correct + 1
    else:
        print("Incorrect - the correct answer is ", int(base**power))
    
    count = count + 1
print("You got", correct, "out of", problems, "problems correct")


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
    while credit < 1 or credit > 4:
        print("Error - invalid number of credits")
        credit = int(input("Enter number of credits: "))

    ## Professor's Solution - using "index"
    grades = "FDCBA"
    grade = "B"
    grades.index("B")

    num = "FDCBA".index(grade)



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


    
    

    

