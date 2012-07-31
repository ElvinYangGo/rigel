import json
from generator.protocol_id_generator.protocol_id_writer import ProtocolIDWriter

if __name__ == '__main__':
	f = open('protocol_id.json')
	protocol_id_list = json.load(f)

	writer = ProtocolIDWriter('../../protocol/protocol_id.py', protocol_id_list)
	writer.write()

	print 'finished'