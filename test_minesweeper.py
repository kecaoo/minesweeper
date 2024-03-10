import pytest
from functions_minesweeper import *
def test_count_adjacent_mines_in_corner():
    board = ["X", "O", "O", "O", "O",
             "O", "O", "O", "O", "O",
             "O", "O", "O", "O", "O",
             "O", "O", "O", "O", "O",
             "O", "O", "O", "O", "O"]
    count = count_adjacent_mines(board,0,4)
    assert(count == 0)

def test_insert_mines():

    board = ["O", "O", "O", "O", "O",
             "O", "O", "O", "O", "O",
             "O", "O", "O", "O", "O",
             "O", "O", "O", "O", "O",
             "O", "O", "O", "O", "O"]

    mine = insert_mines(board, [(2, 3), (0, 0), (4, 4)])

    assert(board == ["X", "O", "O", "O", "O",
                    "O", "O", "O", "O", "O",
                    "O", "O", "O", "X", "O",
                    "O", "O", "O", "O", "O",
                    "O", "O", "O", "O", "X"])

def test_count_adjacent_mines():

    board = ["O", "O", "O", "O", "O",
             "O", "X", "O", "O", "O",
             "X", "O", "X", "O", "O",
             "O", "X", "O", "O", "O",
             "O", "O", "O", "O", "O"]
    count = count_adjacent_mines(board, 2,1)
    assert count == 4

def test_play_turn():
    board = ["O", "O", "O", "O", "O",
             "O", "X", "O", "O", "O",
             "O", "O", "O", "O", "O",
             "O", "O", "O", "O", "O",
             "O", "O", "O", "O", "O"]

    result, mines = play_turn(board.copy(), 1, 1)
    assert result != board
    assert mines == True

def test_check_win():
    board = [" ", "1", " ", " ", " ",
             "1", "X", "1", " ", " ",
             " ", "1", " ", " ", " ",
             " ", " ", " ", " ", " ",
             " ", " ", " ", " ", " "]

    board_two = [" ", "1", " ", " ", " ",
             "1", "X", "1", " ", " ",
             " ", "1", " ", " ", " ",
             " ", " ", " ", "O", " ",
             " ", " ", " ", " ", " "]

    check = check_win(board)
    check_two = check_win(board_two)
    assert check
    assert not check_two

