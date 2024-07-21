def goTo_x_y(x, y):
	while get_pos_x() != x or get_pos_y() != y:
		while get_pos_x() > x:
			if get_pos_x() - x < x + get_world_size() - get_pos_x(): 
				move(West)
			else:
				move(East)
		while get_pos_x() < x:
			if x - get_pos_x() < get_pos_x() + get_world_size() - x: 
				move(East)
			else:
				move(West)
		while get_pos_y() > y:
			if get_pos_y() - y < y + get_world_size() - get_pos_y(): 
				move(South)
			else:
				move(North)
		while get_pos_y() < y:
			if y - get_pos_y() < get_pos_y() + get_world_size() - y: 
				move(North)
			else:
				move(South)