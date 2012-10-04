from protocol.server_protocol_id import ServerProtocolID
import protocol.server_message_pb2
from common.start_server_init_res_handler import StartServerInitResHandler
from common.channel_name import ChannelName
from common.global_data import GlobalData

class GameStartServerInitResHandler(StartServerInitResHandler):
	@staticmethod
	def register_server_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_START_SERVER_INIT_RES,
			GameStartServerInitResHandler()
			)
	
	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.server_message_pb2.StartServerInitRes.FromString(
			channel_buffer.read_all_data()
			)
		if message.HasField('config'):
			if self.has_config(message.config, u'server_option_config'):
				server_option_reader = self.get_server_option_reader(message.config)
				self.init_heart_beat(server_option_reader.get_server_option_config())
		
		GlobalData.inst.rmq.subscribe(ChannelName.SERVER_STATUS)
		message = protocol.server_message_pb2.EndServerInitNotice()
		message.name = GlobalData.inst.server_name
		GlobalData.inst.rmq.send_message(
			message, ChannelName.SERVER_INIT, ServerProtocolID.P_END_SERVER_INIT_NOTICE
			)
