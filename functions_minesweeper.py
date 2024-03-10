def initialise_board():
    """
    This function will initialise the minesweeper board

    Returns
    ---------
    board_list: A list containing 25 items.

    Notes
    ---------
    The items inside the board_list must be string "O" to represent unselected squares.

    """

    """Creating a list of 25 integer 'O's"""
    board_list = ['O' for i in range(25)]

    return board_list

def display_board(board_list):
    """

    This function displays the playing board

    Arguments
    ---------
    board_list: A list containing 25 string values, representing a minesweeper
                board with mines, uncovered squares, and empty squares.

    Notes
    ---------
    The updated board_list will have hidden the locations of the mines. If there
    is an "X" in the list, representing a mine, this will change visually to an O.

    board_list is limited to 25 string values to represent a 5x5 minesweeper board

    """

    """A copy of the board is created"""
    copied_board = board_list.copy()

    """Iterations through the list, hiding the visible mines"""
    for i in range(len(copied_board)):

        if copied_board[i] == 'X':
            copied_board[i] = 'O'

    """Displaying the new covered board"""
    print(copied_board[0:5])
    print(copied_board[5:10])
    print(copied_board[10:15])
    print(copied_board[15:20])
    print(copied_board[20:25])

    return

def insert_mines(board_list, positions):
    """
    This function inserts mines into the playing board

    Arguments
    ---------
    board_list: a list with 25 string items, representing a 5x5 minesweeper board
    positions: a list of tuples, representing the positions of the mines to be inserted

    Returns
    ---------
    board_list: a list with 25 string items, now updated with "X" in the locations
                specified by the positions (list of tuples).

    Notes
    ---------
    List of tuples within "positions" must be within the ranges of the grid (between 0-4
    in the rows and columns respectively).

    At the specified locations defined by the positions, mines represented by "X" will replace
    the item in that location.

    board_list must be a list with 25 values representing the minesweeper board.
    """

    for position in positions:

        row = position[0]
        column = position[1]

        """Adding mines at the specified positions using a formula"""
        location = row * 5 + column
        board_list[location] = "X"

    return board_list

def count_adjacent_mines(board_list, row, column):
    """
    This function counts the adjacent mines relative to specified location

    Arguments
    ---------
    board_list: a list with 25 string items, including the location of
                the mines.

    row: an integer that represents the row of the position that is to be
        checked for mines.

    column: an integer that represents the column of the position that is
            to be checked for mines.

    Returns
    ---------
    mines: an integer that represents the amount of mines around that specified
            location

    Notes
    ---------

    The row and column provided in the arguments must be positive integers, and within the
    range of 0-4.

    The board provided in the arguments must be a 5x5 grid represented by a list with 25
    string values.

    Adjacent squares checked must not out of the bounds of the 5x5 grid. These are ignored.
    """

    """Creating variables to check the adjacent positions"""
    location_up = (row - 1) * 5 + column
    location_down = (row + 1) * 5 + column
    location_right = row * 5 + (column + 1)
    location_left = row * 5 + (column - 1)

    mines = 0

    "Checking for out of bounds values as well as adjacent ones"
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
    """
        This function plays a turn on the minesweeper board using provided row and column values

        Arguments
        ---------
        board_list: a list with 25 string items, including the location of
                    the mines.

        row: an integer that represents the row of the position that is to be
            checked for mines.

        column: an integer that represents the column of the position that is
                to be checked for mines.

        Returns
        ---------
        board_list: a list of updated 25 string items, representing an updated minesweeper board
                    after a play turn.

        selected_mine: a bool value being either True or False depending on whether a mine
                        was selected or not.

        Notes
        ---------
        If the location defined by the row and column arguments is the location of a hidden mine,
        the string is to be changed into a # character.

        If a hidden mine location is not selected, the number of adjacent mines will replace the
        existing character.

        Where there is no adjacent mines, then a "space" character replaces the existing character.

        The row and column provided in the arguments must be positive integers, and within the
        range of 0-4 so that it is within the bounds of the grid.

        Repeated guesses on the same position is possible.
        """


    location = row * 5 + column
    selected_mine = False

    """Checking the location of the given position and altering it"""
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
    """
    This function checks the minesweeper board for a win

    Arguments
    ---------
    board_list: a list of 25 string values representing the minesweeper board

    Returns
    ---------
    A boolean value representing whether the game has been won (True) or
    if there is not yet a win (False)

    Notes
    ---------
    If there are any remaining "O" on the board, then False must be returned

    If there are no more remaining "O" on the board, then True is returned because
    all possible squares have been selected without uncovering a mine.

    A return of False does not end the game, it just means that the game has not
    been won yet.
    """

    for position in board_list:

        if position == "O":
            return False
    return True

def play_game(positions):
    """
    This function will simulate a full minesweeper game using previous functions

    Arguments
    ---------
    positions: a list of tuples, representing the positions (integers) of the mines to be inserted

    Notes
    ---------
    integer values in the "positions" tuples must be within the range (0-4) to avoid going out of bounds
    of the minesweeper grid.

    Selecting a mine will cause the game to end and display a message indicated that

    Selecting all possible locations that have no mines will result in a win and a display
    message will indicate that as well

    User inputted values for the "guess location" must be within the range (0-4) to avoid going out of bounds
    of the minesweeper grid.
    """

    """Calling other functions to initialise and display the minesweeper board"""
    player_board = initialise_board()
    insert_mines(player_board, positions)
    display_board(player_board)


    while True:

        """Taking inputs from user for location guesses"""
        guess_location = input("Input a row and column value, separated by a space: ")

        guess_location = str(guess_location)
        split_guess_location = guess_location.split()
        row = int(split_guess_location[0])
        column = int(split_guess_location[1])

        """Adding the turn to the minesweeper board"""
        player_board, mines = play_turn(player_board, row, column)
        display_board(player_board)

        """Checking the board for a win after each guess"""
        if check_win(player_board):
            print("You win")
            break

        if mines:
            print("BOOM, YOU LOST")
            break





