from protocol.server_protocol_id import ServerProtocolID
from common.start_server_init_res_handler import StartServerInitResHandler

class AuthStartServerInitResHandler(StartServerInitResHandler):
	@staticmethod
	def register_server_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_START_SERVER_INIT_RES,
			AuthStartServerInitResHandler()
			)