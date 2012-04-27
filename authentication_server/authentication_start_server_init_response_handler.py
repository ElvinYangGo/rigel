from protocol.protocol_id import ProtocolID
import protocol.protocol_message_pb2
from common.start_server_init_response_handler import StartServerInitResponseHandler
from common.channel_name import ChannelName
from common.server_option_reader import ServerOptionReader

class AuthenticationStartServerInitResponseHandler(StartServerInitResponseHandler):
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		message = protocol.protocol_message_pb2.StartServerInitResponse.FromString(channel_buffer.read_all_data())
		if message.HasField('config'):
			if self.has_config(message.config, u'server_option_config'):
				server_option_string = self.get_config_string(message.config, u'server_option_config')
				server_option_reader = ServerOptionReader(string_content=server_option_string)
				server_option_reader.parse()
				self.init_heart_beat(global_data, server_option_reader.get_server_option_config())
		
		global_data.rmq.subscribe(ChannelName.SERVER_STATUS)
		message_to_send = protocol.protocol_message_pb2.EndServerInitNotification()
		message_to_send.name = global_data.server_name
		global_data.rmq.send_message_string(message_to_send, ChannelName.SERVER_INITIALIZATION, ProtocolID.END_SERVER_INIT_NOTIFICATION)
