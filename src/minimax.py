from board import Board
from copy import copy, deepcopy

# from player import Player

def getBestMove(game, symbol):

    board = deepcopy(game.get_board())
    possible_moves = game.get_possible_move()[:]
    depth = 1

    isMaximizing = True
    if (symbol == "X"):
        isMaximizing = False

    bestMove = None
    if (isMaximizing):
        bestScore = float("-inf")
    else:
        bestScore = float("inf")

    for m in possible_moves:
        pm = possible_moves[:]
        pm.remove(m)

        curScore, curMove = minimax(deepcopy(board), m, pm, isMaximizing, depth)
        
        # If maximizing, check if curScore is higher than bestScore, and replace
        if (isMaximizing):
            if (curScore > bestScore):
                bestScore = curScore
                bestMove = m
        else: # If minimizing, check if curScore is lower than bestScore, and replace
            if (curScore < bestScore):
                bestScore = curScore
                bestMove = m

    return bestMove


def minimax (board, move, possible_moves, isMaximizing, depth):

    # Maximizing player = "O" and Minimizing player = "X"
    symbol = "X"
    if (isMaximizing):
        symbol= "O"

    # Apply the move to the board
    i, j = move
    board[i][j] = symbol
    depth += 1

    # print("=============")
    # print(isMaximizing)
    # print(depth)
    # print(move)
    # print(board[0])
    # print(board[1])
    # print(board[2])
    # print("=============")
    # Check if game is won by current player. If yes, return score and move
    if(checkBoard(board, move, symbol)):
        return getScore(isMaximizing, depth), move

    # Check if there is no more possible move. Draw - return 0 and move
    if (not possible_moves):
        return 0, move

    # Iterate through each possible move to determine bestScore and bestMove
    bestMove = None
    if (isMaximizing):
        bestScore = float("-inf")
    else:
        bestScore = float("inf")

    for m in possible_moves:

        pm = possible_moves[:]
        pm.remove(m)

        # Recurse with move m and switch the isMaximizing
        curScore, curMove = minimax(deepcopy(board), m, pm, not(isMaximizing), depth)

        # If maximizing, check if curScore is higher than bestScore, and replace
        if (isMaximizing):
            if (curScore > bestScore):
                bestScore = curScore
                bestMove = curMove
        else: # If minimizing, check if curScore is lower than bestScore, and replace
            if (curScore < bestScore):
                bestScore = curScore
                bestMove = curMove

    return bestScore, bestMove

def checkBoard(board, move, symbol):
    i = move[0]
    j = move[1]
    size = len(board)

    vertical = True
    horizontal = True
    diagonal_1 = i == j
    diagonal_2 = i + j == size - 1
    for s in range(size):
        vertical = vertical and board[s][j] == symbol
        horizontal = horizontal and board[i][s] == symbol
        diagonal_1 = diagonal_1 and board[s][s] == symbol
        diagonal_2 = diagonal_2 and board[s][size - 1 - s] == symbol

    return vertical or horizontal or diagonal_1 or diagonal_2

def getScore(isMaximizing, depth):
    if (isMaximizing):
        return 100 / (10 ** (depth - 1))
    else:
        return -100 / (10 ** (depth - 1))

