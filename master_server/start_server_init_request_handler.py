import protocol.protocol_message_pb2
from protocol.protocol_id import ProtocolID

class StartServerInitRequestHandler:
	def __init__(self):
		pass
	
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		message = protocol.protocol_message_pb2.StartServerInitRequest.FromString(channel_buffer.read_all_data())

		global_data.server_manager.add_server(message.name, message.type)
		
		message_to_send = protocol.protocol_message_pb2.StartServerInitResponse()
		global_data.rmq.send_message_string(message_to_send, message.name, ProtocolID.START_SERVER_INIT_RESPONSE)

