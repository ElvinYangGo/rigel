import protocol
import time
from common.server_status import ServerStatus
from common.global_data import GlobalData
from protocol.server_protocol_id import ServerProtocolID

class HeartBeatNoticeHandler:
	@staticmethod
	def register_server_handler(handler_dispatcher):
		handler_dispatcher.append_handler(
			ServerProtocolID.P_HEART_BEAT_NOTICE,
			HeartBeatNoticeHandler()
			)

	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.server_message_pb2.HeartBeatNotice.FromString(channel_buffer.read_all_data())
		server = GlobalData.inst.server_manager.get_server(message.name)
		if server is not None:
			server.set_heart_beat_time(time.time())
			if server.closed():
				server.set_status(ServerStatus.SERVER_STATUS_RUNNING)
