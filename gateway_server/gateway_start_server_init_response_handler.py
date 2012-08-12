from protocol.protocol_id import ProtocolID
import protocol.protocol_message_pb2
from common.start_server_init_response_handler import StartServerInitResponseHandler
from common.global_data import GlobalData

class GatewayStartServerInitResponseHandler(StartServerInitResponseHandler):
	def __init__(self):
		pass
	
	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.protocol_message_pb2.StartServerInitResponse.FromString(channel_buffer.read_all_data())
		if message.HasField('config'):
			if self.has_config(message.config, u'server_option_config'):
				server_option_reader = self.get_server_option_reader(message.config)
				self.init_heart_beat(server_option_reader.get_server_option_config())
		
		GlobalData.instance.rmq.subscribe(u'server_status')
		message = protocol.protocol_message_pb2.EndServerInitNotification()
		message.name = GlobalData.instance.server_name
		GlobalData.instance.rmq.send_message_string(message, u'server_initialization', ProtocolID.END_SERVER_INIT_NOTIFICATION)
