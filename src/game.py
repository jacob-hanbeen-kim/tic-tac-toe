from board import Board
from player import HumanPlayer, RandomPlayer

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

        while not game_over:
            print("======== {} turn! ========".format(self.__active_player__.get_name()))
            game_over, msg = self.__board__.apply_move(self.__active_player__)

            if (game_over):
                ending_msg = "><><><><><>< {} ><><><><><><".format(msg)
                print("*" * len(ending_msg))
                print(ending_msg)
                print("*" * len(ending_msg))
            else:
                self.switch_turn()


player1 = HumanPlayer("O")
player2 = RandomPlayer("X")
board_size = 3

game = Game(player1, player2, board_size)
game.play_game()