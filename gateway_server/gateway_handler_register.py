from protocol.server_protocol_id import ServerProtocolID
from common.handler_register import HandlerRegister
from gateway_server.gateway_start_server_init_res_handler import GatewayStartServerInitResHandler
from gateway_server.sync_server_status_notice_handler import SyncServerStatusNoticeHandler

class GatewayHandlerRegister(HandlerRegister):
	def register(self, handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_START_SERVER_INIT_RES,
			GatewayStartServerInitResHandler()
			)
		handler_dispatcher.append_handler(
			ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE,
			SyncServerStatusNoticeHandler()
			)
	
		return handler_dispatcher
		