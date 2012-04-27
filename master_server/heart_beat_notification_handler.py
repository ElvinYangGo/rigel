import protocol
import time
from common.server_status import ServerStatus

class HeartBeatNotificationHandler:
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		message = protocol.protocol_message_pb2.HeartBeatNotification.FromString(channel_buffer.read_all_data())
		server = global_data.server_manager.get_server(message.name)
		if server is not None:
			server.set_heart_beat_time(time.time())
			if server.closed():
				server.set_status(ServerStatus.SERVER_STATUS_RUNNING)
