from .config import *
from .engine import *
from .transform import *

def main_move(player_num, board, error, prev_move):
	#should never error, but if so, just return next index
	if error:
		return normalize_move_index(
			player_num,
			(
				1 + denormalize_move_index(player_num, prev_move)
			) % G_slots_per_side
		)

	board = untransform_board(board)

	#try to get another turn
	for i in range(G_slots_per_side):
		if process_move(player_num, board[:], normalize_move_index(player_num, i)) == player_num:
			return normalize_move_index(player_num, i)

	#try to capture maximally from opponent
	#do this not so efficiently, but more readably
	for i in sorted(
			range(G_slots_per_side),
			reverse = True,
			key = lambda x: (board[G_store_pos[not player_num] + 1 + x]) * G_slots_per_side + ((G_slots_per_side - 1) - x)):
		best_move = -1
		#try to capture opponent's index i with as small of an index j for our pockets
		#we iterate backwards to make code simpler
		for j in range(G_slots_per_side - 1, -1, -1):
			if board[G_store_pos[not player_num] + 1 + i]:
				temp = board[:]
				process_move(player_num, temp, normalize_move_index(player_num, j))
				if not board[G_store_pos[not player_num] + 1 + i]:
					best_move = j

		if best_move != -1:
			return normalize_move_index(player_num, best_move)

	#finally, first non-empty pocket
	ret = [not not x for x in board[G_store_pos[player_num] + 1:]].index(True)

	return normalize_move_index(player_num, ret)