get_world_size()
while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_water() < 0.5:
			use_item(Items.Water_Tank)
		if (get_pos_y() == get_pos_x()):
			plant(Entities.Tree)
		elif get_pos_x() < 9:
			plant(Entities.Grass)
		else:
			if get_ground_type() == Grounds.Turf:
				till()
			tradeSeed(Items.Carrot_Seed)	
			plant(Entities.Carrots)
		move(North)
	move(East)