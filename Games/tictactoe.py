# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 09:44:23 2018

@author: ShirleyLiu
"""
# Ask player whether they want to play X or O
# randomly choose who play first

import random

# Display the Board as data
# 	7|8|9
# 	4|5|6
# 	1|2|3
# ' '-- None,'X'--X,'O'--O
# Create a list 'Board[10]' to store charator in each position
# from Board[1] to Board[9], without using Board[0]

def drawBoard(board):
    #draw board according present List:Board

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player's letter, the second is the computer's letter.
    if letter=='X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def guessAgain():
    print('Do you want to guess again? (yes or no)')
    return input().lower().startswith('y')

# letter: 'X' or 'O'
# List reference: function parameter in python is default: pass reference
def makeMove(board,letter,move):
    board[move] = letter

def isWinner(bo,le):# True: win
    #bo:board, le:letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

# There are times that we will
# want our AI algorithm to make temporary modifications to a temporary copy of the board
# without changing the original board. In that case, we call this function to make a copy of the
# board's list.
def getBoardCopy(board):
    # Make a copy of the board list and return it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    # whether move is invalid
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMove = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMove.append(i)

    if len(possibleMove) != 0:
        return random.choice(possibleMove)
    else:
        return None

# # AI algorithm
# 1. First, see if there is a move the computer can make that will win the game. If there is,
# take that move. Otherwise, go to step 2.
# 2. See if there is a move the player can make that will cause the computer to lose the
# game. If there is, we should move there to block the player. Otherwise, go to step 3.
# 3. Check if any of the corner spaces (spaces 1, 3, 7, or 9) are free. (We always want to
# take a corner piece instead of the center or a side piece.) If no corner piece is free,
# then go to step 4.
# 4. Check if the center is free. If so, move there. If it isn't, then go to step 5.
# 5. Move on any of the side pieces (spaces 2, 4, 6, or 8). There are no more steps,
# because if we have reached step 5 the side spaces are the only spaces left.

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # check if there are steps that will lead computer win
    for  i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,computerLetter,i)
            if isWinner(copy,computerLetter):
                return i

    # check if the player will win in the next step, and block them
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,playerLetter,i)
            if isWinner(copy,playerLetter):
                return i

    # Try to take ine of the corner
    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

################### Main ################################

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter,move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break