def cell(f, s = None):
	for x in range(get_world_size()):
		for y  in range(get_world_size()):
			s = f(s, x, y)
			move(North)
		move(East)
	return s