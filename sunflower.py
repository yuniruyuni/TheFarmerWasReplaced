import foreach
import pos

def amount():
	return num_items(Items.Power)

def init():
	def do(s, x, y):
		till()
		plant(Entities.Sunflower)
	foreach.cell(do)

def sort_by_height(fs):
	if len(fs) <= 1:
		return fs
	
	pivot = fs.pop(0)
	
	left = []
	for f in fs:
		if f[2] > pivot[2]:
			left.append(f)

	right = []
	for f in fs:
		if f[2] <= pivot[2]:
			right.append(f)

	left = sort_by_height(left)	
	right = sort_by_height(right)
	
	return left + [pivot] + right

def run():
	def do(s, x, y):
		h = measure()
		s.append([x, y, h])
		return s
	
	fs = foreach.cell(do, [])
	fs = sort_by_height(fs)
	for f in fs:
		x, y, h = f
		pos.moves_to(x, y)
		harvest()
	pos.moves_to(0, 0)
	
	def replant(s, x, y):
		plant(Entities.Sunflower)
	foreach.cell(replant)