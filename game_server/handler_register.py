from protocol.protocol_id import ProtocolID
from game_server.start_server_init_response_handler import StartServerInitResponseHandler
from game_server.synchronize_server_status_notification_handler import SynchronizeServerStatusNotificationHandler

class HandlerRegister:
	def __init__(self):
		pass

	def register(self, handler_dispatcher):
		handler_dispatcher.append_handler(
			ProtocolID.START_SERVER_INIT_RESPONSE,
			StartServerInitResponseHandler()
			)
		handler_dispatcher.append_handler(
			ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION,
			SynchronizeServerStatusNotificationHandler()
			)
	
		return handler_dispatcher
		