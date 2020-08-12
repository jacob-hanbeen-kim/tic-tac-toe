from random import randint
import random

class Player:
    def __init__(self, symbol, name="Player"):
        self.name = name
        self.symbol = symbol

    def move(self, game):
        pass

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

class RandomPlayer(Player):
    """Player that chooses a move randomly."""
    def __init__(self, symbol, name="RandomPlayer"):
        super().__init__(symbol, name)

    def move(self, game):
        if not game.get_possible_move():
            return None
        else:
            return random.choice(game.get_possible_move())

class HumanPlayer(Player):
    """
    Player that chooses a move according to user's input. 
    (Useful if you play in the terminal)
    """
    def __init__(self, symbol, name="HumanPlayer"):
        super().__init__(symbol, name)

    def move(self, game):
        legal_moves = game.get_possible_move()
        choice = {}

        if not len(legal_moves):
            print("No more moves left.")
            return None

        counter = 1
        for move in legal_moves:
            choice.update({counter: move})
            print('\t'.join(['[%d] (%d,%d)' % (counter, move[0], move[1])]))
            counter += 1

        valid_choice = False

        while not valid_choice:
            try:
                index = int(input('Select move index [1-' + str(len(legal_moves)) + ']:'))
                print("")
                valid_choice = 1 <= index <= len(legal_moves)

                if not valid_choice:
                    print('Illegal move of queen! Try again.')
            except Exception:
                print('Invalid entry! Try again.')

        return choice[index]

class MiniMax(Player):
    """
    This player will try to beat Player in the game.
    """
    def __init__(self, symbol, name="MiniMax"):
        super().__init__(symbol,move)

    def move(self, game):
        pass