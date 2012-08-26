from protocol.server_protocol_id import ServerProtocolID
import protocol.protocol_message_pb2
from common.start_server_init_res_handler import StartServerInitResHandler
from common.global_data import GlobalData

class GatewayStartServerInitResHandler(StartServerInitResHandler):
	def __init__(self):
		pass
	
	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.protocol_message_pb2.StartServerInitRes.FromString(
			channel_buffer.read_all_data()
			)
		if message.HasField('config'):
			if self.has_config(message.config, u'server_option_config'):
				server_option_reader = self.get_server_option_reader(message.config)
				self.init_heart_beat(server_option_reader.get_server_option_config())
		
		GlobalData.instance.rmq.subscribe(u'server_status')
		message = protocol.protocol_message_pb2.EndServerInitNotice()
		message.name = GlobalData.instance.server_name
		GlobalData.instance.rmq.send_message_string(
			message, u'server_initialization', ServerProtocolID.P_END_SERVER_INIT_NOTICE
			)
