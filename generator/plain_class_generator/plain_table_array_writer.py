from generator.plain_class_generator.plain_map_table_writer import PlainMapTableWriter
from generator.plain_class_generator.plain_list_table_writer import PlainListTableWriter
from generator.plain_class_generator.plain_list_map_table_writer import PlainListMapTableWriter

class PlainTableArrayWriter(object):
	def __init__(self, path, table_desc_array):
		self.path = path
		self.table_desc_array = table_desc_array

	def write(self):
		for table_desc in self.table_desc_array:
			if table_desc['table_type'] == 'map':
				plain_map_table_writer = PlainMapTableWriter(self.path, table_desc)
				plain_map_table_writer.write()
			elif table_desc['table_type'] == 'list':
				plain_list_table_writer = PlainListTableWriter(self.path, table_desc)
				plain_list_table_writer.write()
			elif table_desc['table_type'] == 'list_map':
				plain_list_map_table_writer = PlainListMapTableWriter(self.path, table_desc)
				plain_list_map_table_writer.write()
