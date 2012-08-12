import protocol
import time
from common.server_status import ServerStatus
from common.global_data import GlobalData

class HeartBeatNotificationHandler:
	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.protocol_message_pb2.HeartBeatNotification.FromString(channel_buffer.read_all_data())
		server = GlobalData.instance.server_manager.get_server(message.name)
		if server is not None:
			server.set_heart_beat_time(time.time())
			if server.closed():
				server.set_status(ServerStatus.SERVER_STATUS_RUNNING)
