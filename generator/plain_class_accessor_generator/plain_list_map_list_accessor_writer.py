from generator.plain_class_accessor_generator.plain_list_accessor_writer import PlainListAccessorWriter

class PlainListMapListAccessorWriter(PlainListAccessorWriter):
	def __init__(self, table_desc, f):
		super(PlainListMapListAccessorWriter, self).__init__(table_desc, f)

	def write_getter_function(self):
		self.f.write(
			'\tdef get_{}(self, redis, id_int):\n'.format(
				self.plain_class_name.get_list_file_name(self.table_desc['table_name'])
				)
			)
		self.f.write(
			'\t\t{}_dict_list = self.redis_accessor.{}(redis, str(id_int))\n'.format(
				self.table_desc['table_name'],
				self.redis_accessor_name.get_dict_list_getter_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write(
			'\t\t{}_list = [self.{}({}_dict) for {}_dict in {}_dict_list]\n'.format(
				self.table_desc['table_name'],
				self.plain_class_name.get_map_class_builder_function_name(self.table_desc['table_name']),
				self.table_desc['table_name'],
				self.table_desc['table_name'],
				self.table_desc['table_name']
				)
			)
		self.f.write(
			'\t\treturn {}({}_list)\n\n'.format(
				self.plain_class_name.get_list_class_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
					
	def write_adder_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_int, {}_int, {}):\n'.format(
				self.redis_accessor_name.get_list_adder_function_name(self.table_desc['table_name']),
				self.table_desc['table_name'],
				self.table_desc['table_name']
				)
			)
		self.f.write(
			'\t\t{}_dict = self.{}({})\n'.format(
				self.table_desc['table_name'],
				self.plain_class_name.get_map_dict_builder_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		format_string = '\t\tself.redis_accessor.{}(redis, str(id_int), str({}_int), {}_dict)\n\n'
		self.f.write(
			format_string.format(
				self.redis_accessor_name.get_list_adder_function_name(self.table_desc['table_name']),
				self.table_desc['table_name'],
				self.table_desc['table_name']
				)
			)
	
	def write_remover_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_int, {}_int):\n'.format(
				self.redis_accessor_name.get_list_remover_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		format_string = '\t\tself.redis_accessor.{}(redis, str(id_int), str({}_int))\n\n'
		self.f.write(
			format_string.format(
				self.redis_accessor_name.get_list_remover_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)	
		
"""
	def get_friend_manager(self, redis, id_int):
		friend_dict_list = self.redis_accessor.get_friend_dict_list(redis, str(id_int))
		friend_list = [self.build_friend_from_friend_dict(friend_dict) for friend_dict in friend_dict_list]
		return FriendManager(friend_list)

	def add_friend(self, redis, id_int, friend_int, friend):
		friend_dict = self.build_friend_dict_from_friend(friend)
		self.redis_accessor.add_friend(redis, str(id_int), str(friend_int), friend_dict)

	def remove_friend(self, redis, id_int, friend_int):
		self.redis_accessor.remove_friend(redis, str(id_int), str(friend_int))

"""