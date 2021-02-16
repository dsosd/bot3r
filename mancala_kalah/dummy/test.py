from .config import *
from .engine import *
from .transform import *

def run_test_game(moves):
	board = G_standard_init_board[:]

	print("Initial board:", transform_board(board))

	submove_letters = [chr(i) for i in range(ord("a"), ord("z") + 1)]

	player_num = 0
	next_player = 0
	i = 0

	turn_num = 1
	subturn_num = -1

	while i < len(moves):
		while next_player == player_num and i < len(moves):
			next_player = process_move(player_num, board, normalize_move_index(player_num, moves[i]))

			if subturn_num >= 0:
				print("Move {}{}: {}".format(turn_num, submove_letters[subturn_num], next_player))
			elif next_player == player_num:
				subturn_num = 0
				print("Move {}{}: {}".format(turn_num, submove_letters[subturn_num], next_player))
			else:
				print("Move {}: {}".format(turn_num, next_player))
			print("Curr board:", transform_board(board))

			i += 1
			subturn_num += 1

		print("Stores: {} {}\n".format(board[G_store_pos[0]], board[G_store_pos[1]]))
		player_num = next_player
		turn_num += 1
		subturn_num = -1

def test_game_1():
	moves = [
		0,
		2,

		1,
		3,

		0, 3, 0, 5, 0, 1, 0, 4, 0, 2,
		0,

		0, 1,
		1,

		0, 2,
		0, 2,

		3, 0, 1, 0, 2,
		3,

		4,
		2,

		2,
		1, 0
	]
	run_test_game(moves)

def test_transform():
	transform_test_board = [0, 1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 10, 11, 12]

	print(transform_board(transform_test_board))
	print(untransform_board(transform_board(transform_test_board)))

def test_all():
	test_game_1()
	test_transform()