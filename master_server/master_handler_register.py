from protocol.server_protocol_id import ServerProtocolID
from master_server.start_server_init_req_handler import StartServerInitReqHandler
from master_server.end_server_init_notice_handler import EndServerInitNoticeHandler
from common.handler_register import HandlerRegister
from master_server.heart_beat_notice_handler import HeartBeatNoticeHandler

class MasterHandlerRegister(HandlerRegister):
	def register(self, handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_START_SERVER_INIT_REQ,
			StartServerInitReqHandler()
			)
		handler_dispatcher.append_handler(
			ServerProtocolID.P_END_SERVER_INIT_NOTICE,
			EndServerInitNoticeHandler()
			)
		handler_dispatcher.append_handler(
			ServerProtocolID.P_HEART_BEAT_NOTICE,
			HeartBeatNoticeHandler()
			)

		return handler_dispatcher
		