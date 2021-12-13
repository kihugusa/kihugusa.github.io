# Program 1
# Calculate the monthly income of a salesperson with a commission schedule

sales = float(input("What were your monthly sales? $"))

if sales >= 50000:
    income = 375 + 0.16 * sales
elif sales >= 40000:
    income = 350 + 0.14 * sales
elif sales >= 30000:
    income = 325 + 0.12 * sales
elif sales >= 20000:
    income = 300 + 0.09 * sales
elif sales >= 10000:
    income = 250 + 0.05 * sales
else:
    income = 200 + 0.03 * sales

print("Your income this month is $", income)


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


# Program 3
# Evaluates basketball player's performance

pos = input("Enter your position (g, f, c): ").lower()
score = float(input("Enter your points per game: "))
rebound = float(input("Enter your rebounds per game: "))
g_avg_score = 5.1
g_avg_rebound = 1.3
f_avg_score = 4.2
f_avg_rebound = 2.2
c_avg_score = 3.1
c_avg_rebound = 3.3

if pos == "g":
    points = score*g_avg_score + rebound*g_avg_rebound
elif pos == "f":
    points = score*f_avg_score + rebound*f_avg_rebound
elif pos == "c":
    points = score*c_avg_score + rebound*c_avg_rebound

if points >= 100:
    rating = "Excellent"
elif points >= 85:
    rating = "Good"
elif points >= 70:
    rating = "Fair"
else:
    rating = "Poor"

print("Your rating is:", rating)


