from generator.plain_class_generator.plain_class_writer import PlainClassWriter
from generator.plain_class_name import PlainClassName

class PlainMapTableWriter(PlainClassWriter):
	def __init__(self, path, table_desc):
		super(PlainMapTableWriter, self).__init__(path, table_desc)
		self.plain_class_name = PlainClassName()
		
	def get_class_name(self):
		return self.plain_class_name.get_map_class_name(self.table_desc['table_name'])

	def write_init_function(self, f):
		self.write_init_function_head(f)
		self.write_init_function_body(f)
		f.write('\n')
	
	def write_init_function_head(self, f):
		f.write('\tdef __init__(self, {}):\n'.format(self.get_init_parameter()))
		
	def write_init_function_body(self, f):
		for field in self.table_desc['table_field']:
			f.write('\t\tself.{} = {}\n'.format(
						field['field_name'],
						field['field_name']
						)
					)

	def get_init_parameter(self):
		field_name_list = [field['field_name'] for field in self.table_desc['table_field']]
		parameter_string = ', '.join(field_name_list)
		return parameter_string
	
	def write_class_body(self, f):
		for field in self.table_desc['table_field']:
			self.write_getter_function(f, field['field_name'])
			self.write_setter_function(f, field['field_name'])
		self.write_to_net_function(f)
		self.write_to_net_string_function(f)
	
	def write_getter_function(self, f, field_name):
		f.write(
			'\tdef {}(self):\n'.format(
				self.plain_class_name.get_map_field_getter_function_name(field_name)
				)
			)
		f.write('\t\treturn self.{}\n\n'.format(field_name))

	def write_setter_function(self, f, field_name):
		f.write(
			'\tdef {}(self, {}):\n'.format(
				self.plain_class_name.get_map_field_setter_function_name(field_name),
				field_name
				)
			)
		f.write('\t\tself.{} = {}\n\n'.format(field_name, field_name))

	def write_to_net_body(self, f):
		f.write(
			'\t\tproto = protocol.auto_data_pb2.{}()\n'.format(
				self.get_class_name()
				)
			)
		for field in self.table_desc['table_field']:
			f.write(
				'\t\tproto.{} = self.{}\n'.format(
					field['field_name'],
					field['field_name']
					)
				)
		f.write('\t\treturn proto\n\n')

"""
class User(object):
	def __init__(self, user_id, user_name):
		self.user_id = user_id
		self.user_name = user_name

	def get_user_id(self):
		return self.user_id
	
	def set_user_id(self, user_id):
		self.user_id = user_id
		
	def get_user_name(self):
		return self.user_name
	
	def set_user_name(self, user_name):
		self.user_name = user_name

	def to_net(self):
		proto = protocol.auto_data_pb2.User()
		proto.user_id = self.user_id
		proto.user_name = self.user_name
		return proto

	def to_net_string(self):
		return self.to_net().SerializeToString()
"""	
