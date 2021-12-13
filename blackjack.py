### Assignment 17

## Black Jack

import random

def randomInt():
    x = random.randint(1,10)
    print("Card dealt:",x)
    return x

    
def get2CardsP():
    valueP = 0
    print("Dealing first two cards to player...")
    for i in range(0,2):
        valueP = valueP + randomInt()
        
    print("Value of player's hand:",valueP)   
    return valueP
    
        
def get2CardsD():
    valueD = 0
    print("Dealing first two cards to dealer...")
    for i in range(0,2):
        valueD = valueD + randomInt()

    print("Value of dealer's hand:", valueD)
    return valueD


def moreCards():
    more = input("Do you want another card? y/n ").lower()
    while more.lower() not in ["y","n"]:
        print("Invalid input -- response should be yes(y)/no(n)")
        more = input("Do you want another card? y/n ").lower()  

    print()
    return more


def outcome(valueP, valueD):
    print("Outcome:")
    print("Player has:",valueP,"and Dealer has:",valueD)

    if valueP > 21:
        print("Player busts, dealer wins.")
    elif valueD > 21:
        print("Dealer busts, player wins.")
    elif valueP >= valueD:
        print("Player wins.")
    elif valueP < valueD:
        print("Dealer wins.")
    
    
def main():

    #Deal out the 2 cards to player and dealer
    p = get2CardsP()
    print()
    d = get2CardsD()
    print()

    #Request for more cards from player
    more = moreCards()
    while more == "y":
        p = p + randomInt()
        print("Value of player's hand:", p)
        print()
        more = input("Do you want another card? y/n ").lower()
        print()

    #Dealer is dealt cards till 17    
    print("Dealer taking card(s).\n")

    while d <= 17:
        d = d + randomInt()
        print("Value of dealer's hand:", d)
        print()


    #Game results
    outcome(p, d)

main()

## Professor's Solution
import random

def dealCard():
    card = random.randint(1,10)
    print("Card dealt:", card)
    return card

def numGames():
    games = int(input("How many games would you like to play?"))
    return games

def startPlayer():
    print("Dealing first two cards to player...")
    
    player = dealCard()
    player = player + dealCard()

    print("Value of player's hand:",player)
    print()
    return player


def startDealer():
    print("Dealing first two cards to dealer...")
    
    dealer = dealCard()
    dealer = dealer + dealCard()

    print("Value of player's hand:",dealer)
    print()
    return dealer

def getPlayerCards(player):
    ans = input("Do you want another card? (y/n) ").lower()

    while ans == "y" and player <= 21:
        player = player + dealCard()

        print("Value of player's hand:",player)
        print()
        
        ans = input("Do you want another card? (y/n) ").lower()
    
    return player


def getDealerCards(dealer):
    print("Dealer taking more card(s).")

    while dealer <= 17:
        dealer = dealer + dealCard()
        print("Value of dealer's hand:", dealer)
        print()
        
    return dealer


def outcome(player,dealer,wins):
    
    print("Outcome:")
    print("Player has:", player, "and the Dealer has:", dealer)

    if player > 21:
        print("Player busts, dealer wins.")
    elif dealer > 21:
        print("Dealer busts, player wins.")
        wins = wins + 1
    elif player >= dealer:
        print("Player wins.")
        wins = wins + 1
    elif dealer > player:
        print("Dealer wins.")
        
    return wins


def report():
    wins = outcome(player, dealer, wins)
    games = numGames()
    loss = games - wins
    print("The player 
    

def main():
    wins = 0
    games = numGames()
    
    for i in range(games):
        player = startPlayer()
        dealer = startDealer()

        if player <= 21 and dealer <= 17:
            dealer = getDealerCards(dealer)

        outcome(player, dealer, wins)

main()








