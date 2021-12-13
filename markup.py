purchasePrice = float(input("Enter the purchase price: "))
sellingPrice = float(input("Enter the selling price: "))

markup = round(sellingPrice - purchasePrice,2)
percentageMarkup = round((markup/purchasePrice)*100,2)
profitMargin = round((markup/sellingPrice)*100,2)

print("Markup: $", markup)
print("Percentage Markup:", percentageMarkup, "%")
print("Profit Margin:", profitMargin, "%")
