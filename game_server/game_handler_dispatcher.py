from protocol.server_protocol_id import ServerProtocolID
from game_server.game_start_server_init_res_handler import GameStartServerInitResHandler
from game_server.sync_server_status_notice_handler import SyncServerStatusNoticeHandler
from common.handler_register import HandlerRegister

class GameHandlerRegister(HandlerRegister):
	def register(self, handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_START_SERVER_INIT_RES,
			GameStartServerInitResHandler()
			)
		handler_dispatcher.append_handler(
			ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE,
			SyncServerStatusNoticeHandler()
			)
	
		return handler_dispatcher
		