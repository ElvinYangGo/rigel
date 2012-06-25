class TableMethodName(object):
	def get_table_method_name(self, table_name):
		return 'get_{}_key'.format(table_name)
	
	def get_list_method_name(self, table_name):
		return 'get_{}_list_key'.format(table_name)
	
	def get_table_field_method_name(self, table_name, field_name):
		return 'get_{}_table_{}_field'.format(table_name, field_name)
	