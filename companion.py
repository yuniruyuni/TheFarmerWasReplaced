import foreach
import pos

def amount():
	return min(
		num_items(Items.Carrot),
		num_items(Items.Wood),
		num_items(Items.Carrot),
	)

def init():
	def do(s, x, y):
		till()
	foreach.cell(do)
	
def run():	
	p = pos.get()
	ps = [p]
	m = {p}

	plant(Entities.Grass)
	while True:
		t, (x, y) = get_companion()
		if not t:
			break
		if (x, y) in m:
			break
		m.add((x, y))
		ps.append((x, y))
		pos.moves_to(x, y)
		plant(t)
		while get_water() < 0.5:
			use_item(Items.Water)
		use_item(Items.Fertilizer)
	
	for (x, y) in ps:
		pos.moves_to(x, y)
		while not can_harvest():
			pass
		harvest()