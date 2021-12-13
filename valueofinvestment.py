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




