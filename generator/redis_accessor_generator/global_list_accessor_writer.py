from generator.redis_key_name import RedisKeyName

class GlobalListAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.redis_key_name = RedisKeyName()
	
	def write(self):
		self.write_getter_function()
		self.write_adder_function()
		self.write_remover_function()

	def write_getter_function(self):
		self.f.write('\tdef get_{}_list(self, redis):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\treturn redis.get(self.redis_table.{}())\n\n'.format(
						self.redis_key_name.get_list_method_name(self.table_desc['table_name'])
						)
					)
	
	def write_adder_function(self):
		self.f.write('\tdef add_{}(self, redis, {}_string):\n'.format(
						self.table_desc['table_name'], 
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\tredis.rpush(self.redis_table.{}(), {}_string)\n\n'.format( 
						self.redis_key_name.get_list_method_name(self.table_desc['table_name']),
						self.table_desc['table_name']
						)
					)
		
	def write_remover_function(self):
		self.f.write('\tdef remove_{}(self, redis, {}_string):\n'.format(
						self.table_desc['table_name'], 
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\tredis.lrem(self.redis_table.{}(), 0, {}_string)\n\n'.format( 
						self.redis_key_name.get_list_method_name(self.table_desc['table_name']),
						self.table_desc['table_name']
						)
					)
		
"""		
	def get_online_player_list(self, redis):
		return redis.get(self.redis_table.get_online_player_list_key())
	
	def add_online_player(self, redis, online_player_string):
		redis.rpush(self.redis_table.get_online_player_list_key(), online_player_string)
		
	def remove_online_player(self, redis, online_player_string):
		redis.lrem(self.redis_table.get_online_player_list_key(), 0, item_string)
"""	