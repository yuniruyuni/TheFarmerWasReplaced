import grass
import tree
import carrot
import pumpkin
import sunflower
import fertilizer
import weird
import maze
import companion
import cactus
import dinosaur

MODES = [
  grass,
  tree,
  carrot,
  weird,
  sunflower,
  pumpkin,
  maze,
  companion,
  cactus,
  dinosaur,
]

def least_amount_module():
	lm = MODES[0]
	la = lm.amount()
	for m in MODES[1:]:
		a = m.amount()
		if a < la:
			lm = m
			la = a			
	return lm

last = None

while True:
	m = least_amount_module()
	if last != m:
		clear()
		do_a_flip()
		m.init()
		last = m
	m.run()