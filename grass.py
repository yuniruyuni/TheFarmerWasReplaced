import foreach

def amount():
	return num_items(Items.Hay)

def init():
	pass

def run():
	def do(s, x, y):
		if can_harvest():
			harvest()
			plant(Entities.Grass)
	foreach.cell(do)