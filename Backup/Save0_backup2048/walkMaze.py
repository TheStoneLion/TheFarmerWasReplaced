while True:
	plant(Entities.Bush)
	while get_entity_type() != Entities.Treasure and get_entity_type() != Entities.Hedge:
		trade(Items.Fertilizer)
		use_item(Items.Fertilizer)
	listMoves = [West, North, East, South]
	pointerMoves = 0
	while not get_entity_type() == Entities.Treasure:
		while move(listMoves[pointerMoves]) == False:
			pointerMoves += 1
			if pointerMoves > len(listMoves) - 1:
				pointerMoves = 0
		pointerMoves -= 1
		if pointerMoves < 0:
			pointerMoves += len(listMoves)
	harvest()