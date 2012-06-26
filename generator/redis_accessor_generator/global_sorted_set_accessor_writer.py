from generator.table_method_name import TableMethodName

class GlobalSortedSetAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.table_method_name = TableMethodName()
		
	def write(self):
		self.write_getter_function()
		self.write_adder_function()
		self.write_remover_function()
		self.write_range_getter_function()

	def write_getter_function(self):
		self.f.write('\tdef get_{}(self, redis, member_string):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\treturn redis.zrank(self.redis_table.{}(), member_string)\n\n'.format(
						self.table_method_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
	
	def write_adder_function(self):
		self.f.write('\tdef add_{}(self, redis, member_string, score):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\tredis.zadd(self.redis_table.{}(), score, member_string)\n\n'.format(
						self.table_method_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
			
	def write_remover_function(self):
		self.f.write('\tdef remove_{}(self, redis, member_string):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\tredis.zrem(self.redis_table.{}(), member_string)\n\n'.format(
						self.table_method_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
			
	def write_range_getter_function(self):
		self.f.write('\tdef get_{}_range(self, redis, start, stop):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\treturn redis.zrange(self.redis_table.{}(), start, stop)\n\n'.format(
						self.table_method_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
			
		
"""
	def get_level_rank(self, redis, member_string):
		return redis.zrank(self.redis_table.get_level_rank_key(), member_string)
	
	def add_level_rank(self, redis, member_string, score)
		redis.zadd(self.redis_table.get_level_rank_key(), score, member_string)
	
	def remove_level_rank(self, redis, member_string)
		redis.zrem(self.redis_table.get_level_rank_key(), member_string)
		
	def get_level_rank_range(self, redis, start, stop)
		return redis.zrange(self.redis_table.get_level_rank_key(), start, stop)
"""