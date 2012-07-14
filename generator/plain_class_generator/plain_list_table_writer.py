from generator.plain_class_generator.plain_class_writer import PlainClassWriter
from generator.plain_class_name import PlainClassName

class PlainListTableWriter(PlainClassWriter):
	def __init__(self, path, table_desc):
		super(PlainListTableWriter, self).__init__(path, table_desc)
		self.plain_class_name = PlainClassName()
		
	def get_file_name(self):
		return self.plain_class_name.get_list_file_name(self.table_desc['table_name'])
	
	def get_class_name(self):
		return self.plain_class_name.get_list_class_name(self.table_desc['table_name'])

	def write_init_function(self, f):
		f.write(
			'\tdef __init__(self, {}):\n'.format(
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name'])
				)
			)
		f.write(
			'\t\tself.{} = {}\n\n'.format(
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name']),
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name'])
				)
			)
		
	def write_class_body(self, f):
		f.write(
			'\tdef get_all_{}(self):\n'.format(
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name'])
				)
			)
		f.write(
			'\t\treturn self.{}\n\n'.format(
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name'])
				)
			)
		
		f.write(
			'\tdef add_{}(self, {}):\n'.format(
				self.table_desc['table_name'],
				self.table_desc['table_name']
				)
			)
		f.write(
			'\t\tself.{}.append({})\n\n'.format(
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name']),
				self.table_desc['table_name']
				)
			)
		self.write_to_net_function(f)
		self.write_to_net_string_function(f)

	def write_to_net_body(self, f):
		f.write(
			'\t\tproto = protocol.auto_data_pb2.{}()\n'.format(
				self.plain_class_name.get_list_class_name(self.table_desc['table_name'])
				)
			)
		f.write(
			'\t\tproto.{}.extend(self.{})\n'.format(
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name']),
				self.plain_class_name.get_list_member_variable_name(self.table_desc['table_name'])
				)
			)
		f.write('\t\treturn proto\n\n')

"""
class ItemManager(object):
	def __init__(self):
		self.items = []

	def get_all_items(self):
		return self.items
	
	def add_item(self, item):
		self.items.append(item)

	def to_net(self):
		proto = protocol.auto_data_pb2.ItemManager()
		proto.items.extend(self.items)
		return proto

"""