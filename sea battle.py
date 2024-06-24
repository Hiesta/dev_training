from random import randint


class Ship:
    def __init__(self, length, orientation):
        self.length = length
        self.side = orientation


class Player:
    def __init__(self):
        self.ships = []

    def set_ships(self):
        for _, length in zip(range(6), [3, 2, 2, 1, 1, 1]):
            self.ships.append(Ship(length, input()))


class Board:
    field = [['O']*6]*6

    def get_map(self):
        print('  |', *[f'{i} |' for i in range(1, 7)])
        for i, line in enumerate(self.field):
            print(f'{i+1} | ', end='')
            print(*line, sep=' | ', end=' |\n')


class Notifications:
    @staticmethod
    def move_message():
        print('Your turn, example: (X,Y)')
        print('Make your move!')

    @staticmethod
    def orientation_message():
        return 'Your '


class Move:
    def __init__(self):
        self.messages = Notifications

    def make_move(self):
        self.messages.move_message()
        move = input()  # TODO: DOT CLASS
        print(move.split())  # TODO: DOT REFACT CLASS


test_case1 = Move()
test_case1.make_move()
