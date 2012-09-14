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

	def add_server(self, server):
		if self.contain_server(server.get_name()):
			return
		self.servers.append(server)

	def remove_server(self, server_name):
		if self.contain_server(server_name):
			self.servers = [server for server in self.servers if server.get_name() != server_name]

	def dispatch_server(self):
		if not self.servers:
			return None

		index = self.server_index % len(self.servers)
		self.server_index += 1
		server = self.servers[index]
		return server