class Board:

    BLANK = " "
    PLAYER1_SYMBOL = "X"
    PLAYER2_SYMBOL = "O"

    def __init__(self, size=3):
        self.size = size
        print('Created board of size: {}'.format(self.size))
        self.createGameBoard()

    def createGameBoard(self):
        self.board = [[Board.BLANK for i in range(0, self.size)] for j in range(0, self.size)]
        self.possible_moves = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                self.possible_moves.append((i,j))

        self.not_possible_moves = []

    def get_possible_move(self):
        return self.possible_moves

    def apply_move(self, player):
        move = player.move(self)
        if move in self.possible_moves:
            symbol = player.get_symbol()
            name = player.get_name()

            print("** {} placed '{}' on {} ** \n".format(name, symbol, move))

            self.board[move[0]][move[1]] = symbol
            self.possible_moves.remove(move)
            
            self.printBoard()
            print("")

            if self.__check_game_state__(move, symbol):
                return True, player.get_name() + ' WIN!', player
            else:
                if (not self.possible_moves):
                    return True, 'DRAW :(((((((', None
        else:
            return True, 'Error. Invalid move!'

        return False, '', None

    def __check_game_state__(self, move, symbol):
        i = move[0]
        j = move[1]

        vertical = True
        horizontal = True
        diagonal_1 = i == j
        diagonal_2 = i + j == self.size - 1
        for s in range(self.size):
            vertical = vertical and self.board[s][j] == symbol
            horizontal = horizontal and self.board[i][s] == symbol
            diagonal_1 = diagonal_1 and self.board[s][s] == symbol
            diagonal_2 = diagonal_2 and self.board[s][self.size - 1 - s] == symbol

        return vertical or horizontal or diagonal_1 or diagonal_1


    def printBoard(self):
        out = '   '
        for i in range(len(self.board[0])):
            out += str(i) + ' '
        out += '\n\r'

        for i in range(len(self.board)):
            out += str(i) + ' |'
            for j in range(len(self.board[i])):
                out += self.board[i][j] + '|'

            if i != len(self.board) - 1:
                out += '\n\r'

        print(out)