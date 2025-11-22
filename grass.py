import foreach

def init():
	pass

def run():
	def do(s, x, y):
		if can_harvest():
			harvest()
			plant(Entities.Grass)
	foreach.cell(do)