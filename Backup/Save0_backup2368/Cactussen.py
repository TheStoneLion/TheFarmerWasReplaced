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
for x in range(100):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if measure() > measure(East):
				swap(East)
			move(East)
		move(North)	