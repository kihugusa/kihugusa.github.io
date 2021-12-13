### Assignment 22

# 1) Nested List
import random


board = []

SIZE = 3


def assignValues():
    global board, SIZE
    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            row.append(random.randint(0,9))
        board.append(row)

def printBoard():
    global board, SIZE
    print(board)

def calcSumRow(row):
    global board, SIZE

    sumRow = 0
    for i in board[row]:
        sumRow = i + sumRow
    print("The total of row",i,"is:",sumRow)

def calcSumCol(col):
    global board,SIZE

    sumCol = 0
    for i in range(SIZE):
        sumCol = sumCol + board[i][col]
    print("The total of column",i,"is:",sumCol)       

def calcSumDiag1():
    global board, SIZE

    sumDiag1 = 0
    for i in range(SIZE):
        sumDiag1 = sumDiag1 + board[i][i]
        
    print("The total of the diagonal from top-left to bottom-right is:",sumDiag1)

     
def calcSumDiag2():
    global board, SIZE

    sumDiag2 = 0
    for i in range(SIZE):
        sumDiag2 = sumDiag2 + board[i][SIZE - i - 1]

    print("The total of the diagonal from top-right to bottom-left is:",sumDiag2)

def printBoard():
    global board, SIZE
    for i in range(SIZE):
        for j in range(SIZE):
            print(board[i][j], end=" ")
        print("\n")

    
def main():
    global board, SIZE
    assignValues()
    print("Printing board after random values have been assigned:\n")
    printBoard()

    for i in range(SIZE):
        calcSumRow(i)
        calcSumCol(i)

    calcSumDiag1()
    calcSumDiag2()
       
main()
