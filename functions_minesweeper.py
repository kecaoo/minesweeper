def initialise_board():

    board_list = ['O']*25
    board_list = ['O' for i in range(25)]

    #board_list = []

    #for i in range(25):
    #    board_list.append('0')

    #print(board_list)
    return board_list

def display_board(board_list):

    copied_board = board_list.copy()
    for i in range(len(copied_board)):

        if copied_board[i] == 'X':
            copied_board[i] = 'O'

    print(copied_board[0:5])
    print(copied_board[5:10])
    print(copied_board[10:15])
    print(copied_board[15:20])
    print(copied_board[20:25])

    return

def insert_mines(board_list, positions):


    for position in positions:

        row = position[0]
        column = position[1]

        location = row * 5 + column
        board_list[location] = "X"

    return board_list

def count_adjacent_mines(board_list, row, column):

    location_up = (row - 1) * 5 + column
    location_down = (row + 1) * 5 + column
    location_right = row * 5 + (column + 1)
    location_left = row * 5 + (column - 1)

    mines = 0

    if row > 0 and board_list[location_up] == "X":

        mines += 1

    if row < 4 and board_list[location_down] == "X":
        mines += 1


    if column < 4 and board_list[location_right] == "X":
        mines += 1


    if column > 0 and board_list[location_left] == "X":
        mines += 1

    return mines

def play_turn(board_list, row, column):

    location = row * 5 + column
    selected_mine = False
    if board_list[location] == "X":

        board_list[location] = "#"

        selected_mine = True

    if board_list[location] == "O":

        if count_adjacent_mines(board_list, row, column) == 0:

            board_list[location] = " "
            selected_mine = False

        else:
            board_list[location] = str(count_adjacent_mines(board_list, row, column))
            selected_mine = False

    return board_list, selected_mine

def check_win(board_list):

    for position in board_list:

        if position == "O":
            return False
    return True

def play_game(positions):

    #display_board(hidden_board)

    player_board = initialise_board()

    insert_mines(player_board, positions)
    #player_board = hidden_board.copy()

    display_board(player_board)


    while True:


        guess_location = input("Input a row and column value, separated by a space: ")

        guess_location = str(guess_location)
        split_guess_location = guess_location.split()
        row = int(split_guess_location[0])
        column = int(split_guess_location[1])

        player_board, mines = play_turn(player_board, row, column)
        display_board(player_board)

        if check_win(player_board):
            print("You win")
            break

        if mines:
            print("BOOM, YOU LOST")
            break





