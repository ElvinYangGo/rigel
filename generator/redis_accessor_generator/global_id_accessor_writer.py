from generator.redis_key_name import RedisKeyName
from generator.redis_accessor_name import RedisAccessorName

class GlobalIDAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.redis_key_name = RedisKeyName()
		self.redis_accessor_name = RedisAccessorName()

	def write(self):
		self.write_incr_function()

	def write_incr_function(self):
		self.f.write(
			'\tdef {}(self, redis):\n'.format(
				self.redis_accessor_name.get_global_id_incr_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write(
			'\t\treturn redis.incr(self.redis_key.{}())\n\n'.format(
				self.redis_key_name.get_table_method_name(self.table_desc['table_name'])
				)
			)

"""
	def incr_account_id(self, redis):
		reurn redis.incr(self.redis_key.get_account_id_key())
"""