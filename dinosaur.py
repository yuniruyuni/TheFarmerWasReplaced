import foreach
import pos

def amount():
	return num_items(Items.Bone)

def init():
	pass

def even_route(w):
	s = True
	while move(East):
		for y in range(w):
			d = West
			if y % 2 == 0:
				d = East
			pos.moves(d, w-2)
			if y != w-1:
				pos.moves(North, 1)
		pos.moves(West, 1)
		pos.moves(South, w-1)

def odd_route(w):
	s = True
	while True:
		# first runs
		if not move(East):
			break
		for y in range(w-2):
			d = West
			if y % 2 == 0:
				d = East
			pos.moves(d, w-2)
			pos.moves(North, 1)
		for y in range(w//2):
			pos.moves(North, 1)
			pos.moves(West, 1)
			pos.moves(South, 1)
			pos.moves(West, 1)
		pos.moves(South, w-2)

		# first runs
		if not move(East):
			break
		for y in range(w-2):
			d = West
			if y % 2 == 0:
				d = East
			pos.moves(d, w-2)
			pos.moves(North, 1)
		for y in range(w//2):
			pos.moves(West, 1)
			pos.moves(North, 1)
			pos.moves(West, 1)
			pos.moves(South, 1)
		pos.moves(South, w-2)
		
		
def run():
	change_hat(Hats.Dinosaur_Hat)
		
	ws = get_world_size()
	is_even = (ws % 2 == 0)
	
	if is_even:
		even_route(ws)
	else:
		odd_route(ws)
	
	change_hat(Hats.Brown_Hat)
	pos.moves_to(0, 0)