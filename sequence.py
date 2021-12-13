##Assignment 11
##
## 1) Sums a sequence of integers from a starting int to an ending int

start = int(input("Enter the starting value: "))
while start <= 0:
    print("Error - invalid number")
    start = int(input("Enter the starting value: "))

end = int(input("Enter the ending value: "))
while end <= start:
    print("Error - invalid number")
    end = int(input("Enter the ending value: "))

step = int(input("Enter the value to skip: "))

total = 0
begin = start

while start <= end:
    total = start + total
    start = start + step

print("The sum of the integers from",begin,"to",end,"skipping",step,"is",total)

## 2) Basketball player data and input end when finished with entering data

lst = []
totalPoints = 0
maximum = []

lname = input("Enter player's last name: ")
avgPoints = int(input("Average points scored last season: "))
games = int(input("Number of games projected for this year: "))
lst.append(lname)
maximum.append(avgPoints*games)
totalPoints = avgPoints*games + totalPoints

while lname != "end":
    lname = input("Enter player's last name: ")
    while lname in lst:
        print("Error - repeated player name")
        lname = input("Enter player's last name: ")

    lst.append(lname)
    
    if lname != "end":
        avgPoints = int(input("Average points scored last season: "))
        games = int(input("Number of games projected for this year: "))
        totalPoints = avgPoints*games + totalPoints

        if avgPoints*games >= max(maximum):
            highscore = avgPoints*games
            name = lname
            maximum.append(avgPoints*games)

    else:
        print("The team is projected to score",totalPoints,"points")
        print("The highest scoring playerer is", name, "scoring",highscore)


### Professor's Solution

maxPoints = 0
teamPoints = 0
names = []

name = input("Enter player's last name: ").lower()
while name != "end":
    names.append(name)
    points = int(input("Enter the average number of points the player scored: "))
    gamesTY = int(input("Enter number of games the player is projected to play this year: "))


    playerPoints = (points*gamesTY)
    teamPoints = teamPoints + playerPoints

    if playerPoints > maxPoints:
        maxPoints = playerPoints
        maxPlayer = name

    name = input("Enter player's last name: ").lower()
    while name in names:
        print("Error - name already entered")
        name = input("Enter player's last name: ").lower()

print("The team is projected to score",teamPoints,"points")
print("The highest scoring player is",maxPlater
    

## 3) Program prompt user for date of birth and the number of days till next birthday

from datetime import date

birthday = input("Enter your birthday MMDDYY: ")
datetoday = date.today()
dateString = datetoday.strftime("%m%d%y")

months = birthday[:2]
days = birthday[2:4]
years = birthday[4:]

tmonths = dateString[:2]
tdays = dateString[2:4]
tyears = dateString[4:]

totalBdays = int(months)*30 + int(days)
totalDays = int(tmonths)*30 + int(tdays)

# Professor Solution
print("The number of dats until your birthday is =", ((totalBdays - totalDays)%360)
#

if totalBdays > totalDays:
    diff = totalBdays - totalDays
    print("The number of days until your birthday is =", diff)
else:
    diff = 360 + (totalBdays - totalDays)
    print("The number of days until your birthday is =", diff)    
                                  



    
    
    
    
