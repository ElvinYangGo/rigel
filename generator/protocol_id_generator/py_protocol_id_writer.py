from generator.protocol_id_generator.protocol_id_writer import ProtocolIDWriter

class PyProtocolIDWriter(ProtocolIDWriter):
	def __init__(self, desc_file_name, out_file_name, out_class_name, prefix, suffix):
		super(PyProtocolIDWriter, self).__init__(desc_file_name, out_file_name, out_class_name, prefix, suffix, '#')

	def write_class_head(self, f):
		f.write('class {}(object):\n'.format(self.out_class_name))
