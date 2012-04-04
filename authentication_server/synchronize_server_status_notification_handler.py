from network.channel_buffer import ChannelBuffer
from authentication_server.server import Server
import protocol.protocol_pb2

class SynchronizeServerStatusNotificationHandler:
	def handle_message(self, global_data, channel_name, message_id, channel_buffer):
		message = protocol.protocol_pb2.SynchronizeServerNotification.FromString(channel_buffer.read_all_data())
		for server_net in message.servers:
			#todo: check if it is myself's information
			server = Server(server_net.name, server_net.type, server_net.status)
			global_data.server_manager.add_server(server)
			
		
