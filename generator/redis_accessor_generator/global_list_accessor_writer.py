from generator.table_method_name import TableMethodName

class GlobalListAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.table_method_name = TableMethodName()

	def write(self):
		self.f.write('\tdef get_{}_list(self, redis):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\treturn redis.get(self.redis_table.{}())\n\n'.format(
						self.table_method_name.get_list_method_name(self.table_desc['table_name'])
						)
					)
