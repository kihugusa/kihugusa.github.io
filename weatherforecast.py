# 2) Weather Forecast

color = input("What is the color, red or blue? ").lower()
mode = input("Is the light flashing or steady? ").lower()

if color == "red":
    if mode == "flashing":
        print("The forecast is snow instead.")
    else:
        print("The forecast is rain ahead.")
else:
    if mode == "flashing":
        print("The forecast is clouds due.")
    else:
        print("The forecast is clear view.")
    
