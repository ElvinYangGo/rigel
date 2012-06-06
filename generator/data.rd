[
	{
		"table_name": "user",
		"table_type": "map",
		"table_field": {"user_id": "int", "user_name": "string"}
	},
	
	{
		"table_name": "item",
		"table_type": "list",
		"data_type": "int"
	},
		{
		"table_name": "friend",
		"table_type": "list_map",
		"table_field": {"user_id": "int", "user_name": "string"}
	},
	
	{
		"table_name": "online_player",
		"table_type": "global_list",
		"data_type": "int"
	},
	
	{
		"table_name": "level_rank",
		"table_type": "global_sorted_set",
		"data_type": "int"
	},
	
	{
		"table_name": "race_score_rank",
		"table_type": "sorted_set",
		"data_type": "int"
	}

]
