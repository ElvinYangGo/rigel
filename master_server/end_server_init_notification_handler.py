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

		self.send_other_servers_to_this_server(global_data, message.name)
		self.send_this_server_to_other_servers(global_data, server)
		
	def send_other_servers_to_this_server(self, global_data, this_server_name):
		server_list_message = global_data.server_manager.running_server_to_net()
		global_data.rmq.send_message_string(server_list_message, this_server_name, ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION)

	def send_this_server_to_other_servers(self, global_data, this_server):
		this_server_message = protocol.protocol_message_pb2.SynchronizeServerNotification()
		this_server_message.servers.extend([this_server.to_net()])
		global_data.rmq.send_message_string(this_server_message, u'server_status', ProtocolID.SYNCHRONIZE_SERVER_STATUS_NOTIFICATION)
