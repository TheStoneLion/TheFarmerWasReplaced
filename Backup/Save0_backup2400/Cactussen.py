counterRounds = 3
counterIterations = 2
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type() == Grounds.Turf:
				till()
			tradeSeed(Items.Cactus_Seed)
			while get_water() < 0.5:
				use_item(Items.Water_Tank)
			plant(Entities.Cactus)
			move(North)
		move(East)
	for x in range(counterIterations):    
		for y in range(counterRounds):
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					if measure() > measure(East):
						swap(East)
					move(East)
				move(North)	
		for x in range(counterRounds):
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					if measure() > measure(North):
						swap(North)
					move(North)
				move(East)		
	harvest()
	