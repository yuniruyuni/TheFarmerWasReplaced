import pos

def amount():
	return num_items(Items.Gold)

def search(d):
	ok = move(d)
	if not ok:
		return False
	
	if get_entity_type() == Entities.Treasure:
		return True
	
	cands = pos.dirs_without(pos.anti(d))
	for c in cands:
		ok = search(c)
		if ok:
			return True
	move(pos.anti(d))
	return False
	


def gen_maze():
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def init():
	pass
	
def run():
	gen_maze()
	for d in pos.DIRS:
		found = search(d)
		if found:
			harvest()
			return