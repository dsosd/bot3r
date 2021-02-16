from .config import *
from .transform import *

#returns pocket owner
def get_owner(pos):
	if G_store_pos[0] < pos and pos < G_store_pos[1]:
		return 0
	elif G_store_pos[1] < pos and pos < G_total_slots:
		return 1
	else:
		raise Exception()

def get_correspond_pocket(pos, player_num):
	owner = get_owner(pos)
	if owner == player_num:
		return pos

	#returns (inv_factor - offset) + base, where
	# inv_factor = G_slots_per_side - 1
	# offset = pos - G_store_pos[owner] - 1
	# base = G_store_pos[player_num] + 1
	return (G_slots_per_side - 1) - (pos - G_store_pos[owner] - 1) + G_store_pos[player_num] + 1

#performs move and returns empty pocket landed / store landed
#e.g. landing in a non-empty pocket will return [None, None]
#e.g. landing in an empty pocket will return [{pocket_index}, None]
#e.g. landing in a store will return [None, {store_index}]
def shift_stones(board, index, exclude):
	stones = board[index]

	board[index] = 0
	empty = [not x for x in board]
	last_index = 0

	#"shift" the add array and relevant index
	add = (len(board) - len(exclude)) * [0]
	fake_index = index
	for i in exclude:
		if index >= i:
			fake_index -= 1

	for i in range(0, len(add)):
		relative_index = fake_index - i if fake_index - i >= 0 else len(add) + fake_index - i

		#shift relative index to make it easier
		relative_index -= 1
		relative_index %= len(add)

		#last stone
		if relative_index == (stones - 1) % len(add):
			last_index = i

		add[i] = stones // len(add) + (relative_index < stones % len(add))

	#"unshift" the add array and relevant index
	for i in sorted(exclude):
		if index >= i:
			last_index += 1
		add.insert(i, 0)

	#add add to board
	for i in range(len(board)):
		board[i] += add[i]

	#last_index is store
	if last_index in G_store_pos:
		return [None, last_index]
	#last_index is pocket
	else:
		return [last_index if empty[last_index] and board[last_index] < 2 else None, None]

#deal with player-specific behavior and returns next player number
def process_move(player_num, board, index):
	index = denormalize_move_index(player_num, index)

	pos = G_store_pos[player_num] + index + 1
	exclude = [G_store_pos[not player_num]]

	move_data = shift_stones(board, pos, exclude)

	#landed in own store
	if move_data[1] == G_store_pos[player_num]:
		return player_num

	#capturing enemy stones
	if move_data[0] is not None and get_owner(move_data[0]) == player_num and board[get_correspond_pocket(move_data[0], not player_num)] > 0:
		#MAGIC 2 players
		for i in range(2):
			board[G_store_pos[player_num]] += board[get_correspond_pocket(move_data[0], i)]
			board[get_correspond_pocket(move_data[0], i)] = 0

	return int(not player_num)

def check_game_end(board):
	pocket_sum = {0: 0, 1: 0}
	for i in range(len(board)):
		if i not in G_store_pos:
			pocket_sum[get_owner(i)] += board[i]

	#at least one player's pockets are all empty
	return any([not v for k, v in pocket_sum.items()])

#transfer remaining stones to their respective owner's stores
def end_game(board):
	pocket_sum = {0: 0, 1: 0}
	for i in range(len(board)):
		if i not in G_store_pos:
			pocket_sum[get_owner(i)] += board[i]
			board[i] = 0

	for k, v in pocket_sum.items():
		board[G_store_pos[k]] += v