from board import Board
from player import HumanPlayer, RandomPlayer, MinimaxPlayer

class Game:

    __active_player__ = None
    __inactive_player__ = None

    __player_1__ = None
    __player_2__ = None

    __move_symbol__ = {}

    def __init__(self, player_1, player_2, size):

        self.__player_1__ = player_1
        self.__player_2__ = player_2

        self.__board__ = Board(size)

        self.__active_player__ = player_1
        self.__inactive_player__ = player_2

    def switch_turn(self):
        temp = self.__inactive_player__
        self.__inactive_player__ = self.__active_player__
        self.__active_player__ = temp

    def play_game(self):

        game_over = False
        # self.__board__.board = [["O", "X", " "],
        #                         ["X", " ", " "],
        #                         [" ", " ", " "]]
        # self.__board__.possible_moves = [(0,2), (1, 2), (2,0), (2,2)]

        while not game_over:
            print("======== {} turn! ========".format(self.__active_player__.get_name()))
            move = self.__active_player__.move(self.__board__)
            game_over, msg, player = self.__board__.apply_move(self.__active_player__, move)

            if (game_over):
                ending_msg = "><><><><><>< {} ><><><><><><".format(msg)
                print("*" * len(ending_msg))
                print(ending_msg)
                print("*" * len(ending_msg))
            else:
                self.switch_turn()


player1 = HumanPlayer("O")
player2 = MinimaxPlayer("X")
board_size = 3

game = Game(player1, player2, board_size)
game.play_game()