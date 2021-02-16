import random

from .config import *
from .engine import *
from .transform import *

def random_move(player_num, board, error, prev_move):
	#should never error, but if so, just return next index
	if error:
		return normalize_move_index(
			player_num,
			(
				1 + denormalize_move_index(player_num, prev_move)
			) % G_slots_per_side
		)

	board = untransform_board(board)

	ret = random.sample([i for i in range(G_slots_per_side) if board[G_store_pos[player_num] + 1 + i]], 1)[0]

	return normalize_move_index(player_num, ret)