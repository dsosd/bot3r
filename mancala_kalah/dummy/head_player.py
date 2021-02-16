from .config import *
from .engine import *
from .transform import *

def head_move(player_num, board, error, prev_move):
	#should never error, but if so, just return next index
	if error:
		return normalize_move_index(
			player_num,
			(
				1 + denormalize_move_index(player_num, prev_move)
			) % G_slots_per_side
		)

	board = untransform_board(board)

	#first non-empty pocket
	ret = [not not x for x in board[G_store_pos[player_num] + 1:]].index(True)

	return normalize_move_index(player_num, ret)