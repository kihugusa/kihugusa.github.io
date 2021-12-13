## 2) Savings account revisited

rates = [0.03,0.04,0.05]
principal = 1000

for rate in rates:
    print("Interest rate of", int(rate*100),"%:")
    for year in range(1,6):
        print("Balance after year",year,"is $",round(principal*(1+rate)**int(year),2))
    print("\n")
