import json
import protocol.server_message_pb2
from protocol.server_protocol_id import ServerProtocolID
from common.global_data import GlobalData

class StartServerInitReqHandler:
	@staticmethod
	def register_server_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_START_SERVER_INIT_REQ,
			StartServerInitReqHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.server_message_pb2.StartServerInitReq.FromString(
			channel_buffer.read_all_data()
			)

		GlobalData.inst.server_manager.add_server(message.name, message.type)
		print '%s, starting' % (message.name)
		
		message_to_send = protocol.server_message_pb2.StartServerInitRes()
		message_to_send.config = self.create_config_string()
		GlobalData.inst.rmq.send_message(
			message_to_send, message.name, ServerProtocolID.P_START_SERVER_INIT_RES
			)

	def create_config_string(self):
		config_string = {}
		config_string['server_option_config'] = GlobalData.inst.server_option_config.to_json_string()
		return json.dumps(config_string)