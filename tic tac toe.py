def get_map():
    print(*field[0])
    print(*field[1])
    print(*field[2])
    print(*field[3])


def wrong_move(func, message, player):
    print(message)
    func(player, input())


def win_conditions(player: str):  # <---- FIXME
    if any([*[all([field[n][j] == player for n in range(1, 4)]) for j in range(1, 4)],
            *[all([field[n][j] == player for j in range(1, 4)]) for n in range(1, 4)],
            all([field[n][n] == player for n in range(1, 4)]),
            all([field[n][j] == player for n, j in zip(range(1, 4), range(3, 0, -1))])]):
        print(f'{player} has won!')
        get_map()
        global winner
        winner = not winner


def winner_check(func):
    def wrapper(player, cord):
        func(player, cord)
        win_conditions(player)  # <---- FIXME
    return wrapper


@winner_check
def moving(player: str, cord: str):
    try:
        x, y = map(int, cord.split())
        if field[y+1][x+1] == '-':
            field[y+1][x+1] = player
        else:
            wrong_move(moving, cell_occupied, player)
    except ValueError:
        wrong_move(moving, move_example, player)
    except IndexError:
        wrong_move(moving, index_error, player)


field = [[' ', 0, 1, 2],
         [0, '-', '-', '-'],
         [1, '-', '-', '-'],
         [2, '-', '-', '-']]
winner = False
cell_occupied = 'This cell is already occupied\nmake another move:'
move_example = 'To make a move enter something like this\n---> 0 1 : '
index_error = 'Your map size is 3 cells: 0, 1, 2\nmake new move: '


while not winner:
    get_map()
    move_x = input("'x' turn, make your move; Example = 0 0\n")
    moving('x', move_x)
    if winner:
        break
    get_map()
    move_o = input("'o' turn, make your move; Example = 0 0\n")
    moving('o', move_o)
