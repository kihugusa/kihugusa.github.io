### Assignment 18

## New lottery
import random

def getGames():
    games = int(input("Enter the number of games: "))
    while games < 0:
        print("Error - the number of games should be greater than 0.")
        games = int(input("Enter the number of games: "))
    return games

def randomInt():
    num = random.randint(1,99)
    print("The wheel landed on", num)
    return num

def getGuess():
    guess = int(input("Enter a number between 1 and 99. "))
    while guess < 1 or guess > 99:
        print("Error - guess must be between 1 and 99.")
        guess = int(input("Enter a number between 1 and 99. "))
    return guess

def getChoice():
    choice = input("Do you wish to spin the wheel for your prize (y/n)? ").lower()
    while choice not in ["y","n"]:
       print("Invalid choice. Must be yes(y) or no(n).")
       choice = input("Do you wish to spin the wheel for your prize (y/n)? ").lower()
    return choice              

def getPrize(x, guess):

    if guess == x:
        pay = max(2500, guess * x)
        print("You win", pay)
    elif guess <= (x+10) and guess >= (x-10):
        choice = getChoice()   
        if choice == "y":
            x = randomInt()
            pay = x * 20
        else:
            pay = 750
            
        print("You win", pay)  
    else:
        print("You lose.")
        pay = 0

    return pay
    
def main():
    total = 0
    games = getGames()
    print()
    for i in range(games):
        guess = getGuess()
        x = randomInt()
        prize = getPrize(x, guess)
        print()
        total = total + prize
    

    print("Your total for",games,"games is $", total)
    
main()


## Professor's solution
import random

def games():
    numGames = int(input("Enter the number of games: "))
    while numGames < 0:
        print("Error - number of games should be more than 0")
        numGames = int(input("Enter the number of games: "))
    return numGames

def spinWheel():
    spin = random.randint(1,99)
    print("The wheel landed on", spin)

    return spin


def getGuess():
    guess = int(input("Enter your guess: "))
    while not 1 <= guess <= 99:
        print("Error - invalid guess")
        guess = int(input("Enter your guess: "))

    return guess


    
def playgame():
    guess = getGuess()
    spin = spinWheel()

    if guess == spin:
        if (guess*50) > 2500:
            result = 50*2500
        else:
            result = 2500
    else:
        diff = guess - spin
        if diff >= -10 and diff <= 10:
            ans = input("Do you wish to spin the wheel for the prize (y/n)? ").lower()
            while ans != "y" and ans != "n":
                print("Error = invalid value")
                ans = input("Do you wish to spin the wheel for the prize (y/n)? ").lower()

            if ans == "y":
                spin1 = spinWheel()
                while spin1 == spin:
                    print("Error - the same number",spin1,"has already been spun")
                    spin1 = spinWheel()

                result = spin1 * 20
            else:
                result = 750

    if result == 0:
        print("You lose.")
    else:
        print("You win", result)
    return result

def main():
    numGames = games()        
    winnings = 0

    for i in range(numGames):
        result = playgame()
        winnings = winnings + result

    print("Your total for",numGames,"is $", winnings)

main()







