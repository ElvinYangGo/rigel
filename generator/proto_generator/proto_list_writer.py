from generator.proto_generator.proto_writer import ProtoWriter

class ProtoListWriter(ProtoWriter):
	def __init__(self, table_desc, f):
		super(ProtoListWriter, self).__init__(table_desc, f)

	def get_class_name(self):
		return self.plain_class_name.get_list_class_name(self.table_desc['table_name'])

	def write_fields(self):
		self.f.write(
			'\trepeated int32 {} = 1;\n'.format(
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name'])
				)
			)

"""
message ItemManager
{
	repeated int32 items = 1;
}
"""