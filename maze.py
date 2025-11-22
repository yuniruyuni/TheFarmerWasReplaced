dirs = [North, South, East, West]
def dirs_without(d):
	ret = []
	for dir in dirs:
		if dir != d:
			ret.append(dir)
	return ret
	
def anti(d):
	dirs = {
		North: South,
		South: North,
		East: West,
		West: East,
	}
	return dirs[d]

def search(d):
	ok = move(d)
	if not ok:
		return False
	
	if get_entity_type() == Entities.Treasure:
		return True
	
	cands = dirs_without(anti(d))
	for c in cands:
		ok = search(c)
		if ok:
			return True
	move(anti(d))
	return False
	


def gen_maze():
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def init():
	pass
	
def run():
	gen_maze()
	for d in dirs:
		found = search(d)
		if found:
			harvest()
			return