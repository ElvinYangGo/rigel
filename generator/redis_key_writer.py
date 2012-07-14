from generator.redis_key_name import RedisKeyName

class RedisKeyWriter(object):
	def __init__(self, file_name, table_desc_array):
		self.file_name = file_name
		self.table_desc_array = table_desc_array
		self.redis_key_name = RedisKeyName()

	def write(self):
		with open(self.file_name, 'w') as f:
			self.write_class_head(f)
			self.write_class_body(f)
			f.flush()
	
	def write_class_head(self, f):
		f.write('#This file is generated by program. DO NOT EDIT IT MANUALLY!\n')
		f.write('class RedisKey(object):\n')
	
	def write_class_body(self, f):
		for table_desc in self.table_desc_array:
			table_type = table_desc['table_type']
			if table_type == 'map':
				self.write_map_table(table_desc, f)
			elif table_type == 'list':
				self.write_list_table(table_desc, f)
			elif table_type == 'list_map':
				self.write_list_map_table(table_desc, f)	
			elif table_type == 'global_list':
				self.write_global_list_table(table_desc, f)
			elif table_type == 'global_sorted_set':
				self.write_global_sorted_set_table(table_desc, f)
			elif table_type == 'sorted_set':
				self.write_sorted_set_table(table_desc, f)
				
	def write_map_table(self, table_desc, f):
		self.write_map_key_getter_function(table_desc, f)
		self.write_map_field_getter_function(table_desc, f)

	def write_map_key_getter_function(self, table_desc, f):
		f.write('\tdef {}(self, id_string):\n'.format(
					self.redis_key_name.get_table_method_name(table_desc['table_name'])
					)
				)
		f.write("\t\treturn '{}:' + id_string\n\n".format(table_desc['table_name']))
	
	def write_map_field_getter_function(self, table_desc, f):
		for field in table_desc['table_field'].keys():
			f.write('\tdef {}(self):\n'.format(
						self.redis_key_name.get_table_field_method_name(table_desc['table_name'], field)
						)
					)
			f.write("\t\treturn '{}'\n\n".format(field))
	
	def write_list_table(self, table_desc, f):
		f.write('\tdef {}(self, id_string):\n'.format(
					self.redis_key_name.get_list_method_name(table_desc['table_name'])
					)
				)
		f.write("\t\treturn '{}_list:' + id_string\n\n".format(table_desc['table_name']))

	def write_list_map_table(self, table_desc, f):
		self.write_list_table(table_desc, f)
		self.write_list_map_key_getter_function(table_desc, f)
		self.write_map_field_getter_function(table_desc, f)
		
	def write_list_map_key_getter_function(self, table_desc, f):
		f.write('\tdef {}(self, id_string, second_id_string):\n'.format(
					self.redis_key_name.get_table_method_name(table_desc['table_name'])
					)
				)
		f.write("\t\treturn '{}:' + id_string + ':' + second_id_string\n\n".format(table_desc['table_name']))
		
	def write_global_list_table(self, table_desc, f):
		f.write('\tdef {}(self):\n'.format(
					self.redis_key_name.get_list_method_name(table_desc['table_name'])
					)
				)
		f.write("\t\treturn '{}_list'\n\n".format(table_desc['table_name']))
		
	def write_global_sorted_set_table(self, table_desc, f):
		f.write('\tdef {}(self):\n'.format(
					self.redis_key_name.get_table_method_name(table_desc['table_name'])
					)
				)
		f.write("\t\treturn '{}'\n\n".format(table_desc['table_name']))
		
	def write_sorted_set_table(self, table_desc, f):
		f.write('\tdef {}(self, id_string):\n'.format(
					self.redis_key_name.get_table_method_name(table_desc['table_name'])
					)
				)
		f.write("\t\treturn '{}:' + id_string\n\n".format(table_desc['table_name']))
		
"""
#This file is generated by program. DO NOT EDIT IT MANUALLY!
class RedisKey(object):
	def get_user_key(self, id_string):
		return 'user:' + id_string

	def get_user_table_user_name_field(self):
		return 'user_name'

	def get_user_table_user_id_field(self):
		return 'user_id'

	def get_item_list_key(self, id_string):
		return 'item_list:' + id_string

	def get_friend_list_key(self, id_string):
		return 'friend_list:' + id_string

	def get_friend_key(self, id_string, second_id_string):
		return 'friend:' + id_string + ':' + second_id_string

	def get_friend_table_user_name_field(self):
		return 'user_name'

	def get_friend_table_user_id_field(self):
		return 'user_id'

	def get_online_player_list_key(self):
		return 'online_player_list'

	def get_level_rank_key(self):
		return 'level_rank'

	def get_race_score_rank_key(self, id_string):
		return 'race_score_rank:' + id_string

"""