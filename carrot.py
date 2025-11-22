import foreach

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