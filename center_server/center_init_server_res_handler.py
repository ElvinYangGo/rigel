from protocol.server_protocol_id import ServerProtocolID
from common.init_server_res_handler import InitServerResHandler

class CenterInitServerResHandler(InitServerResHandler):
	@staticmethod
	def register_server_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_INIT_SERVER_RES,
			CenterInitServerResHandler()
			)