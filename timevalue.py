## 3) Time value of money

balance = float(input("Enter starting balance: $"))
srate = int(input("Enter starting interest rate: "))
erate = int(input("Enter ending interest rate: "))
while erate <= srate:
    print("Error - ending rate must be greater than starting rate")
    erate = int(input("Enter ending interest rate: "))
years = int(input("Enter number of years: "))

for i in range(srate,erate+1):
    print("Interest rate of", i, "%:")
    print("Balance after year", years,"is $", round(balance*(1+i/100)**years,2))
    print()
