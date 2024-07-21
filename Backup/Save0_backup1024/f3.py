worldSize = get_world_size()	
while True:
	listPedals = []
	listSunflowers = []
	totalValue = 0
	listCounter = 0	
	for i in range(worldSize):
		for j in range(worldSize):
			if get_ground_type() == Grounds.Turf:
				till()
			tradeSeed(Items.Sunflower_Seed)
			while get_water() < 0.5:
				use_item(Items.Water_Tank)
			plant(Entities.Sunflower)
			listPedals.append(measure())
			tupleSunflower = listCounter, i, j
			listSunflowers.append(tupleSunflower)
			totalValue += measure()
			listCounter = listCounter + 1
			move(North)
		move(East)
	while totalValue > 0:
		maxValue = max(listPedals)
		listCounter = 0			
		for i in range(worldSize):
			for j in range(worldSize):
				if listPedals[listCounter] == maxValue:
					if can_harvest():
						harvest()
						listPedals.pop(listCounter)
						listPedals.insert(listCounter, 0)
						totalValue = totalValue - maxValue				
				listCounter = listCounter + 1
				move(North)
			move(East)
			