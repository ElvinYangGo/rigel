from generator.plain_class_accessor_generator.plain_list_accessor_writer import PlainListAccessorWriter
from generator.plain_class_accessor_generator.plain_list_map_map_accessor_writer import PlainListMapMapAccessorWriter
from generator.redis_accessor_generator.list_map_list_accessor_writer import ListMapListAccessorWriter
from generator.plain_class_accessor_generator.plain_map_accessor_writer import PlainMapAccessorWriter

class PlainListMapListAccessorWriter(PlainListAccessorWriter):
	def __init__(self, table_desc, f):
		PlainListAccessorWriter.__init__(self, table_desc, f)
		self.plain_list_map_map_accessor_writer = PlainListMapMapAccessorWriter(table_desc, f)
		self.list_map_list_accessor_writer = ListMapListAccessorWriter(table_desc, f)
		self.plain_map_accessor_writer = PlainMapAccessorWriter(table_desc, f)
	def write_getter_function(self):
		self.f.write('\tdef get_{}(self, redis, id_int):\n'.format(self.plain_list_table_writer.get_file_name()))
		self.f.write(
			'\t\t{}_dict_list = self.redis_accessor.{}(redis, str(id_int))\n'.format(
				self.table_desc['table_name'],
				self.list_map_list_accessor_writer.get_dict_list_getter_function_name()
				)
			)
		self.f.write(
			'\t\t{}_list = [self.{}({}_dict) for {}_dict in {}_dict_list]\n'.format(
				self.table_desc['table_name'],
				self.plain_map_accessor_writer.get_table_builder_function_name(),
				self.table_desc['table_name'],
				self.table_desc['table_name'],
				self.table_desc['table_name']
				)
			)
		self.f.write(
			'\t\treturn {}({}_list)\n\n'.format(
				self.plain_list_table_writer.get_class_name(),
				self.table_desc['table_name']
				)
			)
					
	def write_adder_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_int, {}_int, {}):\n'.format(
				self.get_adder_function_name(),
				self.table_desc['table_name'],
				self.table_desc['table_name']
				)
			)
		self.f.write(
			'\t\t{}_dict = self.{}({})\n'.format(
				self.table_desc['table_name'],
				self.plain_list_map_map_accessor_writer.get_table_dict_builder_function_name(),
				self.table_desc['table_name']
				)
			)
		format_string = '\t\tself.redis_accessor.{}(redis, str(id_int), str({}_int), {}_dict)\n\n'
		self.f.write(
			format_string.format(
				self.get_adder_function_name(),
				self.table_desc['table_name'],
				self.table_desc['table_name']
				)
			)
	
	def write_remover_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_int, {}_int):\n'.format(
				self.get_remover_function_name(),
				self.table_desc['table_name']
				)
			)
		format_string = '\t\tself.redis_accessor.{}(redis, str(id_int), str({}_int))\n\n'
		self.f.write(
			format_string.format(
				self.get_remover_function_name(),
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