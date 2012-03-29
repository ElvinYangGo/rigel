from master_server.server import Server
import protocol.protocol_pb2

class ServerManager:
	def __init__(self):
		self.servers = {}
		
	def add_server(self, server_name):
		server = Server(server_name)
		self.servers[server_name] = server
		
	def get_server(self, server_name):
		return self.servers.get(server_name)
	
	def running_server_to_net(self):
		server_message_list = []
		for server in self.servers.itervalues():
			server_message_list.append(server.to_net())
		synchronize_server_notification_message = protocol.protocol_pb2.SynchronizeServerNotification()
		synchronize_server_notification_message.servers.extend(server_message_list)
		return synchronize_server_notification_message.SerializeToString()
		