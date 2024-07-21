listMoves = [West, North, East, South]
pointerMoves = 0

while not get_entity_type() == Entities.Treasure:
	boolMove = False
	while boolMove == False:
		boolMove = move(listMoves[pointerMoves])
		pointerMoves += 1
		if pointerMoves > len(listMoves) - 1:
			pointerMoves = 0
	if pointerMoves == 0 or 1:
		pointerMoves = 0
	else:
		pointerMoves -= 2	
	