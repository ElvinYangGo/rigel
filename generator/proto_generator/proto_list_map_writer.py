from generator.proto_generator.proto_writer import ProtoWriter
from generator.proto_generator.proto_map_writer import ProtoMapWriter

class ProtoListMapWriter(ProtoWriter):
	def __init__(self, table_desc, f):
		super(ProtoListMapWriter, self).__init__(table_desc, f)
		self.proto_map_writer = ProtoMapWriter(table_desc, f)

	def write(self):
		self.proto_map_writer.write()
		super(ProtoListMapWriter, self).write()

	def get_class_name(self):
		return self.plain_class_name.get_list_class_name(self.table_desc['table_name'])

	def write_fields(self):
		self.f.write(
			'\trepeated {} {} = 1;\n'.format(
				self.plain_class_name.get_map_class_name(self.table_desc['table_name']),
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name'])
				)
			)

"""
message Friend
{
	optional string user_name = 1;
	optional int32 user_id = 2;
}

message FriendManager
{
	repeated Friend friends = 1;
}
"""