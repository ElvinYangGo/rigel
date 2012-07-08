from generator.redis_accessor_name import RedisAccessorName

class PlainGlobalListAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.redis_accessor_name = RedisAccessorName()

	def write(self):
		self.write_getter_function()
		self.write_adder_function()
		self.write_remover_function()

	def write_getter_function(self):
		self.f.write(
			'\tdef {}(self, redis):\n'.format(
				self.redis_accessor_name.get_list_getter_function_name(self.table_desc['table_name'])
				)
			)
		if self.table_desc['data_type'] == 'string':
			self.f.write(
				'\t\treturn self.redis_accessor.{}(redis)\n\n'.format(
					self.redis_accessor_name.get_list_getter_function_name(self.table_desc['table_name'])
					)
				)
		elif self.table_desc['data_type'] == 'int':
			self.f.write(
				'\t\tstring_list = self.redis_accessor.{}(redis)\n'.format(
					self.redis_accessor_name.get_list_getter_function_name(self.table_desc['table_name'])
					)
				)
			self.f.write(
				'\t\t{}_list = [int({}_string) for {}_string in string_list]\n'.format(
					self.table_desc['table_name'],
					self.table_desc['table_name'],
					self.table_desc['table_name']
					)
				)
			self.f.write(
				'\t\treturn {}_list\n\n'.format(
					self.table_desc['table_name']
					)
				)

	def write_adder_function(self):
		self.f.write(
			'\tdef {}(self, redis, {}):\n'.format(
				self.redis_accessor_name.get_list_adder_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		if self.table_desc['data_type'] == 'string':
			format_string = '\t\tself.redis_accessor.{}(redis, {})\n\n'
		elif self.table_desc['data_type'] == 'int':
			format_string = '\t\tself.redis_accessor.{}(redis, str({}))\n\n'
		self.f.write(
			format_string.format(
				self.redis_accessor_name.get_list_adder_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)

	def write_remover_function(self):
		self.f.write(
			'\tdef {}(self, redis, {}):\n'.format(
				self.redis_accessor_name.get_list_remover_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		if self.table_desc['data_type'] == 'string':
			format_string = '\t\tself.redis_accessor.{}(redis, {})\n\n'
		elif self.table_desc['data_type'] == 'int':
			format_string = '\t\tself.redis_accessor.{}(redis, str({}))\n\n'
		self.f.write(
			format_string.format(
				self.redis_accessor_name.get_list_remover_function_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)

"""
	def get_online_player_list(self, redis):
		#return self.redis_accessor.get_online_player_list(redis)
		string_list = self.redis_accessor.get_online_player_list(redis)
		online_player_list = [int(online_player_string) for online_player_string in string_list]
		return online_player_list

	def add_online_player(self, redis, online_player):
		#self.redis_accessor.add_online_player(redis, online_player)
		self.redis_accessor.add_online_player(redis, str(online_player))

	def remove_online_player(self, redis, online_player):
		#self.redis_accessor.remove_online_player(redis, online_player)
		self.redis_accessor.remove_online_player(redis, str(online_player))
"""