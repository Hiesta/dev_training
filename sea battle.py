from random import randint, choice
from time import sleep


class BoardExcept(Exception):
    pass


class WrongShip(BoardExcept):
    pass


class BoardOutException(BoardExcept):
    def __str__(self):
        return 'Out of border!'


class BoardUsedException(BoardExcept):
    def __str__(self):
        return "You've already shot this cell!"


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'


class Ship:
    def __init__(self, bow: Dot, length: int, vertical: bool):
        self.bow = bow
        self.length = length
        self.vertical = vertical
        self.lives = length

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            curr_x = self.bow.x
            curr_y = self.bow.y
            if self.vertical:
                curr_y += i
            else:
                curr_x += i
            ship_dots.append(Dot(curr_x, curr_y))
        return ship_dots

    def is_hit(self, dot) -> bool:
        return dot in self.dots


class Board:
    def __init__(self, size: int, hid=False):
        self.size = size
        self.hid = hid
        self.field = [['O'] * size for _ in range(size)]
        self.busy = []
        self.ships = []
        self.last_hit = []
        self.count_destr_ships = 0

    def __str__(self):
        res = '  | ' + ' | '.join(map(str, range(1, self.size + 1))) + ' |'
        for i, row in enumerate(self.field):
            res += f'\n{i + 1} | ' + ' | '.join(row) + ' |'
        if self.hid:
            res = res.replace('■', 'O')
        return res

    def out(self, d: Dot) -> bool:
        return not (0 <= d.x < self.size and 0 <= d.y < self.size)

    def contour(self, ship, visible=False):
        around = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
        for dot in ship.dots:
            for dx, dy in around:
                curr_dot = Dot(dot.x + dx, dot.y + dy)
                if not self.out(curr_dot) and curr_dot not in self.busy:
                    if visible:
                        self.field[curr_dot.x][curr_dot.y] = '.'
                    self.busy.append(curr_dot)

    def add_ship(self, ship):
        for d in ship.dots:
            if d in self.busy or self.out(d):
                raise WrongShip()
        for d in ship.dots:
            self.field[d.x][d.y] = '■'
            self.busy.append(d)
        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d: Dot) -> bool:
        if d in self.busy:
            raise BoardUsedException()
        if self.out(d):
            raise BoardOutException()

        self.busy.append(d)

        for ship in self.ships:
            if ship.is_hit(d):
                self.field[d.x][d.y] = 'X'
                print('Hit!')
                ship.lives -= 1
                if ship.lives == 0:
                    self.count_destr_ships += 1
                    self.contour(ship, visible=True)
                    print('Ship was destroyed!')
                    self.last_hit = []
                    return False
                else:
                    print('Ship is wounded!')
                    self.last_hit.append(d)
                    return True

        self.field[d.x][d.y] = '.'
        print('Miss!')
        return False

    def begin(self):
        self.busy = []

    def defeat(self):
        return self.count_destr_ships == len(self.ships)


class Player:
    def __init__(self, board: Board, enemy: Board):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self) -> bool:
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                sleep(1)
                return repeat
            except BoardExcept as exception_:
                print(exception_)


class AI(Player):
    def ask(self) -> Dot:
        last = self.enemy.last_hit
        while True:
            if last:
                if len(last) == 1:
                    near = ((0, 1), (0, -1), (1, 0), (-1, 0))
                else:
                    if last[0].x == last[-1].x:
                        near = ((0, 1), (0, -1))
                    else:
                        near = ((1, 0), (-1, 0))
                dx, dy = choice(near)
                delt = choice((Dot(last[-1].x + dx, last[-1].y + dy), Dot(last[0].x + dx, last[0].y + dy)))
            else:
                delt = Dot(randint(0, 5), randint(0, 5))
            if delt not in self.enemy.busy and not self.enemy.out(delt):
                break
        sleep(2)
        print(f'Enemy hit this point: {delt.x + 1} {delt.y + 1}')
        return delt


class User(Player):
    def ask(self) -> Dot:
        while True:
            coord = input('Enter your shot:\t').split()
            if len(coord) != 2:
                print('Example : (X,Y)')
                continue
            x, y = coord
            if not all((x.isdigit(), y.isdigit())):
                print('Coordinates must be digits')
                continue
            return Dot(int(y) - 1, int(x) - 1)


class Game:
    def __init__(self, size=6):
        self.lens = (3, 2, 2, 1, 1, 1, 1)
        self.size = size
        ai_board = self.random_board()
        user_board = self.random_board()
        ai_board.hid = True

        self.ai = AI(ai_board, user_board)
        self.pl = User(user_board, ai_board)

    def generating_ally_field(self):
        attempts = 0
        board = Board(size=self.size)
        for l in self.lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), (randint(0, self.size))), l, bool(randint(0, 1)))
                try:
                    board.add_ship(ship)
                    break
                except WrongShip:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.generating_ally_field()
        return board

    @staticmethod
    def greet():
        print('-' * 18)
        print(' Entry format: x y ')
        print(' x - column  ')
        print(' y - line ')
        print('-'*18)

    def display_boards(self):
        print('-' * self.size * 10)
        print('Your board:'.ljust((self.size + 1) * 4 - 1) + ' ' * self.size + 'Enemy Board:')
        for s1, s2 in zip(self.pl.board.__str__().split('\n'), self.ai.board.__str__().split('\n')):
            print(s1 + ' ' * self.size + s2)

    def loop(self):
        step = 0
        while True:
            self.display_boards()
            if step % 2 == 0:
                print('Your turn!')
                repeat = self.pl.move()
            else:
                print('Enemy turn!')
                repeat = self.ai.move()
            if repeat:
                step -= 1

            if self.ai.board.defeat():
                self.display_boards()
                print('You won!')
                break
            if self.pl.board.defeat():
                self.display_boards()
                print('You lose!')
                break
            step += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()
