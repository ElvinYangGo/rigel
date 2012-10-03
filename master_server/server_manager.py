from master_server.server import Server
import protocol.server_message_pb2

class ServerManager:
	def __init__(self):
		self.servers = {}
		
	def add_server(self, server_name, type):
		server = Server(server_name, type)
		self.servers[server_name] = server
		
	def get_server(self, server_name):
		return self.servers.get(server_name)
	
	def running_server_to_net(self):
		server_message_list = [server.to_net() for server in self.servers.itervalues()]
		sync_server_notice_message = protocol.server_message_pb2.SyncServerNotice()
		sync_server_notice_message.servers.extend(server_message_list)
		return sync_server_notice_message
		
	def get_all_servers(self):
		return self.servers