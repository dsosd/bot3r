from .config import *

#transforms internal board format to format expected by move(...)
def transform_board(board):
	return [
		board[-G_slots_per_side:],
		board[1:1 + G_slots_per_side][::-1]
	]

#transforms board format expected by move(...) to internal format
def untransform_board(board):
	return [0] + board[1][::-1] + [0] + board[0][:]

#internal -> official as per spec
def normalize_move_index(player_num, index):
	return index if not player_num else 5 - index

#official as per spec -> internal
def denormalize_move_index(player_num, index):
	return index if not player_num else 5 - index