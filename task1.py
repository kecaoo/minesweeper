from functions_minesweeper import *

# board = initialise_board()
# positions = [[2, 3], [1, 4]]
#
# print("Initial Board:")
# display_board(board)
#
# board_with_mines = insert_mines(board, positions)
# print("Mine Board:")
# display_board(board_with_mines)
#
# print("There are", count_adjacent_mines(board_with_mines, 0,4), "adjacent mines")
#
# updated_board, mine_selected = play_turn(board_with_mines, 1, 3)
#
# display_board(updated_board)
#
# print(mine_selected)
#
# check_win(board_with_mines)
positions = [[2,3], [1, 4]]
play_game(positions)


