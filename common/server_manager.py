from common.server import Server
from common.server_status import ServerStatus

class ServerManager(object):
	def __init__(self):
		self.servers = {}
		
	def add_server(self, name, server_type, status=ServerStatus.SERVER_STATUS_RUNNING):
		server = Server(name, server_type, status)
		self.servers[server.get_name()] = server
		
	def remove_server(self, server_type, server_name):
		if self.servers.has_key(server_name):
			self.servers.pop(server_name)