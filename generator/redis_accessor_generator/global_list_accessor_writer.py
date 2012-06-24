from generator.table_method_name import TableMethodName

class GlobalListAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.table_method_name = TableMethodName()

	def write(self):
		self.f.write('\tdef get_' + self.table_desc['table_name'] + '_list(self, redis):\n')
		self.f.write('\t\treturn redis.get(self.redis_table.' + self.table_method_name.get_list_method_name(self.table_desc['table_name']) + '())\n\n')
