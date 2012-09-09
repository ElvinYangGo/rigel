[
	{
		"table_name": "user",
		"table_type": "map",
		"table_field":
			[
				{"field_name": "user_id", "data_type": "int", "default": 0},
				{"field_name": "user_name", "data_type": "string", "default": ""},
				{"field_name": "password", "data_type": "string", "default": ""}
			]
	},
	
	{
		"table_name": "item",
		"table_type": "list",
		"data_type": "int"
	},
	
	{
		"table_name": "friend",
		"table_type": "list_map",
		"table_field":
			[
				{"field_name": "user_id", "data_type": "int", "default": 0},
				{"field_name": "user_name", "data_type": "string", "default": ""}
			]
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
	},

	{
		"table_name": "user_name_to_id",
		"table_type": "pair_map",
		"data_type": "int"
	},

	{
		"table_name": "client_connection_info",
		"table_type": "map",
		"table_field":
			[
				{"field_name": "client_id", "data_type": "int", "default": 0},
				{"field_name": "gateway_server_name", "data_type": "string", "default": ""},
				{"field_name": "game_server_name", "data_type": "string", "default": ""},
				{"field_name": "token", "data_type": "string", "default": ""}
			]
	},

	{
		"table_name": "account_id",
		"table_type": "global_id",
		"data_type": "int"
	}
]
