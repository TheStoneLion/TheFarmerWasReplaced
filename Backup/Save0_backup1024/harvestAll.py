worldSize = get_world_size()	
listPedels = []
while True:
	for i in range(worldSize):
		for j in range(worldSize):
			if can_harvest():
				harvest()
			move(North)
		move(East)