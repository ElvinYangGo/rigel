from generator.proto_generator.proto_writer import ProtoWriter

class ProtoMapWriter(ProtoWriter):
	def __init__(self, table_desc, f):
		super(ProtoMapWriter, self).__init__(table_desc, f)

	def get_class_name(self):
		return self.plain_class_name.get_map_class_name(self.table_desc['table_name'])

	def write_fields(self):
		index = 1
		for field in self.table_desc['table_field']:
			self.write_field(field, index)
			index += 1

	def write_field(self, field, index):
		if field['data_type'] == 'int':
			format_string = '\toptional int32 {} = {};\n'
		elif field['data_type'] == 'string':
			format_string = '\toptional string {} = {};\n'
		self.f.write(format_string.format(field['field_name'], index))

"""
message User
{
	optional int32 user_id = 1;
	optional string user_name = 2;
}
"""