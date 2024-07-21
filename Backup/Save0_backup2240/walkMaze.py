while True:
	plant(Entities.Bush)
	while get_entity_type() != Entities.Treasure and get_entity_type() != Entities.Hedge:
		tradeSeed(Items.Fertilizer)
		use_item(Items.Fertilizer)
	moveList = [West, North, East, South]
	movePointer = 0
	while not get_entity_type() == Entities.Treasure:
		while move(moveList[movePointer]) == False:
			movePointer += 1
			if movePointer > (len(moveList) - 1):
				movePointer = 0
		movePointer -= 1
		if movePointer < 0:
			movePointer += len(moveList)
	harvest()