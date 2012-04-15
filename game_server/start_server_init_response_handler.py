from protocol.protocol_id import ProtocolID
import protocol.protocol_message_pb2

class StartServerInitResponseHandler:
	def __init__(self):
		pass
	
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		global_data.rmq.subscribe(u'server_status')
		message = protocol.protocol_message_pb2.EndServerInitNotification()
		message.name = global_data.server_name
		global_data.rmq.send_message_string(message, u'server_initialization', ProtocolID.END_SERVER_INIT_NOTIFICATION)
