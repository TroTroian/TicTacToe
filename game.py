import time
from player import HumanPlayer, RandomComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #use a single list to rep 3*3 board
       #we will need a board for the structure and a list
        self.current_winner = None #keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:   #getting the rows
            print('| ' + '| '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 |  tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + '| '.join(row) + ' |')

    def available_moves(self):
        #return []
        moves = []
        for (i, spot) in enumerate(self.board): #creates a list and assign tuples that have a comma at the value of that index
            #['x', 'x', 'o'] -->[(0, 'x'), 1, 'x'), (2, 'o')] #the for loop will go through each of these truples
            if spot == ' ':
                moves.append(i) #append that index to move
        return moves
            # return [i for i, spot in enumerate(self.board) if spot == ' ']
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
    # if valid move, then make the move (assign square to letter
    # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #winner if 3 in a row anywhere. Check all possibility for diagonal, row and column
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) *3]
        if all ([spot == letter for spot in row]):
            return True

        col_ind = square  % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def play(game, x_player, o_player, print_game = True): #returns the winner of the game(letter)! or None for a tie
        if print_game:
            game.print_board_nums() #which number belongs to which spot
        letter = 'x' #starting letter
        #while the game still has empty squares, keep iterating
        while game.empty_squares():
            if letter == '0':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)

            if game.make_move(square, letter):
                if print_game:
                    print(letter + f' makes a move to square{square}')
                    game.print_board()
                    print('') #just empty line

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    return letter
                letter = '0'if letter == 'x' else 'x'
                #if letter == 'x':
                    #letter = 'o'
                #else:
                #    letter = 'x'
                time.sleep(0.8)
        if print_game:
            print ('it is a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)







