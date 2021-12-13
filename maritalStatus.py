# Program 2
# Ask user for marital status

marital = input("What is your marital status(s,m,d,w)? ").lower()

if marital == "s":
    status = "single"
elif marital == "m":
    status = "married"
elif marital == "d":
    status = "divorced"
elif marital == "w":
    status = "widowed"
else:
    status = "You have entered an unrecognizable marital status"

print("You are", status)
