counterRounds = 3
counterIterations = 2
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			tradeSeed(Items.Egg)
			use_item(Items.Egg)
#			plant(Entities.Dinosaur)
			move(North)
		move(East)
	for x in range(counterIterations):    
		for y in range(counterRounds):
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					if measure() > measure(East):
						swap(East)
					if measure() > measure(North):
						swap(North)
					move(East)
				move(North)	
		for x in range(counterRounds):
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					if measure() > measure(North):
						swap(North)
					if measure() > measure(East):
						swap(East)
					move(North)
				move(East)		
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			move(North)
		move(East)