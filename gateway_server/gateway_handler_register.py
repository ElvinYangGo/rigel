from protocol.protocol_id import ProtocolID
from gateway_server.synchronize_server_status_notification_handler import SynchronizeServerStatusNotificationHandler
from common.handler_register import HandlerRegister
from game_server.game_start_server_init_response_handler import GameStartServerInitResponseHandler

class GatewayHandlerRegister(HandlerRegister):
	def register(self, handler_dispatcher):
		handler_dispatcher.append_handler(
			ProtocolID.START_SERVER_INIT_RESPONSE,
			GameStartServerInitResponseHandler()
			)
		handler_dispatcher.append_handler(
			ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION,
			SyncServerStatusNoticeHandler()
			)
	
		return handler_dispatcher
		