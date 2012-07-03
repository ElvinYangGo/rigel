from generator.table_method_name import TableMethodName

class ListAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.table_method_name = TableMethodName()

	def write(self):
		self.write_getter_function()
		self.write_adder_function()
		self.write_remover_function()

	def write_getter_function(self):
		self.f.write('\tdef {}(self, redis, id_string):\n'.format(self.get_getter_function_name()))
		self.f.write('\t\treturn redis.lrange(self.redis_table.{}(id_string), 0, -1)\n\n'.format(
						self.table_method_name.get_list_method_name(self.table_desc['table_name']) 
						)
					)
		
	def get_getter_function_name(self):
		return 'get_{}_list'.format(self.table_desc['table_name'])
		
	def write_adder_function(self):
		self.f.write('\tdef {}(self, redis, id_string, {}_string):\n'.format(
						self.get_adder_function_name(), 
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\tredis.rpush(self.redis_table.{}(id_string), {}_string)\n\n'.format( 
						self.table_method_name.get_list_method_name(self.table_desc['table_name']), 
						self.table_desc['table_name']
						)
					)
	
	def get_adder_function_name(self):
		return 'add_{}'.format(self.table_desc['table_name'])
		
	def write_remover_function(self):
		self.f.write('\tdef {}(self, redis, id_string, {}_string):\n'.format(
						self.get_remover_function_name(), 
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\tredis.lrem(self.redis_table.{}(id_string), 0, {}_string)\n\n'.format( 
						self.table_method_name.get_list_method_name(self.table_desc['table_name']),
						self.table_desc['table_name']
						)
					)
		
	def get_remover_function_name(self):
		return 'remove_{}'.format(self.table_desc['table_name'])
	
"""
	def get_item_list(self, redis, id_string):
		return redis.lrange(self.redis_table.get_item_list_key(id_string), 0, -1)
	
	def add_item(self, redis, id_string, item_string):
		redis.rpush(self.redis_table.get_item_list_key(id_string), item_string)
	
	def remove_item(self, redis, id_string, item_string):
		redis.lrem(self.redis_table.get_item_list_key(id_string), 0, item_string)
"""		
	