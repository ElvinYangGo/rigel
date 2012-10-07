from common.server import Server
from common.server_status import ServerStatus

class ServerDispatcher(object):
	def __init__(self, server_type):
		self.server_type = server_type
		self.servers = []
		self.server_index = 0

	def contain_server(self, name):
		for server in self.servers:
			if server.get_name() == name:
				return True
		return False

	def add_server(self, name, server_type, status=ServerStatus.SERVER_STATUS_RUNNING):
		if self.contain_server(name):
			return
		server = Server(name, server_type, status)
		self.servers.append(server)

	def remove_server(self, name):
		if self.contain_server(name):
			self.servers = [server for server in self.servers if server.get_name() != name]

	def dispatch_server(self):
		if not self.servers:
			return None

		index = self.server_index % len(self.servers)
		self.server_index += 1
		server = self.servers[index]
		return server