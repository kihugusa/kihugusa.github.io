# Program 4
# largest of 3 entered values

num1 = float(input("1st Number: "))
num2 = float(input("2nd Number: "))
num3 = float(input("3rd Number: "))
maximum = max(num1, num2, num3)
print("The largest number of the three values is:", maximum)


# Professor Solution
if num1 > num2:
    win = num1
else:
    win = num2

if win > num3:
    print(win)
else:
    print(num3)
