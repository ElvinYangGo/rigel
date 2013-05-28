from generator.protocol_id_generator.protocol_id_writer import ProtocolIDWriter

class CppProtocolIDWriter(ProtocolIDWriter):
	def __init__(self, desc_file_name, out_file_name, out_class_name, prefix, suffix, compile_macro):
		super(CppProtocolIDWriter, self).__init__(desc_file_name, out_file_name, out_class_name, prefix, suffix, '//')
		self.compile_macro = compile_macro

	def write_class_head(self, f):
		f.write('#ifndef {}\n'.format(self.compile_macro))
		f.write('#define {}\n\n'.format(self.compile_macro))
		f.write('class {}\n'.format(self.out_class_name))
		f.write('{\n')
		f.write('public:\n')

	def write_class_tail(self, f):
		f.write('};\n')
		f.write('#endif')
