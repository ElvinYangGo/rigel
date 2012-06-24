from generator.table_method_name import TableMethodName

class MapAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.table_method_name = TableMethodName()
		
	def write(self):
		self.f.write('\tdef get_' + self.table_desc['table_name'] + '(self, redis, id_string):\n')
		self.f.write('\t\treturn redis.hgetall(self.redis_table.' + self.table_method_name.get_table_method_name(self.table_desc['table_name']) + '(id_string))\n\n')
		
		for field in self.table_desc['table_field'].keys():
			self.f.write('\tdef get_' + self.table_desc['table_name'] + '_table_' + field + '(self, redis, id_string):\n')
			self.f.write('\t\treturn redis.hget(\n')
			self.f.write('\t\t\tself.redis_table.' + self.table_method_name.get_table_method_name(self.table_desc['table_name']) + '(id_string),\n')
			self.f.write('\t\t\tself.redis_table.' + self.table_method_name.get_table_field_method_name(self.table_desc['table_name'], field) + '()\n')
			self.f.write('\t\t\t)\n\n')
	