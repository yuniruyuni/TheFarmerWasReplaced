import grass
import tree
import carrot
import pumpkin
import sunflower
import fertilizer
import weird
import maze

MODES = [
  grass,
  tree,
  carrot,
  weird,
  fertilizer,
  sunflower,
  pumpkin,
  maze,
]

while True:
	for mode in MODES:
		clear()
		do_a_flip()
		mode.init()
		for i in range(10):
			mode.run()