from protocol.protocol_id import ProtocolID
from game_server.start_server_init_response_handler import StartServerInitResponseHandler
from game_server.synchronize_server_status_notification_handler import SynchronizeServerStatusNotificationHandler

class HandlerRegister:
	def __init__(self, handler_dispatcher):
		self.handler_dispatcher = handler_dispatcher

	def register(self):
		self.handler_dispatcher.append_handler(
			ProtocolID.START_SERVER_INIT_RESPONSE,
			StartServerInitResponseHandler()
			)
		self.handler_dispatcher.append_handler(
			ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION,
			SynchronizeServerStatusNotificationHandler()
			)
	
		return self.handler_dispatcher
		