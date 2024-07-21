#trade(Items.Empty_Tank)
get_world_size()
while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_water() < 0.5:
			use_item(Items.Water_Tank)
#				if get_pos_x() >= 0:
#					plant_Entity(Entities.Carrots, Grounds.Turf)
#					break
		if (get_pos_y() == get_pos_x()):
			plant_Entity(Entities.Tree, Grounds.Soil)
		elif get_pos_x() < 7:
#			plant_Entity(Entities.Carrots, Grounds.Turf)
			plant_Entity(Entities.Grass, Grounds.Soil)
		else:
			plant_Entity(Entities.Carrots, Grounds.Turf)
#			plant_Entity(Entities.Bush, Grounds.Soil)
#			plant_Entity(Entities.Pumpkin, Grounds.Turf)
		move(North)
	move(East)