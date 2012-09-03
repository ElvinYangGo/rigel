from generator.redis_key_name import RedisKeyName
from generator.redis_accessor_name import RedisAccessorName

class PairMapAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.redis_key_name = RedisKeyName()
		self.redis_accessor_name = RedisAccessorName()

	def write(self):
		self.write_field_getter_function()
		self.write_field_setter_function()

	def write_field_getter_function(self):
		self.f.write(
			'\tdef {}(self, redis, field):\n'.format(
				self.redis_accessor_name.get_map_getter_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write('\t\treturn redis.hget(self.redis_table.{}(), field)\n\n'.format(
						self.redis_key_name.get_table_method_name(self.table_desc['table_name'])
						)
					)

	def write_field_setter_function(self):
		self.f.write(
			'\tdef {}(self, redis, field, value_string):\n'.format(
				self.redis_accessor_name.get_map_setter_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write(
			'\t\tredis.hset(self.redis_table.{}(), field, value_string)\n\n'.format(
				self.redis_key_name.get_table_method_name(self.table_desc['table_name'])
				)
			)

"""
	def get_user_name_to_id(self, redis, field):
		return redis.hget(self.redis_table.get_user_name_to_id_key())

	def set_user_name_to_id(self, redis, field, value_string):
		redis.hset(self.redis_table.get_user_name_to_id_key(), field, value_string)
"""