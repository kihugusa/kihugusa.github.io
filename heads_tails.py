### Assignment 16

 1) Heads/Tails

import random

def gameRules():
    print("Welcome to the coin toss game.")
    print("\t1) The computer will ask the player to call heads or tails.")
    print("\t2) The computer will simulate the flip of a coin.")
    print("\t3) If the outcoem of the flip matches the guess, the player wins otherwise the computer wins the game.\n")

def main():
    gameRules()
    correct = 0
    games = int(input("Enter the number of games:"))
    while games <= 0:
        print("Error - the number of games must be greater than 0")
        games = int(input("Enter the number of games:"))
    
    for i in range(0,games):
        guess = int(input("Enter your guess - 0 for heads, 1 for tails:"))
        while guess != 0 and guess != 1:
          print("Error - the guess must be 0 for heads or 1 for tails.")
          guess = int(input("Enter your guess - 0 for heads, 1 for tails:"))

        x = random.randint(0,1)
        print("The flip is", x)
        if guess == x:
            correct = correct + 1
            print("Correct guess.")
        else:
            print("Incorrect guess.")

    print("The coin was flipped "+str(games)+" times.")
    print("You guessed correctly "+str(correct)+" time(s).")
    print("Your percentage correct is: " + str(round(correct*100/games,2))+"%.")

main()

# Professor's Solution

import random

def intro():
    print("Welcome to coin toss game.")
    numGames = int(input("Enter the number of games:"))
    return numGames

def getGuess():
    guess = int(input("Enter your guess - 0 for heads, 1 for tails:"))
    while guess not in [0,1]:
    #while guess not(guess == 0 or guess == 1):
        print("Error - the guess must be 0 for heads, 1 for tails.")
        guess = int(input("Enter your guess - 0 for heads, 1 for tails."))
    return guess

def getFlip():
    flip = random.randint(0,1)       
    if flip == 0:
        print("The flip is heads.")
    else:
        print("The flip is tails.")
    return flip

def summary(numGames, correct):
    print("The coin was flipped "+str(numGames)+" times.")
    print("You guessed correctly "+str(correct)+" time(s).")
    print("Your percentage correct is:",round((correct*100/numGames),2),"%")
    
    
def main():
    numGames = intro()
    correct = 0
    
    for i in range(numGames):    
        guess = getGuess()
        flip = getFlip()
        if guess == flip:
            print("Correct guess.")
            correct = correct + 1
        else:
            print("Incorrect guess.")

    summary(numGames, correct)

main()

    

