import xml.dom.minidom
import protocol.protocol_message_pb2
from protocol.protocol_id import ProtocolID
from common.global_data import GlobalData

class StartServerInitRequestHandler:
	def __init__(self):
		pass
	
	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.protocol_message_pb2.StartServerInitRequest.FromString(channel_buffer.read_all_data())

		GlobalData.instance.server_manager.add_server(message.name, message.type)
		
		message_to_send = protocol.protocol_message_pb2.StartServerInitResponse()
		message_to_send.config = self.create_config_xml_string()
		GlobalData.instance.rmq.send_message_string(message_to_send, message.name, ProtocolID.START_SERVER_INIT_RESPONSE)

	def create_config_xml_string(self):
		doc = xml.dom.minidom.Document()
		config_element = doc.createElement('config')
		doc.appendChild(config_element)
		server_option_element = doc.createElement('server_option_config')
		config_element.appendChild(server_option_element)
		if GlobalData.instance.server_option_reader.get_root_element() is not None:
			server_option_element.appendChild(GlobalData.instance.server_option_reader.get_root_element())
		
		return doc.toxml('utf-8')
