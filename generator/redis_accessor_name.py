class RedisAccessorName(object):
	def get_map_getter_function_name(self, table_name):
		return 'get_{}'.format(table_name)

	def get_map_setter_function_name(self, table_name):
		return 'set_{}'.format(table_name)

	def get_map_pexpire_function_name(self, table_name):
		return 'pexpire_{}'.format(table_name)

	def get_map_field_getter_function_name(self, table_name, field_name):
		return 'get_{}_table_{}'.format(table_name, field_name)

	def get_map_field_setter_function_name(self, table_name, field_name):
		return 'set_{}_table_{}'.format(table_name, field_name)

	def get_list_getter_function_name(self, table_name):
		return 'get_{}_list'.format(table_name)

	def get_list_adder_function_name(self, table_name):
		return 'add_{}'.format(table_name)

	def get_list_remover_function_name(self, table_name):
		return 'remove_{}'.format(table_name)

	def get_dict_list_getter_function_name(self, table_name):
		return 'get_{}_dict_list'.format(table_name)

	def get_global_sorted_set_getter_function_name(self, table_name):
		return 'get_{}'.format(table_name)

	def get_global_sorted_set_adder_function_name(self, table_name):
		return 'add_{}'.format(table_name)

	def get_global_sorted_set_remover_function_name(self, table_name):
		return 'remove_{}'.format(table_name)

	def get_global_sorted_set_range_getter_function_name(self, table_name):
		return 'get_{}_range'.format(table_name)

	def get_sorted_set_getter_function_name(self, table_name):
		return 'get_{}'.format(table_name)

	def get_sorted_set_adder_function_name(self, table_name):
		return 'add_{}'.format(table_name)

	def get_sorted_set_remover_function_name(self, table_name):
		return 'remove_{}'.format(table_name)

	def get_sorted_set_range_getter_function_name(self, table_name):
		return 'get_{}_range'.format(table_name)
