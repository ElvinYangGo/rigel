from authentication_server.server import Server

class ServerManager:
	def __init__(self):
		self.servers = {}
		
	def add_server(self, server):
		self.servers[server.get_name()] = server