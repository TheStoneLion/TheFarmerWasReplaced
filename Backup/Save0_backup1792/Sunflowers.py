while True:
	listPedals = [[], [], [], [], [], [], [], [], []]
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type() == Grounds.Turf:
				till()
			tradeSeed(Items.Sunflower_Seed)
			while get_water() < 0.5:
				use_item(Items.Water_Tank)
			plant(Entities.Sunflower)
			tupleSunfloweer = measure(), get_pos_x(), get_pos_y()
			if listPedals = None:
				listPedals.append(tupleSunfloweer)
			else:
				counterPedals = 0
				for x in listPedals:
					if measure > x[0]
						listPedals[counterPedals].insert(tupleSunfloweer)
					else:
						listPedals.append(tupleSunfloweer)					
			listPedals[15 - measure()].append(tupleSunfloweer)
			move(North)
		move(East)
	for i in listPedals:
		for j in i:
			goTo_x_y(j[0], j[1])
			while not can_harvest():
				continue
			harvest()