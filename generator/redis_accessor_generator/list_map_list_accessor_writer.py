from generator.redis_accessor_generator.list_accessor_writer import ListAccessorWriter

class ListMapListAccessorWriter(ListAccessorWriter):
	def __init__(self, table_desc, f):
		super(ListMapListAccessorWriter, self).__init__(table_desc, f)

	def write_getter_function(self):
		super(ListMapListAccessorWriter, self).write_getter_function()
		self.write_dict_list_getter_function()
		
	def write_dict_list_getter_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_string):\n'.format(
				self.redis_accessor_name.get_dict_list_getter_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write(
			'\t\t{}_string_list = self.{}(redis, id_string)\n'.format(
				self.table_desc['table_name'],
				self.redis_accessor_name.get_list_getter_function_name(self.table_desc['table_name'])
				)
			)
		self.f.write('\t\twith redis.pipeline() as pipe:\n')
		self.f.write(
			'\t\t\tfor {}_string in {}_string_list:\n'.format(
				self.table_desc['table_name'],
				self.table_desc['table_name']
				)
			)
		self.f.write(
			'\t\t\t\tpipe.hgetall(self.redis_table.{}(id_string, {}_string))\n'.format(
				self.redis_key_name.get_table_method_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		self.f.write(
			'\t\t\t{}_dict_list = pipe.execute()\n'.format(
				self.table_desc['table_name']
				)
			)
		self.f.write('\t\treturn {}_dict_list\n\n'.format(self.table_desc['table_name']))
	
	def write_adder_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_string, {}_string, d):\n'.format(
				self.redis_accessor_name.get_list_adder_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		self.f.write(
			'\t\tredis.rpush(self.redis_table.{}(id_string), {}_string)\n'.format(
				self.redis_key_name.get_list_method_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		self.f.write(
			'\t\tredis.hmset(self.redis_table.{}(id_string, {}_string), d)\n\n'.format(
				self.redis_key_name.get_table_method_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
	
	def write_remover_function(self):
		self.f.write(
			'\tdef {}(self, redis, id_string, {}_string):\n'.format(
				self.redis_accessor_name.get_list_remover_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		self.f.write(
			'\t\tredis.lrem(self.redis_table.{}(id_string), 0, {}_string)\n'.format(
				self.redis_key_name.get_list_method_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		self.f.write(
			'\t\tredis.delete(self.redis_table.{}(id_string, {}_string))\n\n'.format(
				self.redis_key_name.get_table_method_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)

"""
	def get_friend_list(self, redis, id_string):
		return redis.lrange(self.redis_table.get_friend_list_key(id_string), 0, -1)

	def get_friend_dict_list(self, redis, id_string):
		friend_string_list = self.get_friend_list(redis, id_string)
		with redis.pipeline() as pipe:
			for friend_string in friend_string_list:
				pipe.hgetall(self.redis_table.get_friend_key(id_string, friend_string))
			friend_dict_list = pipe.execute()
		return friend_dict_list

	def add_friend(self, redis, id_string, friend_string, d):
		redis.rpush(self.redis_table.get_friend_list_key(id_string), friend_string)
		redis.hmset(self.redis_table.get_friend_key(id_string, friend_string), d)

	def remove_friend(self, redis, id_string, friend_string):
		redis.lrem(self.redis_table.get_friend_list_key(id_string), 0, friend_string)
		redis.delete(self.redis_table.get_friend_key(id_string, friend_string))

"""