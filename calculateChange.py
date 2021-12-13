#Problem 2
purchasePrice = int(input("How much does the item cost (in cents)? "))
change = 100-purchasePrice
print("You should get",change,"cents back.")
quarters = change//25
dimes = (change%25)//10
nickels = ((change%25)%10)//5
pennies = (((change%25)%10)%5)
print("Your change is",quarters,"quarter(s),",dimes,"dime(s),",nickels,"nickel(s) and",pennies,"penny/pennies.")

