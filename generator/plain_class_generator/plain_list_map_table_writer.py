from generator.plain_class_generator.plain_class_writer import PlainClassWriter
from generator.plain_class_generator.plain_list_table_writer import PlainListTableWriter
from generator.plain_class_generator.plain_map_table_writer import PlainMapTableWriter

class PlainListMapTableWriter(PlainClassWriter):
	def __init__(self, path, table_desc):
		PlainClassWriter.__init__(self, path, table_desc)
		self.plain_list_table_writer = PlainListTableWriter(path, table_desc)
		self.plain_map_table_writer = PlainMapTableWriter(path, table_desc)
		
	def write(self):
		self.plain_map_table_writer.write()
		self.plain_list_table_writer.write()
		