### Assignment 13
## 1) Deck of cards

suits = ["hearts","diamonds","spades","clubs"]
ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

for rank in ranks:
    for suit in suits:
        print(rank,"of",suit)
    print("\n") 


## 2) Savings account revisited

rates = [0.03,0.04,0.05]
principal = 1000

for rate in rates:
    print("Interest rate of", int(rate*100),"%:")
    for year in range(1,6):
        print("Balance after year",year,"is $",round(principal*(1+rate)**int(year),2))
    print("\n")

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
