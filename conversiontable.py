## Assignment 9

# 1) Conversion table: gallons --> litres

start = float(input("Enter the starting value: "))
end = float(input("Enter the ending value: "))
increment = float(input("Enter the increment: "))

print("Gallons\t\tLiters")

while end >= start:
    liter = start*3.785
    print(start,"\t\t",round(liter,2))
    start = start+increment

# 2) Depreciation table

rate = 4000
eoy = 28000
counter = 1

print("Year\tDepreciation\tEOY Value\tAcc. Dep.")
print("----\t-----------\t---------\t--------")

while eoy > 0:
    eoy = eoy - rate
    print(counter,"\t",rate,"\t\t",eoy,"\t\t",rate*counter)
    counter = counter + 1
    
# 3) Ending Digits

edigit = int(input("Enter Ending Digit: "))
evalue = int(input("Enter Ending Value: "))
counter = 1

while counter <= evalue:
    if str(counter)[-1] == str(edigit):
        print(counter, "Ends in", edigit)
    else:
        print(counter)
    counter = counter+1

### Anything "% 10" returns the first value between 0 and 9
    
