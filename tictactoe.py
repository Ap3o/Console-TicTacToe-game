board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

MOVES = {1: {"x": 0, "y": 0}, 2: {"x": 0, "y": 1}, 3: {"x": 0, "y": 2},
         4: {"x": 1, "y": 0}, 5: {"x": 1, "y": 1}, 6: {"x": 1, "y": 2},
         7: {"x": 2, "y": 0}, 8: {"x": 2, "y": 1}, 9: {"x": 2, "y": 2},
         }


def empty_cells(board=board):
    cells = []

    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == " ":
                cells.append([x, y])

    return cells


def game_over(board):
    global player_1, player_2
    return is_win(player_1) or is_win(player_2) or len(empty_cells()) == 0


def is_win(player, board=board):
    win_state = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def set_move(move, player, MOVES=MOVES):
    board[MOVES[move]["x"]][MOVES[move]["y"]] = player


def is_valid_move(move, MOVES=MOVES):
    if move < 1 or move > 9:
        return False
    if board[MOVES[move]["x"]][MOVES[move]["y"]] == " ":
        return True
    else:
        return False


def turn(player, board=board):
    if game_over(board):
        return
    print(player)
    move = -1
    while move < 1 or move > 9:
        try:
            move = int(input("Use numpad (1..9) "))
        except ValueError:
            print("Bad value, choose from 1 to 9")
        else:
            if not is_valid_move(move):
                move = -1
                print("Move is not real")
            else:
                set_move(move, player)
                break
    str_line = "--------------"
    print('\n' + str_line)
    for row in board:
        for cell in row:
            symbol = cell
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def main():
    global player_1, player_2
    player_1 = ""
    player_2 = ""

    while player_1 != "X" and player_1 != "0":
        player_1 = input("Choose 'X' or '0': ")

    if player_1 == "X":
        player_2 = "0"
    else:
        player_2 = "X"

    while not game_over(board):
        turn(player_1)
        turn(player_2)


main()
