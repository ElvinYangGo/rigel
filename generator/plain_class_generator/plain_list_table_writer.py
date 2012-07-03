from generator.plain_class_generator.plain_class_writer import PlainClassWriter

class PlainListTableWriter(PlainClassWriter):
	def __init__(self, path, table_desc):
		PlainClassWriter.__init__(self, path, table_desc)
		
	def get_file_name(self):
		return '{}_manager'.format(self.table_desc['table_name'])
	
	def get_class_name(self):
		word_list = self.table_desc['table_name'].split('_')
		capitalized_word_list = [word.capitalize() for word in word_list]
		capitalized_word_list.append('Manager')
		table_name = ''.join(capitalized_word_list)
		return table_name
	
	def write_init_function(self, f):
		f.write('\tdef __init__(self, {}):\n'.format(self.get_member_variable_name()))
		f.write('\t\tself.{} = {}\n\n'.format(
				self.get_member_variable_name(),
				self.get_member_variable_name()
				)
			)
		
	def get_member_variable_name(self):
		return '{}s'.format(self.table_desc['table_name'])
		
	def write_class_body(self, f):
		f.write('\tdef get_all_{}(self):\n'.format(self.get_member_variable_name()))
		f.write('\t\treturn self.{}\n\n'.format(self.get_member_variable_name()))
		
		f.write('\tdef add_{}(self, {}):\n'.format(
					self.table_desc['table_name'],
					self.table_desc['table_name']
					)
				)
		f.write('\t\tself.{}.append({})\n'.format(
					self.get_member_variable_name(), 
					self.table_desc['table_name']
					)
				)
		
"""
class ItemManager(object):
	def __init__(self):
		self.items = []

	def get_all_items(self):
		return self.items
	
	def add_item(self, item):
		self.items.append(item)
"""	
