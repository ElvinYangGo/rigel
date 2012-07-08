from generator.redis_accessor_name import RedisAccessorName
from generator.plain_class_name import PlainClassName
from generator.redis_key_name import RedisKeyName

class PlainMapAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.redis_key_name = RedisKeyName()
		self.redis_accessor_name = RedisAccessorName()
		self.plain_class_name = PlainClassName()
	
	def write_import_declaration(self):
		import_format_string = 'from plain_class.{} import {}\n'.format(
			self.plain_class_name.get_file_name(self.table_desc['table_name']),
			self.plain_class_name.get_map_class_name(self.table_desc['table_name'])
			)
		self.f.write(import_format_string)

	def write(self):
		self.write_table_getter_function()
		self.write_table_setter_function()

		for field_pair in self.table_desc['table_field'].iteritems():
			self.write_field_getter_function(field_pair)
			self.write_field_setter_function(field_pair)

	def get_key_declaration_string(self):
		return 'id_int'
	
	def get_key_param_string(self):
		return 'str(id_int)'

	def write_table_getter_function(self):
		self.write_table_upper_level_getter_function()
		self.write_table_builder_function()
		
	def write_table_upper_level_getter_function(self):
		self.f.write(
			'\tdef {}(self, redis, {}):\n'.format(
				self.redis_accessor_name.get_map_getter_function_name(self.table_desc['table_name']),
				self.get_key_declaration_string()
				)
			)
		self.f.write(
			'\t\t{}_dict = self.redis_accessor.{}(redis, {})\n'.format(
				self.table_desc['table_name'],
				self.redis_accessor_name.get_map_getter_function_name(self.table_desc['table_name']),
				self.get_key_param_string()
				)
			)
		self.f.write(
			'\t\treturn self.build_{}_from_dict({}_dict)\n\n'.format(
				self.table_desc['table_name'],
				self.table_desc['table_name']
				)
			)
		
	def write_table_builder_function(self):
		self.f.write(
			'\tdef {}(self, {}_dict):\n'.format(
				self.plain_class_name.get_map_class_builder_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		for field_pair in self.table_desc['table_field'].iteritems():
			if field_pair[1]['data_type'] == 'int':
				self.f.write('\t\t{}_param = {}\n'.format(field_pair[0], field_pair[1]['default']))
			elif field_pair[1]['data_type'] == 'string':
				self.f.write("\t\t{}_param = '{}'\n".format(field_pair[0], field_pair[1]['default']))
			self.f.write('\t\tif self.redis_table.{}() in {}_dict:\n'.format(
							self.redis_key_name.get_table_field_method_name(
								self.table_desc['table_name'], 
								field_pair[0]
								),
							self.table_desc['table_name']
							)
						)
			format_string = ''
			if field_pair[1]['data_type'] == 'int':
				format_string = '\t\t\t{}_param = int({}_dict[self.redis_table.{}()])\n'
			elif field_pair[1]['data_type'] == 'string':
				format_string = '\t\t\t{}_param = {}_dict[self.redis_table.{}()]\n'
				
			self.f.write(format_string.format(
							field_pair[0],
							self.table_desc['table_name'],
							self.redis_key_name.get_table_field_method_name(
								self.table_desc['table_name'], 
								field_pair[0]
								)
							)
						)
			
		param_list = []
		for field_pair in self.table_desc['table_field'].iteritems():
			param_list.append('{}={}_param'.format(field_pair[0], field_pair[0]))
		param_string = ', '.join(param_list)
		self.f.write(
			'\t\treturn {}({})\n\n'.format(
				self.plain_class_name.get_map_class_name(self.table_desc['table_name']),
				param_string
				)
			)
	
	def write_table_setter_function(self):
		self.write_table_upper_level_setter_function()
		self.write_table_dict_builder_function()
		
	def write_table_upper_level_setter_function(self):
		self.f.write(
			'\tdef {}(self, redis, {}, {}):\n'.format(
				self.redis_accessor_name.get_map_setter_function_name(self.table_desc['table_name']),
				self.get_key_declaration_string(),
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
		self.f.write(
			'\t\tself.redis_accessor.{}(redis, {}, {}_dict)\n\n'.format(
				self.redis_accessor_name.get_map_setter_function_name(self.table_desc['table_name']),
				self.get_key_param_string(),
				self.table_desc['table_name']
				)
			)

	def write_table_dict_builder_function(self):
		self.f.write(
			'\tdef {}(self, {}):\n'.format(
				self.plain_class_name.get_map_dict_builder_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		self.f.write('\t\t{}_dict = {{}}\n'.format(self.table_desc['table_name']))
		for field_pair in self.table_desc['table_field'].iteritems():
			format_string = ''
			if field_pair[1]['data_type'] == 'int':
				format_string = '\t\t{}_dict[self.redis_table.{}()] = str({}.{}())\n'
			elif field_pair[1]['data_type'] == 'string':
				format_string = '\t\t{}_dict[self.redis_table.{}()] = {}.{}()\n'
			self.f.write(
				format_string.format(
					self.table_desc['table_name'],
					self.redis_key_name.get_table_field_method_name(
						self.table_desc['table_name'], 
						field_pair[0]
						),
					self.table_desc['table_name'],
					self.plain_class_name.get_map_field_getter_function_name(field_pair[0])
					)
				)
				
		self.f.write(
			'\t\treturn {}_dict\n\n'.format(
				self.table_desc['table_name']
				)
			)

	def write_field_getter_function(self, field_pair):
		self.f.write(
			'\tdef {}(self, redis, {}):\n'.format(
				self.redis_accessor_name.get_map_field_getter_function_name(self.table_desc['table_name'], field_pair[0]),
				self.get_key_declaration_string()
				)
			)
		if field_pair[1]['data_type'] == 'string':
			self.f.write(
				'\t\treturn self.redis_accessor.{}(redis, {})\n\n'.format(
					self.redis_accessor_name.get_map_field_getter_function_name(self.table_desc['table_name'], field_pair[0]),
					self.get_key_param_string()
					)
				)
		elif field_pair[1]['data_type'] == 'int':
			self.f.write(
				'\t\treturn int(self.redis_accessor.{}(redis, {}))\n\n'.format(
					self.redis_accessor_name.get_map_field_getter_function_name(self.table_desc['table_name'], field_pair[0]),
					self.get_key_param_string()
					)
				)
	
	def write_field_setter_function(self, field_pair):
		self.f.write(
			'\tdef {}(self, redis, {}, {}):\n'.format(
				self.redis_accessor_name.get_map_field_setter_function_name(self.table_desc['table_name'], field_pair[0]),
				self.get_key_declaration_string(),
				field_pair[0])
			)
		if field_pair[1]['data_type'] == 'string':
			self.f.write(
				'\t\tself.redis_accessor.{}(redis, {}, {})\n\n'.format(
					self.redis_accessor_name.get_map_field_setter_function_name(self.table_desc['table_name'], field_pair[0]),
					self.get_key_param_string(),
					field_pair[0]
					)
				)
		elif field_pair[1]['data_type'] == 'int':
			self.f.write(
				'\t\tself.redis_accessor.{}(redis, {}, str({}))\n\n'.format(
					self.redis_accessor_name.get_map_field_setter_function_name(self.table_desc['table_name'], field_pair[0]),
					self.get_key_param_string(),
					field_pair[0]
					)
				)
	
"""
	def get_user(self, redis, id_int):
		user_dict = self.redis_accessor.get_user(redis, str(id_int))
		return self.build_user_from_dict(user_dict)

	def build_user_from_user_dict(self, user_dict):
		user_name_param = ''
		if self.redis_table.get_user_table_user_name_field() in user_dict:
			user_name_param = user_dict[self.redis_table.get_user_table_user_name_field()]
		user_id_param = 0
		if self.redis_table.get_user_table_user_id_field() in user_dict:
			user_id_param = int(user_dict[self.redis_table.get_user_table_user_id_field()])
		return User(user_name=user_name_param, user_id=user_id_param)
	
	def set_user(self, redis, id_int, user):
		user_dict = self.build_user_dict_from_user(user)
		self.redis_accessor.set_user(redis, str(id_int), user_dict)
		
	def build_user_dict_from_user(self, user):
		user_dict = {}
		user_dict[self.redis_table.get_user_table_user_name_field()] = user.get_user_name()
		user_dict[self.redis_table.get_user_table_user_id_field()] = str(user.get_user_id())
		return user_dict

	def get_user_table_user_name(self, redis, id_int):
		return self.redis_accessor.get_user_table_user_name(redis, str(id_int))

	def set_user_table_user_name(self, redis, id_int, user_name):
		self.redis_accessor.set_user_table_user_name(redis, str(id_int), user_name)

	def get_user_table_user_id(self, redis, id_int):
		return int(self.redis_accessor.get_user_table_user_id(redis, str(id_int)))

	def set_user_table_user_id(self, redis, id_int, user_id):
		self.redis_accessor.set_user_table_user_id(redis, str(id_int), str(user_id))
"""	