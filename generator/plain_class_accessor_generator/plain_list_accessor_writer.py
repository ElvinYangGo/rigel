from generator.plain_class_name import PlainClassName
from generator.redis_accessor_name import RedisAccessorName

class PlainListAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.plain_class_name = PlainClassName()
		self.redis_accessor_name = RedisAccessorName()
		
	def write_import_declaration(self):
		import_format_string = 'from plain_class.{} import {}\n'
		self.f.write(
			import_format_string.format(
				self.plain_class_name.get_list_file_name(self.table_desc['table_name']),
				self.plain_class_name.get_list_class_name(self.table_desc['table_name'])
				)
			)

	def write(self):
		self.write_getter_function()
		self.write_adder_function()
		self.write_remover_function()

	def write_getter_function(self):
		self.f.write(
			'\tdef get_{}_manager(self, redis, id_int):\n'.format(
				self.table_desc['table_name']
				)
			)
		if self.table_desc['data_type'] == 'string':
			self.f.write(
				'\t\t{}_list = self.redis_accessor.{}(redis, str(id_int))\n'.format(
					self.table_desc['table_name'],
					self.redis_accessor_name.get_list_getter_function_name(self.table_desc['table_name'])
					)
				)		
			self.f.write(
				'\t\treturn {}({}_list)\n\n'.format(
					self.plain_class_name.get_list_class_name(self.table_desc['table_name']),
					self.table_desc['table_name']
					)
				)
		elif self.table_desc['data_type'] == 'int':
			self.f.write(
				'\t\t{}_list_string = self.redis_accessor.{}(redis, str(id_int))\n'.format(
					self.table_desc['table_name'],
					self.redis_accessor_name.get_list_getter_function_name(self.table_desc['table_name'])
					)
				)
			self.f.write('\t\t{}_list = [int({}_string) for {}_string in {}_list_string]\n'.format(
					self.table_desc['table_name'],
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
			'\tdef {}(self, redis, id_int, {}):\n'.format(
				self.redis_accessor_name.get_list_adder_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		if self.table_desc['data_type'] == 'int':
			format_string = '\t\tself.redis_accessor.{}(redis, str(id_int), str({}))\n\n'
		elif self.table_desc['data_type'] == 'string':
			format_string = '\t\tself.redis_accessor.{}(redis, str(id_int), {})\n\n'
		self.f.write(
			format_string.format(
				self.redis_accessor_name.get_list_adder_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
	
	def write_remover_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_int, {}):\n'.format(
				self.redis_accessor_name.get_list_remover_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		if self.table_desc['data_type'] == 'int':
			format_string = '\t\tself.redis_accessor.{}(redis, str(id_int), str({}))\n\n'
		elif self.table_desc['data_type'] == 'string':
			format_string = '\t\tself.redis_accessor.{}(redis, str(id_int), {})\n\n'
		self.f.write(
			format_string.format(
				self.redis_accessor_name.get_list_remover_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)	
	
"""
	def get_item_manager(self, redis, id_int):
		item_list_string = self.redis_accessor.get_item_list(redis, str(id_int)) 
		item_list = [int(item_string) for item_string in item_list_string] 
		return ItemManager(item_list)
		#item_list = self.redis_accessor.get_item_list(redis, str(id_int))
		#return ItemManager(item_list)

	def add_item(self, redis, id_int, item):
		self.redis_accessor.add_item(redis, str(id_int), str(item))
		#self.redis_accessor.add_item(redis, str(id_int), item)

	def remove_item(self, redis, id_int, item):
		self.redis_accessor.remove_item(redis, str(id_int), str(item))
		#self.redis_accessor.remove_item(redis, str(id_int), item)
"""
