from protocol.protocol_id import ProtocolID
from auth_server.sync_server_status_notice_handler import SyncServerStatusNoticeHandler
from common.handler_register import HandlerRegister
from auth_server.auth_start_server_init_res_handler import AuthStartServerInitResHandler

class AuthHandlerRegister(HandlerRegister):
	def register(self, handler_dispatcher):
		handler_dispatcher.append_handler(
			ProtocolID.START_SERVER_INIT_RESPONSE,
			AuthStartServerInitResHandler()
			)
		handler_dispatcher.append_handler(
			ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION,
			SyncServerStatusNoticeHandler()
			)
	
		return handler_dispatcher
		