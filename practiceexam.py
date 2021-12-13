### Practice Exam

#1) Compares investment returns over a number of years

import random

def getYears():
    year = int(input("Enter the number of years: "))
    while year < 0:
        print("Error - invalid year input")
        year = int(input("Enter the number of years:" ))
    return year

def getFixed():
    fixed = float(input("Enter the fixed rate: "))
    while fixed < 1 or fixed > 20:
        print("Error - invalid fixed rate input")
        fixed = float(input("Enter the fixed rate: "))
    return fixed

def getRandom():
    x = random.randint(-100,100)
    return x

def main():
    years = getYears()
    randReturn = []
    initial = int(input("Enter the initial investment:" ))
    initialF = initial
    fRate = (getFixed()/100)
    print("Year\tR-Rate\tR-Return\t\tF-Rate\tF-Return")
    for i in range(1,years+1):
        rRate = (getRandom()/100)
        initialF = round(initialF*(1+fRate),3)
        initial = round(initial*(1+rRate),3)
        print(i,"\t",rRate,"\t",initial,"\t\t",fRate,"\t",initialF)
        randReturn.append(initial)
    print("The maximum random return:",round(max(randReturn),2))
    print("The average random return:",round(sum(randReturn)/len(randReturn),2))
    
main()

