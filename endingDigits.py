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
