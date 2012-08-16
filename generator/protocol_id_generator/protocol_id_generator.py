from generator.protocol_id_generator.protocol_id_writer import ProtocolIDWriter

if __name__ == '__main__':
	client_protocol_id_writer = ProtocolIDWriter(
			'client_protocol_id.json',
			'../../protocol/client_protocol_id.py',
			'ClientProtocolID'
			)
	client_protocol_id_writer.write()

	server_protocol_id_writer = ProtocolIDWriter(
			'server_protocol_id.json',
			'../../protocol/server_protocol_id.py',
			'ServerProtocolID'
			)
	server_protocol_id_writer.write()

	print 'finished'