from random import randint


class Notifications:
    @staticmethod
    def move_message():
        print('Your turn, example: (X,Y)')
        print('Make your move!')

    @staticmethod
    def orientation_message():
        return 'What type of {0} point ship do you want?\nH/V: '


class Ship:
    def __init__(self, length=1, orientation='H'):
        self.length = length
        self.side = orientation

    def __str__(self):
        return f'Ship {self.length} dot length. {self.side} orientation'


class Player:
    message = Notifications()

    def __init__(self):
        self.ships = []

    def set_ships(self):
        for _, length in zip(range(6), [3, 2, 2]):
            self.ships.append(Ship(length, input(self.message.orientation_message().format(length))))
        for i in range(3):
            self.ships.append(Ship())

    def get_ship_info(self):
        for ship in self.ships:
            print(ship)


class Board:
    ally_board = [['O'] * 6] * 6
    enemy_board = ally_board.copy()

    def get_ally_map(self):
        print('  |', *[f'{i} |' for i in range(1, 7)])
        for i, line in enumerate(self.ally_board):
            print(f'{i+1} | ', end='')
            print(*line, sep=' | ', end=' |\n')


class Dot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            raise ValueError('This point is already placed')
    def moving(self):
        move = input()



class Move:
    def __init__(self):
        self.messages = Notifications

    def make_move(self):
        self.messages.move_message()
        move = input()  # TODO: DOT CLASS
        print(move.split())  # TODO: DOT REFACT CLASS


class Game(Player):

    def setup_ships(self):
        for ship in self.ships:



test = Board()
test.get_ally_map()