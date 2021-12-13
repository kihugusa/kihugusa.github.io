# Program 5
# Convert from Centigrade to Fahrenheit or vice versa
temp = float(input("Enter a temperature: "))
degrees = input("Enter the scale (F or C): ").upper()

if degrees == "C":
    temp1 = temp * 9/5 + 32
    degrees1 = "Fahrenheit"
elif degrees == "F":
    temp1 = (temp - 32)*5/9
    degrees1 = "Celsius"
    
print("A temperature of", temp,degrees, "equals", temp1,degrees1,".")
