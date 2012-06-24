from generator.plain_class_generator.plain_class_writer import PlainClassWriter

class PlainListTableWriter(PlainClassWriter):
	def __init__(self, path, table_desc):
		PlainClassWriter.__init__(self, path, table_desc)
		
	def get_file_name(self):
		return self.path + self.table_desc['table_name'] + '_manager'+ '.py'
	
	def get_class_name(self):
		word_list = self.table_desc['table_name'].split('_')
		capitalized_word_list = [word.capitalize() for word in word_list]
		capitalized_word_list.append('Manager')
		table_name = ''.join(capitalized_word_list)
		return table_name
	
	def write_init_function(self, f):
		f.write('\tdef __init__(self):\n')
		f.write('\t\tself.' + self.get_member_variable_name() + ' = []\n\n')
		
	def get_member_variable_name(self):
		return self.table_desc['table_name'] + 's'
		
	def write_class_body(self, f):
		f.write('\tdef get_all_' + self.get_member_variable_name() + '(self):\n')
		f.write('\t\treturn self.' + self.get_member_variable_name() + '\n\n')
		
		f.write('\tdef add_' + self.table_desc['table_name'] + '(self, ' + self.table_desc['table_name'] + '):\n')
		f.write('\t\tself.' + self.get_member_variable_name() + '.add(' + self.table_desc['table_name'] + ')\n')
		
"""
class ItemManager(object):
	def __init__(self):
		self.items = []

	def get_all_items(self):
		return self.items
	
	def add_item(self, item):
		self.items.add(item)
"""	
