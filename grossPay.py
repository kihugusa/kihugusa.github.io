# Program 3
# Gross pay for hourly employees
hours = float(input("What number of hours did you work in the week? "))
wage = float(input("Hourly wage: "))
hourThreshold = 40
excessRate = 1.5 * wage

if hours > hourThreshold:
    pay = (hours - hourThreshold)*excessRate + hourThreshold * wage
else:
    pay = hours * wage

print("My gross pay will be: $",pay)
