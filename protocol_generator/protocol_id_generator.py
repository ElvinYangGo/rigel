from protocol_generator.protocol_id_parser import ProtocolIDParser
from protocol_generator.protocol_id_writer import ProtocolIDWriter

if __name__ == '__main__':
	parser = ProtocolIDParser('protocol_id.xml')
	parser.parse()
	
	writer = ProtocolIDWriter('../protocol/protocol_id.py', parser.get_id_list())
	writer.write()

	print 'finished'