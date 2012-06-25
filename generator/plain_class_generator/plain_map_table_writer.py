from generator.plain_class_generator.plain_class_writer import PlainClassWriter

class PlainMapTableWriter(PlainClassWriter):
	def __init__(self, path, table_desc):
		PlainClassWriter.__init__(self, path, table_desc)
		
	def get_class_name(self):
		word_list = self.table_desc['table_name'].split('_')
		capitalized_word_list = [word.capitalize() for word in word_list]
		table_name = ''.join(capitalized_word_list)
		return table_name

	def write_init_function(self, f):
		self.write_init_function_head(f)
		self.write_init_function_body(f)
		f.write('\n')
	
	def write_init_function_head(self, f):
		f.write('\tdef __init__(self{}):\n'.format(self.get_init_parameter()))
		
	def write_init_function_body(self, f):
		for field_name in self.table_desc['table_field'].iterkeys():
			f.write('\t\tself.{} = \n'.format(
						field_name, 
						field_name
						)
					)

	def get_init_parameter(self):
		parameter_string = ''
		for field_name in self.table_desc['table_field'].iterkeys():
			parameter_string = parameter_string + ', ' + field_name
		return parameter_string
	
	def write_class_body(self, f):
		for field_name in self.table_desc['table_field'].iterkeys():
			self.write_get_function(f, field_name)
			self.write_set_function(f, field_name)
	
	def write_get_function(self, f, field_name):
		f.write('\tdef get_{}(self):\n'.format(field_name))
		f.write('\t\treturn self.{}\n\n'.format(field_name))
	
	def write_set_function(self, f, field_name):
		f.write('\tdef set_{}(self, {}):\n'.format(field_name, field_name))
		f.write('\t\tself.{} = {}\n\n'.format(field_name, field_name))
		
"""
class User(object):
	def __init__(self, user_id, user_name):
		self.user_id = user_id
		self.user_name = user_name

	def get_user_id(self):
		return self.user_id
	
	def set_user_id(self, user_id):
		self.user_id = user_id
		
	def get_user_name(self):
		return self.user_name
	
	def set_user_name(self, user_name):
		self.user_name = user_name
"""	
