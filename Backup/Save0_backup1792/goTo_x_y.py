def goTo_x_y(x, y):
	while get_pos_x() > x:
		move(West)
	while get_pos_x() < x:
		move(East)	
	while get_pos_y() > y:
		move(South)
	while get_pos_y() < y:
		move(North)	
			
	