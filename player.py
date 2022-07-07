import math
import random


class Player:       # base player class
    def __init__(self, letter):         # initialise the class with the letter the player will use x or o
        self.letter = letter

    # all players to get their next move
    def get_move(self, game):
        pass    # use inheritance in order to create a random computer and human player


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())   # gets a random valid spot for our next moves
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            # 0-9 is the number that the players have to put in
            # we are going to check that this is a correct value by trying to cast
            # it to an integer and if it is not then we say it is invalid
            # if that spot is not available on the board, we also say it is invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if successful
            except ValueError:
                print('Invalid square. Try again')
        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:  # if all the spaces are available, grab a random spot.
            square = random.choice(game.available_moves())
        else:
            # if not all the spaces are available, get the square based on the minmax algorithms
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):  # It is state because it is a rep of the state of the game at the moment.
        max_player = self.letter  # yourself (you want to maximize your score)
        other_player = '0' if player == 'X' else 'X'  # whatever the self.letter is not

        # check if the previous moves is a winner
        # this is a base case (recursion)
        if state.current_winner == other_player:         # return position and the score
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}

        elif not state.empty_squares():  # no empty squares
            return{'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}   # each score should maximize/be larger
        else:
            best = {'position': None, 'score': math.inf}   # each score should minimize

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurse using minimax to stimulate a game after making that move
            sim_score = self.minimax(state, other_player)  # alternating players
            # step 3: undo the move for future iteration
            state.board[possible_move] = ' '
            state.current_winner = None  # undoing the move we just made
            sim_score['position'] = possible_move  # otherwise this will get messed up from the recursion
            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score    # replace with best dictionary

            else:
                if sim_score['score'] < best['score']:
                    best = sim_score  # replace best

        return best




