from protocol.protocol_id import ProtocolID
import protocol.protocol_message_pb2
from common.start_server_init_response_handler import StartServerInitResponseHandler

class GatewayStartServerInitResponseHandler(StartServerInitResponseHandler):
	def __init__(self):
		pass
	
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		message = protocol.protocol_message_pb2.StartServerInitResponse.FromString(channel_buffer.read_all_data())
		if message.HasField('config'):
			if self.has_config(message.config, u'server_option_config'):
				server_option_reader = self.get_server_option_reader(message.config)
				self.init_heart_beat(global_data, server_option_reader.get_server_option_config())
		
		global_data.rmq.subscribe(u'server_status')
		message = protocol.protocol_message_pb2.EndServerInitNotification()
		message.name = global_data.server_name
		global_data.rmq.send_message_string(message, u'server_initialization', ProtocolID.END_SERVER_INIT_NOTIFICATION)
