import foreach

def amount():
	return num_items(Items.Carrot)

def init():
	def do(s, x, y):
		till()
		plant(Entities.Carrot)
	foreach.cell(do)

def run():
	def do(s, x, y):
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
	foreach.cell(do)