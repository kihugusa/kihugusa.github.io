# 2) An additional check that the power to raise is greater than or
## equal to 0 and less than or equal to 50

problems = int(input("Enter the number of problems: "))
count = 1
correct = 0

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
