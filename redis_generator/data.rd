[
	{
		"table_name": "user",
		"table_type": "map",
		"table_field": ["user_id", "user_name"]
	},
	
	{
		"table_name": "item",
		"table_type": "list"
	},
		{
		"table_name": "friend",
		"table_type": "list_map",
		"table_field": ["user_id", "user_name"]
	},
	
	{
		"table_name": "online_player",
		"table_type": "global_list"
	},
	
	{
		"table_name": "level_rank",
		"table_type": "global_sorted_set"
	},
	
	{
		"table_name": "race_score_rank",
		"table_type": "sorted_set"
	}

]
