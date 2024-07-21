makeMaze()
def makeMaze():
	plant_Entity(Entities.Bush, Grounds.Soil)
	while get_entity_type() != Entities.Treasure and get_entity_type() != Entities.Hedge:
		trade(Items.Fertilizer)
		use_item(Items.Fertilizer)