DIRS = [North, South, East, West]

def get():
	return get_pos_x(), get_pos_y()

_anti = {
	North: South,
	South: North,
	East: West,
	West: East,
}
def anti(d):
	return _anti[d]

_dirs_without = {
  North: [South, East, West],
  South: [North, East, West],
  East: [North, South, West],
  West: [North, South, East],
}
def dirs_without(d):
	return _dirs_without[d]

def moves(d, n):
	if n < 0:
		n = -n
		d = anti(d)
	for _ in range(n):
		move(d)

def wrap(l, s, e):
	return (e - s + l//2) % l - l//2

def moves_to(
	ex,
	ey,
	sx = get_pos_x(),
	sy = get_pos_y(),
):
	w = get_world_size()
	moves(East, wrap(w, sx, ex))
	moves(North, wrap(w, sy, ey))