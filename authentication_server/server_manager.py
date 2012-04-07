from authentication_server.server import Server

class ServerManager:
	def __init__(self):
		self.servers = {}
		
	def add_server(self, server):
		self.servers[server.get_name()] = server
		
	def remove_server(self, server_name):
		self.servers.pop(server_name)