### Assignment 15

# 1) Main function and calcFinalBalance()

def calcFinalBalance(a,b,c):
    for i in range(0,c):
        a = a*(1+b/100)
    print(a)

def main():
    principal = float(input("Enter amount of money to be deposited:"))
    rate = float(input("Enter interest rate as an integer:"))
    years = int(input("Enter the number of years:"))
    
    calcFinalBalance(principal, rate, years)

main()

# 2) Modify so calcFinalBalance() returns final balance to main() and main() prints final out

def calcFinalBalance(a,b,c):
    for i in range(0,c):
        a = a*(1+b/100)
    return a

def main():
    principal = float(input("Enter amount of money to be deposited:"))
    rate = float(input("Enter interest rate as an integer:"))
    years = int(input("Enter the number of years:"))
    
    print(calcFinalBalance(principal, rate, years))
    
main()

# 3) Modify such that main() calls a function to get interest rate from user.

def calcFinalBalance(a,b,c):
    for i in range(0,c):
        a = a*(1+b/100)
    return a

def getIntRate():
    rate = float(input("Enter interest rate as an integer:"))
    while rate <= 0:
        print("Error: interest rate must be greater than 0")
        rate = float(input("Enter interest rate as an integer:"))
    return rate


def main():
    principal = float(input("Enter amount of money to be deposited:"))    
    intRate = getIntRate()
    years = int(input("Enter the number of years:"))
   
    print(calcFinalBalance(principal, intRate, years))
    
main()

# 4) Modify to use called functions to get amount deposited and number of years with data validation
def calcFinalBalance(a,b,c):
    for i in range(0,c):
        a = a*(1+b/100)
    return a


def getDeposit():
    principal = float(input("Enter amount of money to be deposited:"))
    while principal <= 0 or principal >= 100000:
        print("Error: principal must be greater than 0 and less than $100,000")
        principal = float(input("Enter amount of money to be deposited:"))
    return principal


def getIntRate():
    rate = float(input("Enter interest rate as an integer:"))
    while rate <= 0:
        print("Error: interest rate must be greater than 0")
        rate = float(input("Enter interest rate as an integer:"))
    return rate

def getYears():
    years = int(input("Enter the number of years:"))
    while years <= 0:
        print("Error: years must be greater than 0")
        years = int(input("Enter the number of years:"))
    return years


def main():
    intBal = getDeposit()
    intRate = getIntRate()
    intYears = getYears()
   
    print(calcFinalBalance(intBal, intRate, intYears))
    
main()

