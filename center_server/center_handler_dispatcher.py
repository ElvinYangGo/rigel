from protocol.server_protocol_id import ServerProtocolID
from center_server.center_start_server_init_res_handler import CenterStartServerInitResHandler
from center_server.sync_server_status_notice_handler import SyncServerStatusNoticeHandler
from common.handler_register import HandlerRegister

class CenterHandlerRegister(HandlerRegister):
	def register(self, handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_START_SERVER_INIT_RES,
			CenterStartServerInitResHandler()
			)
		handler_dispatcher.append_handler(
			ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE,
			SyncServerStatusNoticeHandler()
			)
	
		return handler_dispatcher
		