import math
import random

class Player:       #base player class
    def __init__(self, letter):         #initialise the class with the letter the player will use x or o
        self.letter = letter

    # all players to get their next move
    def get_move(self, game):
        pass    #use inheritance in order to create a random computer and human player

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves()) #gets a random valid spot for our next moves
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            # we are going to check that this is a correct value by trying to cast
            # it to an interger and if it is not then we say it is invalid
            # if that spot is not available on the board, we also say it is invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #if successful
            except ValueError:
                print('Ínvalid square. Try again')
        return val

