from common.server_manager import ServerManager
from common.server_type import ServerType

class AuthenticationServerManager:
	def __init__(self):
		self.gateway_servers = []
		self.game_servers = []
		self.gateway_server_index = 0
		self.game_server_index = 0
		
	def add_server(self, server):
		if server.get_type() == ServerType.GATEWAY_SERVER:
			self.gateway_servers.append(server)
		elif server.get_type() == ServerType.GAME_SERVER:
			self.game_servers.append(server)
		
	def remove_server(self, server_name):
		self.game_servers = [server for server in self.game_servers if server.get_name() == server_name]
		self.gateway_servers = [server for server in self.gateway_servers if server.get_name() == server_name]
		
	def dispatch_gateway_server(self):
		index = self.gateway_server_index % len(self.gateway_servers)
		self.gateway_server_index += 1
		server = self.gateway_servers[index]
		return server

	def dispatch_game_server(self):
		index = self.game_server_index % len(self.game_servers)
		self.game_server_index += 1
		server = self.game_servers[index]
		return server