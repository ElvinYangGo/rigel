from generator.redis_accessor_generator.list_accessor_writer import ListAccessorWriter
from generator.redis_accessor_generator.map_accessor_writer import MapAccessorWriter

class ListMapAccessorWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f

	def write(self):
		list_accessor_writer = ListAccessorWriter(self.table_desc, self.f)
		list_accessor_writer.write()
		map_accessor_writer = MapAccessorWriter(self.table_desc, self.f)
		map_accessor_writer.write()
