import foreach

def amount():
	return num_items(Items.Pumpkin)

def init():
	def do(s, x, y):
		till()
		plant(Entities.Pumpkin)
	foreach.cell(do)

def run():
	def do(s, x, y):
		ent = get_entity_type()
		if ent == None:
			plant(Entities.Pumpkin)
		elif ent == Entities.Dead_Pumpkin:
			harvest()
			plant(Entities.Pumpkin)
		return s and can_harvest()
	
	while not foreach.cell(do, True):
		pass
	harvest()