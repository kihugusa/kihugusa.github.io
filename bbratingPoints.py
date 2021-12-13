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
