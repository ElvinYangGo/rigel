from protocol.protocol_pb2 import EndServerInitNotification
from master_server.global_data import GlobalData
from master_server.server_manager import ServerManager
from master_server.server import Server
from common.server_status import ServerStatus
from network.channel_buffer import ChannelBuffer
from protocol.protocol_id import ProtocolID

class EndServerInitNotificationHandler:
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		message = EndServerInitNotification.FromString(channel_buffer.read_all_data())
		
		server = global_data.server_manager.get_server(message.name)
		server.set_status(ServerStatus.SERVER_STATUS_RUNNING)

		message_string_to_send = global_data.server_manager.running_server_to_net()
		channel_buffer = ChannelBuffer()
		channel_buffer.append(message_string_to_send)
		global_data.rmq.send(channel_buffer, 'server_status', ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION)