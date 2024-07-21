if can_harvest():
	harvest()
while True:
	emptySpaces = 0
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			while get_entity_type() != Entities.Pumpkin:
				if get_ground_type() == Grounds.Turf:
					till()
				if get_water() < 0.5:
					use_item(Items.Water_Tank)
				tradeSeed(Items.Pumpkin_Seed)
				plant(Entities.Pumpkin)
				if not can_harvest():
					emptySpaces += 1
			move(North)
		move(East)
	if emptySpaces == 0:
		harvest()
	
	
	
	
	