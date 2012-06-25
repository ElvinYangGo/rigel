from generator.table_method_name import TableMethodName

class SortedSetAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.table_method_name = TableMethodName()

	def write(self):
		self.f.write('\tdef get_{}(self, redis, id_string, member_string):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\treturn redis.zrank(self.redis_table.{}(id_string), member_string)\n\n'.format(
						self.table_method_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
