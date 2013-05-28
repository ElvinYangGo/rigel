from generator.protocol_id_generator.py_protocol_id_writer import PyProtocolIDWriter
from generator.protocol_id_generator.cpp_protocol_id_writer import CppProtocolIDWriter

if __name__ == '__main__':
	py_client_protocol_id_writer = PyProtocolIDWriter(
			'client_protocol_id.json',
			'../../protocol/client_protocol_id.py',
			'ClientProtocolID',
			'',
			''
			)
	py_client_protocol_id_writer.write()
	cpp_client_protocol_id_writer = CppProtocolIDWriter(
			'client_protocol_id.json',
			'../../protocol/ClientProtocolId.h',
			'ClientProtocolId',
			'static const int ',
			';',
			'__CLIENT_PROTOCOL_ID_H__'
			)
	cpp_client_protocol_id_writer.write()

	server_protocol_id_writer = PyProtocolIDWriter(
			'server_protocol_id.json',
			'../../protocol/server_protocol_id.py',
			'ServerProtocolID',
			'',
			''
			)
	server_protocol_id_writer.write()

	print 'finished'