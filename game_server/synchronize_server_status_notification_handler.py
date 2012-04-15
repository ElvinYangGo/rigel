import protocol.protocol_message_pb2
from common.server_type import ServerType
from common.server_status import ServerStatus
from common.server import Server

class SynchronizeServerStatusNotificationHandler:
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		message = protocol.protocol_message_pb2.SynchronizeServerNotification.FromString(channel_buffer.read_all_data())
		for server_net in message.servers:
			if server_net.status == ServerStatus.SERVER_STATUS_RUNNING:
				self.handle_running_server(global_data, server_net)
			elif server_net.status == ServerStatus.SERVER_STATUS_CLOSED:
				self.handle_closed_server(global_data, server_net)
				
	def handle_running_server(self, global_data, server_net):
		if server_net.type == ServerType.GATEWAY_SERVER:
			server = Server(server_net.name, server_net.type, server_net.status)
			global_data.server_manager.add_server(server)
	
	def handle_closed_server(self, global_data, server_net):
		if server_net.type == ServerType.GATEWAY_SERVER:
			global_data.server_manager.remove_server(server_net.name)
