class TableMethodName(object):
	def get_table_method_name(self, table_name):
		return 'get_' + table_name + '_key'
	
	def get_list_method_name(self, table_name):
		return 'get_' + table_name + '_list_key'
	
	def get_table_field_method_name(self, table_name, field_name):
		return 'get_' + table_name + '_table_' + field_name + '_field'
	