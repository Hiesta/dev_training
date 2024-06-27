from random import randint
ally_board = [['O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', 'O'],]
print(ally_board)


class Notifications:
    @staticmethod
    def move_message():
        print('Your turn, example: (X,Y)')
        print('Make your move!')

    @staticmethod
    def orient_message():
        return 'What type of {0} point ship do you want?\nH/V: '

    @staticmethod
    def placement_message():
        return 'Choose point, where you want to place your ship\nExample (X,Y): '


class Ship:
    message = Notifications()

    def __init__(self, length=1, orientation='H'):
        self.length = length
        self.side = orientation

    def __str__(self):
        return f'Ship {self.length} dot length. {self.side} orientation'


class Player:
    message = Notifications()

    def __init__(self):
        self.ships = []

    def get_ship_info(self):
        for ship in self.ships:
            print(ship)


class Board:
    enemy_board = ally_board.copy()

    @staticmethod
    def get_ally_map():
        print('  |', *[f'{i} |' for i in range(1, 7)])
        for i, line in enumerate(ally_board):
            print(f'{i+1} | ', end='')
            print(*line, sep=' | ', end=' |\n')


class Dot:
    used_dots = []
    placed_ships = []

    def __init__(self, x, y):
        self.cord = (x, y)

    def __eq__(self, other):
        if self.cord == other.cord:
            raise ValueError('This point is already placed')

    def __str__(self):
        return f'{self.cord}'

    def placing_ships(self):
        if self.cord not in self.placed_ships:
            self.placed_ships.append(self.cord)
            ally_board[self.cord[1]-1][self.cord[0]-1] = '☑'
            print(f'cord 1 ={self.cord[1]} //// cord 0 ={self.cord[0]}')
        else:
            print('Already used. TODO!')


class Move:
    def __init__(self):
        self.messages = Notifications

    def make_move(self):
        self.messages.move_message()
        move = input()  # TODO: DOT CLASS
        print(move.split())  # TODO: DOT REFACT CLASS


class Game(Player, Board, Dot):
    def init_ships(self):
        for _, length in zip(range(3), [3, 2, 2]):
            orientation = input(self.message.orient_message().format(length))
            if orientation not in 'HV':
                raise ValueError('Wrong orientation')
            self.ships.append(Ship(length, orientation))
        for i in range(3):
            self.ships.append(Ship())

    def place_ship(self):
        for ship in self.ships:
            self.get_ally_map()
            dot = input(self.message.placement_message())
            Dot(*map(int, dot.split())).placing_ships()
            print(Dot(*map(int, dot.split())))
            print(ally_board)


test = Board()
test.get_ally_map()
test_player = Game()
test_player.init_ships()
test_player.place_ship()
