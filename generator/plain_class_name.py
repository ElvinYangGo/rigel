class PlainClassName(object):
	def get_file_name(self, table_name):
		return table_name

	def get_list_file_name(self, table_name):
		return '{}_manager'.format(table_name)

	def get_map_class_name(self, table_name):
		word_list = table_name.split('_')
		capitalized_word_list = [word.capitalize() for word in word_list]
		class_name = ''.join(capitalized_word_list)
		return class_name

	def get_list_class_name(self, table_name):
		word_list = table_name.split('_')
		capitalized_word_list = [word.capitalize() for word in word_list]
		capitalized_word_list.append('Manager')
		class_name = ''.join(capitalized_word_list)
		return class_name

	def get_map_class_builder_function_name(self, table_name):
		return 'build_{}_from_{}_dict'.format(
			table_name,
			table_name
			)

	def get_map_dict_builder_function_name(self, table_name):
		return 'build_{}_dict_from_{}'.format(
			table_name,
			table_name
			)

	def get_map_field_getter_function_name(self, field_name):
		return 'get_{}'.format(field_name)

	def get_map_field_setter_function_name(self, field_name):
		return 'set_{}'.format(field_name)

	def get_list_member_variable_name(self, table_name):
		return '{}s'.format(table_name)
