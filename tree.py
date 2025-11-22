import foreach

def is_bush(x, y):
	is_x_odd = (x%2 == 0)
	is_y_odd = (y%2 == 0)
	return (is_x_odd == is_y_odd)

def init():
	pass

def run():
	def do(s, x, y):		
		if can_harvest():
			harvest()
			if is_bush(x, y):
				plant(Entities.Bush)
			else:
				plant(Entities.Tree)
	
		if get_water() < 0.5:
			use_item(Items.Water)	
	
	foreach.cell(do)