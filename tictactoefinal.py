"""
Alvin Tang and Isobel Lees

Tic Tac Toe Game for Project Include
Albion Library July 3 to July 7
"""

from random import randint

def genBoard():
    """
    Generates an empty board.
    
    >>> genBoard()
    ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    """
    
    # Empty board
    empty = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    
    # Return it
    return empty

def boardIsFull(board):
    """
    Checks if the board is full.
    
    >>> boardIsFull(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
    False
    >>> boardIsFull(["x", "o", "x", "o", "x", "o", "x", "o", "x"])
    True
    >>> boardIsFull(["x", "o", "C", "o", "x", "o", "x", "o", "x"])
    False
    """
    
    # Assume board is full
    isFull = True
    
    # Empty board
    empty = genBoard()
    
    # Loop through the board to see if any part of the board is still empty
    for i in range(len(board)):
        if(empty[i-1] == board[i-1]):
            isFull = False
    
    # Return if is full
    return isFull

def printBoard(board):
    """
    Prints the board using an exisiting list.
    """
    
    print (str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2])
           + '\n--|---|---'
           + '\n' + str(board[3])+' | ' + str(board[4])+' | ' + str(board[5])
           + '\n--|---|---'
           + '\n' + str(board[6])+' | ' + str(board[7])+' | ' + str(board[8]))


def replace(board, old, replaceWith):
    """
    Replaces a character in the board.
    replace(LIST, CHARACTER, CHARACTER TO REPLACE IT WITH)
    
    >>> replace(["A", "B"], "B", "X")
    ["A", "X"]
    """
    
    # Loops through every index of the board
    for x in range(len(board)):
        # If the current index in the board list matches with the one you want
        # to replace, then replace it with the new one
        if(board[x-1] == old):
            board[x-1] = replaceWith
    
    # Return the changed board
    return board

def checkWin(board):
    """
    Check if there are any wins.
    """
    
    # By default, say there is not winner
    winexists = False
    
    # All possible options to wins tested
    if(board[0] == board[1] and board[1] == board[2]):
        winexists = True
    elif(board[3] == board[4] and board[4] == board[5]):
        winexists = True
    elif(board[6] == board[7] and board[7] == board[8]):
        winexists = True
    elif(board[2] == board[4] and board[4] == board[6]):
        winexists = True
    elif(board[0] == board[4] and board[4] == board[8]):
        winexists = True
    elif(board[2] == board[5] and board[5] == board[8]):
        winexists = True
    elif(board[1] == board[4] and board[4] == board[7]):
        winexists = True
    elif(board[0] == board[3] and board[3] == board[6]):
        winexists = True
        
    return winexists

def winner(board):
    """
    Check if there are any wins. Use only when checkWin() is True.
    """
    
    print("NEEDS TO BE COMPLETED")

def playOne():
    """
    Start a new multiplayer tic tac toe game. 2 players are needed.
    Set player 0 with O and player 1 with X.
    """
    
    # Generate the board
    board = genBoard()
    
    # Whose turn it is, by default it is player 0.
    turn = 0
    
    # Print welcome statement
    print("Welcome to Tic Tac Toe. (2 Players)\n")
    
    # Check if there is a win
    print("NEEDS TO BE COMPLETED")
        
def randomPlay(board, character):
    """
    Gets a board and puts in a valid action with character.
    """
    
    notValid = True
    random = randint(0, 8)
    empty = genBoard()
    
    while notValid:
        if(board[random] == empty[random]):
            notValid = False
            board[random] = character
        random = randint(0, 8)
            
    return board

def playTwo():
    """
    Start a new tic tac toe game with only 1 player necessary.
    Set player 0 with O and player 1 (the computer) with X.
    """
    
    # Generate the board
    board = genBoard()
    
    # Whose turn it is, by default it is player 0.
    turn = 0
    
    # Print welcome statementd
    print("Welcome to Tic Tac Toe (1 Player).\n")
    
    # Check if there is a win
    while not checkWin(board) and not boardIsFull(board):
        printBoard(board)
        if(turn == 0):
            print("\nPlayer O's turn.")
            move = input("Type in the letter that you want to take over. ")
            while(not (move in board)):
                move = input("Invalid. Please type in the letter that you want "
                               + " to take over. ")
            board = replace(board, move, "O")
            turn = 1
        else:
            print("\nPlayer X is playing their move...")
            # Generates a random play by the computer and returns the board
            board = randomPlay(board, "X")
            turn = 0

    if(checkWin(board)):   
        print("\n")
        printBoard(board)
        print("\nThe winner is player " + winner(board))
    else:
        print("\nIt is a tie.")
        
def play():
    
    print("Welcome. Which one do you want to play?")
    print("1. Tic Tac Toe (1 vs 1)")
    print("2. Tic Tac Toe (1 vs computer)")
    print("Type q to quit")
    option = input("Choose an option. ")
    
    while(option != "q"):
        if (option == "1"):
            playOne()
            print("Welcome. Which one do you want to play?")
            print("1. Tic Tac Toe (1 vs 1)")
            print("2. Tic Tac Toe (1 vs computer)")
            print("Type q to quit")
            option = input("Choose an option. ")
        elif (option == "2"):
            playTwo()
            print("Welcome. Which one do you want to play?")
            print("1. Tic Tac Toe (1 vs 1)")
            print("2. Tic Tac Toe (1 vs computer)")
            print("Type q to quit")
            option = input("Choose an option. ")
        else:
            option = input("Invalid. Choose an option. ")
            
play()