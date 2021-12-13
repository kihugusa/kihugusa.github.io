### Assignment 14

## 1) Calculate weekly pay for workers

def printInfo():
    print("This program calculates the weekly pay for hourly workers.")
    print("Workers get\"time and a half\" for overtime.")
    print("That is, for all hours worked above 40, they get paid at 1.5 times their regular hourly rate.")
    print("Enter the number of workers for whom pay is to be calculated.")
    print("Then, for each worker, enter the hourly pay rate and the number of hours worked.\n")

def main():
    printInfo()
    workers = int(input("How many workers? "))
    print()

    for worker in range(1, workers+1):
        rate = float(input("Enter the hourly pay rate for worker "+str(worker)+": "))
        hours = float(input("Enter the number of hours worked for worker "+str(worker)+": "))

        if hours > 40:
            print("This week's pay: $", round(40*rate + (hours-40)*1.5*rate,2))
        else:
            print("This week's pay: $", round(rate*hours,2))
        
main()

## 2) Value of an investment
principal = int(input("Enter the principal amount: "))
years = int(input("Enter number of years: "))

investment = principal
for year in range(1,years+1):
    rate = float(input("Enter interest rate(decimal number) for year "+str(year)+":"))
    while rate <= 0 or rate >= 0.1:
        print("Error - invalid interest rate")
        rate = float(input("Enter interest rate for year "+str(year)+":"))
    investment = investment*(1+rate/365)**365

print("Your investment in "+str(years)+" years will be: "+str(round(investment,2)))



