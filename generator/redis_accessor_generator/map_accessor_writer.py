from generator.table_method_name import TableMethodName

class MapAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.table_method_name = TableMethodName()
		
	def write(self):
		self.write_table_getter_function()
		self.write_table_setter_function()
		
		for field_pair in self.table_desc['table_field'].iteritems():
			self.write_field_getter_function(field_pair)
			self.write_field_setter_function(field_pair)
			
	def get_key_param_string(self):
		return 'id_string'
	
	def write_table_getter_function(self):
		self.f.write('\tdef {}(self, redis, {}):\n'.format(
						self.get_table_getter_function_name(),
						self.get_key_param_string()
						)
					)
		self.f.write('\t\treturn redis.hgetall(self.redis_table.{}({}))\n\n'.format( 
						self.table_method_name.get_table_method_name(self.table_desc['table_name']),
						self.get_key_param_string() 
						)
					)
	
	def get_table_getter_function_name(self):
		return 'get_{}'.format(self.table_desc['table_name'])

	def write_table_setter_function(self):
		self.f.write('\tdef {}(self, redis, {}, d):\n'.format(
						self.get_table_setter_function_name(),
						self.get_key_param_string()
						)
					)
		self.f.write('\t\tredis.hmset(self.redis_table.{}({}), d)\n\n'.format( 
						self.table_method_name.get_table_method_name(self.table_desc['table_name']),
						self.get_key_param_string()
						)
					)
	
	def get_table_setter_function_name(self):
		return 'set_{}'.format(self.table_desc['table_name'])	
	
	def write_field_getter_function(self, field_pair):
		field_name = field_pair[0]
		self.f.write('\tdef {}(self, redis, {}):\n'.format(
						self.get_field_getter_function_name(field_name),
						self.get_key_param_string()
						)
					)
		self.f.write('\t\treturn redis.hget(\n')
		self.f.write('\t\t\tself.redis_table.{}({}),\n'.format( 
						self.table_method_name.get_table_method_name(self.table_desc['table_name']),
						self.get_key_param_string()
						)
					)
		self.f.write('\t\t\tself.redis_table.{}()\n'.format( 
						self.table_method_name.get_table_field_method_name(self.table_desc['table_name'], field_name) 
						)
					)
		self.f.write('\t\t\t)\n\n')	
		
	def get_field_getter_function_name(self, field_name):
		return 'get_{}_table_{}'.format(self.table_desc['table_name'], field_name)
		
	def write_field_setter_function(self, field_pair):
		field_name = field_pair[0]
		self.f.write('\tdef {}(self, redis, {}, {}_string):\n'.format(
						self.get_field_setter_function_name(field_name), 
						self.get_key_param_string(),
						field_name
						)
					)
		self.f.write('\t\tredis.hset(\n')
		self.f.write('\t\t\tself.redis_table.{}({}),\n'.format(
						self.table_method_name.get_table_method_name(self.table_desc['table_name']),
						self.get_key_param_string()
						)
					)
		self.f.write('\t\t\tself.redis_table.{}(),\n'.format(
						self.table_method_name.get_table_field_method_name(self.table_desc['table_name'], field_name) 
						)
					)
		self.f.write('\t\t\t{}_string\n'.format(field_name))
		self.f.write('\t\t\t)\n\n')	
	
	def get_field_setter_function_name(self, field_name):
		return 'set_{}_table_{}'.format(self.table_desc['table_name'], field_name)
		
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