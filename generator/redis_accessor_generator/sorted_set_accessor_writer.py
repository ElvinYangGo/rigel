from generator.table_method_name import TableMethodName

class SortedSetAccessorWriter(object):
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
		self.f.write('\tdef get_{}(self, redis, id_string, member_string):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\treturn redis.zrank(self.redis_table.{}(id_string), member_string)\n\n'.format(
						self.table_method_name.get_table_method_name(self.table_desc['table_name'])
						)
					)

	def write_adder_function(self):
		self.f.write('\tdef add_{}(self, redis, id_string, member_string, score):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\tredis.zadd(self.redis_table.{}(id_string), score, member_string)\n\n'.format(
						self.table_method_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
			
	def write_remover_function(self):
		self.f.write('\tdef remove_{}(self, redis, id_string, member_string):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\tredis.zrem(self.redis_table.{}(id_string), member_string)\n\n'.format(
						self.table_method_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
			
	def write_range_getter_function(self):
		self.f.write('\tdef get_{}_range(self, redis, id_string, start, stop):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\treturn redis.zrange(self.redis_table.{}(id_string), start, stop)\n\n'.format(
						self.table_method_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
	
"""
	def get_race_score_rank(self, redis, id_string, member_string):
		return redis.zrank(self.redis_table.get_race_score_rank_key(id_string), member_string)
		
	def add_race_score_rank(self, redis, id_string, member_string, score):
		redis.zadd(self.redis_table.get_race_score_rank_key(id_string), member_string, score)
	
	def remove_race_score_rank(self, redis, id_string, member_string):
		redis.zrem(self.redis_table.get_race_score_rank_key(id_string), member_string)
	
	def get_race_score_rank_range(self, redis, id_string, start, stop):
		return redis.zrange(self.redis_table.get_race_score_rank_key(id_string), start, stop)
"""
