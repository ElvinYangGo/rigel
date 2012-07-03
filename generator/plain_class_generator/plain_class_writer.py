class PlainClassWriter(object):
	def __init__(self, path, table_desc):
		self.path = path
		self.table_desc = table_desc

	def write(self):
		file_name_with_path = '{}{}.py'.format(self.path, self.get_file_name())
		with open(file_name_with_path, 'w') as f:
			self.write_class_head(f)
			self.write_init_function(f)
			self.write_class_body(f)
			f.flush()
		
	def write_class_head(self, f):
		f.write('#This file is generated by program. DO NOT EDIT IT MANUALLY!\n')
		f.write('class {}(object):\n'.format(self.get_class_name()))

	def write_init_function(self):
		pass
	
	def write_class_body(self, f):
		pass
	
	def get_file_name(self):
		return self.table_desc['table_name']
	
	def get_class_name(self):
		pass
	
