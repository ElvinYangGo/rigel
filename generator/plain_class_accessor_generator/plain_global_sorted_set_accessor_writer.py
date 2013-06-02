from generator.redis_accessor_name import RedisAccessorName

class PlainGlobalSortedSetAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.redis_accessor_name = RedisAccessorName()

	def write(self):
		self.write_getter_function()
		self.write_adder_function()
		self.write_remover_function()
		self.write_range_getter_function()

	def write_getter_function(self):
		self.f.write(
			'\tdef {}(self, redis, member):\n'.format(
				self.redis_accessor_name.get_global_sorted_set_getter_function_name(self.table_desc['table_name'])
				)
			)
		if self.table_desc['data_type'] == 'string':
			format_string = '\t\treturn self.redis_accessor.{}(redis, member)\n\n'
		elif self.table_desc['data_type'] == 'int':
			format_string = '\t\treturn self.redis_accessor.{}(redis, str(member))\n\n'
		self.f.write(
			format_string.format(
				self.redis_accessor_name.get_global_sorted_set_getter_function_name(self.table_desc['table_name'])
				)
			)

	def write_adder_function(self):
		self.f.write(
			'\tdef {}(self, redis, member, score):\n'.format(
				self.redis_accessor_name.get_global_sorted_set_adder_function_name(self.table_desc['table_name'])
				)
			)
		if self.table_desc['data_type'] == 'string':
			format_string = '\t\tself.redis_accessor.{}(redis, member, score)\n\n'
		elif self.table_desc['data_type'] == 'int':
			format_string = '\t\tself.redis_accessor.{}(redis, str(member), score)\n\n'
		self.f.write(
			format_string.format(
				self.redis_accessor_name.get_global_sorted_set_adder_function_name(self.table_desc['table_name'])
				)
			)

	def write_remover_function(self):
		self.f.write(
			'\tdef {}(self, redis, member):\n'.format(
				self.redis_accessor_name.get_global_sorted_set_remover_function_name(self.table_desc['table_name'])
				)
			)
		if self.table_desc['data_type'] == 'string':
			format_string = '\t\tself.redis_accessor.{}(redis, member)\n\n'
		elif self.table_desc['data_type'] == 'int':
			format_string = '\t\tself.redis_accessor.{}(redis, str(member))\n\n'
		self.f.write(
			format_string.format(
				self.redis_accessor_name.get_global_sorted_set_adder_function_name(self.table_desc['table_name'])
				)
			)

	def	write_range_getter_function(self):
		self.f.write(
			'\tdef {}(self, redis, start, stop):\n'.format(
				self.redis_accessor_name.get_global_sorted_set_range_getter_function_name(self.table_desc['table_name'])
				)
			)
		if self.table_desc['data_type'] == 'string':
			self.f.write(
				'\t\treturn self.redis_accessor.{}(redis, start, stop)\n\n'.format(
					self.redis_accessor_name.get_global_sorted_set_range_getter_function_name(self.table_desc['table_name'])
					)
				)
		elif self.table_desc['data_type'] == 'int':
			self.f.write(
				'\t\tstring_list = self.redis_accessor.{}(redis, start, stop)\n'.format(
					self.redis_accessor_name.get_global_sorted_set_range_getter_function_name(self.table_desc['table_name'])
					)
				)
			self.f.write('\t\tmember_list = [int(member_string) for member_string in string_list]\n')
			self.f.write('\t\treturn member_list\n\n')
"""
	def get_level_rank(self, redis, member):
		#return self.redis_accessor.get_level_rank(redis, member)
		return self.redis_accessor.get_level_rank(redis, str(member))

	def add_level_rank(self, redis, member, score):
		#self.redis_accessor.add_level_rank(redis, member, score)
		self.redis_accessor.add_level_rank(redis, str(member), score)

	def remove_level_rank(self, redis, member):
		#self.redis_accessor.remove_level_rank(redis, member)
		self.redis_accessor.remove_level_rank(redis, str(member))

	def get_level_rank_range(self, redis, start, stop):
		#return self.redis_accessor.get_level_rank_range(redis, start, stop)
		string_list = self.redis_accessor.get_level_rank_range(redis, start, stop)
		member_list = [int(member_string) for member_string in string_list]
		return member_list
"""