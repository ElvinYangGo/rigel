from generator.plain_class_name import PlainClassName

class ProtoWriter(object):
	def __init__(self, table_desc, f):
		self.table_desc = table_desc
		self.f = f
		self.plain_class_name = PlainClassName()

	def write(self):
		self.f.write('message {}\n'.format(self.get_class_name()))
		self.f.write('{\n')
		self.write_fields()
		self.f.write('}\n\n')

	def get_class_name(self):
		pass

	def write_fields(self):
		pass
