from board import Board
from player import Player

def minimax (board, active_player, move):

    if (move):
        game_ended, msg, winner = board.apply_move(active_player, move)
    else:
        game_ended = False

    if (game_ended):
        return score(winner)

from random import randint
import random
def score(winner):
    s = [-1, 0, 1]
    return random.choice(s)


board = Board(3)
playerMax = Player("maximizing")
playerMin = Player("minimizing")

minimax(board, playerMax, None)

    


