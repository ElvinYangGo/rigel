from protocol.protocol_id import ProtocolID
from master_server.start_server_init_request_handler import StartServerInitRequestHandler
from master_server.end_server_init_notification_handler import EndServerInitNotificationHandler
from common.handler_register import HandlerRegister
from master_server.heart_beat_notification_handler import HeartBeatNotificationHandler

class MasterHandlerRegister(HandlerRegister):
	def register(self, handler_dispatcher):
		handler_dispatcher.append_handler(
			ProtocolID.START_SERVER_INIT_REQUEST, 
			StartServerInitRequestHandler()
			)
		handler_dispatcher.append_handler(
			ProtocolID.END_SERVER_INIT_NOTIFICATION, 
			EndServerInitNotificationHandler()
			)
		handler_dispatcher.append_handler(
			ProtocolID.HEART_BEAT_NOTIFICATION,
			HeartBeatNotificationHandler()
			)

		return handler_dispatcher
		