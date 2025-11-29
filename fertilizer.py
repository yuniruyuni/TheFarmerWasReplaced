import foreach

def amount():
	return num_items(Items.Fertilizer)

def init():
	pass

def run():
	def do(s, x, y):
		if can_harvest():
			harvest()
			plant(Entities.Grass)
			use_item(Items.Fertilizer)
	foreach.cell(do)