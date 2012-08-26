from master_server.server_manager import ServerManager
from master_server.server import Server
from common.server_status import ServerStatus
from network.channel_buffer import ChannelBuffer
from protocol.server_protocol_id import ServerProtocolID
import protocol.server_message_pb2
from common.channel_name import ChannelName
from common.global_data import GlobalData

class EndServerInitNoticeHandler:
	def handle_message(self, message_id, channel_buffer, **kwargs):
		message = protocol.server_message_pb2.EndServerInitNotice.FromString(
			channel_buffer.read_all_data()
			)
		
		server = GlobalData.instance.server_manager.get_server(message.name)
		server.set_status(ServerStatus.SERVER_STATUS_RUNNING)

		self.send_other_servers_to_this_server(message.name)
		self.send_this_server_to_other_servers(server)
		
	def send_other_servers_to_this_server(self, this_server_name):
		server_list_message = GlobalData.instance.server_manager.running_server_to_net()
		GlobalData.instance.rmq.send_message_string(
			server_list_message, this_server_name, ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE
			)

	def send_this_server_to_other_servers(self, this_server):
		this_server_message = protocol.server_message_pb2.SyncServerNotice()
		this_server_message.servers.extend([this_server.to_net()])
		GlobalData.instance.rmq.send_message_string(
			this_server_message, ChannelName.SERVER_STATUS, ServerProtocolID.P_SYNC_SERVER_STATUS_NOTICE
			)
