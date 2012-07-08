from generator.plain_class_accessor_generator.plain_map_accessor_writer import PlainMapAccessorWriter

class PlainListMapMapAccessorWriter(PlainMapAccessorWriter):
	def __init__(self, table_desc, f):
		super(PlainListMapMapAccessorWriter, self).__init__(table_desc, f)
		
	def get_key_declaration_string(self):
		return 'id_int, {}_int'.format(self.table_desc['table_name'])
	
	def get_key_param_string(self):
		return 'str(id_int), str({}_int)'.format(self.table_desc['table_name'])
