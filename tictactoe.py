from random import randint

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

MOVES = {1: {"x": 0, "y": 0}, 2: {"x": 0, "y": 1}, 3: {"x": 0, "y": 2},
         4: {"x": 1, "y": 0}, 5: {"x": 1, "y": 1}, 6: {"x": 1, "y": 2},
         7: {"x": 2, "y": 0}, 8: {"x": 2, "y": 1}, 9: {"x": 2, "y": 2},
         }
def render(board=board):
    str_line = "--------------"
    print('\n' + str_line)
    for row in board:
        for cell in row:
            symbol = cell
            print(f'| {symbol} |', end='')
        print('\n' + str_line)

def empty_cells(board=board):
    cells = []

    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == " ":
                cells.append([x, y])

    return cells


def game_over(player_1, player_2, board):
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

    
def ai_turn(ai_comp, player, board=board):
    if game_over(ai_comp, player, board):
        return
    print(f'Ход искусственного интеллекта')
    while True:
        move = randint(1, 9)
        if not is_valid_move(move):
            move = -1
        else:
            set_move(move, ai_comp)
            break
    render()

def turn(player, player_2, board=board):
    if game_over(player, player_2, board):
        return
    print(f'Ход игрока "{player}"')
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
    render()


def main():
    global player_1, player_2
    player_1 = ""
    player_2 = ""
    ai_comp = ""
    while player_1 != "X" and player_1 != "0":
        player_1 = input("Choose 'X' or '0': ")
    while ai_comp != "Yes" and ai_comp != "No":
        ai_comp = input("Play with AI? Yes/No: ")
    render()
    if ai_comp == "Yes":
        if player_1 == "X":
            ai_comp = "0"
        else:
            ai_comp = "X"
        while not game_over(player_1, ai_comp, board):
            turn(player_1, ai_comp)
            ai_turn(ai_comp, player_1)
    else:
        if player_1 == "X":
            player_2 = "0"
        else:
            player_2 = "X"
        
        while not game_over(player_1, player_2, board):
            turn(player_1, player_2)
            turn(player_2, player_1)


main()
