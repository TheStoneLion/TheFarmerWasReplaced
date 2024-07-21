counterRounds = 2
counterIterations = 2
while True:
	goTo_x_y(0, 0)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			tradeSeed(Items.Egg)
			use_item(Items.Egg)
			move(North)
		move(East)
	for a in range(counterIterations):    
		for b in range(counterRounds):
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					if measure() > measure(East):
						swap(East)
					if measure() > measure(North):
						swap(North)
					move(East)
				move(North)	
		for r in range(counterRounds):
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					if measure() > measure(North):
						swap(North)
					if measure() > measure(East):
						swap(East)
					move(North)
				move(East)		
	goTo_x_y(0, 0)			
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			move(North)
		move(East)