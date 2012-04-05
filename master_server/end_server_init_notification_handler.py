from master_server.global_data import GlobalData
from master_server.server_manager import ServerManager
from master_server.server import Server
from common.server_status import ServerStatus
from network.channel_buffer import ChannelBuffer
from protocol.protocol_id import ProtocolID
import protocol.protocol_message_pb2

class EndServerInitNotificationHandler:
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		message = protocol.protocol_message_pb2.EndServerInitNotification.FromString(channel_buffer.read_all_data())
		
		server = global_data.server_manager.get_server(message.name)
		server.set_status(ServerStatus.SERVER_STATUS_RUNNING)

		message_string_to_send = global_data.server_manager.running_server_to_net()
		channel_buffer = ChannelBuffer()
		channel_buffer.append(message_string_to_send)
		global_data.rmq.send_channel_buffer(channel_buffer, 'server_status', ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION)