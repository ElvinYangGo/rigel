from generator.table_method_name import TableMethodName

class MapAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.table_method_name = TableMethodName()
		
	def write(self):
		self.write_table_getter_function()
		self.write_table_setter_function()
		
		for field in self.table_desc['table_field'].keys():
			self.write_field_getter_function(field)
			self.write_field_setter_function(field)
	
	def write_table_getter_function(self):
		self.f.write('\tdef get_{}(self, redis, id_string):\n'.format(
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\treturn redis.hgetall(self.redis_table.{}(id_string))\n\n'.format( 
						self.table_method_name.get_table_method_name(self.table_desc['table_name']) 
						)
					)

	def write_table_setter_function(self):
		self.f.write('\tdef set_{}(self, redis, id_string, {}_dict):\n'.format(
						self.table_desc['table_name'], 
						self.table_desc['table_name']
						)
					)
		self.f.write('\t\treturn redis.hmset(self.redis_table.{}(id_string), {}_dict)\n\n'.format( 
						self.table_method_name.get_table_method_name(self.table_desc['table_name']), 
						self.table_desc['table_name']
						)
					)
		
	def write_field_getter_function(self, field):
		self.f.write('\tdef get_{}_table_{}(self, redis, id_string):\n'.format(
						self.table_desc['table_name'],
						field
						)
					)
		self.f.write('\t\treturn redis.hget(\n')
		self.f.write('\t\t\tself.redis_table.{}(id_string),\n'.format( 
						self.table_method_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
		self.f.write('\t\t\tself.redis_table.{}()\n'.format( 
						self.table_method_name.get_table_field_method_name(self.table_desc['table_name'], field) 
						)
					)
		self.f.write('\t\t\t)\n\n')	
		
	def write_field_setter_function(self, field):
		self.f.write('\tdef set_{}_table_{}(self, redis, id_string, {}_string):\n'.format(
						self.table_desc['table_name'], 
						field,
						field
						)
					)
		self.f.write('\t\tredis.hset(\n')
		self.f.write('\t\t\tself.redis_table.{}(id_string),\n'.format(
						self.table_method_name.get_table_method_name(self.table_desc['table_name'])
						)
					)
		self.f.write('\t\t\tself.redis_table.{}(),\n'.format(
						self.table_method_name.get_table_field_method_name(self.table_desc['table_name'], field) 
						)
					)
		self.f.write('\t\t\t{}_string\n'.format(field))
		self.f.write('\t\t\t)\n\n')	
		
"""		
	def get_user(self, redis, id_string):
		return redis.hgetall(self.redis_table.get_user_key(id_string))
		
	def set_user(self, redis, id_string, user_dict):
		redis.hmset(self.redis_table.get_user_key(id_string), user_dict)
		
	def get_user_table_user_id(self, redis, id_string):
		return redis.hget(
			self.redis_table.get_user_key(id_string), 
			self.redis_table.get_user_table_user_id_field()
			)
		
	def get_user_table_user_name(self, redis, id_string):
		return redis.hget(
			self.redis_table.get_user_key(id_string), 
			self.redis_table.get_user_table_user_name_field()
			)
	
	def set_user_table_user_name(self, redis, id_string, user_name_string):
		redis.hset(
			self.redis_table.get_user_key(id_string), 
			self.redis_table.get_user_table_user_name_field()
			user_name_string
			)
"""		