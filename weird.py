import foreach

def init():
	def do(s, x, y):
		if can_harvest():
			harvest()
			plant(Entities.Grass)
			use_item(Items.Weird_Substance)
	foreach.cell(do)

def run():
	def do(s, x, y):
		if can_harvest():
			harvest()
			plant(Entities.Grass)
	foreach.cell(do)