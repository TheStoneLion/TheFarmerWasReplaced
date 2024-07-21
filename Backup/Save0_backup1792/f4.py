makeMaze()
def makeMaze():
	plant(Entities.Bush)
	while get_entity_type() != Entities.Treasure and get_entity_type() != Entities.Hedge:
		trade(Items.Fertilizer)
		use_item(Items.Fertilizer)