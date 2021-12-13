#Problem 1
#Calculating net pay for the week of an hourly worker

workHours = float(input("Enter your work hours: "))
payRate = float(input("Enter your pay rate: "))
grossPay = payRate*workHours
federalTax = 0.25*grossPay
stateTax = 0.15*grossPay
totalDeductions = stateTax + federalTax
print("Gross Pay: $",grossPay)
print("Federal Tax Deducted: $", federalTax)
print("State Tax Deducted: $", stateTax)
print("Total Deductions: $",stateTax+federalTax)
print("Net Pay: $", grossPay-totalDeductions)

