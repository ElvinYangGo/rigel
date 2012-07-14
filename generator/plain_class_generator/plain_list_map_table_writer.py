from generator.plain_class_generator.plain_list_table_writer import PlainListTableWriter
from generator.plain_class_generator.plain_map_table_writer import PlainMapTableWriter

class PlainListMapTableWriter(PlainListTableWriter):
	def __init__(self, path, table_desc):
		super(PlainListMapTableWriter, self).__init__(path, table_desc)
		self.plain_map_table_writer = PlainMapTableWriter(path, table_desc)
		
	def write(self):
		self.plain_map_table_writer.write()
		super(PlainListMapTableWriter, self).write()

	def write_to_net_body(self, f):
		f.write(
			'\t\tproto_list = [{}.to_net() for {} in self.{}]\n'.format(
				self.table_desc['table_name'],
				self.table_desc['table_name'],
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name'])
				)
			)
		f.write(
			'\t\tproto = protocol.auto_data_pb2.{}()\n'.format(
				self.plain_class_name.get_list_class_name(self.table_desc['table_name'])
				)
			)
		f.write(
			'\t\tproto.{}.extend(proto_list)\n'.format(
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name'])
				)
			)
		f.write('\t\treturn proto\n\n')

"""
	def to_net(self):
		proto_list = [friend.to_net() for friend in self.friends]
		proto = protocol.auto_data_pb2.FriendManager()
		proto.friends.extend(proto_list)
		return proto

	def to_net_string(self):
		return self.to_net().SerializeToString()
"""