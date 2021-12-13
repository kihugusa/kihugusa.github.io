import random  

def intro():
    print("Welcome to the coin toss game.")
    numGames = int(input("Enter the number of games to play: "))
    while numGames <=0:
        print("Invalid input - enter a positive number.")
        numGames = int(input("Enter the number of games to play: "))

    print("")
    return numGames

def getGuess():
    guess=int(input("Enter your guess - 0 for heads, 1 for tails: "))
    while guess not in [0,1]:  #guess !=0 and guess != 1:
        print("Invalid input")
        guess=int(input("Enter your guess - 0 for heads, 1 for tails: "))
    
    return guess

def getFlip():
    flip = random.randint(0,1)
    if flip == 0:
        print("The flip is tails.")
    else:
        print("The flip is heads.")
    return flip

def summary(wins,times,wbets,lbets):
    print("The coin was flipped",times,"times.")
    print("You guess correctly",wins,"time(s).")
    print("Your percentage correct is:",round((wins/times)*100,2),"%")
    print("You won $"+str(wbets))
    print("You lost $"+str(lbets))
    print("You netted $" + str(wbets - lbets))

def getBet():
    bet = int(input("Enter your bet:"))
    while bet <= 0 or bet >= 500:
        print("Error - bet must greater than 0 or less than 500")
        bet = int(input("Enter your bet:"))
    return bet

def main():

    numWins=0
    wbets = 0
    lbets = 0
    
    numGames=intro()

    for i in range(0,numGames):
        bet = getBet()
        guess=getGuess()
        flip=getFlip()
        if guess==flip:
            print("Correct guess.\n")
            numWins=numWins+1
            wbets = wbets + bet
        else:
            print("Incorrect guess\n")
            lbets = lbets + bet

    summary(numWins,numGames,wbets,lbets)

    
main()    


