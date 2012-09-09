from generator.redis_accessor_name import RedisAccessorName

class PlainGlobalIDAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.redis_accessor_name = RedisAccessorName()

	def write(self):
		self.write_incr_function()

	def write_incr_function(self):
		self.f.write(
			'\tdef {}(self, redis):\n'.format(
				self.redis_accessor_name.get_global_id_incr_function_name(self.table_desc['table_name'])
				)
			)
		if self.table_desc['data_type'] == 'string':
			self.f.write(
				'\t\treturn self.redis_accessor.{}(redis)\n\n'.format(
					self.redis_accessor_name.get_global_id_incr_function_name(self.table_desc['table_name'])
					)
				)
		elif self.table_desc['data_type'] == 'int':
			self.f.write(
				'\t\tvalue_string = self.redis_accessor.{}(redis)\n'.format(
					self.redis_accessor_name.get_global_id_incr_function_name(self.table_desc['table_name'])
					)
				)
			self.f.write('\t\tif value_string is not None:\n')
			self.f.write('\t\t\treturn int(value_string)\n')
			self.f.write('\t\telse:\n')
			self.f.write('\t\t\treturn 0\n\n')
"""
	def incr_account_id(self, redis, field):
		#return self.redis_accessor.incr_account_id(redis)
		value_string = self.redis_accessor.incr_account_id(redis)
		if not value_string:
			return int(value_string)
		else:
			return 0
"""