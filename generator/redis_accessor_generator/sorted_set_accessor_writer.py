from generator.redis_key_name import RedisKeyName
from generator.redis_accessor_name import RedisAccessorName

class SortedSetAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.redis_key_name = RedisKeyName()
		self.redis_accessor_name = RedisAccessorName()

	def write(self):
		self.write_getter_function()
		self.write_adder_function()
		self.write_remover_function()
		self.write_range_getter_function()

	def write_getter_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_string, member_string):\n'.format(
				self.redis_accessor_name.get_sorted_set_getter_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write('\t\treturn redis.zrank(self.redis_key.{}(id_string), member_string)\n\n'.format(
						self.redis_key_name.get_table_method_name(self.table_desc['table_name'])
						)
					)

	def write_adder_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_string, member_string, score):\n'.format(
				self.redis_accessor_name.get_sorted_set_adder_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write('\t\tredis.zadd(self.redis_key.{}(id_string), score, member_string)\n\n'.format(
						self.redis_key_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
			
	def write_remover_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_string, member_string):\n'.format(
				self.redis_accessor_name.get_sorted_set_remover_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write('\t\tredis.zrem(self.redis_key.{}(id_string), member_string)\n\n'.format(
						self.redis_key_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
			
	def write_range_getter_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_string, start, stop):\n'.format(
				self.redis_accessor_name.get_sorted_set_range_getter_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write('\t\treturn redis.zrange(self.redis_key.{}(id_string), start, stop)\n\n'.format(
						self.redis_key_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
	
"""
	def get_race_score_rank(self, redis, id_string, member_string):
		return redis.zrank(self.redis_key.get_race_score_rank_key(id_string), member_string)
		
	def add_race_score_rank(self, redis, id_string, member_string, score):
		redis.zadd(self.redis_key.get_race_score_rank_key(id_string), member_string, score)
	
	def remove_race_score_rank(self, redis, id_string, member_string):
		redis.zrem(self.redis_key.get_race_score_rank_key(id_string), member_string)
	
	def get_race_score_rank_range(self, redis, id_string, start, stop):
		return redis.zrange(self.redis_key.get_race_score_rank_key(id_string), start, stop)
"""
