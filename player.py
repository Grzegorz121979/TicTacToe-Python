import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):

    def get_move(self, game):
        square = random.choice(game.available_move())
        return square


class HumanPlayer(Player):

    def get_move(self, game) -> int:
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_move():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class GeniusComputerPlayer(Player):

    def get_move(self, game):
        if len(game.available_move() == 9):
            square = random.choice(game.available_move())
        else:
            square = self.minimax(game, self.letter)
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_square() + 1) if other_player == max_player else -1 * (
                            state.num_empty_square() + 1)
                    }
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
