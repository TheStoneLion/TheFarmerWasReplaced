while True:
    listPedals = []
    listCounter = 0
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_ground_type() == Grounds.Turf:
                till()
            tradeSeed(Items.Sunflower_Seed)
            while get_water() < 0.5:
                use_item(Items.Water_Tank)
            plant(Entities.Sunflower)
            tupleSunflower = measure(), get_pos_x(), get_pos_y()
            if listcounter == 0
            listPedals[15 - measure()].append(tupleSunflower)
            move(North)
        move(East)
    for i in listPedals:
        for j in i:
            goTo_x_y(j[0], j[1])
            while not can_harvest():
                continue
			harvest()