import foreach
import pos

def amount():
	return num_items(Items.Cactus)

def shell_sort(ws, d):
	ad = pos.anti(d)
	l, r = 0, ws
	while l < r:
		for i in range(l, r, +1):
			move(d)
			if measure() < measure(ad):
				swap(ad)
		r -= 1
		for j in range(r, l, -1):
			move(ad)
			if measure() < measure(ad):
				swap(ad)
		l += 1


def init():
	def do(s, x, y):
		till()
	foreach.cell(do)
	
def run():
	def do(s, x, y):
		plant(Entities.Cactus)
	foreach.cell(do)
	
	ws = get_world_size()
	for h in range(ws):
		shell_sort(ws, East)
		pos.moves_to(0, h)
		move(North)
	
	for w in range(ws):
		shell_sort(ws, North)
		pos.moves_to(w, 0)
		move(East)
	
	harvest()