from generator.redis_accessor_name import RedisAccessorName

class PlainPairMapAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.redis_accessor_name = RedisAccessorName()

	def write(self):
		self.write_table_getter_function()
		self.write_table_setter_function()
		self.write_table_setnx_function()

	def write_table_getter_function(self):
		self.f.write(
			'\tdef {}(self, redis, field):\n'.format(
				self.redis_accessor_name.get_map_getter_function_name(self.table_desc['table_name'])
				)
			)
		if self.table_desc['data_type'] == 'string':
			self.f.write(
				'\t\treturn self.redis_accessor.{}(redis, field)\n\n'.format(
					self.redis_accessor_name.get_map_getter_function_name(self.table_desc['table_name'])
					)
				)
		elif self.table_desc['data_type'] == 'int':
			self.f.write(
				'\t\tvalue_string = self.redis_accessor.{}(redis, field)\n'.format(
					self.redis_accessor_name.get_map_getter_function_name(self.table_desc['table_name'])
					)
				)
			self.f.write('\t\tif value_string is not None:\n')
			self.f.write('\t\t\treturn int(value_string)\n')
			self.f.write('\t\telse:\n')
			self.f.write('\t\t\treturn 0\n\n')

	def write_table_setter_function(self):
		self.f.write(
			'\tdef {}(self, redis, field, value):\n'.format(
				self.redis_accessor_name.get_map_setter_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write(
			'\t\tself.redis_accessor.{}(redis, field, str(value))\n\n'.format(
				self.redis_accessor_name.get_map_setter_function_name(self.table_desc['table_name'])
				)
			)

	def write_table_setnx_function(self):
		self.f.write(
			'\tdef {}(self, redis, field, value):\n'.format(
				self.redis_accessor_name.get_map_setnx_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write(
			'\t\treturn self.redis_accessor.{}(redis, field, str(value))\n\n'.format(
				self.redis_accessor_name.get_map_setnx_function_name(self.table_desc['table_name'])
				)
			)

"""
	def get_user_name_to_id(self, redis, field):
		#return self.redis_accessor.get_user_name_to_id(redis, field)
		value_string = self.redis_accessor.get_user_name_to_id(redis, field)
		if not value_string:
			return int(value_string)
		else:
			return 0

	def set_user_name_to_id(self, redis, field, value):
		self.redis_accessor.set_user_name_to_id(redis, field, str(value))

	def setnx_user_name_to_id(self, redis, field, value):
		self.redis_accessor.setnx_user_name_to_id(redis, field, str(value))
"""