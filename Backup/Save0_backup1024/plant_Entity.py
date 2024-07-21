def plant_Entity(entityType, groundType):	
	if (entityType == Entities.Carrots):
		tradeSeed(Items.Carrot_Seed)
		if get_ground_type() == Grounds.Turf:
			till()
	elif (entityType == Entities.Pumpkin):
		tradeSeed(Items.Pumpkin_Seed)
		if get_ground_type() == Grounds.Turf:
			till()
	elif (entityType == Entities.Sunflower):
		tradeSeed(Items.Sunflower_Seed)
		if get_ground_type() == Grounds.Turf:
			till()
	else:
		if get_ground_type() == Grounds.Soil:
			till()
	plant(entityType)	